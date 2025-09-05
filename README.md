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

&nbsp;

- [✋ Introducing `ggGit`](#-introducing-gggit)
- [🧭 Vibedoc Methodology](#-vibedoc-methodology)
- [🚀 Installation](#-installation)
  - [🚀 Quick Installation (Recommended)](#-quick-installation-recommended)
  - [🐍 Development Environment](#-development-environment)
  - [📋 Manual Installation](#-manual-installation)
    - [Install in Linux Systems](#install-in-linux-systems)
    - [Install in Windows (PowerShell)](#install-in-windows-powershell)
- [🤖 AI Configuration](#-ai-configuration)
  - [Quick AI Setup](#quick-ai-setup)
  - [AI Features](#ai-features)
- [📚 Available Commands](#-available-commands)
  - [🔧 Basic Git Operations](#-basic-git-operations)
  - [🌿 Branch Management](#-branch-management)
  - [📤 Remote Operations](#-remote-operations)
  - [📝 Conventional Commits (with AI Support)](#-conventional-commits-with-ai-support)
  - [🤖 AI Commands](#-ai-commands)
  - [⚙️ Configuration](#️-configuration)
  - [ℹ️ Information](#ℹ️-information)
- [💡 Usage Examples](#-usage-examples)
  - [Basic Workflow with AI](#basic-workflow-with-ai)
  - [AI-Powered Commits](#ai-powered-commits)
  - [Conventional Commits](#conventional-commits)
  - [Branch Management](#branch-management)
  - [Configuration Management](#configuration-management)
  - [AI Usage Tracking](#ai-usage-tracking)
- [🔧 Command Options](#-command-options)
  - [Global Options](#global-options)
  - [Conventional Commit Options](#conventional-commit-options)
  - [AI Configuration Options](#ai-configuration-options)
- [🏗️ Architecture](#️-architecture)
  - [Core Components](#core-components)
  - [AI Components](#ai-components)
  - [Configuration System](#configuration-system)
- [📋 Requirements](#-requirements)
- [🐛 Troubleshooting](#-troubleshooting)
  - [Quick Health Check](#quick-health-check)
  - [Command not found](#command-not-found)
  - [Permission denied](#permission-denied)
  - [Configuration Issues](#configuration-issues)
  - [AI Issues](#ai-issues)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [📜 Code of Conduct](#-code-of-conduct)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [📚 Documentation](#-documentation)

## ✋ Introducing `ggGit`

`ggGit` is a fast, intelligent Git command line tool with full support for Conventional Commits and AI-powered commit message generation. Built with a clean architecture and comprehensive configuration system, it helps you work with Git more efficiently and intelligently.

**Key Features:**
- 🤖 **AI-powered commit messages** with intelligent complexity analysis
- 📝 **Conventional Commits** with full validation and support
- ⚙️ **Hierarchical configuration** system with validation
- 🧠 **Smart decision making** between AI generation and educational fallback
- 📊 **Usage tracking** and cost management for AI features
- 🏗️ **Clean architecture** with modular, testable components

## 🧭 Vibedoc Methodology

This project follows the **Vibedoc** methodology for collaborative human-AI design. Vibedoc emphasizes clear documentation, iterative dialogue, and thoughtful design before coding. Our project documentation is maintained in the [`.vibedoc/`](./.vibedoc/) directory, following a structured approach to product development.

**Current Stage**: Implementation Complete ✅  
**Methodology Status**: Fully Adopted and Validated ✅

Learn more about our methodology: [Vibedoc Documentation](./.vibedoc/README.md)

## 🚀 Installation

The installation process is simple and fast. You can use our automatic installation scripts or manually configure your PATH.

### 🚀 Quick Installation (Recommended)

**Linux/macOS:**
```bash
git clone https://github.com/novafuria/ggGit
cd ggGit
# Set up development environment
conda env create -f environment.yml
conda activate gggit
# Or with mamba (if available):
# mamba env create -f environment.yml
# mamba activate gggit
./install.sh
```

**Windows:**
```powershell
git clone https://github.com/novafuria/ggGit
cd ggGit
# Set up development environment
conda env create -f environment.yml
conda activate gggit
# Or with mamba (if available):
# mamba env create -f environment.yml
# mamba activate gggit
.\install.ps1
```

### 🐍 Development Environment

ggGit uses conda/mamba for dependency management, ensuring a reproducible development environment:

- **Python 3.12** (recommended version)
- **Click** for CLI framework
- **PyYAML** for configuration management
- **Colorama** for cross-platform colors
- **jsonschema** for configuration validation
- **pytest** for comprehensive testing

The `environment.yml` file defines all dependencies and can be used with both conda and mamba.

### 📋 Manual Installation

If you prefer to install manually, follow these steps:

#### Install in Linux Systems

> [!NOTE]
> The installation process is the same for Bash emulation in Windows.

1. **Clone the repository**
```bash
git clone https://github.com/novafuria/ggGit
cd ggGit
```

2. **Make scripts executable**
```bash
chmod +x commands/*
```

3. **Add the path to the `PATH` environment variable in the `.bashrc` file**
```bash
echo "export PATH=\$PATH:$(pwd)/commands" >> ~/.bashrc
```

> [!NOTE]
> If you are using `zsh`, you need to add the path to the `PATH` environment variable in the `.zshrc` file.

4. **Reload the `.bashrc` file**
```bash
source ~/.bashrc
```

5. **Check the installation**
```bash
ggv
```

#### Install in Windows (PowerShell)

1. **Clone the repository**
```powershell
git clone https://github.com/novafuria/ggGit
cd ggGit
```

2. **Add to PATH environment variable**
```powershell
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
$newPath = "$currentPath;$(Get-Location)\commands"
[Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
```

3. **Restart your terminal and test**
```powershell
ggv
```

## 🤖 AI Configuration

ggGit includes intelligent AI-powered commit message generation. Configure it once and enjoy automatic, context-aware commit messages.

### Quick AI Setup

```bash
# Enable AI features
ggconfig set ai.enabled true

# Configure AI provider (OpenAI, Anthropic, Azure, or local)
ggconfig set ai.provider openai

# Set your API key
export OPENAI_API_KEY="your-api-key-here"

# Configure model
ggconfig set ai.model gpt-3.5-turbo

# Set cost limit (optional)
ggconfig set ai.cost_limit 5.00
```

### AI Features

- **Automatic activation**: Run any commit command without arguments to trigger AI
- **Intelligent analysis**: AI decides when to generate vs. show educational fallback
- **Usage tracking**: Monitor AI consumption and costs
- **Flexible configuration**: Support for multiple AI providers
- **Cost management**: Set limits and track usage

## 📚 Available Commands

### 🔧 Basic Git Operations

| Command | Description | Usage |
|---------|-------------|-------|
| `gga` | Add files to staging area | `gga [file...]` |
| `ggs` | Show git status | `ggs [options]` |
| `ggl` | Show git log with graph | `ggl [options]` |
| `ggdif` | Show changes between commits | `ggdif [options]` |
| `ggunstage` | Unstage changes | `ggunstage [file...]` |
| `ggreset` | Reset to last commit | `ggreset` |

### 🌿 Branch Management

| Command | Description | Usage |
|---------|-------------|-------|
| `ggmain` | Checkout main branch | `ggmain` |
| `ggdevelop` | Checkout develop branch | `ggdevelop` |
| `ggb` | Create and checkout new branch | `ggb <branch-name>` |
| `ggmerge` | Merge branches (no fast-forward) | `ggmerge [branch]` |

### 📤 Remote Operations

| Command | Description | Usage |
|---------|-------------|-------|
| `ggpl` | Pull all branches and tags | `ggpl` |
| `ggpp` | Push current branch | `ggpp` |

### 📝 Conventional Commits (with AI Support)

| Command | Description | Usage |
|---------|-------------|-------|
| `ggfeat` | Commit with feat prefix | `ggfeat [-s scope] [message]` |
| `ggfix` | Commit with fix prefix | `ggfix [-s scope] [message]` |
| `ggdocs` | Commit with docs prefix | `ggdocs [-s scope] [message]` |
| `ggstyle` | Commit with style prefix | `ggstyle [-s scope] [message]` |
| `ggchore` | Commit with chore prefix | `ggchore [-s scope] [message]` |
| `ggbuild` | Commit with build prefix | `ggbuild [-s scope] [message]` |
| `ggci` | Commit with ci prefix | `ggci [-s scope] [message]` |
| `ggperf` | Commit with perf prefix | `ggperf [-s scope] [message]` |
| `ggtest` | Commit with test prefix | `ggtest [-s scope] [message]` |
| `ggbreak` | Commit with break prefix | `ggbreak [-s scope] [message]` |

### 🤖 AI Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `ggai` | Generate AI commit message | `ggai` |
| `ggai usage` | Show AI usage statistics | `ggai usage` |
| `ggai usage reset` | Reset AI usage counters | `ggai usage reset` |
| `ggai test` | Test AI connection | `ggai test` |

### ⚙️ Configuration

| Command | Description | Usage |
|---------|-------------|-------|
| `ggconfig` | Manage configuration | `ggconfig [get|set|list|reset] [key] [value]` |

### ℹ️ Information

| Command | Description | Usage |
|---------|-------------|-------|
| `ggv` | Show latest tag | `ggv` |

## 💡 Usage Examples

### Basic Workflow with AI

```bash
# Check status
ggs

# Add all changes
gga

# Commit with AI (if configured) or manual message
ggfeat  # AI will generate message based on changes
# OR
ggfeat -s auth Add user authentication system

# Push changes
ggpp
```

### AI-Powered Commits

```bash
# AI generates message automatically
ggfeat  # "feat: implement user authentication system"

# AI with scope
ggfix -s api  # "fix(api): resolve authentication token validation"

# Manual override
ggfeat -s auth "Add OAuth2 integration"
```

### Conventional Commits

```bash
# Feature commit
ggfeat Add new user dashboard

# Feature with scope
ggfeat -s api Add user endpoint

# Bug fix
ggfix -s auth Fix login validation

# Breaking change
ggbreak -s database Remove deprecated user table

# Documentation
ggdocs -s api Update API documentation

# Performance improvement
ggperf -s database Optimize user queries
```

### Branch Management

```bash
# Switch to main
ggmain

# Create and switch to new branch
ggb feature/new-dashboard

# Merge feature branch
ggmerge feature/new-dashboard

# Pull latest changes
ggpl
```

### Configuration Management

```bash
# Show current configuration
ggconfig list

# Set AI configuration
ggconfig set ai.enabled true
ggconfig set ai.provider openai
ggconfig set ai.model gpt-3.5-turbo

# Set cost limit
ggconfig set ai.cost_limit 10.00

# Reset configuration
ggconfig reset
```

### AI Usage Tracking

```bash
# Check AI usage
ggai usage

# Reset usage counters
ggai usage reset

# Test AI connection
ggai test
```

## 🔧 Command Options

### Global Options
All commands support:
- `-h, --help`: Display help message

### Conventional Commit Options
- `-a, --amend`: Amend the last commit
- `-s, --scope <scope>`: Add scope to commit message
- `--ai`: Use AI for message generation (legacy, now automatic)

### AI Configuration Options
- `ai.enabled`: Enable/disable AI features
- `ai.provider`: AI provider (openai, anthropic, azure, local)
- `ai.model`: AI model to use
- `ai.api_key_env`: Environment variable for API key
- `ai.cost_limit`: Maximum cost per period
- `ai.tracking_enabled`: Enable usage tracking

## 🏗️ Architecture

ggGit is built with a clean, modular architecture:

### Core Components
- **BaseCommand**: Base class for all commands with common functionality
- **ConfigManager**: Hierarchical configuration system with validation
- **GitInterface**: Unified interface for Git operations
- **Validation**: Comprehensive input validation with JSON Schema

### AI Components
- **ComplexityAnalyzer**: Intelligent analysis of changes for AI decision
- **AiMessageGenerator**: AI-powered commit message generation
- **AiUsageTracker**: Usage and cost tracking for AI features

### Configuration System
- **Hierarchical**: Repository > Module > User > Default
- **Validated**: JSON Schema validation for all configurations
- **Flexible**: Easy to extend with new configuration options

## 📋 Requirements

- Git installed and configured
- Python 3.12+ (for development)
- Bash (Linux/macOS) or PowerShell (Windows)
- Basic knowledge of Git commands
- API key for AI providers (optional)

## 🐛 Troubleshooting

### Quick Health Check
Run our health check script to diagnose issues:
```bash
./health-check.sh
```

### Command not found
If you get "command not found" error:
1. Verify the scripts are executable: `ls -la commands/`
2. Check PATH: `echo $PATH`
3. Re-source your shell configuration: `source ~/.bashrc`

### Permission denied
If you get permission errors:
```bash
chmod +x commands/*
```

### Configuration Issues
Use the `ggconfig` command to check your setup:
```bash
ggconfig list
```

### AI Issues
If AI features are not working:
1. Check AI configuration: `ggconfig get ai.enabled`
2. Verify API key: `echo $OPENAI_API_KEY`
3. Test connection: `ggai test`
4. Check usage: `ggai usage`

## 🧪 Testing

ggGit includes comprehensive tests with >80% coverage:

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src

# Run specific test categories
python -m pytest tests/test_commands.py
python -m pytest tests/test_ai_integration.py
```

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contributing guidelines.

## 📜 Code of Conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for community guidelines.

## 📄 License

See [LICENSE](./LICENSE) for license information.

## 🙏 Acknowledgments

- Conventional Commits specification
- Git community
- All contributors to this project
- Vibedoc methodology for collaborative design

## 📚 Documentation

- [Vibedoc Methodology](./.vibedoc/README.md)
- [Configuration Schema](./config/config-schema.yaml)
- [Development Environment](./environment.yml)
- [Health Check Script](./health-check.sh)

---

**Built with ❤️ using the Vibedoc methodology for collaborative human-AI design**