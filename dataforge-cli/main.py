import sys
import os
import json
import urllib.request
import urllib.parse
import webbrowser
import platform
import uuid
from datetime import datetime
from dataforge.config_manager import init_config, get_config, setup_config, save_license_advanced, LICENSE_FILE
from dataforge.api_handler import ask_groq
from dataforge.core import get_all_files, read_file_content, save_report, get_single_file_content, prepare_code_payload

WELCOME_URL = "https://rabbitgamesdev.github.io/DataForge-CLI/"
SUPABASE_FUNCTION_URL = "https://yultjjqcxtqfakppxyqv.supabase.co/functions/v1/validate-license"

def get_theme_color():
    config = get_config() or {}
    theme = config.get("theme", "dark")
    if theme == "tokyo_night": return "\033[38;5;189m"
    elif theme == "dracula": return "\033[38;5;212m"
    elif theme == "light": return "\033[30m"
    return "\033[38;5;248m"

def cprint(text, style="normal"):
    reset = "\033[0m"
    color = get_theme_color()
    if style == "success": color = "\033[32m"
    elif style == "error": color = "\033[31m"
    elif style == "warning": color = "\033[33m"
    elif style == "pro": color = "\033[38;5;220m"
    elif style == "teams": color = "\033[38;5;141m"
    print(f"{color}{text}{reset}")

def get_language_prefix():
    config = get_config() or {}
    lang = config.get("language", "es")
    if lang == "en":
        return "[SYSTEM DIRECTIVE: You MUST respond entirely and strictly in English.]\n\n"
    return "[DIRECTIVA DEL SISTEMA: Debes responder entera y estrictamente en Español.]\n\n"

