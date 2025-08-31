# [architecture] - ggGit

> Este documento es la culminación de la investigación y el diseño de producto. Consiste en la creación de una arquitectura de software que resuelva el problema planteado en el documento [01-research-and-assessment-of-the-problem](01-research-and-assessment-of-the-problem.md). Para eso se describirán los enfoques de cada una de las partes del sistema.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Descripción general](#descripción-general)
- [Arquitectura Legacy vs Nueva Propuesta](#arquitectura-legacy-vs-nueva-propuesta)
- [Sistema de comandos independientes](#sistema-de-comandos-independientes)
- [Sistema de configuración jerárquica](#sistema-de-configuración-jerárquica)
- [Sistema de interfaz de usuario CLI](#sistema-de-interfaz-de-usuario-cli)
- [Sistema de instalación y distribución](#sistema-de-instalación-y-distribución)
- [Sistema de validación y esquemas](#sistema-de-validación-y-esquemas)
- [Sistema de integración con Git](#sistema-de-integración-con-git)
- [Sistema de IA para generación de commits](#sistema-de-ia-para-generación-de-commits)
- [Sistema de observabilidad y logging](#sistema-de-observabilidad-y-logging)
- [Integraciones con terceros](#integraciones-con-terceros)

## Descripción general

ggGit es una suite de comandos independientes de línea de comandos que simplifica y acelera el trabajo con Git, especialmente enfocada en Conventional Commits. La arquitectura está diseñada para ser modular, extensible y mantener consistencia entre diferentes implementaciones de comandos.

### Principios Arquitectónicos

1. **Comandos Independientes**: Cada comando es un ejecutable independiente que puede estar implementado en diferentes tecnologías
2. **Configuración Jerárquica**: Sistema de configuración local con prioridad repositorio > módulo > usuario > default
3. **Interfaz Consistente**: Todos los comandos comparten el mismo sistema de colores, mensajes y estructura de ayuda
4. **Flexibilidad Tecnológica**: Los comandos pueden estar implementados en bash, Python, Go, o cualquier lenguaje apropiado
5. **Validación en la Nube**: Los commits se generan correctamente por defecto, con validación final en CI/CD

### Arquitectura General

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ggGit Architecture                                │
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │   Comandos      │    │  Configuración  │    │   Interfaz      │        │
│  │   Independientes│    │   Jerárquica    │    │   CLI Unificada │        │
│  │                 │    │                 │    │                 │        │
│  │ • ggfeat (bash)│    │ • Repositorio   │    │ • Colores       │        │
│  │ • ggfix (bash) │    │ • Módulos       │    │ • Mensajes      │        │
│  │ • ggconfig (py)│    │ • Usuario       │    │ • Ayuda         │        │
│  │ • ggai (go)    │    │ • Default       │    │ • Validación    │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│           │                       │                       │                │
│           ▼                       ▼                       ▼                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Sistema de Integración Git                      │   │
│  │                                                                     │   │
│  │  • Validación de estado del repositorio                            │   │
│  │  • Ejecución de comandos Git nativos                               │   │
│  │  • Manejo de errores y feedback                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Sistema de IA (Futuro)                          │   │
│  │                                                                     │   │
│  │  • Análisis de cambios staged                                      │   │
│  │  • Generación de mensajes de commit                                │   │
│  │  • Integración con servicios de IA                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Arquitectura Legacy vs Nueva Propuesta

### Arquitectura Legacy (Implementación Actual)

**Características:**
- Todos los comandos implementados en bash
- Sistema de utilidades compartido (`_utils.sh`)
- Configuración básica sin jerarquía
- Instalación manual en PATH
- Colores hardcodeados en cada script

**Limitaciones:**
- Dificultad para implementar funcionalidades complejas en bash
- Falta de validación de esquemas
- Configuración limitada
- No soporte para múltiples lenguajes
- Difícil testing y mantenimiento

### Nueva Propuesta Arquitectónica

**Mejoras:**
- Comandos independientes en múltiples lenguajes
- Sistema de configuración jerárquica con YAML
- Interfaz CLI unificada y consistente
- Validación de esquemas
- Sistema de módulos por contexto
- Mejor testing y mantenimiento

## Sistema de comandos independientes

### Descripción
Cada comando ggGit es un ejecutable independiente que puede estar implementado en la tecnología más apropiada para su funcionalidad específica.

### Componentes

#### 1. Comandos Básicos (Bash)
- **ggfeat, ggfix, ggbreak**: Comandos de commit simples
- **gga, ggs, ggl**: Comandos de visualización básicos
- **ggmain, ggmaster, ggmerge**: Comandos de ramas

**Justificación**: Bash es ideal para comandos simples que principalmente ejecutan Git y formatean salida.

#### 2. Comandos de Configuración (Python)
- **ggconfig**: Gestión de configuración jerárquica
- **ggsetup**: Configuración inicial y módulos

**Justificación**: Python es ideal para manejo de archivos YAML, validación de esquemas, y lógica compleja de configuración.

#### 3. Comandos de IA (Go/Python)
- **ggai**: Generación de mensajes con IA
- **ggsuggest**: Autocompletado inteligente

**Justificación**: Go para rendimiento en análisis de código, Python para integración con APIs de IA.

### Estructura de Comandos

```
commands/
├── _utils.sh              # Utilidades compartidas (legacy)
├── _cli_interface.py      # Interfaz CLI unificada (nueva)
├── _config_manager.py     # Gestor de configuración (nueva)
├── _git_interface.py      # Interfaz con Git (nueva)
├── ggfeat                 # Comando bash (legacy)
├── ggfix                  # Comando bash (legacy)
├── ggconfig               # Comando Python (nueva)
├── ggai                   # Comando Go/Python (nueva)
└── ...
```

### Interfaz Unificada

Todos los comandos deben seguir la misma interfaz:

```bash
# Sintaxis estándar
<comando> [opciones] [argumentos]

# Opciones estándar
-h, --help          # Mostrar ayuda
-v, --version       # Mostrar versión
--verbose           # Modo verboso
--quiet             # Modo silencioso

# Códigos de salida estándar
0                   # Éxito
1                   # Error general
2                   # Error de sintaxis
3                   # Error de configuración
```

## Sistema de configuración jerárquica

### Descripción
Sistema de configuración local que permite configuraciones específicas por contexto, con prioridad repositorio > módulo > usuario > default.

### Jerarquía de Configuración

```
Prioridad (más alta a más baja):
1. .gggit/repo-config.yaml     # Configuración específica del repositorio
2. ~/.gggit/modules/<module>.yaml  # Configuración de módulo
3. ~/.gggit/user-config.yaml   # Configuración de usuario
4. ~/.gggit/default-config.yaml # Configuración por defecto
```

### Estructura de Configuración

```yaml
# Ejemplo de configuración
version: "1.0"
git:
  default_branch: "main"
  commit_template: "{type}({scope}): {description}"
  
conventional_commits:
  types:
    - feat
    - fix
    - docs
    - style
    - refactor
    - test
    - chore
  scopes:
    - auth
    - api
    - ui
    - db
    
ai:
  enabled: true
  provider: "openai"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  
ui:
  colors:
    success: "green"
    error: "red"
    warning: "yellow"
    info: "blue"
  verbose: false
```

### Componentes del Sistema

#### 1. Config Manager (Python)
```python
class ConfigManager:
    def __init__(self):
        self.config = self.load_hierarchical_config()
    
    def load_hierarchical_config(self):
        # Cargar configuración siguiendo jerarquía
        pass
    
    def get_config(self, key, default=None):
        # Obtener valor de configuración
        pass
    
    def validate_config(self, config):
        # Validar configuración con esquema
        pass
```

#### 2. Esquemas de Validación
```yaml
# config-schema.yaml
type: object
properties:
  version:
    type: string
    pattern: "^[0-9]+\.[0-9]+$"
  git:
    type: object
    properties:
      default_branch:
        type: string
  conventional_commits:
    type: object
    properties:
      types:
        type: array
        items:
          type: string
```

## Sistema de interfaz de usuario CLI

### Descripción
Sistema unificado para proporcionar una experiencia de usuario consistente en todos los comandos, independientemente del lenguaje de implementación.

### Componentes

#### 1. Sistema de Colores Unificado
```python
# _cli_interface.py
class Colors:
    SUCCESS = "\033[32m"
    ERROR = "\033[31m"
    WARNING = "\033[33m"
    INFO = "\033[34m"
    RESET = "\033[0m"

class CLIInterface:
    @staticmethod
    def print_success(message):
        print(f"{Colors.SUCCESS}[SUCCESS] {message}{Colors.RESET}")
    
    @staticmethod
    def print_error(message):
        print(f"{Colors.ERROR}[ERROR] {message}{Colors.RESET}")
    
    @staticmethod
    def print_warning(message):
        print(f"{Colors.WARNING}[WARNING] {message}{Colors.RESET}")
    
    @staticmethod
    def print_info(section, message):
        print(f"{Colors.INFO}{section}{Colors.RESET}: {message}")
```

#### 2. Sistema de Ayuda Unificado
```python
class HelpSystem:
    def __init__(self, command_name, description):
        self.command_name = command_name
        self.description = description
        self.examples = []
        self.options = []
    
    def add_example(self, command, description):
        self.examples.append((command, description))
    
    def add_option(self, short, long, description):
        self.options.append((short, long, description))
    
    def print_help(self):
        # Generar ayuda consistente
        pass
```

#### 3. Sistema de Validación de Argumentos
```python
class ArgumentValidator:
    @staticmethod
    def validate_required_args(args, required_count):
        if len(args) < required_count:
            raise ValueError(f"Se requieren {required_count} argumentos")
    
    @staticmethod
    def validate_commit_message(message):
        if not message or len(message.strip()) == 0:
            raise ValueError("El mensaje de commit no puede estar vacío")
```

### Consistencia entre Lenguajes

Para mantener consistencia entre diferentes implementaciones:

1. **Esquema de Colores**: Todos los comandos usan los mismos códigos de color
2. **Formato de Mensajes**: Estructura consistente para errores, warnings, y éxito
3. **Sistema de Ayuda**: Formato unificado para todos los comandos
4. **Códigos de Salida**: Estandarización de códigos de error

## Sistema de instalación y distribución

### Descripción
Sistema que facilita la instalación, actualización y distribución de ggGit en diferentes entornos.

### Componentes

#### 1. Script de Instalación Mejorado
```bash
#!/bin/bash
# install.sh mejorado

# Detectar sistema operativo
detect_os() {
    case "$(uname -s)" in
        Linux*)     echo "linux";;
        Darwin*)    echo "macos";;
        CYGWIN*)    echo "windows";;
        MINGW*)     echo "windows";;
        *)          echo "unknown";;
    esac
}

# Instalar dependencias
install_dependencies() {
    local os=$(detect_os)
    case $os in
        linux)
            # Instalar Python, Go si es necesario
            ;;
        macos)
            # Usar Homebrew si está disponible
            ;;
        windows)
            # Usar Chocolatey o winget
            ;;
    esac
}

# Configurar PATH
setup_path() {
    # Agregar comandos al PATH
    # Crear directorios de configuración
    # Configurar archivos de configuración inicial
}
```

#### 2. Gestor de Paquetes
```python
# package_manager.py
class PackageManager:
    def __init__(self):
        self.install_dir = "~/.gggit"
        self.config_dir = "~/.gggit/config"
    
    def install(self):
        # Instalar comandos
        # Crear directorios
        # Configurar PATH
        pass
    
    def update(self):
        # Actualizar comandos
        # Mantener configuraciones
        pass
    
    def uninstall(self):
        # Remover comandos
        # Limpiar configuraciones
        pass
```

#### 3. Distribución Multiplataforma
- **Linux**: Paquetes .deb, .rpm, AppImage
- **macOS**: Homebrew, MacPorts
- **Windows**: Chocolatey, winget, instalador MSI

## Sistema de validación y esquemas

### Descripción
Sistema que valida configuraciones, argumentos de comandos y mensajes de commit usando esquemas predefinidos.

### Componentes

#### 1. Validador de Configuración
```python
# config_validator.py
import yaml
import jsonschema

class ConfigValidator:
    def __init__(self):
        self.schemas = self.load_schemas()
    
    def validate_config(self, config, config_type):
        schema = self.schemas.get(config_type)
        if schema:
            jsonschema.validate(config, schema)
    
    def validate_commit_message(self, message):
        # Validar formato de Conventional Commits
        pattern = r"^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"
        if not re.match(pattern, message):
            raise ValueError("Formato de commit inválido")
```

#### 2. Esquemas de Validación
```yaml
# commit-schema.yaml
type: object
properties:
  type:
    type: string
    enum: [feat, fix, docs, style, refactor, test, chore]
  scope:
    type: string
    pattern: "^[a-z0-9-]+$"
  description:
    type: string
    minLength: 1
    maxLength: 72
required: [type, description]
```

#### 3. Validación de Argumentos
```python
# argument_validator.py
class ArgumentValidator:
    @staticmethod
    def validate_scope(scope):
        if scope and not re.match(r"^[a-z0-9-]+$", scope):
            raise ValueError("Scope debe contener solo letras minúsculas, números y guiones")
    
    @staticmethod
    def validate_branch_name(branch):
        if not re.match(r"^[a-zA-Z0-9/_-]+$", branch):
            raise ValueError("Nombre de rama inválido")
```

## Sistema de integración con Git

### Descripción
Sistema que proporciona una interfaz unificada para interactuar con Git, manejando errores y proporcionando feedback consistente.

### Componentes

#### 1. Interfaz Git Unificada
```python
# git_interface.py
import subprocess
import os

class GitInterface:
    def __init__(self):
        self.check_git_installed()
    
    def check_git_installed(self):
        try:
            subprocess.run(["git", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("Git no está instalado")
    
    def is_git_repository(self):
        return os.path.exists(".git")
    
    def get_current_branch(self):
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    
    def stage_all_changes(self):
        subprocess.run(["git", "add", "."], check=True)
    
    def commit(self, message):
        subprocess.run(["git", "commit", "-m", message], check=True)
    
    def get_staged_files(self):
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
```

#### 2. Manejo de Errores Git
```python
# git_error_handler.py
class GitErrorHandler:
    @staticmethod
    def handle_git_error(error, context=""):
        if "not a git repository" in str(error):
            raise RuntimeError(f"No es un repositorio Git válido. {context}")
        elif "nothing to commit" in str(error):
            raise RuntimeError("No hay cambios para hacer commit")
        elif "merge conflict" in str(error):
            raise RuntimeError("Hay conflictos de merge que resolver")
        else:
            raise RuntimeError(f"Error de Git: {error}")
```

#### 3. Validación de Estado
```python
# git_state_validator.py
class GitStateValidator:
    @staticmethod
    def validate_clean_working_directory():
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, check=True
        )
        if result.stdout.strip():
            raise RuntimeError("El directorio de trabajo no está limpio")
    
    @staticmethod
    def validate_staged_changes():
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            capture_output=True
        )
        if result.returncode != 0:
            raise RuntimeError("No hay cambios staged para commit")
```

## Sistema de IA para generación de commits

### Descripción
Sistema que utiliza inteligencia artificial para analizar cambios y generar mensajes de commit automáticamente.

### Componentes

#### 1. Analizador de Cambios
```python
# change_analyzer.py
import difflib
import os

class ChangeAnalyzer:
    def __init__(self):
        self.git_interface = GitInterface()
    
    def analyze_staged_changes(self):
        """Analiza los cambios staged para determinar el tipo de commit"""
        staged_files = self.git_interface.get_staged_files()
        
        analysis = {
            'files_changed': len(staged_files),
            'file_types': self.categorize_files(staged_files),
            'change_patterns': self.analyze_change_patterns(staged_files),
            'suggested_type': self.suggest_commit_type(staged_files)
        }
        
        return analysis
    
    def categorize_files(self, files):
        """Categoriza archivos por tipo"""
        categories = {
            'source': [],
            'test': [],
            'docs': [],
            'config': [],
            'assets': []
        }
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.py', '.js', '.java', '.cpp', '.c']:
                categories['source'].append(file)
            elif 'test' in file.lower() or ext in ['.test', '.spec']:
                categories['test'].append(file)
            elif ext in ['.md', '.txt', '.rst']:
                categories['docs'].append(file)
            elif ext in ['.yml', '.yaml', '.json', '.toml']:
                categories['config'].append(file)
            else:
                categories['assets'].append(file)
        
        return categories
    
    def analyze_change_patterns(self, files):
        """Analiza patrones de cambios"""
        patterns = []
        
        # Analizar diffs para detectar patrones
        for file in files:
            diff = self.get_file_diff(file)
            if self.is_bug_fix(diff):
                patterns.append('bug_fix')
            elif self.is_feature_addition(diff):
                patterns.append('feature')
            elif self.is_refactoring(diff):
                patterns.append('refactor')
        
        return patterns
    
    def suggest_commit_type(self, files):
        """Sugiere el tipo de commit basado en el análisis"""
        categories = self.categorize_files(files)
        patterns = self.analyze_change_patterns(files)
        
        if 'bug_fix' in patterns:
            return 'fix'
        elif 'feature' in patterns:
            return 'feat'
        elif 'refactor' in patterns:
            return 'refactor'
        elif categories['docs']:
            return 'docs'
        elif categories['test']:
            return 'test'
        else:
            return 'chore'
```

#### 2. Generador de Mensajes con IA
```python
# ai_message_generator.py
import openai
import os

class AIMessageGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY no está configurada")
        
        openai.api_key = self.api_key
    
    def generate_commit_message(self, analysis):
        """Genera un mensaje de commit usando IA"""
        prompt = self.build_prompt(analysis)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en Conventional Commits. Genera mensajes de commit concisos y descriptivos."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=100,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            raise RuntimeError(f"Error al generar mensaje con IA: {e}")
    
    def build_prompt(self, analysis):
        """Construye el prompt para la IA"""
        prompt = f"""
        Analiza los siguientes cambios y genera un mensaje de commit siguiendo Conventional Commits:
        
        Archivos cambiados: {analysis['files_changed']}
        Tipos de archivo: {analysis['file_types']}
        Patrones detectados: {analysis['change_patterns']}
        Tipo sugerido: {analysis['suggested_type']}
        
        Genera un mensaje de commit que sea:
        1. Conciso (máximo 50 caracteres)
        2. Descriptivo
        3. Siga el formato: <type>(<scope>): <description>
        
        Solo devuelve el mensaje, sin explicaciones adicionales.
        """
        
        return prompt
```

#### 3. Integración con Comandos
```python
# ggai command implementation
#!/usr/bin/env python3

import sys
from change_analyzer import ChangeAnalyzer
from ai_message_generator import AIMessageGenerator
from cli_interface import CLIInterface

def main():
    try:
        # Analizar cambios
        analyzer = ChangeAnalyzer()
        analysis = analyzer.analyze_staged_changes()
        
        # Generar mensaje con IA
        ai_generator = AIMessageGenerator()
        message = ai_generator.generate_commit_message(analysis)
        
        # Mostrar sugerencia
        CLIInterface.print_info("Mensaje sugerido", message)
        
        # Preguntar si aceptar
        response = input("¿Aceptar este mensaje? (y/N): ")
        if response.lower() in ['y', 'yes']:
            # Hacer commit
            git_interface = GitInterface()
            git_interface.commit(message)
            CLIInterface.print_success("Commit realizado exitosamente")
        else:
            CLIInterface.print_info("Operación cancelada", "Puedes escribir tu propio mensaje")
    
    except Exception as e:
        CLIInterface.print_error(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Sistema de observabilidad y logging

### Descripción
Sistema que proporciona logging, métricas y debugging para facilitar el mantenimiento y troubleshooting de ggGit.

### Componentes

#### 1. Sistema de Logging
```python
# logger.py
import logging
import os
from datetime import datetime

class GGLogger:
    def __init__(self, command_name):
        self.logger = logging.getLogger(f"gggit.{command_name}")
        self.setup_logging()
    
    def setup_logging(self):
        """Configura el sistema de logging"""
        log_dir = os.path.expanduser("~/.gggit/logs")
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(log_dir, f"gggit_{datetime.now().strftime('%Y%m')}.log")
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)
    
    def log_command_execution(self, command, args, result):
        """Registra la ejecución de un comando"""
        self.logger.info(f"Command: {command} Args: {args} Result: {result}")
    
    def log_error(self, error, context=""):
        """Registra errores"""
        self.logger.error(f"Error: {error} Context: {context}")
    
    def log_configuration_change(self, config_type, changes):
        """Registra cambios de configuración"""
        self.logger.info(f"Config change: {config_type} Changes: {changes}")
```

#### 2. Métricas de Uso
```python
# metrics.py
import json
import os
from datetime import datetime

class MetricsCollector:
    def __init__(self):
        self.metrics_file = os.path.expanduser("~/.gggit/metrics.json")
        self.load_metrics()
    
    def load_metrics(self):
        """Carga métricas existentes"""
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'r') as f:
                self.metrics = json.load(f)
        else:
            self.metrics = {
                'commands_used': {},
                'errors': {},
                'daily_usage': {},
                'total_executions': 0
            }
    
    def record_command_usage(self, command):
        """Registra el uso de un comando"""
        self.metrics['commands_used'][command] = self.metrics['commands_used'].get(command, 0) + 1
        self.metrics['total_executions'] += 1
        
        today = datetime.now().strftime('%Y-%m-%d')
        if today not in self.metrics['daily_usage']:
            self.metrics['daily_usage'][today] = 0
        self.metrics['daily_usage'][today] += 1
        
        self.save_metrics()
    
    def record_error(self, command, error_type):
        """Registra errores"""
        if command not in self.metrics['errors']:
            self.metrics['errors'][command] = {}
        
        self.metrics['errors'][command][error_type] = self.metrics['errors'][command].get(error_type, 0) + 1
        self.save_metrics()
    
    def save_metrics(self):
        """Guarda métricas en archivo"""
        with open(self.metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def get_usage_stats(self):
        """Obtiene estadísticas de uso"""
        return {
            'total_executions': self.metrics['total_executions'],
            'most_used_command': max(self.metrics['commands_used'].items(), key=lambda x: x[1])[0] if self.metrics['commands_used'] else None,
            'commands_used': self.metrics['commands_used'],
            'recent_errors': self.metrics['errors']
        }
```

#### 3. Debug Mode
```python
# debug.py
import os
import sys

class DebugMode:
    def __init__(self):
        self.debug_enabled = os.getenv('GGGIT_DEBUG', 'false').lower() == 'true'
    
    def debug_print(self, message):
        """Imprime mensajes de debug si está habilitado"""
        if self.debug_enabled:
            print(f"[DEBUG] {message}", file=sys.stderr)
    
    def debug_config(self, config):
        """Imprime configuración en modo debug"""
        if self.debug_enabled:
            print(f"[DEBUG] Config: {config}", file=sys.stderr)
    
    def debug_command(self, command, args):
        """Imprime información del comando en modo debug"""
        if self.debug_enabled:
            print(f"[DEBUG] Command: {command} Args: {args}", file=sys.stderr)
```

## Integraciones con terceros

### Descripción
Sistema que maneja integraciones con servicios externos como APIs de IA, gestores de paquetes, y herramientas de CI/CD.

### Componentes

#### 1. Gestor de APIs de IA
```python
# ai_provider_manager.py
import os
from abc import ABC, abstractmethod

class AIProvider(ABC):
    @abstractmethod
    def generate_commit_message(self, analysis):
        pass

class OpenAIProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY no configurada")
    
    def generate_commit_message(self, analysis):
        # Implementación específica de OpenAI
        pass

class AnthropicProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise RuntimeError("ANTHROPIC_API_KEY no configurada")
    
    def generate_commit_message(self, analysis):
        # Implementación específica de Anthropic
        pass

class AIProviderManager:
    def __init__(self):
        self.providers = {
            'openai': OpenAIProvider,
            'anthropic': AnthropicProvider
        }
    
    def get_provider(self, provider_name):
        """Obtiene el proveedor de IA especificado"""
        if provider_name not in self.providers:
            raise ValueError(f"Proveedor no soportado: {provider_name}")
        
        return self.providers[provider_name]()
```

#### 2. Integración con CI/CD
```python
# cicd_integration.py
import os

class CICDIntegration:
    def __init__(self):
        self.is_ci_environment = self.detect_ci_environment()
    
    def detect_ci_environment(self):
        """Detecta si estamos en un entorno de CI/CD"""
        ci_vars = ['CI', 'GITHUB_ACTIONS', 'GITLAB_CI', 'JENKINS_URL']
        return any(os.getenv(var) for var in ci_vars)
    
    def get_ci_info(self):
        """Obtiene información del entorno de CI/CD"""
        if os.getenv('GITHUB_ACTIONS'):
            return {
                'provider': 'github',
                'repository': os.getenv('GITHUB_REPOSITORY'),
                'workflow': os.getenv('GITHUB_WORKFLOW'),
                'run_id': os.getenv('GITHUB_RUN_ID')
            }
        elif os.getenv('GITLAB_CI'):
            return {
                'provider': 'gitlab',
                'project': os.getenv('CI_PROJECT_PATH'),
                'pipeline': os.getenv('CI_PIPELINE_ID')
            }
        else:
            return None
    
    def validate_commit_in_ci(self, commit_message):
        """Valida el commit en entorno de CI/CD"""
        if not self.is_ci_environment:
            return True
        
        # Implementar validación específica para CI/CD
        # Por ejemplo, verificar que el commit siga las reglas del equipo
        return True
```

#### 3. Gestor de Paquetes
```python
# package_manager_integration.py
import subprocess
import sys

class PackageManagerIntegration:
    def __init__(self):
        self.package_managers = {
            'npm': self.check_npm,
            'pip': self.check_pip,
            'go': self.check_go,
            'cargo': self.check_cargo
        }
    
    def check_dependencies(self):
        """Verifica que las dependencias estén instaladas"""
        missing_deps = []
        
        for manager, check_func in self.package_managers.items():
            if not check_func():
                missing_deps.append(manager)
        
        return missing_deps
    
    def check_npm(self):
        """Verifica si npm está disponible"""
        try:
            subprocess.run(['npm', '--version'], check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def check_pip(self):
        """Verifica si pip está disponible"""
        try:
            subprocess.run([sys.executable, '-m', 'pip', '--version'], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def check_go(self):
        """Verifica si Go está disponible"""
        try:
            subprocess.run(['go', 'version'], check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def check_cargo(self):
        """Verifica si Cargo está disponible"""
        try:
            subprocess.run(['cargo', '--version'], check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
```

### Consideraciones de Seguridad

#### 1. Manejo de Credenciales
- Las API keys se almacenan en variables de entorno
- No se incluyen credenciales en archivos de configuración
- Validación de permisos para archivos de configuración

#### 2. Validación de Entrada
- Todos los argumentos de comandos se validan
- Sanitización de entrada para prevenir inyección
- Validación de esquemas para configuraciones

#### 3. Logging Seguro
- No se registran credenciales en logs
- Rotación automática de archivos de log
- Permisos restrictivos en archivos de configuración

### Consideraciones de Rendimiento

#### 1. Optimización de Comandos
- Comandos bash para operaciones simples
- Python para lógica compleja
- Go para operaciones de alto rendimiento

#### 2. Caching
- Cache de configuraciones para evitar re-lectura
- Cache de análisis de cambios para IA
- Cache de validaciones de esquemas

#### 3. Lazy Loading
- Carga de módulos solo cuando son necesarios
- Inicialización diferida de componentes pesados
- Carga condicional de proveedores de IA

Esta arquitectura proporciona una base sólida para el desarrollo futuro de ggGit, manteniendo la flexibilidad para evolucionar según las necesidades del proyecto y la comunidad.
