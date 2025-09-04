# [architecture] - ggGit

> Este documento es la culminación de la investigación y el diseño de producto. Consiste en la creación de una arquitectura de software que resuelva el problema planteado en el documento [01-research-and-assessment-of-the-problem](01-research-and-assessment-of-the-problem.md). Para eso se describirán los enfoques de cada una de las partes del sistema.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Descripción general](#descripción-general)

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
│  │ • ggfeat (py)  │    │ • Repositorio   │    │ • Click/Typer   │        │
│  │ • ggfix (py)   │    │ • Módulos       │    │ • Colores       │        │
│  │ • ggconfig (py)│    │ • Usuario       │    │ • Ayuda         │        │
│  │ • ggai (py)    │    │ • Default       │    │ • IA Integrada  │        │
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
│  │                    Sistema de IA Integrado                         │   │
│  │                                                                     │   │
│  │  • IA automática en comandos existentes                            │   │
│  │  • Comando conversacional ggai                                     │   │
│  │  • Análisis y generación automática                                │   │
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
- **Testing**: Framework de testing unificado con pytest y coverage progresivo (60% → 70% → 80%+)
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
│   ├── git.py             # GitWrapper
│   ├── validation.py      # Validadores
│   ├── base_commands/     # Comandos base reutilizables
│   │   ├── __init__.py
│   │   ├── base.py        # BaseCommand
│   │   ├── commit.py      # CommitCommand
│   │   └── config.py      # ConfigCommand
│   └── utils/             # Utilidades
│       ├── __init__.py
│       ├── colors.py      # Sistema de colores
│       └── logging.py     # Sistema de logging
└── commands/              # Comandos específicos ejecutables
    ├── ggfeat.py          # Comando de feature commits
    ├── ggfix.py           # Comando de fix commits
    ├── ggbreak.py         # Comando de breaking changes
    ├── ggdocs.py          # Comando de documentación
    ├── ggstyle.py         # Comando de cambios de estilo
    ├── ggrefactor.py      # Comando de refactorización
    ├── ggtest.py          # Comando de tests
    ├── ggchore.py         # Comando de tareas de mantenimiento
    ├── ggperf.py          # Comando de mejoras de rendimiento
    ├── ggci.py            # Comando de cambios en CI/CD
    ├── ggbuild.py         # Comando de cambios en build system
    ├── ggconfig.py        # Gestión de configuración
    ├── ggai.py            # Generación de commits con IA
    ├── gga.py             # Git add simplificado
    ├── ggs.py             # Git status simplificado
    ├── ggl.py             # Git log simplificado
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

import click
from core.config import ConfigManager
from core.git import GitInterface
from core.validation import ArgumentValidator

@click.command()
@click.option('--scope', '-s', help='Scope del commit')
@click.option('--ai', is_flag=True, help='Usar IA para generar mensaje')
@click.option('--amend', '-a', is_flag=True, help='Amend the last commit')
@click.argument('message', required=False)
def main(scope, ai, amend, message):
    """Commit changes adding the feat prefix to the message"""
    try:
        # Inicializar componentes
        config = ConfigManager()
        git = GitInterface()
        validator = ArgumentValidator()
        
        # Si no hay mensaje y IA está habilitada, generar automáticamente
        if not message and ai:
            message = generate_ai_message(git, config)
        
        # Validar entrada
        if message:
            validator.validate_commit_message(message)
        
        # Ejecutar operación
        git.stage_all_changes()
        commit_message = f"feat({scope}): {message}" if scope else f"feat: {message}"
        git.commit(commit_message)
        
        # Mostrar resultado
        click.echo(click.style("✅ Commit realizado exitosamente", fg="green"))
        
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg="red"))
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### Abstracciones Reutilizables

**Click Integration**: Todos los comandos usan Click para interfaz unificada:
- Decoradores `@click.command()` y `@click.option()` para definición de comandos
- `click.echo()` y `click.style()` para salida con colores
- Ayuda automática generada por Click
- Validación automática de argumentos y tipos

