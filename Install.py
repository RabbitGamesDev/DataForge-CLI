#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

def print_banner():
    print("=" * 50)
    print("      RGS Labs - DataForge CLI v2.0 Installer      ")
    print("=" * 50)

def check_python_version():
    print("[*] Verificando versión de Python...")
    if sys.version_info < (3, 8):
        print("[!] Error: Se requiere Python 3.8 o superior.")
        sys.exit(1)
    print(f"[+] Python {platform.python_version()} detectado.")

def install_dependencies():
    print("[*] Instalando dependencias necesarias (requirements.txt)...")
    req_path = os.path.join("dataforge-cli", "requirements.txt")
    if not os.path.exists(req_path):
        # Intentar ruta alternativa si se ejecuta desde otra ubicación
        req_path = "requirements.txt"
    
    if os.path.exists(req_path):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_path])
            print("[+] Dependencias instaladas correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al instalar dependencias: {e}")
            sys.exit(1)
    else:
        print("[!] Advertencia: No se encontró el archivo requirements.txt.")

def main():
    print_banner()
    check_python_version()
    install_dependencies()
    print("\n" + "=" * 50)
    print(" ¡Instalación completada con éxito!")
    print(" Ya puedes usar DataForge CLI ejecutando: python dataforge-cli/main.py")
    print("=" * 50)

if __name__ == "__main__":
    main()
