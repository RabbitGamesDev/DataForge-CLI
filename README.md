<div align="center">

# 🛠️ DataForge CLI

### Your AI consultant inside the terminal.

**Understand. Analyze. Organize.**

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
> **New to GitHub?**
>
> No worries. DataForge can be installed simply by downloading the repository as a ZIP file—no Git knowledge required.

</div>

---

# 📖 Overview

Reading hundreds of documents, source files or project folders takes time.

**DataForge CLI** helps automate that process.

Instead of manually opening every file, DataForge scans your project, extracts useful information and uses AI to generate organized summaries directly inside your terminal.

The project is designed to be lightweight, easy to configure and respectful of your privacy.

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

---

## 📦 Option 1 — Download as ZIP (Recommended)

If you don't have Git installed, this is the easiest way.

### Step 1

Open the GitHub repository.

### Step 2

Click the green **Code** button.

### Step 3

Select **Download ZIP**.

### Step 4

Extract the downloaded ZIP file anywhere on your computer.

After extracting, you should have a folder similar to this:

```text
DataForge-CLI/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
│
└── dataforge-cli/
    ├── main.py
    ├── requirements.txt
    ├── dataforge/
    └── ...
```

### Step 5

Open the **dataforge-cli** folder.

### Step 6

Open a terminal inside that folder.

On **Windows**:

- Hold **Shift**
- Right click inside the folder
- Select **Open in Terminal**

Or simply open the folder in **Visual Studio Code** and use:

```
Terminal → New Terminal
```

### Step 7

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 8

Run DataForge CLI:

```bash
python main.py
```

On the first launch, DataForge will automatically guide you through the initial setup, including your **Groq API Key**.

---

## 💻 Option 2 — Clone with Git

If you already have Git installed:

```bash
git clone https://github.com/RabbitGamesDev/DataForge-CLI.git
cd DataForge-CLI/dataforge-cli
pip install -r requirements.txt
python main.py
```

---

# 🔑 Getting your Groq API Key

DataForge uses Groq to power its AI features.

Getting an API Key only takes a minute.

### Step 1

Create a free account at:

https://console.groq.com/

---

### Step 2

Open:

https://console.groq.com/keys

---

### Step 3

Click

```
Create API Key
```

---

### Step 4

Copy the generated key.

It will look similar to:

```
gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 5

Launch DataForge.

During the first execution you'll be asked:

```
Enter your Groq API Key:
```

Paste it and press ENTER.

Your key will be stored locally on your own computer.

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

</div>
