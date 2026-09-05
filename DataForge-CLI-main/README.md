<div align="center">

<img src=".github/assets/Data%20Forge_CLI%20(GitHub%20Banner)%20.jpg" width="100%" alt="DataForge CLI Banner">

<br><br>

# 🛠️ DataForge CLI

### Your AI consultant inside the terminal.

**Analyze • Visualize • Document**

Transform documents and project files into structured knowledge using AI directly from your terminal.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-F55036?style=for-the-badge)
![Platform](https://img.shields.io/badge/Windows-macOS-Linux-4CAF50?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

<br>

**DataForge CLI** is an AI-powered toolkit for developers who need to analyze, summarize and organize files directly from the command line.

Built with a simple philosophy:

### **Local-first. Fast. Professional.**

> [!TIP]
> New to GitHub?
>
> No worries. DataForge can be installed simply by downloading the repository as a ZIP file—no Git knowledge required.

</div>

---

# 📖 Overview

Reading hundreds of documents, source files or project folders takes time.

**DataForge CLI** helps automate that process.

Instead of manually opening every file, DataForge scans your project, extracts useful information and uses AI to generate organized summaries directly inside your terminal.

The project is designed to be lightweight, easy to configure and respectful of your privacy.

<div align="center">

# 🎬 Watch the Launch Video

See DataForge CLI in action and discover how it transforms project analysis with AI.

<br>

<a href="https://youtu.be/gqvA_W7dlo8">

<img src="https://img.shields.io/badge/▶_Watch_the_Launch_Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white">

</a>

</div>

---

---

# ✨ Current Features

| Feature | Description |
|:---------|:------------|
| ⚙️ Interactive Setup | First launch configuration wizard. |
| 🔐 Secure API Storage | Saves your Groq API Key locally. |
| 🌎 Language Selection | Configure the interface language. |
| 🎨 Terminal Theme | Choose between Dark and Light mode. |
| 📂 Project Scanner | Scan folders for future AI analysis. |
| 📝 Report Generation | Creates organized text reports. |
| 🤖 Groq Integration | Powered by Groq LLMs. |
| 🧩 Modular Architecture | Easy to extend and maintain. |

---

# 🚀 Why DataForge?

DataForge was created with one objective:

> **Reduce the time developers spend reading projects manually.**

Whether you're exploring a new codebase, organizing documentation or preparing technical reports, DataForge aims to become your AI assistant directly inside the terminal.

---

# ⚡ Installation

DataForge CLI can be installed in **two different ways** depending on your experience.


> [!TIP]
> New to the command line?
>
> Don't worry.
> This guide walks you through installation step by step, even if you've never used Git before.

---

---

# 📦 Installation

## Option 1 — Clone the Repository (Recommended)

If you have Git installed, clone the project:

```bash
git clone https://github.com/RabbitGamesDev/DataForge-CLI.git
```

Enter the project folder:

```bash
cd DataForge-CLI/dataforge-cli
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Launch DataForge:

```bash
python main.py
```

---

## Option 2 — Download as ZIP

If you don't use Git:

1. Open this repository on GitHub.
2. Click **Code**.
3. Click **Download ZIP**.
4. Extract the ZIP anywhere on your computer.
5. Open a terminal inside the **dataforge-cli** folder.
6. Install the dependencies:

```bash
pip install -r requirements.txt
```

7. Run the application:

```bash
python main.py
```

---

## 🔑 Configure your Groq API Key

DataForge requires a Groq API Key to communicate with the AI model.

Getting one only takes a minute.

1. Visit **https://console.groq.com/**
2. Sign in or create a free account.
3. Open **API Keys**.
4. Click **Create API Key**.
5. Copy your key.

The first time DataForge starts it will ask for your API Key and save it locally on your computer.

Your key is never uploaded to GitHub and is automatically ignored by `.gitignore`.

---

# 🚀 Using DataForge from Anywhere (Windows)

After installing DataForge you may want to execute it from any folder without navigating to the project directory every time.

You can do this by creating a small launcher.

Create a file called:

```text
dataforge.bat
```

Paste the following content inside it:

```bat
@echo off
python "C:\PATH\TO\DataForge-CLI\dataforge-cli\main.py" %*
```

Replace the path with the location where **main.py** is stored on your computer.

Save the file.

You can either:

- keep it inside your own tools folder,
- or place it inside a folder that exists in your Windows PATH.

After that, simply open any terminal and type:

```bash
dataforge
```

or

```bash
dataforge scan .
```

without navigating to the DataForge directory.

---

# 💻 Basic Usage

Open a terminal inside the project you want to analyze.

Examples:

Analyze the current project:

```bash
dataforge scan .
```

Explain a specific file:

```bash
dataforge explain main.py
```

Generate the architecture map:

```bash
dataforge map .
```

Start an interactive AI session:

```bash
dataforge ask
```

Generate onboarding documentation:

```bash
dataforge onboard .
```

Need help?

Simply type:

```bash
dataforge
```

or

```bash
dataforge help
```

to display the list of available commands.

---

# 💻 First Run

The first execution only happens once.

DataForge will ask for:

- Your Groq API Key
- Preferred language
- Terminal theme

After that, your configuration is saved automatically.

Future launches skip this setup.

---

# 📁 Project Structure

```
Repository/

│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
│
└── dataforge-cli/
    │
    ├── dataforge/
    │   ├── __init__.py
    │   ├── api_handler.py
    │   ├── config_manager.py
    │   └── core.py
    │
    ├── dataforge-reports/
    │
    ├── .gitignore
    ├── main.py
    └── requirements.txt
```

---

# 🔒 Security

DataForge follows a **Local-first** approach.

- Your API Key remains on your computer.
- Your configuration is stored locally.
- Reports are generated locally.
- No project files are modified.
- Sensitive files are excluded through `.gitignore`.

---

# 🗺️ Roadmap

## Version 1.0

- [x] Interactive setup
- [x] Groq integration
- [x] Report generation
- [x] Modular architecture

---

## Version 1.5

- [ ] PDF support
- [ ] Markdown export
- [ ] JSON export
- [ ] Better error handling

---

## Version 2.0

- [ ] Chunk processing
- [ ] Resume interrupted scans
- [ ] Cost estimation
- [ ] Plugin system
- [ ] Multiple AI providers

---

# 🤝 Contributing

Contributions, suggestions and ideas are welcome.

If you'd like to improve DataForge, feel free to open:

- Issues
- Pull Requests
- Feature Requests

---

# 📄 License

Licensed under the **Apache License 2.0**.

See the **LICENSE** file for details.

---

<div align="center">

## Developed by **RGS Labs™**

Building tools for developers.

⭐ If you like this project, consider giving it a star.

<br>

Made with ❤️ by **RGS Labs™**

</div>
