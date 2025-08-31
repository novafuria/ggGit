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

## Arquitectura Unificada en Python

### Principios de Diseño

**Lenguaje Unificado**: Todos los comandos se implementarán en Python para mantener consistencia, facilitar el mantenimiento y aprovechar las capacidades de IA.

**Comandos Independientes**: Cada comando es un script Python ejecutable independiente que reutiliza abstracciones comunes.

**Reutilización de Código**: Las funcionalidades comunes se implementan como módulos Python reutilizables.

**Configuración Jerárquica**: Sistema de configuración local con prioridad repositorio > módulo > usuario > default.

### Ventajas de la Arquitectura Unificada

- **Consistencia**: Todos los comandos comparten el mismo entorno y patrones
- **Mantenibilidad**: Un solo lenguaje reduce la complejidad de mantenimiento
- **Capacidades de IA**: Python es ideal para integración con APIs de IA
- **Testing**: Framework de testing unificado para todos los comandos
- **Dependencias**: Gestión simplificada de dependencias

## Sistema de comandos independientes

### Descripción
Cada comando ggGit es un script Python ejecutable independiente que reutiliza abstracciones comunes. Todos los comandos comparten la misma estructura y patrones de implementación.

### Estructura de Comandos

```
commands/
├── _cli_interface.py      # Interfaz CLI unificada
├── _config_manager.py     # Gestor de configuración jerárquica
├── _git_interface.py      # Interfaz con Git
├── _ai_interface.py       # Interfaz con servicios de IA
├── _validators.py         # Validadores de esquemas y argumentos
├── _logger.py             # Sistema de logging unificado
├── ggfeat.py              # Comando de feature commits
├── ggfix.py               # Comando de fix commits
├── ggbreak.py             # Comando de breaking changes
├── ggconfig.py            # Gestión de configuración
├── ggai.py                # Generación de commits con IA
├── gga.py                 # Git add simplificado
├── ggs.py                 # Git status simplificado
├── ggl.py                 # Git log simplificado
└── ...
```

### Especificación de Implementación de Comandos

#### Estructura Estándar de un Comando
Cada comando debe seguir esta estructura:

