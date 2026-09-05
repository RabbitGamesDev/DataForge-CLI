import os
import sys
from dataforge.config_manager import is_pro_active, get_config
from dataforge.api_handler import ask_enterprise_ai  # Usamos el enrutador universal

def run_doc_plus(path: str = "."):
    """Comando PRO: doc++ (Generación de documentación de producción)"""
    if not is_pro_active():
        print("🔒 [PRO] Esta función requiere una licencia PRO activa.")
        print("💡 Actívala con: python main.py license TU-CODIGO")
        return

    print(f"🚀 [PRO] Analizando el proyecto en '{path}' para generar documentación de producción...")
    
    project_files = []
    ignore_dirs = {".git", "__pycache__", "venv", "env", "node_modules", ".dataforge"}
    
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".md", ".json", ".html", ".css")):
                project_files.append(os.path.join(root, file))

    print(f"📁 Se encontraron {len(project_files)} archivos para documentar.")
    
    file_list_str = "\n".join(project_files[:50])
    
    prompt = (
        "Actúa como un Arquitecto de Software Senior. Genera una documentación de nivel producción "
        "completa en formato Markdown (README.md profesional, guía técnica, arquitectura y dependencias) "
        "para este proyecto basado en esta lista de archivos:\n" + file_list_str
    )
    
    print("🤖 Consultando al motor de IA configurado para generar la documentación avanzada...")
    response = ask_enterprise_ai(prompt)  # Soporta Groq, OpenAI, Gemini, Claude u Ollama local
    
    output_file = os.path.join(path, "PRODUCTION_DOCS.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response)
        
    print(f"✅ ¡Documentación avanzada generada y guardada exitosamente en {output_file}!")

def run_architecture_plus(path: str = "."):
    """Comando PRO: architecture++ (Generación de diagramas Mermaid y análisis profundo)"""
    if not is_pro_active():
        print("🔒 [PRO] Esta función requiere una licencia PRO activa.")
        print("💡 Actívala con: python main.py license TU-CODIGO")
        return

    print(f"🏗️ [PRO] Analizando arquitectura y generando diagramas Mermaid para: {path}...")
    
    project_files = []
    ignore_dirs = {".git", "__pycache__", "venv", "env", "node_modules", ".dataforge"}
    
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".json")):
                project_files.append(os.path.join(root, file))

    file_list_str = "\n".join(project_files[:50])
    
    prompt = (
        "Actúa como un Arquitecto de Software experto. Analiza la estructura de este proyecto y genera "
        "un reporte de arquitectura detallado que incluya:\n"
        "1. Un diagrama en código Mermaid (graph TD o similar) que muestre la relación entre módulos y carpetas.\n"
        "2. Explicación de flujos internos y componentes críticos.\n"
        "Devuelve el resultado en formato Markdown limpio."
    )
    
    print("🤖 Consultando al motor de IA configurado para construir el reporte de arquitectura...")
    response = ask_enterprise_ai(prompt)  # Universal y compatible con offline
    
    output_file = os.path.join(path, "ARCHITECTURE_REPORT.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response)
        
    print(f"✅ ¡Reporte de arquitectura y diagramas Mermaid guardados en {output_file}!")