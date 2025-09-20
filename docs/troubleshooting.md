# Troubleshooting Guide

This guide helps you resolve common issues with ggGit installation, configuration, and usage.

## 🚨 Common Issues

### AI Configuration Issues

#### "IA no configurada" Error
**Symptoms**: Commands show "IA no configurada" message
**Cause**: Environment variable mismatch between configuration and actual environment
**Solution**:
```bash
# Check current configuration
ggconfig list

# Fix environment variable (this is the most common issue)
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama

# Test AI connection
ggai test
```

**Why this happens**: The default configuration expects `OPENAI_API_KEY` but Ollama works better with `GGGIT_AI_KEY`.

#### Ollama Connection Failed
**Symptoms**: AI commands fail with connection error
**Cause**: Ollama not running or wrong URL
**Solution**:
```bash
# Start Ollama
ollama serve

# Check if running
curl http://localhost:11434/api/tags

# Fix URL if needed (note: no /v1 at the end)
ggconfig set ai.base_url http://localhost:11434

# Test connection
ggai test
```

#### Model Not Found
**Symptoms**: "Model not found" error
**Cause**: Model not pulled or wrong name
**Solution**:
```bash
# List available models
ollama list

# Pull the recommended model
ollama pull gemma3:4b

# Update configuration
ggconfig set ai.model gemma3:4b

# Test again
ggai test
```

#### Slow AI Responses
**Symptoms**: AI commands take too long
**Cause**: Large model or insufficient system resources
**Solution**:
```bash
# Use smaller, faster model
ollama pull llama3.2:3b
ggconfig set ai.model llama3.2:3b

# Or use the recommended balanced model
ollama pull gemma3:4b
ggconfig set ai.model gemma3:4b

# Ensure Ollama is running
ollama serve
```

### Installation Issues

#### Commands Not Found
**Symptoms**: `ggfeat: command not found`
**Cause**: Aliases not set up correctly
**Solution**:
```bash
# Re-run installation
python install.py

# Reload shell configuration
source ~/.bashrc  # or ~/.zshrc

# Or restart terminal
```

#### Permission Denied
**Symptoms**: Permission errors when running commands
**Cause**: File permissions or Python path issues
**Solution**:
```bash
# Make scripts executable
chmod +x src/commands/*.py

# Check Python path
echo $PYTHONPATH

# Fix Python path
export PYTHONPATH="$GGGIT_ROOT/src:$PYTHONPATH"
```

#### Python Not Found
**Symptoms**: `python: command not found`
**Cause**: Python not installed or not in PATH
**Solution**:
```bash
# Install Python 3.12+ (recommended)
# Ubuntu/Debian
sudo apt update
sudo apt install python3.12 python3.12-pip

# macOS
brew install python@3.12

# Windows
# Download from https://python.org

# Verify installation
python3 --version
```

### Git Issues

#### Not a Git Repository
**Symptoms**: "Not a git repository" error
**Cause**: Not in a Git repository
**Solution**:
```bash
# Initialize Git repository
git init

# Or navigate to existing repository
cd /path/to/your/git/repo
```

#### Nothing to Commit
**Symptoms**: "Nothing to commit" error
**Cause**: No changes staged or no changes at all
**Solution**:
```bash
# Check status
ggs

# Stage changes
gga

# Or stage specific files
git add filename.py

# Then commit
ggfeat
```

#### Merge Conflicts
**Symptoms**: Merge conflicts when using ggmerge
**Cause**: Conflicting changes in files
**Solution**:
```bash
# Resolve conflicts manually
# Edit conflicted files
# Remove conflict markers

# Continue merge
ggmerge --continue

# Or abort merge
ggmerge --abort
```

## 🔍 Debug Commands

### Check Configuration
```bash
# View all configuration
ggconfig list

# Check specific setting
ggconfig get ai.enabled
ggconfig get ai.api_key_env
ggconfig get ai.base_url
```

