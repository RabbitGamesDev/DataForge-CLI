import os
import json
import urllib.request
from groq import Groq
from dataforge.config_manager import get_config

def ask_enterprise_ai(prompt):
    """Enruta el prompt al proveedor de IA configurado (Groq, OpenAI, Gemini, Claude u Ollama local)"""
    config = get_config()
    if not config:
        config = {}
    
    # Soporta tanto 'ai_provider' como 'provider' según la versión del diccionario de configuración
    provider = config.get("ai_provider", config.get("provider", "groq")).lower()
    
    # 1. Proveedor Ollama (100% Offline / Local)
    if provider == "ollama":
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3",  # O el modelo local que prefiera el usuario
            "prompt": prompt,
            "stream": False
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result.get("response", "Error: Respuesta vacía de Ollama.")
        except Exception as e:
            return f"⚠️ Error de conexión con Ollama local (Verifica que esté abierto y el modelo instalado): {e}"

    # 2. Proveedor Groq (Nube Ultra Rápida)
    elif provider == "groq":
        # Revisa tanto 'groq_api_key' como 'api_key'
        api_key = config.get("groq_api_key", config.get("api_key"))
        if not api_key:
            raise ValueError("Falta la API Key de Groq. Ejecuta 'python main.py setup'")
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

    # 3. Otros proveedores en nube (OpenAI, Gemini, Claude)
    else:
        raise ValueError(f"Proveedor de IA '{provider}' no soportado o pendiente de credenciales.")

def ask_groq(prompt, api_key=None):
    """Puente de compatibilidad para llamadas antiguas a ask_groq"""
    return ask_enterprise_ai(prompt)