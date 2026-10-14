import os
import fnmatch
from datetime import datetime

# Extensiones que nos interesan
VALID_EXTENSIONS = {'.py', '.js', '.ts', '.txt', '.md', '.html', '.css', '.json', '.go', '.rs', '.java', '.cpp'}

# Directorios excluidos por seguridad y rendimiento
EXCLUDED_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'dataforge-reports', 'dist', 'build', '.idea', '.vscode', 'target', 'bin', 'obj', '.dataforge'}
EXCLUDED_FILES = {'.env', '.env.local', '.env.production', 'id_rsa', 'id_ed25519', 'credentials.json', 'secrets.json'}
MAX_FILE_BYTES = 1_000_000


def _load_gitignore_patterns(root_path):
    """Read simple .gitignore patterns; unsupported negation patterns are ignored safely."""
    patterns = []
    ignore_path = os.path.join(root_path, ".gitignore")
    try:
        with open(ignore_path, "r", encoding="utf-8", errors="ignore") as handle:
            for raw in handle:
                pattern = raw.strip()
                if pattern and not pattern.startswith("#") and not pattern.startswith("!"):
                    patterns.append(pattern.rstrip("/"))
    except OSError:
        pass
    return patterns


def _is_ignored(relative_path, patterns):
    normalized = relative_path.replace(os.sep, "/")
    parts = normalized.split("/")
    for pattern in patterns:
        if "/" in pattern:
            if fnmatch.fnmatch(normalized, pattern) or normalized == pattern:
                return True
        elif any(fnmatch.fnmatch(part, pattern) for part in parts):
            return True
    return False

def get_all_files(root_path):
    root_path = os.path.abspath(root_path)
    patterns = _load_gitignore_patterns(root_path)
    files_to_process = []
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDED_DIRS
            and not _is_ignored(os.path.relpath(os.path.join(root, d), root_path), patterns)
        ]
        for file in files:
            if file.lower() in EXCLUDED_FILES or file.lower().startswith(".env."):
                continue
            relative_path = os.path.relpath(os.path.join(root, file), root_path)
            if _is_ignored(relative_path, patterns):
                continue
            ext = os.path.splitext(file)[1].lower()
            if ext in VALID_EXTENSIONS:
                files_to_process.append(os.path.join(root, file))
    return files_to_process

def read_file_content(file_path, max_bytes=MAX_FILE_BYTES):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(max_bytes + 1)
        if len(content) > max_bytes:
            return content[:max_bytes] + "\\n[DataForge: file truncated at configured safety limit.]"
        return content
    except Exception as e:
        return f"Error al leer {file_path}: {e}"

def get_single_file_content(file_path):
    if not os.path.exists(file_path):
        return None
    return read_file_content(file_path)

def prepare_code_payload(files_list, max_chars=35000):
    """Combina el contenido de los archivos y aplica un recorte estricto para evitar el Error 413 de tokens."""
    project_data = []
    total_chars = 0
    
    for file_path in files_list:
        content = read_file_content(file_path)
        file_header = f"--- FILE: {file_path} ---\n"
        file_block = f"{file_header}{content}\n\n"
        
        # Si agregar este archivo rebasa el límite seguro de caracteres, recortamos o detenemos
        if total_chars + len(file_block) > max_chars:
            remaining_chars = max_chars - total_chars
            if remaining_chars > 100:
                project_data.append(file_block[:remaining_chars] + "\n[... Archivo recortado por límite de presupuesto de tokens ...]")
            project_data.append("\n⚠️ [Aviso del Sistema]: El proyecto excede el presupuesto seguro de tokens. Se omitieron algunos archivos restantes.")
            break
            
        project_data.append(file_block)
        total_chars += len(file_block)
        
    return "".join(project_data)

def save_report(content, target_path):
    report_dir = os.path.join(target_path, "dataforge-reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reporte_{timestamp}.txt"
    file_path = os.path.join(report_dir, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path