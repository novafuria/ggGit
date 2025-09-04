# Estructura de Directorios Python - ggGit

Esta documentación describe la organización de directorios implementada para la migración de ggGit de Bash a Python, siguiendo las decisiones tomadas en el zettel 1.2.1.1.

## 📁 Estructura General

```
src/
├── core/                  # Lógica central y abstracciones
│   ├── __init__.py
│   ├── cli.py             # Abstracción CLI base
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
    ├── ggfeat.py
    ├── ggfix.py
    ├── ggbreak.py
    └── ... (todos los comandos)
```

## 🎯 Principios de Organización

### Separación de Responsabilidades

- **`core/`**: Contiene abstracciones reutilizables y lógica central
- **`commands/`**: Contiene scripts Python ejecutables independientes
- **`config/`**: Contiene esquemas de configuración
- **`tests/`**: Contiene pruebas unitarias e integración

### Convenciones Python

- Todos los directorios contienen `__init__.py` para ser paquetes Python válidos
- Los archivos siguen convenciones de nomenclatura snake_case
- Cada módulo tiene docstrings descriptivos
- Las importaciones siguen el patrón `from core.module import Class`

## 📦 Módulos Core

### `core/cli.py`
Abstracción base para operaciones CLI con Click, proporcionando métodos comunes para:
- Impresión de mensajes con colores
- Manejo de errores
- Interfaz unificada

### `core/config.py`
Gestión de configuración jerárquica con prioridad:
1. Repositorio (`.gggit/repo-config.yaml`)
2. Módulo (`~/.gggit/modules/`)
3. Usuario (`~/.gggit/user-config.yaml`)
4. Default (`~/.gggit/default-config.yaml`)

### `core/git.py`
Interfaz unificada para operaciones Git:
- Validación de repositorio
- Operaciones de staging y commit
- Manejo de errores Git

### `core/validation.py`
Validación de argumentos y entradas:
- Mensajes de commit (Conventional Commits)
- Scopes y nombres de rama
- Rutas de archivos

### `core/base_commands/`
Comandos base reutilizables:
- **`base.py`**: Clase base para todos los comandos
- **`commit.py`**: Funcionalidad común para comandos de commit
- **`config.py`**: Gestión de configuración

### `core/utils/`
Utilidades comunes:
- **`colors.py`**: Sistema de colores unificado
- **`logging.py`**: Configuración de logging centralizada

## 🚀 Comandos Específicos

Los comandos en `commands/` son scripts Python ejecutables independientes que:
- Usan Click para interfaz CLI
- Importan abstracciones desde `core/`
- Siguen el patrón estándar definido en la arquitectura
- Son ejecutables directamente (`chmod +x`)

## 🔧 Configuración

Los esquemas de configuración están en `config/`:
- **`config-schema.yaml`**: Esquema principal de configuración
- **`commit-schema.yaml`**: Esquema para validación de commits

## 🧪 Testing

La estructura de tests está en `tests/`:
- **`test_core.py`**: Tests para módulos core
- **`test_commands.py`**: Tests para comandos
- Todos los tests siguen el patrón unittest de Python

## 📋 Próximos Pasos

Esta estructura establece la base para:
1. Implementación de abstracciones (Historia 1.2.2)
2. Comandos base (Historia 1.2.3)
3. Comando de configuración (Historia 1.2.4)
4. Comandos específicos (Historia 1.2.5)

## ✅ Validación

Para verificar que la estructura es correcta, ejecuta:
```bash
python validate_structure.py
```

Este script valida:
- Presencia de todos los directorios y archivos
- Archivos `__init__.py` en todos los paquetes
- Importaciones básicas funcionando
- Comandos Python ejecutables
