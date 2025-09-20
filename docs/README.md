# ggGit Documentation

Welcome to the ggGit documentation! This guide covers everything you need to know about installing, configuring, and using ggGit.

## 📚 Documentation Index

### Getting Started
- **[Installation Guide](installation.md)** - Detailed installation instructions for all platforms
- **[AI Configuration](ai-setup.md)** - Complete guide to setting up AI features
- **[Command Reference](commands.md)** - All 26 commands explained with examples

### Configuration
- **[Configuration Guide](configuration.md)** - Hierarchical configuration system
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
- **[Development Guide](development.md)** - Contributing and development setup

### Examples
- **[Usage Examples](examples.md)** - Real-world examples and workflows
- **[Best Practices](best-practices.md)** - Tips for effective use

## 🚀 Quick Start

### 1. Install ggGit
```bash
git clone https://github.com/novafuria/ggGit.git
cd ggGit
python install.py
```

### 2. Configure AI (Recommended)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull gemma3:4b

# Configure ggGit
ggconfig set ai.enabled true
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama
```

### 3. Use it!
```bash
ggfeat    # AI generates commit message
ggfix     # AI generates commit message
ggs       # Check status
```

## 🤖 AI Features

ggGit includes **real AI integration** for intelligent commit message generation:

- **Local Processing**: Uses Ollama for privacy and speed
- **Context-Aware**: AI understands your changes and commit type
- **Cost-Free**: No API costs with local models
- **Smart Fallbacks**: Clear error messages when AI isn't available

### Supported AI Providers

| Provider | Type | Setup | Cost |
|----------|------|-------|------|
| **Ollama (Recommended)** | Local | `ollama pull gemma3:4b` | Free |
| **OpenAI** | Cloud | API key required | Pay-per-use |
| **Anthropic** | Cloud | API key required | Pay-per-use |
| **Azure OpenAI** | Cloud | Enterprise setup | Pay-per-use |

## 📋 Command Categories

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

Learn more: [Vibedoc Documentation](../.vibedoc/README.md)

## 🆘 Need Help?

### Common Issues
- **"IA no configurada" error**: Check [AI Configuration](ai-setup.md)
- **Commands not found**: Check [Installation Guide](installation.md)
- **Slow AI responses**: Check [Troubleshooting](troubleshooting.md)

### Getting Support
1. **Check this documentation** first
2. **Search existing issues**: [GitHub Issues](https://github.com/novafuria/ggGit/issues)
3. **Ask a question**: [GitHub Discussions](https://github.com/novafuria/ggGit/discussions)
4. **Report a bug**: [Open an issue](https://github.com/novafuria/ggGit/issues/new)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](../CONTRIBUTING.md) for details.

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

This project is licensed under the NIL License - see the [LICENSE](../LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by [Novafuria](https://github.com/novafuria)**

[Website](https://novafuria.com) • [GitHub](https://github.com/novafuria/ggGit) • [Issues](https://github.com/novafuria/ggGit/issues) • [Discussions](https://github.com/novafuria/ggGit/discussions)

</div>
