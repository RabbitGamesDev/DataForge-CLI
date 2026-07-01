import sys
import os
from dataforge.config_manager import init_config, get_config, setup_config
from dataforge.api_handler import ask_groq
from dataforge.core import get_all_files, read_file_content, save_report, get_single_file_content

def run_scan(target_path):
    print(f"🔍 Escaneando: {target_path}...")
    files = get_all_files(target_path)
    if not files:
        print("No se encontraron archivos válidos.")
        return
    print(f"✅ Se encontraron {len(files)} archivos.")
    file_list_str = "\n".join([f"- {f}" for f in files])
    full_context = "".join([f"\n--- ARCHIVO: {f} ---\n{read_file_content(f)}" for f in files])
    
    print("🤖 Consultando a la IA...")
    respuesta = ask_groq(f"Analiza la estructura y el código de este proyecto:\n{full_context}")
    report_path = save_report(f"ARCHIVO DE REPORTE - DataForge CLI\nArchivos analizados:\n{file_list_str}\n\n{respuesta}", target_path)
    print(f"\n✅ Reporte guardado en: {report_path}\n{respuesta}")

def run_explain(file_path):
    content = get_single_file_content(file_path)
    if content is None:
        print("Error: El archivo no existe.")
        return
    respuesta = ask_groq(f"Explica detalladamente qué hace este archivo:\n{content}")
    print(f"\n--- EXPLICACIÓN ---\n{respuesta}")

def run_map(target_path):
    print(f"🗺️ Generando mapa de dependencias...")
    files = get_all_files(target_path)
    file_names = "\n".join([os.path.relpath(f, target_path) for f in files])
    respuesta = ask_groq(f"Basado en:\n{file_names}\n\nGenera un mapa visual (ASCII) de la arquitectura.")
    print(f"\n--- MAPA DE ARQUITECTURA ---\n{respuesta}")

def run_chat(target_path):
    print(f"🤖 Iniciando modo Chat Consultor. Analizando archivos...")
    files = get_all_files(target_path)
    full_context = "CONTEXTO:\n" + "\n".join([f"\n--- {f} ---\n{read_file_content(f)}" for f in files])
    system_prompt = "Eres Consultor Senior de DataForge. Prioriza seguridad, legibilidad y escalabilidad. Analiza los módulos específicos antes de dar consejos."
    history = [{"role": "system", "content": system_prompt}, {"role": "system", "content": full_context}]
    
    print("✅ Consultor listo. (Escribe 'salir' para terminar).")
    while True:
        user_input = input("\n👤 Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]: break
        history.append({"role": "user", "content": user_input})
        respuesta = ask_groq(str(history))
        print(f"🤖 IA: {respuesta}")
        history.append({"role": "assistant", "content": respuesta})

def run_onboard(target_path):
    print(f"🚀 Generando onboarding...")
    files = get_all_files(target_path)
    full_context = "\n".join([f"--- {f} ---\n{read_file_content(f)}" for f in files])
    respuesta = ask_groq(f"Actúa como Líder Técnico. Genera un Onboarding: resumen, punto de entrada, archivos críticos y guía.\n{full_context}")
    report_path = save_report(f"--- ONBOARDING DOCUMENT ---\n{respuesta}", target_path)
    print(f"✅ Onboarding generado: {report_path}\n\n{respuesta}")

def main():
    init_config()
    if get_config() is None: setup_config()

    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h", "help"]:
        print("""
🚀 DataForge CLI - Asistente de Código con IA
---------------------------------------------
Uso: python main.py [comando] [ruta/archivo]

Comandos disponibles:
  scan    [ruta]      : Analiza proyecto y guarda reporte.
  explain [archivo]   : Explica un archivo específico.
  map     [ruta]      : Mapa de arquitectura (ASCII).
  ask     [ruta]      : Chat interactivo con tu código.
  onboard [ruta]      : Guía de bienvenida para nuevos devs.
        """)
        return

    command = sys.argv[1]
    path = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else ".")
    
    if command == "scan": run_scan(path)
    elif command == "explain":
        if len(sys.argv) > 2: run_explain(path)
        else: print("Error: Especifica un archivo para 'explain'.")
    elif command == "map": run_map(path)
    elif command == "ask": run_chat(path)
    elif command == "onboard": run_onboard(path)
    else: print(f"Comando '{command}' no reconocido. Escribe 'python main.py' para ver ayuda.")

if __name__ == "__main__":
    main()