```python
#!/usr/bin/env python3
"""
ggfeat - Commit changes adding the feat prefix to the message

Usage: ggfeat [options] <message>
"""

import sys
from _cli_interface import CLIInterface
from _config_manager import ConfigManager
from _git_interface import GitInterface
from _validators import ArgumentValidator

def print_usage():
    """Imprime la ayuda del comando"""
    CLIInterface.print_help(
        command_name="ggfeat",
        description="Commit changes adding the feat prefix to the message",
        usage="ggfeat [options] <message>",
        examples=[
            ("ggfeat Add new feature", "Commit simple sin scope"),
            ("ggfeat -s auth Add authentication", "Commit con scope específico")
        ],
        options=[
            ("-s, --scope", "Add scope to commit type"),
            ("-a, --amend", "Amend the last commit"),
            ("-h, --help", "Show this help message")
        ]
    )

def main():
    """Función principal del comando"""
    try:
        # Inicializar componentes
        config = ConfigManager()
        git = GitInterface()
        validator = ArgumentValidator()
        
        # Procesar argumentos
        args = sys.argv[1:]
        # ... lógica de procesamiento de argumentos
        
        # Validar entrada
        validator.validate_commit_message(message)
        
        # Ejecutar operación
        git.stage_all_changes()
        git.commit(f"feat{scope}: {message}")
        
        # Mostrar resultado
        CLIInterface.print_success("Commit realizado exitosamente")
        
    except Exception as e:
        CLIInterface.print_error(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### Abstracciones Reutilizables

**CLIInterface**: Proporciona métodos unificados para:
- `print_success(message)`: Mensajes de éxito
- `print_error(message)`: Mensajes de error
- `print_warning(message)`: Mensajes de advertencia
- `print_info(section, message)`: Mensajes informativos
- `print_help(...)`: Sistema de ayuda unificado

**ConfigManager**: Gestiona configuración jerárquica:
- `get_config(key, default=None)`: Obtener valor de configuración
- `load_hierarchical_config()`: Cargar configuración siguiendo jerarquía
- `validate_config(config)`: Validar configuración con esquemas

**GitInterface**: Interfaz unificada con Git:
- `stage_all_changes()`: Stage todos los cambios
- `commit(message)`: Realizar commit
- `get_current_branch()`: Obtener rama actual
- `is_git_repository()`: Verificar si es repositorio Git

**ArgumentValidator**: Validación de argumentos:
- `validate_commit_message(message)`: Validar mensaje de commit
- `validate_scope(scope)`: Validar scope
- `validate_required_args(args, count)`: Validar argumentos requeridos

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

### Especificación del Sistema de Configuración

#### 1. Estructura de Archivos de Configuración

**Ubicaciones de Configuración:**
- `~/.gggit/default-config.yaml` - Configuración por defecto del sistema
- `~/.gggit/user-config.yaml` - Configuración personal del usuario
- `~/.gggit/modules/<module>.yaml` - Configuraciones de módulos específicos
- `.gggit/repo-config.yaml` - Configuración específica del repositorio

**Prioridad de Carga:**
1. Configuración de repositorio (más alta)
2. Configuración de módulo activo
3. Configuración de usuario
4. Configuración por defecto (más baja)

#### 2. Esquema de Configuración

**Archivo: `config-schema.yaml`**
```yaml
type: object
properties:
  version:
    type: string
    pattern: "^[0-9]+\.[0-9]+$"
    description: "Versión del esquema de configuración"
  
  git:
    type: object
    properties:
      default_branch:
        type: string
        default: "main"
        description: "Rama por defecto del repositorio"
      commit_template:
        type: string
        default: "{type}({scope}): {description}"
        description: "Template para mensajes de commit"
  
  conventional_commits:
    type: object
    properties:
      types:
        type: array
        items:
          type: string
        default: ["feat", "fix", "docs", "style", "refactor", "test", "chore"]
        description: "Tipos de commit permitidos"
      scopes:
        type: array
        items:
          type: string
        description: "Scopes permitidos para commits"
      require_scope:
        type: boolean
        default: false
        description: "Si se requiere scope en todos los commits"
  
  ai:
    type: object
    properties:
      enabled:
        type: boolean
        default: false
        description: "Habilitar funcionalidades de IA"
      provider:
        type: string
        enum: ["openai", "anthropic", "local"]
        default: "openai"
        description: "Proveedor de servicios de IA"
      api_key_env:
        type: string
        description: "Variable de entorno para API key"
      model:
        type: string
        default: "gpt-3.5-turbo"
        description: "Modelo de IA a utilizar"
  
  ui:
    type: object
    properties:
      colors:
        type: object
        properties:
          success:
            type: string
            default: "green"
          error:
            type: string
            default: "red"
          warning:
            type: string
            default: "yellow"
          info:
            type: string
            default: "blue"
      verbose:
        type: boolean
        default: false
        description: "Modo verboso para salida detallada"
      quiet:
        type: boolean
        default: false
        description: "Modo silencioso para salida mínima"

