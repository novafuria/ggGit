# ggGit <!-- omit in toc -->

***Fast Git commands with full support for Conventional Commits***

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

## ✋ Introducing `ggGit`

`ggGit` is a fast Git command line tool with full support for Conventional Commits. Contains a set of commands to help you to work with Git in a more efficient way and easy to understand.

Internally, `ggGit` uses the `git` command to execute the operations.

## 🧭 Vibedoc Methodology

This project follows the **Vibedoc** methodology for collaborative human-AI design. Vibedoc emphasizes clear documentation, iterative dialogue, and thoughtful design before coding. Our project documentation is maintained in the [`.vibedoc/`](./.vibedoc/) directory, following a structured approach to product development.

**Current Stage**: Project Definition ✅  
**Next Stage**: Problem Research and Assessment 🔍

Learn more about our methodology: [Vibedoc Documentation](./.vibedoc/README.md)

## 🚀 Installation

The installation process is simple and fast. You can use our automatic installation scripts or manually configure your PATH.

### 🚀 Quick Installation (Recommended)

**Linux/macOS:**
```bash
git clone https://github.com/novafuria/ggGit
cd ggGit
./install.sh
```

**Windows:**
```powershell
git clone https://github.com/novafuria/ggGit
cd ggGit
.\install.ps1
```

### 📋 Manual Installation

If you prefer to install manually, follow these steps:

### Install in Linux Systems

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

### Install in Windows (PowerShell)

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
| `ggmaster` | Checkout master branch | `ggmaster` |
| `ggmerge` | Merge branches (no fast-forward) | `ggmerge [branch]` |

### 📤 Remote Operations

| Command | Description | Usage |
|---------|-------------|-------|
| `ggpl` | Pull all branches and tags | `ggpl` |
| `ggpp` | Push current branch | `ggpp` |

### 📝 Conventional Commits

| Command | Description | Usage |
|---------|-------------|-------|
| `ggfeat` | Commit with feat prefix | `ggfeat [-s scope] message` |
| `ggfix` | Commit with fix prefix | `ggfix [-s scope] message` |
| `ggbreak` | Commit with break prefix | `ggbreak [-s scope] message` |

### ℹ️ Information

| Command | Description | Usage |
|---------|-------------|-------|
| `ggv` | Show latest tag | `ggv` |
| `ggconfig` | Show Git and ggGit configuration | `ggconfig` |

## 💡 Usage Examples

### Basic Workflow
```bash
# Check status
ggs

# Add all changes
gga

# Commit with conventional commit
ggfeat -s auth Add user authentication system

# Push changes
ggpp
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
```

### Branch Management
```bash
# Switch to main
ggmain

# Merge feature branch
ggmerge feature/new-dashboard

# Pull latest changes
ggpl
```

## 🔧 Command Options

### Global Options
All commands support:
- `-h, --help`: Display help message

### Conventional Commit Options
- `-a, --amend`: Amend the last commit
- `-s, --scope <scope>`: Add scope to commit message

## 📋 Requirements

- Git installed and configured
- Bash (Linux/macOS) or PowerShell (Windows)
- Basic knowledge of Git commands

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
./commands/ggconfig
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
