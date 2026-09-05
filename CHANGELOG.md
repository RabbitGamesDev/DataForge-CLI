# Changelog

All notable changes to **DataForge CLI** will be documented in this file.

This project follows the **Keep a Changelog** format and adheres to **Semantic Versioning (SemVer)**.

- 📖 https://keepachangelog.com/en/1.1.0/
- 🔖 https://semver.org/

---

## [1.0.0] - 2026-07-01

### 🚀 Initial Release

This is the first public release of **DataForge CLI**.

### ✨ Added

- Initial architecture of the DataForge CLI toolkit.
- AI-powered code analysis using the **Groq API**.
- Interactive command-line interface (CLI).
- Project scanning and technical auditing.
- Context-aware file explanation.
- ASCII project architecture mapping.
- AI-powered project onboarding generation.
- Automatic report generation in plain text.
- Cross-platform support for Windows, macOS and Linux.
- Local-first configuration philosophy.
- Secure local API Key storage.
- Professional project documentation.
- Apache 2.0 License.
- Initial GitHub repository structure.

### 🔒 Security

- Sensitive files excluded through `.gitignore`.
- API Keys are never committed to the repository.
- Reports are generated separately from the analyzed project.

### 📚 Documentation

The first public documentation includes:

- README
- LICENSE
- CONTRIBUTING
- SECURITY
- CHANGELOG

---

## Upcoming

Future releases are expected to include:

- PDF and Markdown export.
- Multiple AI provider support.
- Configuration command (`dataforge config`).
- Cost estimation (`--dry-run`).
- Checkpoint recovery system.
- Additional report formats.
- Plugin architecture.


---

## [2.0.0] - 2026-09-05

### 🚀 Major Release: Ecosystem & Multi-Provider Upgrade

This release brings a complete overhaul to DataForge CLI, transitioning into a full hybrid web-and-CLI ecosystem with advanced multi-provider support, local caching, and a professional user dashboard.

### ✨ Added

- **Multi-Provider LLM API Support**: Expanded beyond initial Groq integration to support flexible multi-provider routing.
- **Advanced CLI Pro Commands (`pro_commands.py`)**: Added dedicated modules for enhanced execution and power features.
- **Hybrid Licensing & Web Dashboard**: 
  - Integrated Supabase license verification with local offline caching.
  - Web frontend management synced via URL parameters from Lemon Squeezy.
  - Management portal and web assets (`index.html`, favicon suite, and configuration interfaces).
- **Token Optimization**: Integrated `tiktoken` for advanced token tracking and cost optimization.
- **Robust Configuration Management**: New config handling (`config_manager.py`) and API communication layer (`api_handler.py`).
- **Comprehensive Marketing & Media Assets**: Included official launch trailers, teasers, promotional artwork, and production elements for community rollout.

---

