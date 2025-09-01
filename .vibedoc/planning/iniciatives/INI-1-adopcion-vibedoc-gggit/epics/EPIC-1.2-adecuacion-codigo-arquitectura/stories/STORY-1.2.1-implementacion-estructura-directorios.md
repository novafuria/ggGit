# [HISTORIA] - Implementación de Estructura de Directorios Python

## 🎯 Objetivo

Crear la estructura de directorios Python para ggGit siguiendo las decisiones tomadas en el zettel 1.2.1.1, estableciendo la base arquitectónica para la migración de Bash a Python y sentando las bases para la implementación de abstracciones y comandos.

## 🌎 Contexto

Esta historia es fundamental para la épica "Adecuación del Código a la Nueva Arquitectura Documentada". Sin la estructura de directorios correcta, no es posible avanzar con la implementación de abstracciones, comandos base o comandos específicos. La estructura definida en las decisiones (src/core/ para abstracciones, src/commands/ para ejecutables) debe ser implementada físicamente en el repositorio.

Esta implementación permitirá que las historias siguientes (implementación de abstracciones, comandos base, etc.) tengan un lugar claro donde desarrollar su código, siguiendo la separación de responsabilidades definida en la arquitectura.

## 💡 Propuesta de Resolución

Se propone crear la estructura de directorios completa siguiendo las decisiones tomadas:

```
gggit/
├── src/
│   ├── core/                  # Lógica central y abstracciones
│   │   ├── __init__.py
│   │   ├── cli.py             # Abstracción CLI base
│   │   ├── config.py          # ConfigManager
│   │   ├── git.py             # GitWrapper
│   │   ├── validation.py      # Validadores
│   │   ├── base_commands/     # Comandos base reutilizables
│   │   │   ├── __init__.py
│   │   │   ├── base.py        # BaseCommand
│   │   │   ├── commit.py      # CommitCommand
│   │   │   └── config.py      # ConfigCommand
│   │   └── utils/             # Utilidades
│   │       ├── __init__.py
│   │       ├── colors.py      # Sistema de colores
│   │       └── logging.py     # Sistema de logging
│   └── commands/              # Comandos específicos ejecutables
│       ├── ggfeat.py
│       ├── ggfix.py
│       ├── ggbreak.py
│       └── ... (todos los comandos)
├── config/
│   ├── config-schema.yaml
│   └── commit-schema.yaml
└── tests/
    ├── __init__.py
    └── test_*.py
```

Cada archivo Python incluirá docstrings básicos y estructura mínima para permitir importaciones correctas.

## 📦 Artefactos

- 📦 **Estructura de directorios completa**: Creación de todas las carpetas y archivos __init__.py necesarios
- 📦 **Archivos de configuración**: Creación de config-schema.yaml y commit-schema.yaml con estructura básica
- 📦 **Estructura de tests**: Creación de la carpeta tests/ con __init__.py
- 📦 **Documentación de estructura**: README.md en src/ explicando la organización de directorios
- 📦 **Scripts de validación**: Script básico para verificar que la estructura es correcta

## 🔍 Criterios de Aceptación

### Estructura de directorios:
- Dado que se debe implementar la estructura de directorios Python
- Cuando se ejecute el script de validación
- Entonces todos los directorios y archivos __init__.py deben estar presentes

### Importaciones básicas:
- Dado que la estructura debe permitir importaciones
- Cuando se intente importar desde cualquier módulo
- Entonces las importaciones deben funcionar sin errores de módulo no encontrado

### Coherencia con decisiones:
- Dado que la estructura debe reflejar las decisiones tomadas
- Cuando se compare con el zettel 1.2.1.1
- Entonces debe coincidir exactamente con la estructura definida

### Preparación para desarrollo:
- Dado que la estructura debe facilitar el desarrollo
- Cuando se intente crear un archivo en cualquier directorio
- Entonces debe ser posible crear y editar archivos sin problemas de permisos

## 🔗 Dependencias y Recursos

### Dependencias

- **Decisión de estructura**: El zettel 1.2.1.1 debe estar completado y commiteado
- **Documentación de arquitectura**: La arquitectura debe estar actualizada para reflejar la nueva estructura
- **Repositorio Git**: El repositorio debe estar en un estado limpio para crear la nueva estructura

### Recursos

- **Acceso al repositorio**: Permisos de escritura en el repositorio ggGit
- **Conocimiento de Python**: Comprensión de la estructura de paquetes Python y archivos __init__.py
- **Herramientas de desarrollo**: Editor de código y terminal para crear la estructura
- **Documentación de referencia**: Acceso al zettel 1.2.1.1 y documentación de arquitectura
