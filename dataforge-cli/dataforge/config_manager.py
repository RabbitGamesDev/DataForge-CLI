import os
import json
from datetime import datetime
import inquirer

CONFIG_DIR = os.path.expanduser("~/.dataforge")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
LICENSE_FILE = os.path.join(CONFIG_DIR, "license.json")

def init_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

def get_config():
    """Lee la configuración local de forma segura, manejando archivos corruptos o malformados."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            print("⚠️ [Aviso] El archivo de configuración local está corrupto o dañado.")
            print("🔄 Restableciendo configuración para evitar cierres inesperados...")
            try:
                os.remove(CONFIG_FILE)
            except Exception:
                pass
            return None
    return None

def get_license_tier():
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("active", False):
                    return data.get("tier", "").lower()
        except Exception:
            return "free"
        return "free"
    return "free"

def setup_config():
    """Configuración inicial adaptada estrictamente a los Tiers de DataForge con enmascaramiento seguro de API Key"""
    tier = get_license_tier()
    is_pro_or_team = tier in ["pro", "teams"]

    print("\n⚙️ [DataForge CLI] Configuración Inicial del Sistema\n")
    
    provider = "groq"
    api_key = ""
    
    if is_pro_or_team:
        print("🤖 Selecciona tu motor de IA Enterprise:")
        print("   [1] groq   -> Ultra rápido")
        print("   [2] openai -> Máxima precisión lógica")
        print("   [3] gemini -> Análisis masivo y contexto global")
        print("   [4] claude -> Prosa técnica de nivel producción")
        print("   [5] ollama -> Ejecución local y offline")
        
        choice = input("\nElige proveedor [1-5 o nombre] (default: groq): ").strip().lower()
        provider_map = {"1": "groq", "2": "openai", "3": "gemini", "4": "claude", "5": "ollama"}
        provider = provider_map.get(choice, choice if choice in provider_map.values() else "groq")
        
        if provider != "ollama":
            key_question = [
                inquirer.Password(
                    "api_key",
                    message=f"Introduce tu API Key para [{provider.upper()}] (se ocultará con ****):"
                )
            ]
            key_answer = inquirer.prompt(key_question)
            api_key = key_answer.get("api_key", "").strip() if key_answer else ""
    else:
        print("ℹ️ [Plan Free] Motor predeterminado: GROQ.")
        key_question = [
            inquirer.Password(
                "api_key",
                message="Introduce tu Groq API Key (se ocultará con ****):"
            )
        ]
        key_answer = inquirer.prompt(key_question)
        api_key = key_answer.get("api_key", "").strip() if key_answer else ""

    language = input("Idioma de los reportes [es / en] (default: es): ").strip().lower()
    if not language: language = "es"
    
    theme = "dark"
    if is_pro_or_team:
        theme = input("Tema visual [dark / light / tokyo_night / dracula] (default: dark): ").strip().lower()
        if not theme: theme = "dark"
    else:
        print("ℹ️ [Plan Free] Tema visual estándar establecido.")

    # Si es una licencia Teams, hereda automáticamente el nombre de la organización
    if tier == "teams" and os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r", encoding="utf-8") as lf:
                l_data = json.load(lf)
                brand_name = l_data.get("team_name", "Enterprise Team")
                print(f"🏢 [TEAMS Branding Automático]: Usando firma corporativa de la organización: '{brand_name}'")
        except Exception:
            brand_name = input("Nombre del autor/desarrollador para la firma: ").strip() or "Developer"
    else:
        brand_name = input("Nombre del autor/desarrollador para la firma: ").strip() or "Developer"
    
    config_data = {
        "provider": provider,
        "api_key": api_key,
        "language": language,
        "theme": theme,
        "brand_name": brand_name
    }
    
    init_config()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)
    
    print("\n✅ ¡Configuración guardada y sincronizada con éxito!\n")

def save_license_advanced(key: str, tier: str = "pro", owner: str = "", team_name: str = ""):
    init_config()
    
    # Valores por defecto para el control de asientos en licencias Teams
    max_seats = 5 if tier == "teams" else 1
    registered_devices = [os.environ.get("COMPUTERNAME", "default-device-id")]
    
    # Si ya existe una licencia previa con los mismos datos, preservamos los dispositivos registrados
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if old_data.get("key") == key:
                    registered_devices = old_data.get("registered_devices", registered_devices)
                    max_seats = old_data.get("max_seats", max_seats)
        except Exception:
            pass

    license_payload = {
        "key": key,
        "tier": tier,
        "active": True,
        "owner": owner,
        "team_name": team_name,
        "max_seats": max_seats,
        "registered_devices": registered_devices,
        "activated_at": datetime.now().isoformat()
    }
    
    with open(LICENSE_FILE, "w", encoding="utf-8") as f:
        json.dump(license_payload, f, indent=4)