def get_license_data():
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def verify_license_hybrid() -> bool:
    """Motor de Licenciamiento Híbrido: Supabase Cloud + Offline Grace Period + Expiration Check"""
    data = get_license_data()
    if not data or not data.get("active", False):
        return False
    
    key = data.get("key")
    if not key:
        return False

    now = datetime.now()

    # Validar expiración local inmediata si existe el campo
    if data.get("expires_at"):
        try:
            if now > datetime.fromisoformat(data["expires_at"]):
                data["active"] = False
                with open(LICENSE_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                return False
        except Exception:
            pass

    last_checked_str = data.get("last_checked")
    should_check = True
    
    if last_checked_str:
        try:
            last_checked = datetime.fromisoformat(last_checked_str)
            if (now - last_checked).days < 7:
                should_check = False
        except Exception:
            pass

    if should_check:
        machine_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, platform.node()))
        payload = json.dumps({
            "license_key": key,
            "machine_id": machine_id
        }).encode("utf-8")

        try:
            req = urllib.request.Request(
                SUPABASE_FUNCTION_URL,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                if not res_data.get("success", False):
                    data["active"] = False
                    with open(LICENSE_FILE, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4)
                    return False
                
                # Actualizar datos con sincronización exitosa de servidor
                data["tier"] = res_data.get("tier", data.get("tier"))
                data["expires_at"] = res_data.get("expires_at", data.get("expires_at"))
                data["last_checked"] = now.isoformat()
                with open(LICENSE_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
        except Exception:
            # Modo Offline Grace Period (si falla la red, permite acceso si se verificó hace menos de 7 días)
            pass

    return True

def is_pro_active() -> bool:
    data = get_license_data()
    if not data or not data.get("active", False):
        return False
    if not verify_license_hybrid():
        return False
    return data.get("tier", "").lower() in ["pro", "teams"]

def is_teams_active() -> bool:
    data = get_license_data()
    if not data or not data.get("active", False):
        return False
    if not verify_license_hybrid():
        return False
    return data.get("tier", "").lower() == "teams"

def ask_enterprise_ai(prompt):
    config = get_config() or {}
    provider = config.get("provider", "groq").lower()
    
    if provider == "ollama":
        try:
            url = "http://localhost:11434/api/generate"
            payload = json.dumps({
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=45) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                return res_data.get("response", "Error: Respuesta vacía de Ollama.")
        except Exception as e:
            return f"⚠️ Error de conexión con Ollama local: {e}"

    if provider == "claude":
        system_directive = "[EXPERT CLAUDE ENGINE: Prioritize deep architectural nuance, pristine production documentation structure.]\n"
        return ask_groq(system_directive + prompt)
    elif provider == "openai":
        system_directive = "[EXPERT OPENAI ENGINE: Prioritize absolute logical precision, strict code correctness.]\n"
        return ask_groq(system_directive + prompt)
    elif provider == "gemini":
        system_directive = "[EXPERT GEMINI ENGINE: Prioritize exhaustive global context handling, multi-step structural breakdown.]\n"
        return ask_groq(system_directive + prompt)
    
    return ask_groq(prompt)

def get_footer_branding():
    config = get_config() or {}
    brand = config.get("brand_name", "Developer")
    
    if is_teams_active():
        license_data = get_license_data() or {}
        team_name = license_data.get("team_name", brand)
        return f"\n\n---\n*Generated by {team_name}*\n>_ Enterprise Architecture Documentation Pipeline"
    elif is_pro_active():
        return f"\n\n---\n*Created by {brand}*\n>_ [Powered by DataForge CLI](https://rabbitgamesdev.github.io/DataForge-CLI/)"
    else:
        return (
            f"\n\n---\n"
            f"<!-- Generated by DataForge CLI Free Tier - RGS Labs™ -->\n"
            f"*Created by {brand}*\n"
            f">_ **Powered by DataForge CLI by RGS Labs™**\n"
            f">_ [https://rabbitgamesdev.github.io/DataForge-CLI/](https://rabbitgamesdev.github.io/DataForge-CLI/)"
        )

def open_welcome_page():
    try: webbrowser.open(WELCOME_URL, new=2)
    except Exception: cprint(f"👉 Carta de bienvenida: {WELCOME_URL}", "warning")

def show_help_table():
    status = "💜 TEAMS (Enterprise Branding)" if is_teams_active() else ("⭐ PRO (Developer Suite)" if is_pro_active() else "🔓 Free Tier")
    config = get_config() or {}
    
    cprint(f"\n======================================================================", "pro")
    cprint(f" 🚀 DataForge CLI v2.0 - RGS Labs™ | Estado: [{status}]", "pro")
    cprint(f" 🤖 IA Activa: {config.get('provider', 'groq').upper()} | Idioma: {config.get('language', 'es').upper()}", "success")
    cprint(f"======================================================================", "pro")
    
    print("\n📋 TABLA DE COMANDOS DISPONIBLES:\n")
    print(f"{'Comando':<18} | {'Tipo':<10} | {'Descripción detallada de la función'}")
    print("-" * 75)
    print(f"{'scan':<18} | {'Free/Pro':<10} | Escanea el proyecto completo y genera un reporte de análisis de IA.")
    print(f"{'explain':<18} | {'Free/Pro':<10} | Explica a detalle un archivo de código específico (admite perfiles).")
    print(f"{'map':<18} | {'Free/Pro':<10} | Genera un diagrama ASCII visual de la arquitectura del proyecto.")
    print(f"{'onboard':<18} | {'Free/Pro':<10} | Crea una guía de incorporación técnica corporativa automatizada.")
    print(f"{'doc++':<18} | {'PRO / TEAMS':<10} | Genera documentación técnica avanzada lista para producción.")
    print(f"{'architecture++':<18} | {'PRO / TEAMS':<10} | Genera diagramas estructurales Mermaid y análisis profundo.")
    print(f"{'export':<18} | {'PRO / TEAMS':<10} | Exporta los reportes generados a formatos limpios (--md, --json, --html).")
    print(f"{'preset':<18} | {'PRO / TEAMS':<10} | Ejecuta un pipeline completo automatizado de desarrollo.")
    print(f"{'setup':<18} | {'Global':<10} | Reconfigura el motor de IA, API Keys, idioma y tema visual.")
    print(f"{'license':<18} | {'Global':<10} | Activa licencias de categoría PRO o TEAMS (con branding corporativo).")
    print(f"{'license status':<18} | {'Global':<10} | Activa o consulta el estado de licencias (ej. license status).")
    print("-" * 75)

def run_scan(target_path):
    cprint(f"🔍 Escaneando proyecto en: {target_path}...")
    files = get_all_files(target_path)
    if not files: return cprint("No se encontraron archivos válidos.", "error")
    
    file_list_str = "\n".join([f"- {f}" for f in files])
    # Payload optimizado con presupuesto seguro de tokens para evitar Error 413
    full_context = prepare_code_payload(files, max_chars=35000)
    
    prompt = f"{get_language_prefix()}Analiza la arquitectura y código de este proyecto:\n{full_context}"
    respuesta = ask_enterprise_ai(prompt)
    
    final_content = f"# ARCHIVO DE REPORTE - DataForge CLI\n\n**Archivos analizados:**\n{file_list_str}\n\n{respuesta}{get_footer_branding()}"
    report_path = save_report(final_content, target_path)
    cprint(f"\n✅ Reporte guardado en: {report_path}\n", "success")
    print(respuesta)

def run_explain(file_path, audience=""):
    content = get_single_file_content(file_path)
    if content is None: return cprint("Error: El archivo no existe.", "error")
    
    modifier = f"Adapta la explicación para un perfil: {audience.upper()}." if audience else ""
    if audience and not is_pro_active():
        return cprint("🔒 Requiere licencia PRO.", "warning")
        
    prompt = f"{get_language_prefix()}Explica detalladamente qué hace este archivo. {modifier}\n{content}"
    respuesta = ask_enterprise_ai(prompt)
    cprint(f"\n--- EXPLICACIÓN ({audience.upper() if audience else 'GENERAL'}) ---")
    print(respuesta)

def run_map(target_path):
    cprint(f"🗺️ Generando mapa de dependencias ASCII...")
    files = get_all_files(target_path)
    file_names = "\n".join([os.path.relpath(f, target_path) for f in files])
    prompt = f"{get_language_prefix()}Basado en:\n{file_names}\n\nGenera un mapa visual (ASCII) limpio de la arquitectura."
    respuesta = ask_enterprise_ai(prompt)
    cprint(f"\n--- MAPA DE ARQUITECTURA ---\n{respuesta}")

def run_onboard(target_path):
    cprint(f"🚀 Generando guía de onboarding...")
    files = get_all_files(target_path)
    if not files: return cprint("No se encontraron archivos válidos.", "error")
    
    full_context = prepare_code_payload(files, max_chars=35000)
    prompt = f"{get_language_prefix()}Actúa como Líder Técnico. Genera Onboarding corporativo:\n{full_context}"
    respuesta = ask_enterprise_ai(prompt)
    
    final_content = f"# ONBOARDING GUIDE\n\n{respuesta}{get_footer_branding()}"
    report_path = save_report(final_content, target_path)
    cprint(f"✅ Onboarding generado: {report_path}", "success")
    print(f"\n{respuesta}")

def run_doc_pro(target_path):
    if not is_pro_active(): return cprint("🔒 Exclusivo PRO/TEAMS.", "warning")
    cprint(f"🚀 Generando documentación técnica de producción (Documentation++)...", "teams" if is_teams_active() else "pro")
    files = get_all_files(target_path)
    if not files: return
    
    file_list = "\n".join([os.path.relpath(f, target_path) for f in files[:50]])
    prompt = f"{get_language_prefix()}Arquitecto Senior. Genera README profesional y documentación técnica basada en:\n{file_list}"
    respuesta = ask_enterprise_ai(prompt)
    
    output = os.path.join(target_path, "PRODUCTION_DOCS.md")
    with open(output, "w", encoding="utf-8") as f: f.write(respuesta + get_footer_branding())
    cprint(f"✅ Documentación guardada en: {output}", "success")

def run_architecture_pro(target_path):
    if not is_pro_active(): return cprint("🔒 Exclusivo PRO/TEAMS.", "warning")
    cprint(f"📐 Generando diagramas Mermaid y análisis profundo...", "pro")
    files = get_all_files(target_path)
    if not files: return
    file_names = "\n".join([os.path.relpath(f, target_path) for f in files[:50]])
    prompt = f"{get_language_prefix()}Arquitecto Experto. Genera código Mermaid (graph TD) y explicación basada en:\n{file_names}"
    respuesta = ask_enterprise_ai(prompt)
    
    output = os.path.join(target_path, "ARCHITECTURE_REPORT.md")
    with open(output, "w", encoding="utf-8") as f: f.write(respuesta + get_footer_branding())
    cprint(f"✅ Arquitectura guardada en: {output}", "success")

def run_export(target_path, fmt):
    if not is_pro_active(): return cprint("🔒 Exclusivo PRO/TEAMS.", "warning")
    fmt = fmt.replace("--", "").lower()
    reports_dir = os.path.join(target_path, "dataforge-reports")
    if not os.path.exists(reports_dir): return cprint("⚠️ Sin reportes previos.", "warning")
    reports = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.endswith(".txt") or f.endswith(".md")]
    if not reports: return cprint("⚠️ No hay reportes para exportar.", "warning")
    
    target_file = max(reports, key=os.path.getmtime)
    with open(target_file, "r", encoding="utf-8") as f: content = f.read()
    output_path = f"{os.path.splitext(target_file)[0]}.{fmt}"
    
    if fmt == "json":
        with open(output_path, "w", encoding="utf-8") as out: json.dump({"content": content}, out, indent=4)
    elif fmt == "html":
        with open(output_path, "w", encoding="utf-8") as out: out.write(f"<html><body><pre>{content}</pre></body></html>")
    else:
        with open(output_path, "w", encoding="utf-8") as out: out.write(content)
    cprint(f"✅ Exportado a: {output_path}", "success")

def run_preset(name, target_path):
    if not is_pro_active(): return cprint("🔒 Exclusivo PRO/TEAMS.", "warning")
    if name == "onboarding":
        cprint(f"⚡ Ejecutando Pipeline Automático de Ingeniería...", "pro")
        run_scan(target_path)
        run_onboard(target_path)
        run_doc_pro(target_path)
        run_architecture_pro(target_path)
        run_export(target_path, "--html")
        cprint("🎉 ¡Preset completado exitosamente!", "success")
    else:
        cprint(f"⚠️ Preset desconocido: {name}.", "warning")

def run_license_activation(key: str):
    machine_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, platform.node()))
    owner = input("Introduce tu correo de compra (ej. tu@email.com): ").strip()
    if not owner: owner = "cliente@dataforge.dev"

    upper_key = key.upper()
    is_team = "TEAM" in upper_key or "TEAMS" in upper_key
    
    team_name = ""
    if is_team:
        print("\n🏢 [TEAMS] Licencia corporativa detectada.")
        team_name = input("Introduce el Nombre de tu Estudio / Empresa para el Team Branding: ").strip()
        if not team_name: team_name = "Enterprise Team"

    payload = json.dumps({
        "license_key": key,
        "machine_id": machine_id,
        "email": owner,
        "team_branding": team_name
    }).encode("utf-8")

    try:
        req = urllib.request.Request(
            SUPABASE_FUNCTION_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            if not res_data.get("success", False):
                return cprint(f"❌ Error de activación: {res_data.get('message', 'Clave inválida')}", "error")
            
            tier = res_data.get("tier", "pro").lower()
            saved_owner = owner 
            saved_branding = res_data.get("team_branding", team_name)
            expires_at = res_data.get("expires_at")
    except Exception as e:
        return cprint(f"⚠️ Error conectando con el servidor de licencias: {e}", "error")

    # Guardar licencia avanzada
    save_license_advanced(key=key, tier=tier, owner=saved_owner, team_name=saved_branding)
    
    # Inyectar timestamp del último heartbeat y fecha de expiración inmediatamente
    data = get_license_data()
    if data:
        data["last_checked"] = datetime.now().isoformat()
        if expires_at:
            data["expires_at"] = expires_at
        with open(LICENSE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    if tier == "teams":
        cprint(f"💜 ¡Licencia TEAMS activada para {saved_owner}! Branding: '{saved_branding}'.", "teams")
    else:
        cprint(f"🎉 ¡Licencia PRO activada exitosamente para {saved_owner}!", "success")

def run_license_status():
    data = get_license_data()
    if not data or not data.get("active", False):
        return cprint("🔓 No hay ninguna licencia activa. Actualmente estás en el Plan Free.", "warning")
    
    tier = data.get("tier", "free").upper()
    key = data.get("key", "N/A")
    owner = data.get("owner", "N/A")
    team_name = data.get("team_name", "N/A")
    activated_at = data.get("activated_at", "N/A")
    last_checked = data.get("last_checked", "Nunca (Modo Local)")
    expires_at = data.get("expires_at")
    
    cprint(f"\n========================================================", "pro")
    cprint(f" 🛡️ ESTADO DE LICENCIA HÍBRIDA — DATAFORGE CLI v2.0", "pro")
    cprint(f"========================================================", "pro")
    print(f"  • Plan Activo      : {tier}")
    print(f"  • Clave Registrada : {key}")
    print(f"  • Propietario      : {owner}")
    if team_name and team_name != "N/A":
        print(f"  • Team Branding    : {team_name}")
        
    print(f"  • Fecha Activación : {activated_at}")
    print(f"  • Último Heartbeat : {last_checked}")
    
    if expires_at:
        print(f"  • Expiración       : {expires_at}")
        try:
            exp_date = datetime.fromisoformat(expires_at)
            days_left = (exp_date - datetime.now()).days
            if days_left <= 7 and days_left >= 0:
                cprint(f"⚠️ ¡Atención! Tu licencia vence en {days_left} días. Renueva pronto en RGS Labs.", "warning")
            elif days_left < 0:
                cprint(f"❌ Tu licencia ha expirado. Por favor renueva tu plan.", "error")
        except Exception:
            pass

    cprint(f"========================================================\n", "pro")

def main():
    init_config()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "license":
            if len(sys.argv) > 2:
                arg = sys.argv[2]
                if arg.lower() == "status":
                    run_license_status()
                else:
                    run_license_activation(arg)
            else:
                cprint("⚠️ Falta la clave o argumento. Usa: python main.py license [KEY | status]", "error")
            return
        elif cmd in ["--help", "-h", "help"]:
            show_help_table()
            return

    if get_config() is None:
        open_welcome_page()
        setup_config()

    if len(sys.argv) < 2:
        show_help_table()
        return

    cmd = sys.argv[1]
    target = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else ".")
    
    if cmd == "scan": run_scan(target)
    elif cmd == "setup": setup_config()
    elif cmd == "explain": run_explain(sys.argv[2] if len(sys.argv) > 2 else "", sys.argv[3].replace("--","") if len(sys.argv)>3 else "")
    elif cmd == "map": run_map(target)
    elif cmd == "onboard": run_onboard(target)
    elif cmd == "welcome": open_welcome_page()
    elif cmd == "doc++": run_doc_pro(target)
    elif cmd == "architecture++": run_architecture_pro(target)
    elif cmd == "export": run_export(target, sys.argv[3] if len(sys.argv) > 3 else "--md")
    elif cmd == "preset": run_preset(sys.argv[2] if len(sys.argv) > 2 else "", target)
    else:
        show_help_table()

if __name__ == "__main__": main()