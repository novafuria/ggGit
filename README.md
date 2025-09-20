# ggGit <!-- omit in toc -->

***Fast Git commands with full support for Conventional Commits and AI-powered commit message generation***

<div align="center">

&nbsp;

[![License: NIL](https://img.shields.io/badge/License-NIL-yellow.svg)](./LICENSE)
[![Contributor covenant: 3.0](https://img.shields.io/badge/Contributor%20Covenant-3.0-4baaaa.svg)](./CODE_OF_CONDUCT.md)
[![Semantic Versioning: 2.0.0](https://img.shields.io/badge/Semantic--Versioning-2.0.0-a05f79?logo=semantic-release&logoColor=f97ff0)](https://semver.org/)

[![Labeling](https://github.com/novafuria/ggGit/actions/workflows/labeling.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/labeling.yml)
[![Test ggGit Commands](https://github.com/novafuria/ggGit/actions/workflows/test-commands.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/test-commands.yml)
[![Cross-Platform Testing](https://github.com/novafuria/ggGit/actions/workflows/cross-platform-test.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/cross-platform-test.yml)
[![Continuous Integration](https://github.com/novafuria/ggGit/actions/workflows/ci.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/ci.yml)
[![Liberation](https://github.com/novafuria/ggGit/actions/workflows/liberation.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/liberation.yml)
[![Dependabot Updates](https://github.com/novafuria/ggGit/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/dependabot/dependabot-updates)

[Bug Report](./issues/new?assignees=&labels=bug%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=1-bug-report.yml&title=...+is+broken)
⭕
[Feature Request](./issues/new?assignees=&labels=enhancement%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=2-feature-request.yml&title=As+a+%5Btype+of+user%5D%2C+I+want+%5Ba+goal%5D+so+that+%5Bbenefit%5D)
⭕
[Help Wanted](./issues/new?assignees=&labels=help+wanted%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=3-help-wanted.yml&title=I+need+help+with...)

[![Share on X](https://img.shields.io/twitter/url?label=Share%20on%20Twitter&style=social&url=https%3A%2F%2Fgithub.com%2Fatapas%2Fmodel-repo)](https://twitter.com/intent/tweet?text=👋%20Check%20this%20amazing%20repo%20https://github.com/novafuria/ggGit,%20created%20by%20@_novafuria%0A%0A%23Git%20%23Coding%20%23DevOps)

&nbsp;

</div>

## Tabla de Contenidos <!-- omit in toc -->

- [✋ Introducing `ggGit`](#-introducing-gggit)
  - [🚀 Key Features](#-key-features)
- [🚀 Quick Start](#-quick-start)
  - [1. Install ggGit](#1-install-gggit)
  - [2. Configure AI (Recommended)](#2-configure-ai-recommended)
  - [3. Use it!](#3-use-it)
- [📚 Documentation](#-documentation)
- [🤖 AI Features](#-ai-features)
  - [Supported AI Providers](#supported-ai-providers)
- [📋 Available Commands](#-available-commands)
  - [Conventional Commits](#conventional-commits)
  - [Git Operations](#git-operations)
  - [Branch Management](#branch-management)
  - [Remote Operations](#remote-operations)
  - [AI \& Configuration](#ai--configuration)
- [🧭 Vibedoc Methodology](#-vibedoc-methodology)
- [🤝 Contributing](#-contributing)
  - [Development Setup](#development-setup)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

## ✋ Introducing `ggGit`

ggGit is a suite of 26 independent Git commands that simplify your workflow with **Conventional Commits** and **AI-powered commit message generation**. Built with Python and designed for developers who want to work faster and more consistently.

### 🚀 Key Features

- **26 Git Commands**: Complete set of Git operations with consistent interface
- **AI-Powered Commits**: Automatic commit message generation using real AI (Ollama)
- **Conventional Commits**: Built-in support for standardized commit messages
- **Hierarchical Configuration**: Project, user, and team-specific settings
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **Zero Dependencies**: No complex setup, just clone and use

## 🚀 Quick Start

### 1. Install ggGit
```bash
# Clone the repository
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Install (Linux/macOS)
python install.py

# Install (Windows)
.\install.ps1
```

### 2. Configure AI (Recommended)
```bash
# Enable AI features
ggconfig set ai.enabled true

# Configure for Ollama (local AI)
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama

# Test AI connection
ggai test
```

### 3. Use it!
```bash
# Make a feature commit (AI generates message)
ggfeat

# Make a bug fix (AI generates message)
ggfix

# Check status
ggs
```

## 📚 Documentation

- **[Installation Guide](docs/installation.md)** - Detailed installation instructions
- **[AI Configuration](docs/ai-setup.md)** - Complete AI setup guide
- **[Command Reference](docs/commands.md)** - All 26 commands explained
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[Development Guide](docs/development.md)** - Contributing and development

## 🤖 AI Features

ggGit includes **real AI integration** using Ollama for intelligent commit message generation:

- **Automatic Generation**: Run any commit command without arguments
- **Context-Aware**: AI understands your changes and commit type
- **Local Processing**: Uses Ollama for privacy and speed
- **Cost-Free**: No API costs with local models
- **Smart Fallbacks**: Clear error messages when AI isn't available

### Supported AI Providers

| Provider | Type | Setup | Cost |
|----------|------|-------|------|
| **Ollama (Recommended)** | Local | `ollama pull gemma3:4b` | Free |
| **OpenAI** | Cloud | API key required | Pay-per-use |
| **Anthropic** | Cloud | API key required | Pay-per-use |
| **Azure OpenAI** | Cloud | Enterprise setup | Pay-per-use |

## 📋 Available Commands

### Conventional Commits
- `ggfeat` - Feature commits
- `ggfix` - Bug fix commits  
- `ggdocs` - Documentation commits
- `ggstyle` - Code style commits
- `ggrefactor` - Refactoring commits
- `ggtest` - Test commits
- `ggchore` - Maintenance commits
- `ggperf` - Performance commits
- `ggci` - CI/CD commits
- `ggbuild` - Build system commits
- `ggbreak` - Breaking change commits

### Git Operations
- `gga` - Git add
- `ggs` - Git status
- `ggl` - Git log
- `ggdif` - Git diff
- `ggunstage` - Git unstage
- `ggreset` - Git reset

### Branch Management
- `ggmain` - Switch to main branch
- `ggdevelop` - Switch to develop branch
- `ggb` - Create/switch branches
- `ggmerge` - Merge branches

### Remote Operations
- `ggpl` - Git pull
- `ggpp` - Git push

### AI & Configuration
- `ggai` - AI commands and testing
- `ggconfig` - Configuration management
- `ggv` - Version information

## 🧭 Vibedoc Methodology

This project follows the **Vibedoc methodology** for collaborative human-AI design:

- **Documentation as Product**: Comprehensive documentation drives development
- **Iterative Design**: Continuous refinement through dialogue
- **Traceable Decisions**: All decisions documented in zettelkasten
- **Quality Focus**: Design before code, clarity before complexity

Learn more: [Vibedoc Documentation](.vibedoc/README.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Install in development mode
python install.py
```

## 📄 License

This project is licensed under the NIL License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Vibedoc Methodology** - For structured design approach
- **Conventional Commits** - For commit message standardization
- **Ollama** - For local AI capabilities
- **Click** - For CLI framework
- **All Contributors** - For making this project better

---

<div align="center">

**Made with ❤️ by [Novafuria](https://github.com/novafuria)**

[Website](https://novafuria.com) • [Documentation](docs/) • [Issues](https://github.com/novafuria/ggGit/issues) • [Discussions](https://github.com/novafuria/ggGit/discussions)

</div>