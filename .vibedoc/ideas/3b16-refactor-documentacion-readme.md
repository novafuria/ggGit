# 3b16 - Refactor: Documentación README y estructura de docs

## Problema Identificado

**README.md actual**: 655 líneas, información desactualizada, difícil navegación
**Configuración de IA**: Documentación incorrecta sobre variables de entorno
**Estructura**: Mezcla instalación, configuración, desarrollo en un solo archivo

## Análisis del README Actual

### **Problemas Específicos**
1. **Configuración de IA incorrecta**:
   - Dice `OPENAI_API_KEY` por defecto → Debe ser `GGGIT_AI_KEY`
   - Base URL incorrecta: `http://localhost:11434/v1` → `http://localhost:11434`
   - No menciona modelo recomendado `gemma3:4b`

2. **Estructura confusa**:
   - 655 líneas en un solo archivo
   - Mezcla temas diferentes
   - Información crítica perdida

3. **Falta información crítica**:
   - Bug de configuración desalineada no documentado
   - Troubleshooting para problemas comunes
   - Configuración real vs documentada

## Propuesta de Estructura

### **README.md (Simplificado)**
- **Introducción**: Qué es ggGit, beneficios principales
- **Quick Start**: Instalación rápida y primer uso
- **Enlaces**: A documentación detallada
- **Badges**: Estado del proyecto

### **docs/ (Nueva carpeta)**
```
docs/
├── README.md                    # Índice de documentación
├── installation.md              # Guía de instalación detallada
├── configuration.md             # Configuración completa
├── commands.md                  # Lista de comandos
├── ai-setup.md                  # Configuración de IA específica
├── troubleshooting.md           # Guía de resolución de problemas
├── development.md               # Guía para desarrolladores
└── examples.md                  # Ejemplos de uso
```

## Implementación Propuesta

### **1. README.md Simplificado**
```markdown
# ggGit

***Fast Git commands with full support for Conventional Commits and AI-powered commit message generation***

## Quick Start

```bash
# Clone and install
git clone https://github.com/novafuria/ggGit.git
cd ggGit
python install.py

# Configure AI (Ollama recommended)
ggconfig set ai.enabled true
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama

# Use it!
ggfeat  # AI generates commit message
```

## Documentation

- [Installation Guide](docs/installation.md)
- [AI Configuration](docs/ai-setup.md)
- [Command Reference](docs/commands.md)
- [Troubleshooting](docs/troubleshooting.md)

## Features

- 26 Git commands with Conventional Commits
- AI-powered commit message generation
- Hierarchical configuration system
- Cross-platform support
```

### **2. docs/ai-setup.md (Nuevo)**
```markdown
# AI Configuration Guide

## Quick Setup (Ollama - Recommended)

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

# Set environment variable
export GGGIT_AI_KEY=ollama
```

## Troubleshooting

### Problem: "IA no configurada" error
**Cause**: Variable de entorno incorrecta
**Solution**: 
```bash
# Check current config
ggconfig list

# Fix environment variable
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama
```

### Problem: Ollama connection failed
**Cause**: Ollama not running
**Solution**:
```bash
# Start Ollama
ollama serve

# Test connection
ggai test
```
```

### **3. docs/troubleshooting.md (Nuevo)**
```markdown
# Troubleshooting Guide

## Common Issues

### AI Configuration Issues

#### "IA no configurada" Error
**Symptoms**: Commands show "IA no configurada" message
**Cause**: Environment variable mismatch
**Solution**:
```bash
# Check configuration
ggconfig list

# Fix environment variable
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama
```

#### Ollama Connection Failed
**Symptoms**: AI commands fail with connection error
**Cause**: Ollama not running or wrong URL
**Solution**:
```bash
# Start Ollama
ollama serve

# Check URL
ggconfig set ai.base_url http://localhost:11434

# Test connection
ggai test
```

### Installation Issues

#### Commands Not Found
**Symptoms**: `ggfeat: command not found`
**Cause**: Aliases not set up correctly
**Solution**:
```bash
# Re-run installation
python install.py

# Reload shell
source ~/.bashrc  # or ~/.zshrc
```
```

## Beneficios de la Nueva Estructura

### **1. README Limpio**
- **Foco**: Solo información esencial
- **Navegación**: Enlaces claros a documentación
- **Quick Start**: Usuario puede empezar inmediatamente

### **2. Documentación Organizada**
- **Temas separados**: Cada archivo tiene un propósito específico
- **Fácil mantenimiento**: Cambios en un tema no afectan otros
- **Búsqueda**: Más fácil encontrar información específica

### **3. Configuración Correcta**
- **IA Setup**: Documentación específica y correcta
- **Troubleshooting**: Guía para problemas comunes
- **Ejemplos reales**: Configuración que funciona

## Próximos Pasos

1. ✅ **Crear estructura docs/** - COMPLETADO
2. ✅ **Refactorizar README.md** - COMPLETADO
3. ✅ **Crear documentación específica** - COMPLETADO
   - [x] docs/ai-setup.md - Configuración de IA
   - [x] docs/troubleshooting.md - Guía de resolución de problemas
   - [x] docs/README.md - Índice de documentación
4. [ ] **Actualizar enlaces** - PENDIENTE
5. [ ] **Validar con usuarios** - PENDIENTE

## Conclusión

La documentación actual está desactualizada y es difícil de navegar. La nueva estructura:
- **Separa responsabilidades** en archivos específicos
- **Corrige configuración** de IA
- **Mejora experiencia** del usuario
- **Facilita mantenimiento** futuro

---

*"La documentación es el producto. Si es confusa, el producto está roto."* - Nathan Bateman
