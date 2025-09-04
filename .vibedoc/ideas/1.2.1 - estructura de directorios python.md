# estructura de directorios python

## Idea
Necesitamos definir la estructura de directorios python para ggGit.

La estructura de directorios python para ggGit debe ser coherente con la documentación escrita hasta el momento.

Cursor sugiere seguir esta estructura:

```bash
gggit/
├── src/
│   ├── gggit/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── cli.py          # Abstracción CLI base
│   │   │   ├── config.py       # ConfigManager
│   │   │   ├── git.py          # GitWrapper
│   │   │   └── validation.py   # Validadores
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── base.py         # BaseCommand
│   │   │   ├── commit.py       # CommitCommand
│   │   │   └── config.py       # ConfigCommand
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── colors.py       # Sistema de colores
│   │       └── logging.py      # Sistema de logging
│   └── scripts/
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

Pero creo que seria mejor ir por una estructura que no separe el src internamente en modulos scripts y el resto del codigo, esto podria generar confusiones.

```bash
gggit/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── cli.py          # Abstracción CLI base
│   │   ├── config.py       # ConfigManager
│   │   ├── git.py          # GitWrapper
│   │   └── validation.py   # Validadores
│   ├── base_commands/
│   │   ├── __init__.py
│   │   ├── base.py         # BaseCommand
│   │   ├── commit.py       # CommitCommand
│   │   └── config.py       # ConfigCommand
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── colors.py       # Sistema de colores
│   │   └── logging.py      # Sistema de logging
│   └── commands/
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

Con este cambio, se puede ver que las estructuras son equivalentes, y se pueden usar las mismas abstracciones. Sin embargo, la segunda estructura es mas consistente con la arquitectura de ggGit, y es mas facil de entender.
