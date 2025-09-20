# decisiones estructura directorios python

## Idea
Decidimos sobre la estructura de directorios Python para ggGit basándonos en la idea [2a - estructura directorios python](2a%20-%20estructura%20directorios%20python.md).

## Decisiones Tomadas

### Estructura Final Aprobada
```bash
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
│   │   │   ├── base.py
│   │   │   ├── commit.py
│   │   │   └── config.py
│   │   └── utils/             # Utilidades
│   │       ├── __init__.py
│   │       ├── colors.py
│   │       └── logging.py
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

### Cambios Aplicados a la Primera Propuesta

1. **`src/gggit/` → `src/core/`**: Eliminamos la redundancia del nombre y usamos `core/` que es más común en herramientas CLI de Python
2. **`src/scripts/` → `src/commands/`**: Más descriptivo y coherente con la arquitectura documentada
3. **`gggit/commands/` → `core/base_commands/`**: Clarifica que son comandos base reutilizables, no ejecutables directos

### Justificación

- **Separación clara**: `core/` contiene abstracciones reutilizables, `commands/` contiene ejecutables
- **Convenciones Python**: `core/` es más común que `domain/` en herramientas CLI
- **Coherencia arquitectural**: Alineado con la documentación de arquitectura existente
- **Importaciones claras**: `from core.config import ConfigManager` es más intuitivo

### Impacto en Ideas Siguientes

Esta estructura facilita las implementaciones de:
- [2b - implementacion abstracciones](2b%20-%20implementacion%20abstracciones.md): Trabajar en `core/`
- [3a - comandos base](3a%20-%20comandos%20base.md): Trabajar en `core/base_commands/`
- [4a1 - comando de configuracion](4a1%20-%20comando%20de%20configuracion.md): Usar abstracciones de `core/`

### Próximos Pasos

1. Actualizar documentación de arquitectura para reflejar esta estructura
2. Proceder con la planificación detallada de implementación
3. Implementar las abstracciones base en `core/`