**ConfigManager** (`core/config.py`): Gestiona configuración jerárquica:
- `get_config(key, default=None)`: Obtener valor de configuración
- `load_hierarchical_config()`: Cargar configuración siguiendo jerarquía
- `validate_config(config)`: Validar configuración con esquemas

**GitInterface** (`core/git.py`): Interfaz unificada con Git:
- `stage_all_changes()`: Stage todos los cambios
- `commit(message)`: Realizar commit
- `get_current_branch()`: Obtener rama actual
- `is_git_repository()`: Verificar si es repositorio Git

**ArgumentValidator** (`core/validation.py`): Validación de argumentos:
- `validate_commit_message(message)`: Validar mensaje de commit
- `validate_scope(scope)`: Validar scope
- `validate_required_args(args, count)`: Validar argumentos requeridos

**BaseCommand** (`core/base_commands/base.py`): Clase base para comandos:
- `execute()`: Método abstracto para ejecutar comando
- `validate_args()`: Validación común de argumentos
- `setup_logging()`: Configuración de logging

**ColorManager** (`core/utils/colors.py`): Sistema de colores unificado:
- `success(message)`: Mensajes de éxito en verde
- `error(message)`: Mensajes de error en rojo
- `warning(message)`: Mensajes de advertencia en amarillo
- `info(message)`: Mensajes informativos en azul

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

**Estructura de Instalación:**
```
~/.gggit/
├── commands/              # Scripts Python ejecutables (desde src/commands/)
├── core/                  # Módulos core (desde src/core/)
├── config/               # Archivos de configuración
│   ├── default-config.yaml
│   ├── user-config.yaml
│   └── modules/
├── logs/                 # Archivos de log
└── cache/                # Cache temporal
```

**Proceso de Instalación:**
1. **Verificación de Dependencias**: Comprobar Python, Git y Conda/Mamba
2. **Configuración del Ambiente**: Crear ambiente virtual con `environment.yml`
3. **Creación de Directorios**: Estructura de directorios estándar
4. **Copia de Módulos Core**: Instalar módulos de `src/core/` a `~/.gggit/core/`
5. **Copia de Comandos**: Instalar scripts Python ejecutables de `src/commands/` a `~/.gggit/commands/`
6. **Configuración de PATH**: Agregar `~/.gggit/commands` al PATH
7. **Configuración Inicial**: Crear archivos de configuración por defecto
8. **Verificación**: Comprobar que la instalación fue exitosa

#### 2. Especificación de Instalación desde Repositorio

**Instalación Directa:**
- Clonar repositorio desde GitHub
- Ejecutar script de instalación local
- Copia automática de `src/core/` y `src/commands/` a `~/.gggit/`
- Configuración automática de PATH
- Creación de directorios de configuración

**Ventajas de Instalación Local:**
- Consistencia entre usuarios y CI/CD
- Sin dependencia de gestores de paquetes
- Actualizaciones mediante `git pull`
- Fácil desarrollo y testing

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
Sistema que utiliza inteligencia artificial para analizar cambios y generar mensajes de commit automáticamente. La integración de IA está simplificada para usar solo proveedores con API compatible con OpenAI.

### Principios de Diseño de IA

**API Estándar**: Solo se soportan proveedores con API compatible con OpenAI para simplificar la integración y mantenimiento.

**Configuración Única**: La configuración de IA se maneja en un solo lugar (archivo de configuración) sin necesidad de múltiples archivos o esquemas.

**Integración Natural**: La IA se integra naturalmente en comandos existentes sin requerir configuración adicional.

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
- **OpenAI**: GPT-3.5-turbo, GPT-4 (API estándar)
- **Anthropic**: Claude (API compatible con OpenAI)
- **Azure OpenAI**: Servicios de Azure (API compatible)
- **Local**: Modelos locales con API compatible (opcional)