### Test AI Connection
```bash
# Test AI connection
ggai test

# Test with specific model
ollama run gemma3:4b "Generate a commit message for: fix bug in login"
```

### Check Ollama Status
```bash
# List available models
ollama list

# Check running models
ollama ps

# Test Ollama API
curl http://localhost:11434/api/tags
```

### Check Git Status
```bash
# Check Git status
ggs

# Check current branch
git branch

# Check remote
git remote -v
```

## 🛠️ Advanced Troubleshooting

### Environment Variables
```bash
# Check all environment variables
env | grep -i gggit
env | grep -i ollama

# Set environment variables
export GGGIT_ROOT="/path/to/ggGit"
export PYTHONPATH="$GGGIT_ROOT/src:$PYTHONPATH"
export GGGIT_AI_KEY=ollama
```

### Python Path Issues
```bash
# Check Python path
python3 -c "import sys; print(sys.path)"

# Add ggGit to Python path
export PYTHONPATH="/path/to/ggGit/src:$PYTHONPATH"

# Test import
python3 -c "from core.config import ConfigManager; print('Import successful')"
```

### Ollama Issues
```bash
# Check Ollama logs
ollama logs

# Restart Ollama
pkill ollama
ollama serve

# Check Ollama configuration
ollama config

# Update Ollama
ollama update
```

### File Permissions
```bash
# Check file permissions
ls -la src/commands/

# Fix permissions
chmod +x src/commands/*.py

# Check ownership
ls -la src/commands/ggfeat.py
```

## 📊 Performance Issues

### Slow AI Responses
**Causes and Solutions**:

1. **Large Model**: Use smaller model
   ```bash
   ollama pull llama3.2:3b
   ggconfig set ai.model llama3.2:3b
   ```

2. **Insufficient RAM**: Close other applications
   ```bash
   # Check memory usage
   free -h  # Linux
   top      # macOS/Linux
   ```

3. **Slow Storage**: Use SSD instead of HDD
4. **Background Processes**: Stop unnecessary services

### Slow Git Operations
**Causes and Solutions**:

1. **Large Repository**: Use `.gitignore` to exclude unnecessary files
2. **Network Issues**: Check internet connection for remote operations
3. **File System**: Use faster storage (SSD)

## 🆘 Getting Help

### Before Asking for Help

1. **Check this guide**: Your issue might be covered here
2. **Check configuration**: Run `ggconfig list`
3. **Test AI connection**: Run `ggai test`
4. **Check logs**: Look for error messages
5. **Try restarting**: Restart terminal and Ollama

### When Reporting Issues

Include this information:

```bash
# System information
uname -a
python3 --version
git --version

# ggGit configuration
ggconfig list

# AI status
ggai test
ollama list

# Error messages
# (Copy the exact error message)
```

### Where to Get Help

1. **GitHub Issues**: [Open an issue](https://github.com/novafuria/ggGit/issues)
2. **Discussions**: [GitHub Discussions](https://github.com/novafuria/ggGit/discussions)
3. **Documentation**: Check [docs/](docs/) folder
4. **Vibedoc**: Check [.vibedoc/](.vibedoc/) for design decisions

## 🔧 Configuration Reference

### Complete AI Setup
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull model
ollama pull gemma3:4b

# Configure ggGit
ggconfig set ai.enabled true
ggconfig set ai.provider openai
ggconfig set ai.api_key_env GGGIT_AI_KEY
ggconfig set ai.model gemma3:4b
ggconfig set ai.base_url http://localhost:11434

# Set environment
export GGGIT_AI_KEY=ollama

# Test
ggai test
```

### Complete Installation
```bash
# Clone repository
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Install
python install.py

# Configure environment
export GGGIT_ROOT="$(pwd)"
export PYTHONPATH="$GGGIT_ROOT/src:$PYTHONPATH"

# Test
ggv --help
```

---

**Still having issues?** [Open an issue](https://github.com/novafuria/ggGit/issues) with the information above, and we'll help you resolve it!