required: ["version"]
```

#### 3. Especificación de ConfigManager

**Métodos Requeridos:**
- `load_hierarchical_config()`: Carga configuración siguiendo jerarquía de prioridad
- `get_config(key, default=None)`: Obtiene valor de configuración
- `set_config(key, value, level='user')`: Establece valor de configuración
- `validate_config(config)`: Valida configuración contra esquema
- `get_active_module()`: Detecta y retorna módulo activo basado en directorio actual
- `create_module_config(module_name, config_data)`: Crea nueva configuración de módulo

## Sistema de interfaz de usuario CLI

### Descripción
Sistema unificado para proporcionar una experiencia de usuario consistente en todos los comandos, independientemente del lenguaje de implementación.

### Componentes

#### 1. Especificación del Sistema de Colores

**Paleta de Colores Estándar:**
- **Success**: Verde (`\033[32m`) - Operaciones exitosas
- **Error**: Rojo (`\033[31m`) - Errores y fallos
- **Warning**: Amarillo (`\033[33m`) - Advertencias
- **Info**: Azul (`\033[34m`) - Información general
- **Reset**: (`\033[0m`) - Reset de colores

**Métodos de Salida Requeridos:**
- `print_success(message)`: Mensajes de éxito con formato `[SUCCESS] mensaje`
- `print_error(message)`: Mensajes de error con formato `[ERROR] mensaje`
- `print_warning(message)`: Mensajes de advertencia con formato `[WARNING] mensaje`
- `print_info(section, message)`: Mensajes informativos con formato `section: mensaje`
- `print_text(message)`: Texto normal sin formato especial

#### 2. Especificación del Sistema de Ayuda

**Formato de Ayuda Estándar:**
```
NAME
    <comando> - <descripción>

SYNOPSIS
    <comando> [opciones] <argumentos>

DESCRIPTION
    <descripción detallada>

EXAMPLES
    <comando> <ejemplo1>    <descripción1>
    <comando> <ejemplo2>    <descripción2>

OPTIONS
    -s, --scope <scope>     <descripción de la opción>
    -a, --amend             <descripción de la opción>
    -h, --help              Show this help message
```

**Método de Ayuda:**
- `print_help(command_name, description, usage, examples, options)`: Genera ayuda con formato estándar

#### 3. Especificación de Validación de Argumentos

**Validaciones Estándar:**
- `validate_required_args(args, count)`: Verifica número mínimo de argumentos
- `validate_commit_message(message)`: Valida formato y contenido de mensaje de commit
- `validate_scope(scope)`: Valida formato de scope (letras minúsculas, números, guiones)
- `validate_branch_name(branch)`: Valida nombre de rama Git
- `validate_file_path(path)`: Valida existencia y permisos de archivo

**Códigos de Salida Estándar:**
- `0`: Éxito
- `1`: Error general
- `2`: Error de sintaxis o argumentos inválidos
- `3`: Error de configuración
- `4`: Error de Git (no es repositorio, conflictos, etc.)

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

#### 1. Especificación del Proceso de Instalación

**Dependencias Requeridas:**
- Python 3.8 o superior
- Git instalado y configurado
- Permisos de escritura en directorio home del usuario

**Estructura de Instalación:**
```
~/.gggit/
├── commands/              # Scripts Python ejecutables
├── config/               # Archivos de configuración
│   ├── default-config.yaml
│   ├── user-config.yaml
│   └── modules/
├── logs/                 # Archivos de log
└── cache/                # Cache temporal
```

**Proceso de Instalación:**
1. **Verificación de Dependencias**: Comprobar Python y Git
2. **Creación de Directorios**: Estructura de directorios estándar
3. **Copia de Comandos**: Instalar scripts Python ejecutables
4. **Configuración de PATH**: Agregar `~/.gggit/commands` al PATH
5. **Configuración Inicial**: Crear archivos de configuración por defecto
6. **Verificación**: Comprobar que la instalación fue exitosa

#### 2. Especificación de Gestores de Paquetes

**Distribución Multiplataforma:**
- **Linux**: Paquetes .deb, .rpm, AppImage
- **macOS**: Homebrew, MacPorts
- **Windows**: Chocolatey, winget, instalador MSI

**Requisitos de Empaquetado:**
- Script de instalación multiplataforma
- Dependencias declaradas en archivo de manifiesto
- Configuración automática de PATH
- Verificación post-instalación

#### 3. Especificación de Actualización

**Proceso de Actualización:**
- Descarga de nueva versión
- Backup de configuraciones existentes
- Actualización de comandos
- Restauración de configuraciones personalizadas
- Verificación de integridad

## Sistema de validación y esquemas

### Descripción
Sistema que valida configuraciones, argumentos de comandos y mensajes de commit usando esquemas predefinidos.

### Componentes

#### 1. Especificación de Validación de Configuración

**Validación de Esquemas:**
- Todas las configuraciones deben validarse contra esquemas JSON Schema
- Validación automática al cargar configuraciones
- Mensajes de error descriptivos para configuraciones inválidas
- Fallback a configuración por defecto en caso de error

**Esquemas Requeridos:**
- `config-schema.yaml`: Esquema principal de configuración
- `commit-schema.yaml`: Esquema para validación de mensajes de commit
- `module-schema.yaml`: Esquema para configuraciones de módulos

#### 2. Especificación de Validación de Mensajes de Commit

**Formato Conventional Commits:**
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Validaciones Requeridas:**
- Tipo de commit debe estar en lista permitida
- Scope debe seguir formato: letras minúsculas, números, guiones
- Descripción no puede estar vacía y máximo 72 caracteres
- Cuerpo opcional con máximo 1000 caracteres por línea
- Footer opcional para referencias de issues

**Esquema de Validación de Commit:**
```yaml
# commit-schema.yaml
type: object
properties:
  type:
    type: string
    enum: [feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert]
    description: "Tipo de commit según Conventional Commits"
  scope:
    type: string
    pattern: "^[a-z0-9-]+$"
    description: "Scope del commit (opcional)"
  description:
    type: string
    minLength: 1
    maxLength: 72
    description: "Descripción del commit"
  body:
    type: string
    maxLength: 1000
    description: "Cuerpo del commit (opcional)"
  footer:
    type: string
    description: "Footer del commit (opcional)"
required: [type, description]
```

#### 3. Especificación de Validación de Argumentos

**Validaciones Estándar:**
- `validate_scope(scope)`: Scope debe ser alfanumérico con guiones
- `validate_branch_name(branch)`: Nombre de rama válido para Git
- `validate_file_path(path)`: Archivo existe y es accesible
- `validate_url(url)`: URL válida para descarga de configuraciones
- `validate_module_name(name)`: Nombre de módulo válido

**Mensajes de Error:**
- Mensajes claros y descriptivos
- Sugerencias de corrección cuando sea posible
- Códigos de error específicos para diferentes tipos de validación

## Sistema de integración con Git

### Descripción
Sistema que proporciona una interfaz unificada para interactuar con Git, manejando errores y proporcionando feedback consistente.

### Componentes

#### 1. Especificación de Interfaz Git

**Verificaciones Requeridas:**
- Verificar que Git esté instalado y disponible en PATH
- Verificar que el directorio actual sea un repositorio Git válido
- Verificar permisos de escritura en el repositorio

**Operaciones Git Principales:**
- `stage_all_changes()`: Stage todos los cambios modificados
- `stage_files(files)`: Stage archivos específicos
- `commit(message)`: Realizar commit con mensaje
- `get_current_branch()`: Obtener rama actual
- `get_staged_files()`: Obtener lista de archivos staged
- `get_unstaged_files()`: Obtener lista de archivos modificados no staged
- `get_repository_status()`: Obtener estado completo del repositorio

**Validaciones de Estado:**
- `validate_git_repository()`: Verificar que es repositorio Git
- `validate_clean_working_directory()`: Verificar directorio limpio
- `validate_staged_changes()`: Verificar que hay cambios staged
- `validate_no_conflicts()`: Verificar que no hay conflictos de merge

#### 2. Especificación de Manejo de Errores Git

**Errores Comunes y Respuestas:**
- **"not a git repository"**: Error 4 - No es un repositorio Git válido
- **"nothing to commit"**: Error 4 - No hay cambios para hacer commit
- **"merge conflict"**: Error 4 - Hay conflictos de merge que resolver
- **"permission denied"**: Error 4 - Sin permisos de escritura
- **"detached HEAD"**: Error 4 - Estado HEAD desconectado

**Mensajes de Error:**
- Mensajes descriptivos y accionables
- Sugerencias de comandos para resolver problemas
- Códigos de error específicos para diferentes situaciones

#### 3. Especificación de Comandos Git Wrapper

**Comandos Simplificados:**
- `gga`: Equivalente a `git add .`
- `ggs`: Equivalente a `git status` con formato mejorado
- `ggl`: Equivalente a `git log` con formato compacto
- `ggdif`: Equivalente a `git diff` con colores
- `ggunstage`: Equivalente a `git reset HEAD <file>`
- `ggreset`: Equivalente a `git reset --hard HEAD`

**Formato de Salida Mejorado:**
- Colores consistentes para diferentes tipos de información
- Formato compacto para información de estado
- Resaltado de archivos modificados, staged, y untracked

## Sistema de IA para generación de commits

### Descripción
Sistema que utiliza inteligencia artificial para analizar cambios y generar mensajes de commit automáticamente.

### Componentes

#### 1. Especificación del Analizador de Cambios

**Análisis de Archivos Staged:**
- Categorización automática de archivos por tipo (source, test, docs, config, assets)
- Detección de patrones de cambios (bug fix, feature, refactor, docs)
- Análisis de diffs para determinar el tipo de cambio
- Sugerencia automática del tipo de commit

**Categorización de Archivos:**
- **Source**: `.py`, `.js`, `.java`, `.cpp`, `.c`, `.go`, `.rs`
- **Test**: Archivos con `test`, `spec`, `.test`, `.spec`
- **Docs**: `.md`, `.txt`, `.rst`, `.adoc`
- **Config**: `.yml`, `.yaml`, `.json`, `.toml`, `.ini`
- **Assets**: Imágenes, fuentes, archivos binarios

**Patrones de Cambio:**
- **Bug Fix**: Cambios en lógica de manejo de errores, correcciones de bugs
- **Feature**: Nuevas funcionalidades, métodos, clases
- **Refactor**: Reestructuración de código sin cambiar funcionalidad
- **Docs**: Cambios en documentación
- **Test**: Agregado o modificación de tests

#### 2. Especificación del Generador de Mensajes con IA

**Proveedores de IA Soportados:**
- **OpenAI**: GPT-3.5-turbo, GPT-4
- **Anthropic**: Claude
- **Local**: Modelos locales (opcional)

**Configuración de IA:**
```yaml
ai:
  enabled: true
  provider: "openai"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  max_tokens: 100
  temperature: 0.7
  prompt_template: "custom_prompt.txt"  # Opcional
```

**Prompt Estándar:**
El sistema debe generar prompts que incluyan:
- Lista de archivos modificados
- Categorización de archivos
- Patrones de cambio detectados
- Tipo de commit sugerido
- Instrucciones para formato Conventional Commits

**Validación de Respuesta:**
- Verificar que el mensaje siga formato Conventional Commits
- Validar longitud máxima de descripción
- Confirmar que el tipo sugerido sea válido
- Proponer correcciones si es necesario

#### 3. Especificación del Comando ggai

**Funcionalidad:**
- Analizar automáticamente cambios staged
- Generar mensaje de commit con IA
- Mostrar sugerencia al usuario
- Permitir aceptar, rechazar o modificar el mensaje
- Realizar commit si se acepta

**Opciones del Comando:**
- `--auto`: Aceptar automáticamente la sugerencia
- `--provider <provider>`: Especificar proveedor de IA
- `--model <model>`: Especificar modelo de IA
- `--verbose`: Mostrar análisis detallado
- `--dry-run`: Solo mostrar sugerencia sin hacer commit

**Flujo de Interacción:**
1. Analizar cambios staged
2. Generar mensaje con IA
3. Mostrar sugerencia
4. Preguntar confirmación
5. Realizar commit o cancelar

## Sistema de observabilidad y logging

### Descripción
Sistema que proporciona logging, métricas y debugging para facilitar el mantenimiento y troubleshooting de ggGit.

### Componentes

#### 1. Especificación del Sistema de Logging

**Estructura de Logs:**
- **Ubicación**: `~/.gggit/logs/`
- **Formato**: `gggit_YYYYMM.log` (rotación mensual)
- **Nivel**: INFO por defecto, DEBUG si está habilitado
- **Formato de Entrada**: `YYYY-MM-DD HH:MM:SS - gggit.<command> - LEVEL - message`

**Eventos a Registrar:**
- Ejecución de comandos con argumentos
- Errores y excepciones con contexto
- Cambios de configuración
- Operaciones de IA (solicitudes, respuestas, errores)
- Operaciones Git (commits, stage, etc.)

**Configuración de Logging:**
```yaml
logging:
  level: "INFO"  # DEBUG, INFO, WARNING, ERROR
  max_size: "10MB"
  backup_count: 5
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

#### 2. Especificación de Métricas de Uso

**Métricas a Recolectar:**
- **Uso de Comandos**: Frecuencia de uso de cada comando
- **Errores**: Tipos y frecuencia de errores por comando
- **Uso Diario**: Actividad diaria del usuario
- **Configuraciones**: Módulos y configuraciones más usadas
- **IA**: Uso de funcionalidades de IA

**Almacenamiento de Métricas:**
- **Archivo**: `~/.gggit/metrics.json`
- **Formato**: JSON estructurado
- **Privacidad**: Solo datos de uso, sin información personal
- **Retención**: Historial de 12 meses

**Estructura de Métricas:**
```json
{
  "commands_used": {
    "ggfeat": 150,
    "ggfix": 89,
    "ggai": 45
  },
  "errors": {
    "ggfeat": {
      "invalid_message": 5,
      "no_changes": 12
    }
  },
  "daily_usage": {
    "2024-01-15": 25,
    "2024-01-16": 18
  },
  "total_executions": 284,
  "ai_usage": {
    "requests": 45,
    "success_rate": 0.93
  }
}
```

#### 3. Especificación del Modo Debug

**Activación del Debug:**
- **Variable de Entorno**: `GGGIT_DEBUG=true`
- **Configuración**: `debug: true` en configuración
- **Comando**: `--debug` flag en comandos

**Información de Debug:**
- Configuración cargada y valores utilizados
- Argumentos de comandos procesados
- Operaciones Git ejecutadas
- Llamadas a APIs de IA
- Validaciones realizadas

**Salida de Debug:**
- **Destino**: stderr para no interferir con salida normal
- **Formato**: `[DEBUG] <context>: <message>`
- **Nivel**: Detallado para troubleshooting

## Integraciones con terceros

### Descripción
Sistema que maneja integraciones con servicios externos como APIs de IA, gestores de paquetes, y herramientas de CI/CD.

### Componentes

#### 1. Especificación de Integración con APIs de IA

**Proveedores Soportados:**
- **OpenAI**: GPT-3.5-turbo, GPT-4
- **Anthropic**: Claude
- **Local**: Modelos locales (opcional)

**Configuración de Proveedores:**
```yaml
ai_providers:
  openai:
    api_key_env: "OPENAI_API_KEY"
    models: ["gpt-3.5-turbo", "gpt-4"]
    rate_limit: 60  # requests per minute
    timeout: 30     # seconds
  
  anthropic:
    api_key_env: "ANTHROPIC_API_KEY"
    models: ["claude-3-sonnet", "claude-3-haiku"]
    rate_limit: 50
    timeout: 30
  
  local:
    endpoint: "http://localhost:8000"
    models: ["local-model"]
    timeout: 10
```

**Manejo de Errores de IA:**
- **Rate Limiting**: Reintentos automáticos con backoff exponencial
- **Timeouts**: Configuración de timeouts por proveedor
- **Fallbacks**: Cambio automático de proveedor en caso de error
- **Cache**: Cache de respuestas para evitar llamadas repetidas

#### 2. Especificación de Integración con CI/CD

**Entornos de CI/CD Soportados:**
- **GitHub Actions**: Detección automática y validación
- **GitLab CI**: Integración con pipelines
- **Jenkins**: Soporte para builds automatizados
- **Azure DevOps**: Integración con pipelines de Azure

**Validaciones en CI/CD:**
- Verificación de formato de Conventional Commits
- Validación de tipos de commit permitidos
- Verificación de scopes requeridos
- Validación de longitud de mensajes

**Configuración de CI/CD:**
```yaml
cicd:
  enabled: true
  strict_mode: false  # Validación estricta en CI
  allowed_types: ["feat", "fix", "docs", "style", "refactor", "test", "chore"]
  require_scope: false
  max_description_length: 72
```

#### 3. Especificación de Gestores de Paquetes

**Distribución Multiplataforma:**
- **Linux**: Paquetes .deb, .rpm, AppImage
- **macOS**: Homebrew, MacPorts
- **Windows**: Chocolatey, winget, instalador MSI

**Requisitos de Empaquetado:**
- Script de instalación multiplataforma
- Dependencias declaradas en archivo de manifiesto
- Configuración automática de PATH
- Verificación post-instalación
- Actualizaciones automáticas

**Integración con Gestores:**
- **Homebrew**: Formula para macOS
- **Chocolatey**: Package para Windows
- **Snap**: Package para Linux
- **Flatpak**: Package universal

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
