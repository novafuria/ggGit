# [architecture] - ggGit <!-- omit in toc -->

> Este documento es la culminación de la investigación y el diseño de producto. Consiste en la creación de una arquitectura de software que resuelva el problema planteado en el documento [01-research-and-assessment-of-the-problem](01-research-and-assessment-of-the-problem.md). Para eso se describirán los enfoques de cada una de las partes del sistema.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Descripción general](#descripción-general)
  - [Principios Arquitectónicos](#principios-arquitectónicos)
  - [Arquitectura General](#arquitectura-general)
- [Arquitectura Unificada en Python](#arquitectura-unificada-en-python)
  - [Principios de Diseño](#principios-de-diseño)
  - [Ventajas de la Arquitectura Unificada](#ventajas-de-la-arquitectura-unificada)
- [Sistema de comandos independientes](#sistema-de-comandos-independientes)
  - [Descripción](#descripción)
  - [Estructura de Comandos](#estructura-de-comandos)
  - [Especificación de Implementación de Comandos](#especificación-de-implementación-de-comandos)
    - [Estructura Estándar de un Comando](#estructura-estándar-de-un-comando)
    - [Abstracciones Reutilizables Implementadas](#abstracciones-reutilizables-implementadas)
  - [Interfaz Unificada](#interfaz-unificada)
- [Sistema de configuración jerárquica](#sistema-de-configuración-jerárquica)
  - [Descripción](#descripción-1)
  - [Jerarquía de Configuración](#jerarquía-de-configuración)
  - [Estructura de Configuración](#estructura-de-configuración)
  - [Especificación del Sistema de Configuración](#especificación-del-sistema-de-configuración)
    - [1. Estructura de Archivos de Configuración](#1-estructura-de-archivos-de-configuración)
    - [2. Esquema de Configuración](#2-esquema-de-configuración)
    - [3. Especificación de ConfigManager](#3-especificación-de-configmanager)
- [Sistema de interfaz de usuario CLI](#sistema-de-interfaz-de-usuario-cli)
  - [Descripción](#descripción-2)
  - [Componentes](#componentes)
    - [1. Especificación del Sistema de Colores](#1-especificación-del-sistema-de-colores)
    - [2. Especificación del Sistema de Ayuda](#2-especificación-del-sistema-de-ayuda)
    - [3. Especificación de Validación de Argumentos](#3-especificación-de-validación-de-argumentos)
  - [Consistencia entre Comandos](#consistencia-entre-comandos)
  - [Bibliotecas CLI Recomendadas](#bibliotecas-cli-recomendadas)
- [Sistema de instalación y distribución](#sistema-de-instalación-y-distribución)
  - [Descripción](#descripción-3)
  - [Componentes](#componentes-1)
    - [1. Especificación del Proceso de Instalación](#1-especificación-del-proceso-de-instalación)
    - [2. Especificación de Instalación desde Repositorio](#2-especificación-de-instalación-desde-repositorio)
    - [3. Gestión de Dependencias y Ambientes](#3-gestión-de-dependencias-y-ambientes)
    - [4. Especificación de Actualización](#4-especificación-de-actualización)
- [Sistema de validación y esquemas](#sistema-de-validación-y-esquemas)
  - [Descripción](#descripción-4)
  - [Principios de Validación](#principios-de-validación)
  - [Componentes](#componentes-2)
    - [1. Especificación de Validación de Configuración](#1-especificación-de-validación-de-configuración)
    - [2. Especificación de Validación de Mensajes de Commit](#2-especificación-de-validación-de-mensajes-de-commit)
    - [3. Especificación de Validación de Argumentos](#3-especificación-de-validación-de-argumentos-1)
- [Sistema de integración con Git](#sistema-de-integración-con-git)
  - [Descripción](#descripción-5)
  - [Componentes](#componentes-3)
    - [1. Especificación de Interfaz Git](#1-especificación-de-interfaz-git)
    - [2. Especificación de Manejo de Errores Git](#2-especificación-de-manejo-de-errores-git)
    - [3. Especificación de Comandos Git Wrapper](#3-especificación-de-comandos-git-wrapper)
- [Sistema de IA para generación de commits](#sistema-de-ia-para-generación-de-commits)
  - [Descripción](#descripción-6)
  - [Principios de Diseño de IA](#principios-de-diseño-de-ia)
  - [Componentes](#componentes-4)
    - [1. ComplexityAnalyzer - Analizador de Complejidad](#1-complexityanalyzer---analizador-de-complejidad)
    - [2. AiUsageTracker - Tracking de Uso de IA](#2-aiusagetracker---tracking-de-uso-de-ia)
    - [3. AiMessageGenerator - Generador de Mensajes con IA](#3-aimessagegenerator---generador-de-mensajes-con-ia)
    - [4. Comando ggai - Interfaz de IA](#4-comando-ggai---interfaz-de-ia)
    - [5. Integración de IA en Comandos Existentes](#5-integración-de-ia-en-comandos-existentes)
    - [6. Arquitectura de Integración de IA](#6-arquitectura-de-integración-de-ia)
- [Sistema de observabilidad y logging](#sistema-de-observabilidad-y-logging)
  - [Descripción](#descripción-7)
  - [Componentes](#componentes-5)
    - [1. Especificación del Sistema de Logging](#1-especificación-del-sistema-de-logging)
    - [2. Especificación de Niveles de Log y Verbose](#2-especificación-de-niveles-de-log-y-verbose)
- [Sistema de testing y calidad](#sistema-de-testing-y-calidad)
  - [Descripción](#descripción-8)
  - [Framework de Testing](#framework-de-testing)
  - [Estrategia de Coverage Progresivo](#estrategia-de-coverage-progresivo)
  - [Estructura de Testing Implementada](#estructura-de-testing-implementada)
  - [CI/CD y Quality Gates](#cicd-y-quality-gates)
- [Integraciones con terceros](#integraciones-con-terceros)
  - [Descripción](#descripción-9)
  - [Componentes](#componentes-6)
    - [1. Integración con APIs de IA](#1-integración-con-apis-de-ia)
  - [Consideraciones de Seguridad](#consideraciones-de-seguridad)
    - [1. Manejo de Credenciales](#1-manejo-de-credenciales)
    - [2. Validación de Entrada](#2-validación-de-entrada)
    - [3. Logging Seguro](#3-logging-seguro)
  - [Consideraciones de Rendimiento](#consideraciones-de-rendimiento)
    - [1. Optimización de Comandos](#1-optimización-de-comandos)
    - [2. Caching y Optimización](#2-caching-y-optimización)
    - [3. Análisis de Complejidad](#3-análisis-de-complejidad)

## Descripción general

ggGit es una suite de comandos independientes de línea de comandos que simplifica y acelera el trabajo con Git, especialmente enfocada en Conventional Commits. La arquitectura está diseñada para ser modular, extensible y mantener consistencia entre todos los comandos.

### Principios Arquitectónicos

1. **Comandos Independientes**: Cada comando es un script Python ejecutable independiente que reutiliza abstracciones comunes
2. **Configuración Jerárquica**: Sistema de configuración local con prioridad repositorio > módulo > usuario > default
3. **Interfaz Consistente**: Todos los comandos comparten el mismo sistema de colores, mensajes y estructura de ayuda
4. **Lenguaje Unificado**: Todos los comandos implementados en Python para consistencia y facilidad de mantenimiento
5. **IA Integrada**: Funcionalidades de IA integradas en comandos existentes y comandos conversacionales especializados

### Arquitectura General

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ggGit Architecture                                │
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │   Comandos      │    │  Configuración  │    │   Interfaz      │        │
│  │   Independientes│    │   Jerárquica    │    │   CLI Unificada │        │
│  │                 │    │                 │    │                 │        │
│  │ • 26 comandos   │    │ • Repositorio   │    │ • Click         │        │
│  │ • Python aliases│    │ • Usuario       │    │ • ColorManager  │        │
│  │ • BaseCommand   │    │ • Default       │    │ • Ayuda auto    │        │
│  │ • CommitCommand │    │ • JSON Schema   │    │ • IA Integrada  │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│           │                       │                       │                │
│           ▼                       ▼                       ▼                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Sistema de Integración Git                      │   │
│  │                                                                     │   │
│  │  • GitInterface (operaciones básicas, ramas, remotos)              │   │
│  │  • Validación de estado del repositorio                            │   │
│  │  • Manejo de errores y feedback                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Sistema de IA Integrado                         │   │
│  │                                                                     │   │
│  │  • ComplexityAnalyzer (análisis de complejidad)                    │   │
│  │  • AiMessageGenerator (generación de mensajes)                     │   │
│  │  • AiUsageTracker (monitoreo de uso y costos)                      │   │
│  │  • IA automática en comandos existentes                            │   │
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
- **Testing**: Framework de testing unificado con pytest y coverage progresivo (60% → 70% → 75% → 80%+)
- **Dependencias**: Gestión simplificada de dependencias

## Sistema de comandos independientes

### Descripción
Cada comando ggGit es un script Python ejecutable independiente que reutiliza abstracciones comunes. Todos los comandos comparten la misma estructura y patrones de implementación.

### Estructura de Comandos

```
src/
├── core/                  # Lógica central y abstracciones
│   ├── __init__.py
│   ├── config.py          # ConfigManager
│   ├── git.py             # GitInterface
│   ├── validation.py      # Validadores
│   ├── base_commands/     # Comandos base reutilizables
│   │   ├── __init__.py
│   │   ├── base.py        # BaseCommand
│   │   ├── commit.py      # CommitCommand
│   │   └── config.py      # ConfigCommand
│   ├── ai/                # Sistema de IA
│   │   ├── __init__.py
│   │   ├── complexity_analyzer.py  # ComplexityAnalyzer
│   │   ├── usage_tracker.py        # AiUsageTracker
│   │   └── message_generator.py    # AiMessageGenerator
│   └── utils/             # Utilidades
│       ├── __init__.py
│       ├── colors.py      # ColorManager
│       └── logging.py     # LoggingManager
└── commands/              # Comandos específicos ejecutables
    ├── # Conventional Commits
    ├── ggfeat.py          # Feature commits
    ├── ggfix.py           # Fix commits
    ├── ggdocs.py          # Documentation commits
    ├── ggstyle.py         # Style commits
    ├── ggrefactor.py      # Refactor commits
    ├── ggtest.py          # Test commits
    ├── ggchore.py         # Chore commits
    ├── ggperf.py          # Performance commits
    ├── ggci.py            # CI/CD commits
    ├── ggbuild.py         # Build system commits
    ├── ggbreak.py         # Breaking change commits
    ├── # Git Operations
    ├── gga.py             # Git add
    ├── ggs.py             # Git status
    ├── ggl.py             # Git log
    ├── ggdif.py           # Git diff
    ├── ggunstage.py       # Git unstage
    ├── ggreset.py         # Git reset
    ├── # Branch Management
    ├── ggmain.py          # Switch to main
    ├── ggdevelop.py       # Switch to develop
    ├── ggb.py             # List/create branches
    ├── ggmerge.py         # Merge branches
    ├── # Remote Operations
    ├── ggpl.py            # Git pull
    ├── ggpp.py            # Git push
    ├── # AI & Configuration
    ├── ggai.py            # AI commands
    ├── ggconfig.py        # Configuration management
    └── ggv.py             # Version info
```

### Especificación de Implementación de Comandos

#### Estructura Estándar de un Comando
Cada comando sigue esta estructura implementada:

```python
#!/usr/bin/env python3
"""
ggfeat - Commit changes adding the feat prefix to the message

Usage: ggfeat [options] <message>
"""

import click
import sys
from core.base_commands.base import BaseCommand
from core.base_commands.commit import CommitCommand
from core.utils.colors import ColorManager


class FeatCommand(BaseCommand):
    """Command for creating feature commits."""
    
    def execute(self, message, scope=None, ai=False, amend=False):
        """Execute the feat command."""
        # Si no hay mensaje y IA está habilitada, generar automáticamente
        if not message and self._is_ai_configured():
            message = self._generate_ai_message()
            if not message:
                return 1
        
        # Crear commit command
        commit_cmd = CommitCommand("feat")
        
        # Ejecutar commit (validación incluida en CommitCommand)
        result = commit_cmd.execute(message, scope, amend)
        
        # Manejar resultado
        if result == 0:
            click.echo(ColorManager.success("Commit realizado exitosamente"))
        else:
            click.echo(ColorManager.error("Error al realizar commit"))
            return result
        
        return result


@click.command()
@click.option('--scope', '-s', help='Scope del commit')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit')
@click.argument('message', required=False)
def main(scope, ai, amend, message):
    """Commit changes adding the feat prefix to the message"""
    try:
        command = FeatCommand()
        result = command.execute(message, scope, ai, amend)
        sys.exit(result)
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {str(e)}"))
        sys.exit(1)


if __name__ == "__main__":
    main()
```

#### Abstracciones Reutilizables Implementadas

**BaseCommand** (`core/base_commands/base.py`): Clase base para todos los comandos:
- `execute()`: Método abstracto para ejecutar comando
- `_is_ai_configured()`: Verificar si IA está configurada
- `_generate_ai_message()`: Generar mensaje usando IA
- `_execute_manual_commit()`: Ejecutar commit manual
- `_get_commit_prefix()`: Obtener prefijo del comando

**CommitCommand** (`core/base_commands/commit.py`): Lógica reutilizable de commits:
- `execute(message, scope, amend)`: Ejecutar commit con validación
- Validación automática de mensajes y scopes
- Integración con GitInterface para operaciones Git
- Manejo de errores y códigos de salida

**ConfigCommand** (`core/base_commands/config.py`): Gestión de configuración:
- `execute(action, key, value, level)`: Ejecutar operaciones de configuración
- Soporte para `get`, `set`, `list`, `reset`
- Validación de esquemas JSON
- Manejo de jerarquía de configuración

**ConfigManager** (`core/config.py`): Gestión de configuración jerárquica:
- `get_config(key, default=None)`: Obtener valor de configuración
- `set_config(key, value, level)`: Establecer valor de configuración
- `load_hierarchical_config()`: Cargar configuración siguiendo jerarquía
- `validate_config(config)`: Validar configuración con esquemas
- `get_config_level(key)`: Obtener nivel de configuración
- `list_config_keys(level)`: Listar claves de configuración
- `reset_config(level, key)`: Resetear configuración

**GitInterface** (`core/git.py`): Interfaz unificada con Git:
- **Operaciones básicas**: `stage_all_changes()`, `commit()`, `get_current_branch()`
- **Operaciones de ramas**: `switch_branch()`, `get_branches()`, `merge_branch()`
- **Operaciones remotas**: `pull()`, `push()`, `get_remote_branches()`
- **Análisis**: `get_diff_content()`, `get_files_to_analyze()`, `get_file_size()`
- **Validación**: `is_git_repository()`, `validate_clean_working_directory()`

**ColorManager** (`core/utils/colors.py`): Sistema de colores unificado:
- `success(message)`: Mensajes de éxito en verde
- `error(message)`: Mensajes de error en rojo
- `warning(message)`: Mensajes de advertencia en amarillo
- `info(message)`: Mensajes informativos en azul
- `operation(message)`: Mensajes de operación en cyan
- `highlight(message)`: Mensajes destacados en negrita

**LoggingManager** (`core/utils/logging.py`): Sistema de logging:
- Configuración centralizada de logging
- Rotación automática de archivos de log
- Niveles configurables (DEBUG, INFO, WARNING, ERROR)
- Formato consistente de mensajes de log

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
      scopes:
        type: array
        items:
          type: string
        description: "Scopes permitidos para commits (opcional)"
      require_scope:
        type: boolean
        default: false
        description: "Si se requiere scope en todos los commits"
      custom_types:
        type: array
        items:
          type: string
        description: "Tipos de commit personalizados adicionales (opcional)"
  
  ai:
    type: object
    properties:
      enabled:
        type: boolean
        default: false
        description: "Habilitar funcionalidades de IA"
      provider:
        type: string
        enum: ["openai", "anthropic", "azure", "local"]
        default: "openai"
        description: "Proveedor de servicios de IA (API compatible con OpenAI)"
      api_key_env:
        type: string
        default: "OPENAI_API_KEY"
        description: "Variable de entorno para API key"
      model:
        type: string
        default: "gpt-3.5-turbo"
        description: "Modelo de IA a utilizar"
      base_url:
        type: string
        description: "URL base para proveedores alternativos (opcional)"
  
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

**Paleta de Colores Estándar (Click):**
- **Success**: Verde (`green`) - Operaciones exitosas
- **Error**: Rojo (`red`) - Errores y fallos
- **Warning**: Amarillo (`yellow`) - Advertencias
- **Info**: Azul (`blue`) - Información general
- **Reset**: (`reset`) - Reset de colores

**Métodos de Salida con ColorManager:**
- `ColorManager.success(message)`: Mensajes de éxito en verde
- `ColorManager.error(message)`: Mensajes de error en rojo
- `ColorManager.warning(message)`: Mensajes de advertencia en amarillo
- `ColorManager.info(message)`: Mensajes informativos en azul
- `ColorManager.operation(message)`: Mensajes de operación en cyan
- `ColorManager.highlight(message)`: Mensajes destacados en negrita

#### 2. Especificación del Sistema de Ayuda

**Formato de Ayuda Automático (Click):**
Click genera automáticamente ayuda con formato estándar basado en:
- Docstring del comando
- Decoradores `@click.option()` con parámetro `help`
- Decoradores `@click.argument()` con descripción

**Ejemplo de Ayuda Generada:**
```
Usage: ggfeat [OPTIONS] [MESSAGE]

  Commit changes adding the feat prefix to the message

Options:
  -s, --scope TEXT    Scope del commit
  --ai               Usar IA para generar mensaje
  -a, --amend        Amend the last commit
  --help             Show this message and exit.
```

**Configuración de Ayuda:**
- Docstring del comando como descripción principal
- Parámetro `help` en `@click.option()` para descripción de opciones
- Parámetro `help` en `@click.argument()` para descripción de argumentos

#### 3. Especificación de Validación de Argumentos

**Validaciones con Click:**
- **Validación Automática**: Click valida automáticamente tipos y argumentos requeridos
- **Validación Personalizada**: Funciones de validación en `_validators.py`
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

### Consistencia entre Comandos

Para mantener consistencia entre todos los comandos:

1. **Esquema de Colores**: Todos los comandos usan los mismos códigos de color
2. **Formato de Mensajes**: Estructura consistente para errores, warnings, y éxito
3. **Sistema de Ayuda**: Formato unificado para todos los comandos
4. **Códigos de Salida**: Estandarización de códigos de error

### Bibliotecas CLI Recomendadas

**Opción Principal: Click**
- **Ventajas**: Sintaxis decorativa, manejo automático de ayuda, validación de tipos
- **Colores**: Integración con `colorama` para colores multiplataforma
- **Formato**: Ayuda automática con formato estándar
- **Validación**: Validación automática de argumentos y tipos

**Alternativa: Typer**
- **Ventajas**: Basado en type hints, generación automática de CLI
- **Colores**: Soporte nativo para colores con `rich`
- **Formato**: Ayuda automática con formato moderno
- **Validación**: Validación automática basada en tipos

**Configuración Recomendada:**
```python
# Ejemplo con Click y ColorManager
import click
from core.utils.colors import ColorManager
from core.base_commands.base import BaseCommand

@click.command()
@click.option('--scope', '-s', help='Scope del commit')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.argument('message', required=False)
def ggfeat(scope, ai, message):
    """Commit changes adding the feat prefix to the message"""
    # Usar ColorManager para mensajes
    click.echo(ColorManager.success("Commit realizado exitosamente"))
    click.echo(ColorManager.error("Error al realizar commit"))
    # Implementación del comando
    pass
```

## Sistema de instalación y distribución

### Descripción
Sistema que facilita la instalación, actualización y distribución de ggGit en diferentes entornos.

### Componentes

#### 1. Especificación del Proceso de Instalación

**Dependencias Requeridas:**
- Python 3.12 (versión recomendada)
- Git instalado y configurado
- Conda o Mamba (para gestión de dependencias)
- Permisos de escritura en directorio home del usuario

**Dependencias de Python:**
- click>=8.0.0 (framework CLI)
- pyyaml>=6.0 (manejo de configuración)
- colorama (colores multiplataforma)

**Estructura de Instalación (Sistema de Aliases):**
```
ggGit/                    # Directorio del proyecto clonado
├── src/                  # Código fuente
│   ├── core/            # Módulos core
│   └── commands/        # Scripts Python ejecutables
├── install.py           # Script de instalación Python
├── install.ps1          # Script de instalación PowerShell
├── environment.yml      # Dependencias conda
└── requirements-dev.txt # Dependencias de desarrollo

# Aliases creados en shell config (~/.bashrc, ~/.zshrc, PowerShell profile)
export GGGIT_ROOT="/path/to/ggGit"
export PYTHONPATH="$GGGIT_ROOT/src:$PYTHONPATH"
alias ggfeat='python $GGGIT_ROOT/src/commands/ggfeat.py'
alias ggfix='python $GGGIT_ROOT/src/commands/ggfix.py'
# ... (todos los comandos)
```

**Proceso de Instalación (Sistema de Aliases):**
1. **Verificación de Dependencias**: Comprobar Python 3.12+ y Git
2. **Clonado del Repositorio**: `git clone https://github.com/novafuria/ggGit`
3. **Instalación de Dependencias**: `pip install click pyyaml jsonschema colorama`
4. **Creación de Aliases**: Script automático crea aliases en shell config
5. **Configuración de Variables**: `GGGIT_ROOT` y `PYTHONPATH` configurados
6. **Verificación**: Comprobar que la instalación fue exitosa
7. **Activación**: Reiniciar terminal o ejecutar `source ~/.bashrc`

#### 2. Especificación de Instalación desde Repositorio

**Instalación Directa (Sistema de Aliases):**
- Clonar repositorio desde GitHub
- Ejecutar `python install.py` (Linux/macOS) o `.\install.ps1` (Windows)
- Creación automática de aliases en shell config
- Configuración automática de variables de entorno
- Instalación automática de dependencias Python

**Ventajas del Sistema de Aliases:**
- **Simplicidad**: Solo clonar y ejecutar script
- **Consistencia**: Mismo código fuente para todos los usuarios
- **Actualizaciones**: `git pull` para obtener últimas versiones
- **Desarrollo**: Fácil testing y desarrollo local
- **Multiplataforma**: Funciona en Linux, macOS y Windows
- **Sin PATH**: No requiere modificar PATH del sistema

#### 3. Gestión de Dependencias y Ambientes

**Estrategia de Dependencias:**
ggGit utiliza conda/mamba para la gestión de dependencias, alineándose con las prácticas de Novafuria y proporcionando un ambiente reproducible y aislado.

**Archivo de Configuración:**
- `environment.yml`: Especifica el ambiente de desarrollo con Python 3.12 y dependencias mínimas
- Compatible tanto con conda como con mamba
- Incluye canales conda-forge para paquetes actualizados

**Dependencias Principales:**
- **click>=8.0.0**: Framework CLI para comandos
- **pyyaml>=6.0**: Manejo de archivos de configuración YAML
- **colorama**: Colores multiplataforma para terminal

**Comandos de Desarrollo:**
- `conda env create -f environment.yml`: Crear ambiente de desarrollo
- `conda activate gggit`: Activar ambiente de desarrollo
- `mamba env create -f environment.yml`: Alternativa con mamba (si está disponible)
- `mamba activate gggit`: Activar ambiente con mamba

**Ventajas de la Estrategia:**
- **Reproducibilidad**: Ambiente idéntico en todos los entornos
- **Aislamiento**: No interfiere con otros proyectos Python
- **Rendimiento**: mamba es significativamente más rápido que conda
- **Compatibilidad**: Funciona en Windows, macOS y Linux
- **Escalabilidad**: Fácil adición de dependencias científicas futuras

#### 4. Especificación de Actualización

**Proceso de Actualización:**
- `git pull` para obtener última versión
- Actualizar ambiente con `conda env update -f environment.yml` o `mamba env update -f environment.yml`
- Re-ejecutar script de instalación si es necesario
- Actualizar módulos core y comandos desde `src/`
- Mantener configuraciones existentes
- Verificación automática de integridad

## Sistema de validación y esquemas

### Descripción
Sistema que valida configuraciones, argumentos de comandos y mensajes de commit usando esquemas predefinidos. La validación distingue claramente entre tipos de commit fijos (ligados a comandos) y scopes configurables.

### Principios de Validación

**Tipos de Commit Fijos**: Los tipos están ligados a comandos específicos y no son configurables. Cada comando genera un tipo específico de commit.

**Scopes Configurables**: Los scopes son opcionales y configurables, permitiendo personalización por proyecto o equipo.

**Configuración Jerárquica**: La validación respeta la jerarquía de configuración (repositorio > módulo > usuario > default).

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

**Tipos de Commit Fijos:**
Los tipos de commit están ligados a comandos específicos y no son configurables:
- **feat**: Comando `ggfeat` - Nuevas funcionalidades
- **fix**: Comando `ggfix` - Correcciones de bugs
- **docs**: Comando `ggdocs` - Documentación
- **style**: Comando `ggstyle` - Cambios de estilo
- **refactor**: Comando `ggrefactor` - Refactorización
- **test**: Comando `ggtest` - Tests
- **chore**: Comando `ggchore` - Tareas de mantenimiento
- **perf**: Comando `ggperf` - Mejoras de rendimiento
- **ci**: Comando `ggci` - Cambios en CI/CD
- **build**: Comando `ggbuild` - Cambios en build system
- **break**: Comando `ggbreak` - Cambios breaking (incompatibles)

**Scopes Configurables:**
Los scopes son configurables y opcionales:
- Configuración en `conventional_commits.scopes`
- Validación de formato: letras minúsculas, números, guiones
- Opción `require_scope` para hacer scopes obligatorios

**Validaciones Requeridas:**
- Tipo de commit debe corresponder al comando ejecutado
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
    enum: [feat, fix, docs, style, refactor, test, chore, perf, ci, build, break]
    description: "Tipo de commit según comando ejecutado"
  scope:
    type: string
    pattern: "^[a-z0-9-]+$"
    description: "Scope del commit (opcional, configurable)"
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
Sistema que utiliza inteligencia artificial para analizar cambios y generar mensajes de commit automáticamente. La integración de IA está implementada con componentes modulares que proporcionan análisis de complejidad, generación de mensajes y tracking de uso.

### Principios de Diseño de IA

**API Estándar**: Solo se soportan proveedores con API compatible con OpenAI para simplificar la integración y mantenimiento.

**Configuración Única**: La configuración de IA se maneja en un solo lugar (archivo de configuración) sin necesidad de múltiples archivos o esquemas.

**Integración Natural**: La IA se integra naturalmente en comandos existentes sin requerir configuración adicional.

**Análisis Inteligente**: El sistema analiza la complejidad de los cambios para decidir entre generación automática con IA o mensajes educativos de fallback.

**Tracking de Uso**: Monitoreo de consumo de IA, costos y límites para control de gastos.

### Componentes

#### 1. ComplexityAnalyzer - Analizador de Complejidad

**Funcionalidad:**
- Analiza la complejidad de cambios para decidir entre IA y fallback
- Evalúa número de archivos, líneas de diff y tamaño de archivos
- Aplica límites configurables para determinar si usar IA
- Genera mensajes educativos de fallback cuando no se recomienda IA

**Métodos Principales:**
- `should_use_ai()`: Determina si usar IA basado en complejidad
- `get_fallback_message()`: Genera mensaje educativo de fallback
- `get_analysis_summary()`: Proporciona resumen del análisis

**Criterios de Análisis:**
- **Número de archivos**: Límite configurable (default: 10)
- **Líneas de diff**: Límite configurable (default: 200)
- **Tamaño de archivos**: Límite configurable (default: 5000 bytes)
- **Tipos de archivos**: Categorización por extensión y patrón

#### 2. AiUsageTracker - Tracking de Uso de IA

**Funcionalidad:**
- Monitorea consumo de IA, tokens y costos estimados
- Aplica límites de costo configurados
- Almacena estadísticas en archivo YAML
- Proporciona comandos para reset y consulta de uso

**Métodos Principales:**
- `increment_usage()`: Incrementa contadores de uso
- `get_usage_stats()`: Obtiene estadísticas de uso
- `is_cost_limit_exceeded()`: Verifica si se excedió límite de costo
- `reset_usage()`: Resetea contadores de uso

**Configuración:**
- Archivo de tracking: `.gggit/ai-usage.yaml` (configurable)
- Límite de costo: `ai.cost_limit` en configuración
- Tracking habilitado: `ai.tracking_enabled` en configuración

#### 3. AiMessageGenerator - Generador de Mensajes con IA

**Funcionalidad:**
- Genera mensajes de commit usando servicios de IA reales
- Implementa integración completa con Ollama (modelo local)
- Integra con tracking de uso para monitoreo
- Soporta múltiples proveedores de IA con API compatible

**Métodos Principales:**
- `generate_message(files, diff_content, commit_type)`: Genera mensaje con contexto específico
- `test_connection()`: Prueba conexión real con proveedor de IA
- `_call_ollama_api(prompt)`: Llamada real a API de Ollama
- `_build_context_prompt(files, diff, commit_type)`: Construye prompt contextual
- `_process_ai_response(response)`: Procesa y limpia respuesta de IA
- `_get_commit_type_context(commit_type)`: Contexto específico por tipo de commit

**Proveedores Soportados:**
- **Ollama (Local)**: Modelos locales como gemma3:4b (IMPLEMENTADO)
- **OpenAI**: GPT-3.5-turbo, GPT-4 (API compatible)
- **Anthropic**: Claude (API compatible)
- **Azure OpenAI**: Servicios empresariales (API compatible)

**Características Implementadas:**
- **Prompt contextual inteligente**: Incluye tipo de commit, archivos y diff
- **Procesamiento robusto**: Manejo de markdown, prefijos y formato
- **Contexto específico**: Diferentes prompts según tipo de commit
- **Error handling**: Sin fallback a mock, errores claros

#### 4. Comando ggai - Interfaz de IA

**Funcionalidad:**
- Comando principal para gestión de IA
- Subcomandos para diferentes operaciones
- Integración con todos los componentes de IA
- Interfaz unificada para testing y monitoreo

**Subcomandos:**
- `ggai main`: Genera mensaje de commit usando IA
- `ggai usage`: Muestra estadísticas de uso de IA
- `ggai usage reset`: Resetea contadores de uso
- `ggai test`: Prueba conexión con proveedor de IA

**Configuración de IA Implementada:**
```yaml
ai:
  enabled: true                    # Habilitar funcionalidades de IA
  provider: "openai"              # openai, anthropic, azure, local
  api_key_env: "GGGIT_AI_KEY"     # Variable de entorno para API key (ACTUALIZADO)
  model: "gemma3:4b"              # Modelo de IA a utilizar (Ollama local)
  base_url: "http://localhost:11434"  # URL base para Ollama local
  cost_limit: 5.00                # Límite de costo en USD por período
  tracking_enabled: true          # Habilitar tracking de uso
  usage_file: ".gggit/ai-usage.yaml"  # Archivo de tracking de uso
  analysis:                       # Configuración de análisis de complejidad
    max_files: 10                 # Máximo número de archivos para análisis
    max_diff_lines: 200           # Máximo número de líneas de diff
    max_file_size: 5000           # Máximo tamaño de archivo en bytes
```

**Nota de Configuración:**
- **Variable de entorno**: Debe configurarse `GGGIT_AI_KEY` (no `OPENAI_API_KEY`)
- **Ollama local**: Requiere Ollama ejecutándose en `http://localhost:11434`
- **Modelo recomendado**: `gemma3:4b` para mejor rendimiento local
- **Bug resuelto**: Configuración desalineada entre variable de entorno y configuración

**Parámetros de Configuración Detallados:**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `ai.enabled` | boolean | `false` | Habilitar/deshabilitar funcionalidades de IA |
| `ai.provider` | string | `"openai"` | Proveedor de IA (openai, anthropic, azure, local) |
| `ai.api_key_env` | string | `"OPENAI_API_KEY"` | Nombre de variable de entorno para API key |
| `ai.model` | string | `"gpt-3.5-turbo"` | Modelo de IA a utilizar |
| `ai.base_url` | string | `null` | URL base para proveedores alternativos |
| `ai.cost_limit` | number | `5.00` | Límite de costo en USD por período |
| `ai.tracking_enabled` | boolean | `true` | Habilitar tracking de uso de IA |
| `ai.usage_file` | string | `".gggit/ai-usage.yaml"` | Archivo para tracking de uso |
| `ai.analysis.max_files` | integer | `10` | Máximo archivos para análisis de complejidad |
| `ai.analysis.max_diff_lines` | integer | `200` | Máximo líneas de diff para análisis |
| `ai.analysis.max_file_size` | integer | `5000` | Máximo tamaño de archivo en bytes |

**Integración en Comandos Existentes:**
- **IA Automática**: Comandos sin argumentos activan IA automáticamente
- **Análisis Inteligente**: ComplexityAnalyzer decide si usar IA o fallback
- **Fallback Educativo**: Mensajes informativos cuando no se recomienda IA
- **Tracking Automático**: Monitoreo de uso en todas las operaciones de IA

#### 5. Integración de IA en Comandos Existentes

**IA Automática en Comandos (UNIFICADA):**
- **TODOS los comandos de commit**: Activan IA automáticamente sin argumentos
- **Sin análisis de complejidad**: Lógica de protección removida (commit `9c6755a`)
- **IA real implementada**: Usa Ollama local para generación de mensajes
- **Contexto específico**: Cada comando pasa su tipo de commit a la IA
- **Tracking automático**: Monitoreo de uso en todas las operaciones

**Flujo de IA Automática Unificado:**
1. Usuario ejecuta comando sin argumentos (ej: `ggfeat`)
2. Sistema verifica si IA está habilitada
3. **IA se ejecuta directamente** (sin análisis de complejidad)
4. Genera mensaje contextual con tipo de commit específico
5. Procesa respuesta y limpia prefijos automáticamente
6. Tracking de uso se actualiza automáticamente

**Comandos con IA Integrada (TODOS):**
- **Conventional Commits**: `ggfeat`, `ggfix`, `ggdocs`, `ggstyle`, `ggchore`
- **Comandos Especializados**: `ggbuild`, `ggci`, `ggperf`, `ggtest`, `ggbreak`
- **Comandos de Navegación**: `ggmain`, `ggb`, `ggmerge` (implementados)
- **Todos los comandos de commit** ahora usan IA automáticamente

**Configuración de IA por Comando:**
- **Configuración global**: `ai.*` se aplica a todos los comandos
- **Patrón unificado**: BaseCommand pasa `commit_type` a AiMessageGenerator
- **Sin flags específicos**: Comportamiento automático en todos los comandos
- **Contexto inteligente**: Prompts específicos según tipo de commit

#### 6. Arquitectura de Integración de IA

**Patrón de Integración (ACTUALIZADO):**
```python
# En cada comando de commit
def execute(self, message, scope=None, ai=False, amend=False):
    # Verificar si IA está configurada
    if not message and self._is_ai_configured():
        # Generar mensaje con IA directamente (sin análisis de complejidad)
        return self._generate_ai_message(scope, amend)
    
    # Continuar con commit normal
    return self._execute_manual_commit(message, scope, amend)

# En BaseCommand._generate_ai_message()
def _generate_ai_message(self, scope=None, amend=False):
    # Obtener archivos y diff
    files = analysis['files']
    diff_content = self.git.get_diff_content(files, staged=analysis['has_staged'])
    
    # Obtener tipo de commit del comando
    commit_type = self._get_commit_prefix() if hasattr(self, '_get_commit_prefix') else None
    
    # Generar mensaje con contexto específico
    message = generator.generate_message(files, diff_content, commit_type)
    
    # Ejecutar commit con mensaje generado
    return self._execute_manual_commit(message, scope, amend)
```

**Componentes de Integración (ACTUALIZADOS):**
- **BaseCommand**: Métodos helper para IA (`_is_ai_configured`, `_generate_ai_message`)
- **CommitCommand**: Lógica de commit reutilizable
- **AiMessageGenerator**: Generación de mensajes con IA real (Ollama)
- **AiUsageTracker**: Tracking de uso
- **ComplexityAnalyzer**: Ya no se usa (lógica de protección removida)

**Configuración de IA por Componente (ACTUALIZADA):**

**AiMessageGenerator (PRINCIPAL):**
- `ai.enabled`: Habilitar/deshabilitar generación de mensajes
- `ai.provider`: Proveedor de IA (openai, anthropic, azure, local)
- `ai.api_key_env`: Variable de entorno para API key (GGGIT_AI_KEY)
- `ai.model`: Modelo de IA a utilizar (gemma3:4b)
- `ai.base_url`: URL base para proveedores alternativos (http://localhost:11434)

**AiUsageTracker:**
- `ai.tracking_enabled`: Habilitar/deshabilitar tracking
- `ai.usage_file`: Archivo de almacenamiento de estadísticas
- `ai.cost_limit`: Límite de costo en USD

**ComplexityAnalyzer (OBSOLETO):**
- Ya no se usa en la implementación actual
- Lógica de protección removida en commit `9c6755a`
- Configuración `ai.analysis.*` no se aplica

**Integración en Comandos (UNIFICADA):**
- `ai.enabled`: Controla activación global de IA
- **Todos los comandos** usan IA automáticamente sin argumentos
- **Contexto específico**: Cada comando pasa su tipo de commit
- **Sin configuración adicional**: Comportamiento automático en todos los comandos

## Sistema de observabilidad y logging

### Descripción
Sistema que proporciona logging y debugging para facilitar el mantenimiento y troubleshooting de ggGit.

### Componentes

#### 1. Especificación del Sistema de Logging

**Estructura de Logs:**
- **Ubicación**: `~/.gggit/logs/`
- **Formato**: `gggit_YYYYMM.log` (rotación mensual)
- **Nivel**: INFO por defecto, DEBUG si está habilitado
- **Formato de Entrada**: `YYYY-MM-DD HH:MM:SS - gggit.<command> - LEVEL - message`
- **Módulo de Logging**: `core/utils/logging.py` para configuración centralizada

**Eventos a Registrar:**
- Ejecución de comandos con argumentos
- Errores y excepciones con contexto
- Cambios de configuración
- Operaciones de IA (solicitudes, respuestas, errores)
- Operaciones Git (commits, stage, etc.)

**Configuración de Logging:**
```yaml
logging:
  level: "INFO"  # ERROR, WARNING, INFO, DEBUG
  max_size: "10MB"
  backup_count: 5
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

#### 2. Especificación de Niveles de Log y Verbose

**Niveles de Log:**
- **ERROR**: Solo errores críticos
- **WARNING**: Advertencias y errores no críticos
- **INFO**: Información general de operaciones
- **DEBUG**: Información detallada para troubleshooting

**Modo Verbose:**
- **Activación**: `--verbose` flag en comandos
- **Configuración**: `ui.verbose: true` en configuración
- **Salida**: Información detallada de operaciones
- **Destino**: stdout para información del usuario

## Sistema de testing y calidad

### Descripción
Sistema de testing unificado que garantiza la calidad del código mediante pruebas unitarias, de integración y métricas de cobertura progresivas.

### Framework de Testing

**pytest como framework principal:**
- Sintaxis simple y legible
- Fixtures y parametrización avanzadas
- Integración nativa con GitHub Actions
- Soporte para TDD (Desarrollo Guiado por Pruebas)

### Estrategia de Coverage Progresivo

**Fase 1 - Abstracciones Base (60%):**
- Coverage mínimo del 60% para abstracciones básicas
- Tests para `ColorManager` y `BaseCommand`
- Configuración básica de pytest

**Fase 2 - Estructura Base (70%):**
- Coverage mínimo del 70% para estructura base optimizada
- Tests de integración para patrones de uso
- Quality gates en CI/CD

**Fase 3 - Implementaciones Completas (80%+):**
- Coverage mínimo del 80% para implementaciones funcionales
- Tests completos para `ConfigManager`, `GitInterface`, `LoggingManager`
- Coverage reporting y quality gates avanzados

### Estructura de Testing Implementada

```
tests/
├── __init__.py
├── conftest.py                      # Fixtures globales
├── test_base_command.py             # Tests para BaseCommand
├── test_colors.py                   # Tests para ColorManager
├── test_core.py                     # Tests para core modules
├── test_commands.py                 # Tests para comandos básicos
├── test_integration.py              # Tests de integración
├── test_config_manager.py           # Tests para ConfigManager
├── test_config_validation.py        # Tests para validación de esquemas
├── test_config_advanced.py          # Tests para funcionalidades avanzadas
├── test_config_command.py           # Tests para ConfigCommand
├── test_git_interface.py            # Tests para GitInterface básico
├── test_git_interface_extended.py   # Tests para GitInterface extendido
├── test_git_interface_branches.py   # Tests para operaciones de ramas
├── test_git_interface_merge.py      # Tests para operaciones de merge
├── test_git_interface_analysis.py   # Tests para análisis de archivos
├── test_git_interface_interactive.py # Tests para operaciones interactivas
├── test_git_utility_commands.py     # Tests para comandos de utilidad Git
├── test_git_navigation_commands.py  # Tests para comandos de navegación
├── test_git_advanced_commands.py    # Tests para comandos avanzados
├── test_git_interactive_commands.py # Tests para comandos interactivos
├── test_conventional_commits_basic.py      # Tests para commits básicos
├── test_conventional_commits_specialized.py # Tests para commits especializados
├── test_commit_command_final.py     # Tests para CommitCommand final
├── test_commit_command_integration.py # Tests para integración de CommitCommand
├── test_ggdocs.py                   # Tests para comando ggdocs
├── test_logging_manager.py          # Tests para LoggingManager
├── test_ai_configuration.py         # Tests para configuración de IA
├── test_complexity_analyzer.py      # Tests para ComplexityAnalyzer
├── test_ai_usage_tracker.py         # Tests para AiUsageTracker
├── test_ggai_command.py             # Tests para comando ggai
└── test_ai_integration.py           # Tests para integración de IA
```

### CI/CD y Quality Gates

**GitHub Actions:**
- Ejecución automática de tests en cada push/PR
- Coverage reporting con badges
- Quality gates que bloquean merge si no se cumple coverage mínimo
- Testing cross-platform (Linux, macOS, Windows)

**Métricas de Calidad:**
- Coverage de código progresivo
- Detección de código duplicado
- Análisis estático con herramientas como flake8
- Validación de tipos con mypy (opcional)

## Integraciones con terceros

### Descripción
Sistema que maneja integraciones con servicios externos, principalmente APIs de IA, manteniendo la simplicidad y consistencia del proyecto.

### Componentes

#### 1. Integración con APIs de IA

**Proveedores Soportados:**
- **OpenAI**: GPT-3.5-turbo, GPT-4 (API estándar)
- **Anthropic**: Claude (API compatible con OpenAI)
- **Azure OpenAI**: Servicios empresariales (API compatible)
- **Local**: Ollama y otros modelos locales (API compatible)

**Configuración Unificada:**
```yaml
ai:
  enabled: true
  provider: "openai"  # openai, anthropic, azure, local
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  base_url: "https://api.openai.com/v1"  # Opcional para proveedores alternativos
  cost_limit: 5.00
  tracking_enabled: true
```

**Manejo de Errores de IA:**
- **Rate Limiting**: Reintentos automáticos con backoff exponencial
- **Timeouts**: Configuración de timeouts por proveedor
- **Fallbacks**: Mensajes educativos cuando IA no está disponible
- **Tracking**: Monitoreo de uso y costos para control de gastos





### Consideraciones de Seguridad

#### 1. Manejo de Credenciales
- **API keys**: Almacenadas en variables de entorno (no en archivos de configuración)
- **Validación**: Verificación de permisos para archivos de configuración
- **Configuración**: `ai.api_key_env` especifica variable de entorno a usar
- **Seguridad**: No se registran credenciales en logs ni archivos

#### 2. Validación de Entrada
- **Argumentos**: Validación automática con Click y validadores personalizados
- **Configuración**: Validación con JSON Schema para prevenir configuraciones inválidas
- **Git**: Validación de estado del repositorio antes de operaciones
- **IA**: Sanitización de entrada para prompts y respuestas

#### 3. Logging Seguro
- **Credenciales**: No se registran API keys ni tokens en logs
- **Rotación**: Rotación automática de archivos de log
- **Permisos**: Archivos de configuración con permisos restrictivos
- **Tracking**: Archivo de uso de IA con permisos de usuario únicamente

### Consideraciones de Rendimiento

#### 1. Optimización de Comandos
- **Python unificado**: Todos los comandos en Python para consistencia
- **Aliases**: Sistema de aliases evita copia de archivos
- **Imports**: Importaciones optimizadas con `from core.*`
- **Lazy loading**: Carga de módulos IA solo cuando es necesario

#### 2. Caching y Optimización
- **Configuración**: Cache de configuración para evitar re-lectura
- **Análisis IA**: Cache de análisis de complejidad para evitar recálculos
- **Git**: Operaciones Git optimizadas con validaciones mínimas
- **Tracking**: Almacenamiento eficiente de estadísticas de uso

#### 3. Análisis de Complejidad
- **Límites configurables**: Análisis de complejidad con límites ajustables
- **Fallback inteligente**: Mensajes educativos cuando IA no es recomendable
- **Tracking automático**: Monitoreo de uso sin impacto en rendimiento
- **Configuración flexible**: Parámetros de análisis configurables por proyecto

Esta arquitectura proporciona una base sólida para el desarrollo futuro de ggGit, manteniendo la flexibilidad para evolucionar según las necesidades del proyecto y la comunidad.