**Configuración de IA:**
```yaml
ai:
  enabled: true
  provider: "openai"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  base_url: "https://api.openai.com/v1"  # Opcional para proveedores alternativos
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

#### 3. Especificación de Integración de IA en Comandos Existentes

**IA Automática en Comandos:**
- **ggfeat sin argumentos**: Analizar cambios y generar mensaje automáticamente
- **ggfix sin argumentos**: Analizar cambios y generar mensaje automáticamente
- **ggbreak sin argumentos**: Analizar cambios y generar mensaje automáticamente

**Flags de IA:**
- `--ai`: Habilitar generación automática con IA
- `--no-ai`: Deshabilitar IA (comportamiento manual)
- `--ai-provider <provider>`: Especificar proveedor de IA
- `--ai-model <model>`: Especificar modelo de IA

**Flujo de IA Automática:**
1. Usuario ejecuta comando sin argumentos
2. Sistema detecta que se requiere mensaje
3. Analiza cambios staged automáticamente
4. Genera mensaje con IA
5. Muestra sugerencia al usuario
6. Permite aceptar, rechazar o modificar

#### 4. Especificación del Comando ggai Conversacional

**Funcionalidad:**
- Iniciar conversación interactiva con IA
- Ejecutar acciones complejas relacionadas con Git
- Generar scripts y comandos automáticamente
- Resolver problemas de Git con asistencia de IA

**Modos de Operación:**
- **Conversacional**: Chat interactivo con IA
- **Ejecutivo**: Ejecutar comandos sugeridos por IA
- **Asistente**: Ayuda para resolver problemas de Git

**Opciones del Comando:**
- `--conversation`: Modo conversacional interactivo
- `--execute`: Ejecutar comandos sugeridos por IA
- `--help`: Modo asistente para problemas
- `--provider <provider>`: Especificar proveedor de IA
- `--model <model>`: Especificar modelo de IA

**Ejemplos de Uso:**
```bash
# Conversación interactiva
ggai --conversation

# Ejecutar comandos sugeridos por IA
ggai --execute "resuelve conflictos de merge"

# Asistente para problemas
ggai --help "error al hacer push"
```

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

### Estructura de Testing

```
tests/
├── __init__.py
├── conftest.py              # Fixtures globales
├── test_core/               # Tests para abstracciones core
│   ├── test_colors.py       # Tests para ColorManager
│   ├── test_validation.py   # Tests para ArgumentValidator
│   └── test_base_command.py # Tests para BaseCommand
├── test_commands/           # Tests para comandos específicos
│   ├── test_ggfeat.py
│   ├── test_ggfix.py
│   └── test_ggbreak.py
└── test_integration/        # Tests de integración
    ├── test_command_flow.py
    └── test_error_handling.py
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
Sistema que maneja integraciones con servicios externos como APIs de IA, manteniendo la simplicidad y consistencia del proyecto.

### Componentes

#### 1. Especificación de Integración con APIs de IA

**Proveedores Soportados:**
- **OpenAI**: GPT-3.5-turbo, GPT-4
- **Anthropic**: Claude
- **Local**: Modelos locales (opcional)

**Configuración Simplificada:**
```yaml
ai:
  enabled: true
  provider: "openai"  # openai, anthropic, azure, local
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  base_url: "https://api.openai.com/v1"  # Solo para proveedores alternativos
```

**Manejo de Errores de IA:**
- **Rate Limiting**: Reintentos automáticos con backoff exponencial
- **Timeouts**: Configuración de timeouts por proveedor
- **Fallbacks**: Cambio automático de proveedor en caso de error
- **Cache**: Cache de respuestas para evitar llamadas repetidas





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
- Todos los comandos implementados en Python
- Uso de bibliotecas optimizadas para operaciones específicas
- Lazy loading de módulos pesados desde `core/`
- Importaciones optimizadas entre módulos core y commands

#### 2. Caching
- Cache de configuraciones para evitar re-lectura
- Cache de análisis de cambios para IA
- Cache de validaciones de esquemas

#### 3. Lazy Loading
- Carga de módulos solo cuando son necesarios
- Inicialización diferida de componentes pesados desde `core/`
- Carga condicional de proveedores de IA
- Importaciones dinámicas entre `commands/` y `core/`

Esta arquitectura proporciona una base sólida para el desarrollo futuro de ggGit, manteniendo la flexibilidad para evolucionar según las necesidades del proyecto y la comunidad.
