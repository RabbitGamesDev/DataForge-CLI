<div align="center">

# 🛠️ DataForge CLI

### Your AI consultant inside the terminal.

**Understand. Analyze. Document.**

Transform complex codebases into actionable technical knowledge using AI-powered analysis directly from your terminal.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-F55036?style=for-the-badge)
![Platform](https://img.shields.io/badge/Windows-macOS-Linux-4CAF50?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

**DataForge CLI** is an AI-powered toolkit that helps developers understand, analyze and document any codebase in minutes.

Built with a **Local-first. Fast. Professional.** philosophy.

</div>

---

# ✨ Overview

Modern software projects grow fast.

Understanding an unfamiliar codebase, documenting it properly, or auditing hundreds of files can easily consume hours—or even days.

**DataForge CLI** was created to eliminate that friction.

Instead of manually reading every file, DataForge analyzes your project, understands its structure, extracts meaningful information using AI, and generates clear, structured reports directly from your terminal.

Whether you're joining an existing project, auditing legacy software, documenting your own code, or exploring an open-source repository, DataForge helps you spend less time reading code and more time building software.

---

# 🎯 Philosophy

DataForge follows three simple principles.

| Principle           | Description                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 🔒 **Local-first**  | Your files remain on your computer whenever possible. Only the extracted text required for AI analysis is processed. |
| ⚡ **Fast**          | Built around Groq's ultra-fast inference to minimize waiting time.                                                   |
| 💼 **Professional** | Clean architecture, modular code and production-ready workflows.                                                     |

---

# 🚀 Why DataForge?

Most AI developer tools focus on **writing code**.

DataForge focuses on **understanding it.**

It helps developers:

* 📖 Understand unfamiliar repositories.
* 📄 Generate technical documentation.
* 🧠 Explain complex source code.
* 🗺️ Visualize project architecture.
* 🚀 Speed up developer onboarding.
* ⏱️ Reduce manual analysis time.

---

# ✨ Features

| Feature                    | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| 🔍 Smart Scan              | Analyze complete projects automatically.                    |
| 🤖 AI Explanations         | Explain files and source code in plain language.            |
| 📄 Documentation Generator | Produce professional technical reports.                     |
| 🗺️ Architecture Map       | Generate project structure maps directly from the terminal. |
| 💬 Interactive AI          | Ask questions about your own codebase.                      |
| ⚡ Dry Run Mode             | Estimate token usage before processing.                     |
| 🔄 Resume Support          | Continue interrupted scans automatically.                   |
| 📊 Cost Reports            | Transparent token usage and estimated costs.                |
| 📂 Multi-format Support    | Analyze source code, text files and documentation.          |
| 🛡️ Secure Configuration   | API Keys stored locally and never committed to Git.         |

---

# ⚡ Quick Start

## Requirements

* Python **3.10** or newer
* A free **Groq API Key**
* Internet connection for AI requests

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RabbitGamesDev/DataForge-CLI.git
cd DataForge-CLI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run DataForge:

```bash
python main.py
```

---

# 🔑 Getting a Groq API Key

DataForge uses the Groq API for AI-powered analysis.

Creating an API key only takes a few minutes.

1. Visit **https://console.groq.com/**
2. Sign in or create a free account.
3. Open **API Keys**.
4. Click **Create API Key**.
5. Copy your key.

During the first launch, DataForge will ask for your API Key and securely save your configuration locally.

Your API key is never uploaded to GitHub.

---

# ⚙️ Configuration

Run:

```bash
dataforge config
```

The setup wizard lets you configure:

* Groq API Key
* Preferred language
* Output format
* Default model
* Report location

---

# 💻 Commands

| Command     | Description                          |
| ----------- | ------------------------------------ |
| `scan`      | Analyze an entire project.           |
| `explain`   | Explain a specific file.             |
| `map`       | Generate a project architecture map. |
| `ask`       | Start an interactive AI session.     |
| `config`    | Configure DataForge.                 |
| `--dry-run` | Estimate tokens before processing.   |

---

# 📖 Example Workflow

```text
Project Folder
      │
      ▼
dataforge scan .
      │
      ▼
AI Analysis
      │
      ▼
Technical Report
      │
      ▼
Developer
```

---

# 📂 Project Structure

```text
DataForge-CLI/
│
├── dataforge/
│   ├── core/
│   ├── ai/
│   ├── cli/
│   ├── config/
│   ├── reports/
│   └── utils/
│
├── docs/
├── tests/
├── requirements.txt
├── main.py
├── LICENSE
├── README.md
└── .gitignore
```

---

# 🛣️ Roadmap

## Version 1.0

* [x] Interactive configuration
* [x] Groq integration
* [x] Smart project scanning
* [x] AI explanations
* [x] Professional report generation

## Version 1.5

* [ ] PDF export
* [ ] Markdown export
* [ ] JSON reports
* [ ] Interactive dashboard

## Version 2.0

* [ ] Plugin system
* [ ] Multi-provider AI support
* [ ] Local LLM support
* [ ] Project memory
* [ ] Team collaboration

---

# 🔒 Security

DataForge was designed with privacy in mind.

* API Keys remain local.
* Sensitive files are ignored by default.
* No project files are modified.
* Reports are generated separately from your source code.

If you discover a security issue, please open a private report before creating a public issue.

---

# 🤝 Contributing

Contributions, bug reports and feature suggestions are welcome.

Please read the **CONTRIBUTING.md** guide before submitting a Pull Request.

---

# 📄 License

This project is licensed under the **Apache License 2.0**.

See the **LICENSE** file for more information.

---

<div align="center">

# Developed by RGS Labs™

### Building intelligent tools for developers.

⭐ If DataForge helped you, consider giving this repository a star.

</div>
