<div align="center">

# 🛠️ DataForge CLI

### AI-powered code intelligence for developers.

Analyze, document and understand software projects directly from your terminal.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-F55036?style=for-the-badge)
![Platform](https://img.shields.io/badge/Windows-macOS-Linux-4CAF50?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

**DataForge CLI** transforma cualquier proyecto de software en documentación técnica, resúmenes inteligentes y análisis arquitectónicos utilizando IA.

Pensado para desarrolladores que desean comprender grandes bases de código en minutos en lugar de horas.

</div>

---

# ✨ Características

- 🔍 Escaneo inteligente de proyectos
- 🤖 IA contextual sobre todo el código
- 📄 Documentación automática
- 🗺️ Mapa de arquitectura del proyecto
- 📚 Onboarding para nuevos desarrolladores
- 📊 Reportes profesionales
- ⚡ Procesamiento rápido mediante Groq
- 🔒 Configuración local y privada
- 🌎 Windows, macOS y Linux

---

# 🚀 ¿Qué puede hacer?

DataForge analiza directorios completos y utiliza IA para responder preguntas como:

> ¿Cómo funciona este proyecto?

> ¿Qué hace este archivo?

> ¿Dónde está la lógica principal?

> ¿Qué dependencias existen?

> ¿Cómo está organizada la arquitectura?

En lugar de leer cientos de archivos manualmente, DataForge genera respuestas claras y estructuradas.

---

# 📦 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/RabbitGamesDev/DataForge-CLI.git

cd DataForge-CLI
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Obtener una API Key de Groq

DataForge utiliza la API oficial de Groq.

1. Crear una cuenta gratuita:

https://console.groq.com/

2. Acceder al panel de API Keys:

https://console.groq.com/keys

3. Crear una nueva Key.

4. Copiar la clave.

La primera vez que ejecutes DataForge se solicitará automáticamente.

---

## 4. Ejecutar

```bash
python main.py
```

La configuración únicamente se realiza una vez.

---

# ⚙️ Configuración Inicial

Durante el primer inicio aparecerá un asistente interactivo.

```text
Bienvenido a DataForge CLI!

Ingrese su API Key:

*********************

Idioma

> Español
  English

Tema

> Dark
  Light
```

La configuración se guarda localmente para futuras ejecuciones.

---

# 💻 Comandos

## Escanear un proyecto

```bash
python main.py scan
```

o

```bash
python main.py scan C:\MiProyecto
```

---

## Explicar un archivo

```bash
python main.py explain archivo.py
```

---

## Chat con tu proyecto

```bash
python main.py ask
```

---

## Generar documentación

```bash
python main.py onboard
```

---

## Mapa de arquitectura

```bash
python main.py map
```

---

# 📂 Estructura del proyecto

```text
dataforge-cli/

│
├── dataforge/
│   ├── api_handler.py
│   ├── config_manager.py
│   ├── core.py
│   └── __init__.py
│
├── reports/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Roadmap

## Versión 1.0

- [x] Configuración inicial
- [x] Integración con Groq
- [x] CLI interactiva
- [ ] Scan inteligente
- [ ] Reportes TXT

---

## Versión 1.5

- [ ] PDFs
- [ ] Markdown
- [ ] JSON
- [ ] Resúmenes automáticos

---

## Versión 2.0

- [ ] Chat contextual
- [ ] Arquitectura ASCII
- [ ] Memoria entre sesiones
- [ ] Plugins

---

# 🔒 Seguridad

DataForge fue diseñado siguiendo una filosofía **Local First**.

✔ La configuración permanece en tu equipo.

✔ Los archivos originales nunca son modificados.

✔ Solo el texto necesario se envía a la API de Groq.

✔ `.gitignore` protege archivos sensibles.

✔ Las API Keys nunca se publican automáticamente.

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas.

Si encuentras un error o tienes una idea:

1. Haz un Fork.

2. Crea una nueva rama.

3. Envía un Pull Request.

---

# 📜 Licencia

Este proyecto está distribuido bajo la licencia Apache 2.0.

Consulta el archivo **LICENSE** para más información.

---

# ❤️ Desarrollado por

## RGS Labs™

Construyendo herramientas inteligentes para desarrolladores.

GitHub:
https://github.com/RabbitGamesDev

---

<div align="center">

⭐ Si este proyecto te resulta útil, considera darle una estrella al repositorio.

</div>
