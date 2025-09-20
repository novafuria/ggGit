# AI Configuration Guide

ggGit includes **real AI integration** for intelligent commit message generation. This guide covers everything you need to know about setting up and using AI features.

## 🚀 Quick Setup (Ollama - Recommended)

### 1. Install Ollama
```bash
# Linux/macOS
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Pull AI Model
```bash
# Pull recommended model (4B parameters, fast and accurate)
ollama pull gemma3:4b

# Alternative models
ollama pull llama3.2:3b    # Smaller, faster
ollama pull llama3.2:8b    # Larger, more accurate
```

### 3. Configure ggGit
```bash
# Enable AI features
ggconfig set ai.enabled true

# Configure for Ollama
ggconfig set ai.provider openai
ggconfig set ai.api_key_env GGGIT_AI_KEY
ggconfig set ai.model gemma3:4b
ggconfig set ai.base_url http://localhost:11434

# Set environment variable
export GGGIT_AI_KEY=ollama
```

### 4. Test AI Connection
```bash
# Test connection
ggai test

# Expected output:
# ✅ AI connection successful
# Model: gemma3:4b
# Provider: openai (Ollama)
```

### 5. Use AI Features
```bash
# Make commits with AI-generated messages
ggfeat    # AI generates feature commit message
ggfix     # AI generates bug fix commit message
ggdocs    # AI generates documentation commit message

# Test AI directly
ggai main  # Generate commit message for current changes
```

## 🔧 Advanced Configuration

### Environment Variables
The `ai.api_key_env` setting specifies which environment variable contains your API key:

```bash
# Default configuration (recommended)
ggconfig set ai.api_key_env "GGGIT_AI_KEY"
export GGGIT_AI_KEY=ollama

# Custom environment variable
ggconfig set ai.api_key_env "MY_CUSTOM_KEY"
export MY_CUSTOM_KEY=your-custom-key-here
```

### Base URL Configuration
For different AI providers, configure the base URL:

```bash
# Ollama (local) - RECOMMENDED
ggconfig set ai.base_url "http://localhost:11434"
ggconfig set ai.api_key_env "GGGIT_AI_KEY"
export GGGIT_AI_KEY=ollama

# OpenAI (cloud)
ggconfig set ai.base_url "https://api.openai.com/v1"
ggconfig set ai.api_key_env "OPENAI_API_KEY"
export OPENAI_API_KEY="sk-your-key-here"

# Anthropic (cloud)
ggconfig set ai.base_url "https://api.anthropic.com"
ggconfig set ai.api_key_env "ANTHROPIC_API_KEY"
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Azure OpenAI (enterprise)
ggconfig set ai.base_url "https://your-resource.openai.azure.com/openai/deployments/your-deployment"
ggconfig set ai.api_key_env "AZURE_OPENAI_API_KEY"
export AZURE_OPENAI_API_KEY="your-azure-key"
```

### Model Configuration
Choose the right model for your needs:

```bash
# Fast models (recommended for development)
ggconfig set ai.model "gemma3:4b"      # 4B parameters, very fast
ggconfig set ai.model "llama3.2:3b"   # 3B parameters, fastest

# Balanced models
ggconfig set ai.model "llama3.2:8b"   # 8B parameters, good balance
ggconfig set ai.model "qwen2.5:7b"    # 7B parameters, multilingual

# High-quality models (slower)
ggconfig set ai.model "llama3.1:8b"   # 8B parameters, high quality
ggconfig set ai.model "qwen2.5:14b"   # 14B parameters, very high quality
```

## 🛠️ Troubleshooting

### Common Issues

#### "IA no configurada" Error
**Symptoms**: Commands show "IA no configurada" message
**Cause**: Environment variable mismatch
**Solution**:
```bash
# Check current configuration
ggconfig list

# Fix environment variable
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama

# Test again
ggai test
```

#### Ollama Connection Failed
**Symptoms**: AI commands fail with connection error
**Cause**: Ollama not running or wrong URL
**Solution**:
```bash
# Start Ollama
ollama serve

# Check if running
curl http://localhost:11434/api/tags

# Fix URL if needed
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

# Pull the model
ollama pull gemma3:4b

# Update configuration
ggconfig set ai.model gemma3:4b

# Test again
ggai test
```

#### Slow AI Responses
**Symptoms**: AI commands take too long
**Cause**: Large model or system resources
**Solution**:
```bash
# Use smaller model
ollama pull llama3.2:3b
ggconfig set ai.model llama3.2:3b

# Or use faster model
ollama pull gemma3:4b
ggconfig set ai.model gemma3:4b
```

### Debug Commands

```bash
# Check AI configuration
ggconfig list

# Test AI connection
ggai test

# Check Ollama status
ollama list
ollama ps

# Test specific model
ollama run gemma3:4b "Generate a commit message for: fix bug in login"
```

## 📊 AI Features Explained

### How AI Works in ggGit

1. **Automatic Activation**: Run any commit command without arguments
2. **Context Analysis**: AI analyzes your changes and commit type
3. **Message Generation**: Creates appropriate commit message
4. **Smart Processing**: Cleans and formats the response
5. **Commit Execution**: Executes the commit with generated message

### Context-Aware Generation

The AI receives:
- **Commit Type**: feat, fix, docs, etc.
- **File List**: Which files were modified
- **Diff Content**: What changes were made
- **Additional Context**: File types, complexity hints

### Example AI Prompts

```bash
# Feature commit
ggfeat
# AI receives: "Type: New feature or functionality"
# Files: src/auth.py, tests/test_auth.py
# Diff: +def login(): +def logout():

# Bug fix commit  
ggfix
# AI receives: "Type: Bug fix or issue resolution"
# Files: src/validator.py
# Diff: -if email == "": +if not email or email.strip() == "":
```

## 🔒 Privacy and Security

### Local Processing (Ollama)
- **No data sent to cloud**: All processing happens locally
- **No API keys required**: Ollama is free and open-source
- **Full privacy**: Your code never leaves your machine
- **Offline capable**: Works without internet connection

### Cloud Providers
- **API keys required**: Store securely in environment variables
- **Data sent to provider**: Check provider's privacy policy
- **Cost considerations**: Monitor usage and set limits
- **Rate limits**: Be aware of provider limitations

## 📈 Performance Tips

### Optimize for Speed
```bash
# Use smaller models
ggconfig set ai.model "llama3.2:3b"

# Ensure Ollama is running
ollama serve

# Close other applications to free memory
```

### Optimize for Quality
```bash
# Use larger models
ggconfig set ai.model "llama3.1:8b"

# Ensure sufficient RAM (8GB+ recommended)
# Use SSD storage for faster model loading
```

## 🆘 Getting Help

If you're still having issues:

1. **Check the logs**: Look for error messages in terminal
2. **Verify configuration**: Run `ggconfig list`
3. **Test Ollama**: Run `ollama list` and `ollama ps`
4. **Check environment**: Verify `GGGIT_AI_KEY` is set
5. **Open an issue**: [GitHub Issues](https://github.com/novafuria/ggGit/issues)

---

**Need more help?** Check out our [Troubleshooting Guide](troubleshooting.md) or [open an issue](https://github.com/novafuria/ggGit/issues).
