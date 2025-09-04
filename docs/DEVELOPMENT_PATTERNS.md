# Patrones de Desarrollo para ggGit

Este documento describe los patrones de desarrollo establecidos para ggGit, proporcionando guías claras para implementar nuevas funcionalidades y mantener la consistencia del código.

## Tabla de Contenidos

- [Arquitectura General](#arquitectura-general)
- [Patrón BaseCommand](#patrón-basecommand)
- [Gestión de Configuración](#gestión-de-configuración)
- [Operaciones Git](#operaciones-git)
- [Sistema de Logging](#sistema-de-logging)
- [Validación de Entrada](#validación-de-entrada)
- [Manejo de Errores](#manejo-de-errores)
- [Testing](#testing)
- [Convenciones de Código](#convenciones-de-código)

## Arquitectura General

ggGit sigue los principios de Clean Architecture, separando la capa de presentación de la capa de infraestructura:

```
src/
├── core/                    # Lógica de negocio (Clean Architecture)
│   ├── base_commands/       # Comandos base (Template Method Pattern)
│   ├── utils/              # Utilidades compartidas
│   ├── config.py           # Gestión de configuración
│   ├── git.py              # Interfaz Git
│   └── validation.py       # Validación de entrada
└── commands/               # Implementaciones específicas de comandos
```

### Principios Clave

1. **Separación de Responsabilidades**: Cada clase tiene una responsabilidad específica
2. **Inversión de Dependencias**: Las clases de alto nivel no dependen de las de bajo nivel
3. **Abstracción**: Las interfaces definen contratos claros
4. **Testabilidad**: Todo el código debe ser fácilmente testeable

## Patrón BaseCommand

### Estructura

Todas las implementaciones de comandos deben extender `BaseCommand`:

```python
from src.core.base_commands.base import BaseCommand

class MyCommand(BaseCommand):
    def execute(self, *args, **kwargs) -> int:
        """
        Implementar la lógica del comando.
        
        Returns:
            int: 0 para éxito, código de error para fallo
        """
        # 1. Validar argumentos
        if not self.validate_args(list(args)):
            return 1
        
        # 2. Usar componentes disponibles
        if not self.git.is_git_repository():
            click.echo(ColorManager.error("No es un repositorio Git"))
            return 1
        
        # 3. Ejecutar lógica del comando
        # ...
        
        return 0
```

### Componentes Disponibles

- `self.config`: Acceso a configuración
- `self.git`: Operaciones Git
- `self.validator`: Validación de entrada
- `self.logger`: Sistema de logging

### Métodos a Implementar

- `execute(*args, **kwargs) -> int`: Lógica principal del comando

### Métodos Opcionales a Sobrescribir

- `validate_args(args: List[str]) -> bool`: Validación específica del comando
- `setup_logging() -> None`: Configuración de logging específica

## Gestión de Configuración

### Uso del ConfigManager

```python
# Obtener configuración
commit_format = self.config.get_config('commit.format', 'conventional')
auto_stage = self.config.get_config('git.auto_stage', True)

# Establecer configuración
self.config.set_config('commit.format', 'conventional', level='user')

# Validar configuración
if not self.config.validate_config(config_data):
    raise ValueError("Configuración inválida")
```

### Niveles de Configuración

1. **Repository** (`.gggit/repo-config.yaml`) - Mayor prioridad
2. **Module** (`.gggit/modules/*.yaml`) - Configuración por módulo
3. **User** (`~/.gggit/user-config.yaml`) - Preferencias del usuario
4. **Default** (`~/.gggit/default-config.yaml`) - Valores por defecto

### Estructura de Configuración

```yaml
commit:
  format: conventional
  auto_stage: true
  max_length: 72

git:
  auto_stage: true
  default_branch: main

ui:
  colors:
    enabled: true
    theme: default
```

## Operaciones Git

### Uso del GitInterface

```python
# Verificar repositorio
if not self.git.is_git_repository():
    click.echo(ColorManager.error("No es un repositorio Git"))
    return 1

# Staging
if not self.git.stage_all_changes():
    click.echo(ColorManager.error("Error al hacer staging"))
    return 1

# Commit
if not self.git.commit("feat: add new feature"):
    click.echo(ColorManager.error("Error al hacer commit"))
    return 1

# Obtener estado
status = self.git.get_repository_status()
print(f"Rama actual: {status['current_branch']}")
```

### Patrones de Manejo de Errores

```python
try:
    if not self.git.commit(message):
        click.echo(ColorManager.error("Error en commit"))
        return 1
except subprocess.CalledProcessError as e:
    click.echo(ColorManager.error(f"Error de Git: {e.stderr.decode()}"))
    return 1
```

## Sistema de Logging

### Uso del LoggingManager

```python
# Logging básico
logger = self.logger.get_logger("my_command")
logger.info("Comando ejecutado exitosamente")

# Logging de ejecución de comando
self.logger.log_command_execution("ggfeat", ["add user auth"])

# Logging de errores
try:
    risky_operation()
except Exception as e:
    self.logger.log_error(e, "risky_operation")

# Logging de rendimiento
start_time = time.time()
# ... operación ...
duration = time.time() - start_time
self.logger.log_performance("git_commit", duration, {"files_count": 5})
```

### Niveles de Logging

- `DEBUG`: Información detallada para debugging
- `INFO`: Información general de ejecución
- `WARNING`: Advertencias que no detienen la ejecución
- `ERROR`: Errores que requieren atención
- `CRITICAL`: Errores críticos que detienen la ejecución

## Validación de Entrada

### Uso del ArgumentValidator

```python
# Validar mensaje de commit
try:
    self.validator.validate_commit_message(message)
except ValueError as e:
    click.echo(ColorManager.error(f"Error en mensaje: {e}"))
    return 1

# Validar scope
if scope:
    try:
        self.validator.validate_scope(scope)
    except ValueError as e:
        click.echo(ColorManager.error(f"Error en scope: {e}"))
        return 1

# Validar nombre de rama
try:
    self.validator.validate_branch_name(branch_name)
except ValueError as e:
    click.echo(ColorManager.error(f"Error en nombre de rama: {e}"))
    return 1
```

### Convenciones de Validación

- **Mensajes de commit**: Máximo 72 caracteres, no vacío
- **Scopes**: Solo letras minúsculas, números y guiones
- **Nombres de rama**: No vacío, caracteres válidos para Git

## Manejo de Errores

### Patrón Estándar

```python
def execute(self, *args, **kwargs) -> int:
    try:
        # Lógica del comando
        return 0
    except ValueError as e:
        click.echo(ColorManager.error(f"Error de validación: {e}"))
        return 1
    except subprocess.CalledProcessError as e:
        click.echo(ColorManager.error(f"Error de Git: {e.stderr.decode()}"))
        return 1
    except Exception as e:
        click.echo(ColorManager.error(f"Error inesperado: {e}"))
        return 1
```

### Códigos de Retorno

- `0`: Éxito
- `1`: Error general
- `2`: Error de validación
- `3`: Error de Git
- `4`: Error de configuración

## Testing

### Estructura de Tests

```
tests/
├── conftest.py              # Configuración global y fixtures
├── test_base_command.py     # Tests de BaseCommand
├── test_integration.py      # Tests de integración
├── test_commands.py         # Tests de comandos específicos
└── test_utils.py            # Tests de utilidades
```

### Patrones de Testing

```python
def test_command_execution(concrete_command, mock_click_echo):
    """Test de ejecución de comando."""
    result = concrete_command.run("test_arg")
    assert result == 0

def test_error_handling(concrete_command, mock_click_echo):
    """Test de manejo de errores."""
    class FailingCommand(BaseCommand):
        def execute(self, *args, **kwargs):
            raise ValueError("Test error")
    
    failing_command = FailingCommand()
    result = failing_command.run("test")
    
    assert result == 1
    mock_click_echo.assert_called_once()
```

### Fixtures Disponibles

- `concrete_command`: Implementación de BaseCommand para testing
- `config_manager`: Instancia de ConfigManager
- `git_interface`: Instancia de GitInterface
- `mock_click_echo`: Mock de click.echo
- `mock_subprocess`: Mock de subprocess
- `temp_git_repo`: Repositorio Git temporal

## Convenciones de Código

### Naming

- **Clases**: PascalCase (`BaseCommand`, `ConfigManager`)
- **Métodos**: snake_case (`execute`, `get_config`)
- **Variables**: snake_case (`commit_message`, `config_data`)
- **Constantes**: UPPER_SNAKE_CASE (`MAX_COMMIT_LENGTH`)

### Docstrings

```python
def execute(self, message: str, scope: Optional[str] = None) -> int:
    """
    Ejecutar comando de commit.
    
    Args:
        message (str): Mensaje de commit
        scope (Optional[str]): Scope del commit
        
    Returns:
        int: 0 para éxito, código de error para fallo
        
    Raises:
        ValueError: Si el mensaje es inválido
        RuntimeError: Si no es un repositorio Git
    """
```

### Type Hints

```python
from typing import List, Optional, Dict, Any

def process_files(files: List[str], config: Dict[str, Any]) -> Optional[int]:
    """Procesar archivos con configuración."""
    pass
```

### Imports

```python
# Imports estándar
import os
import sys
from pathlib import Path
from typing import List, Optional

# Imports de terceros
import click
import pytest

# Imports locales
from src.core.base_commands.base import BaseCommand
from src.core.utils.colors import ColorManager
```

## Guías de Implementación

### Para Nuevos Comandos

1. Crear clase que extienda `BaseCommand`
2. Implementar método `execute`
3. Agregar validación específica si es necesario
4. Escribir tests unitarios e integración
5. Documentar el comando

### Para Nuevas Funcionalidades

1. Identificar la capa apropiada (core vs commands)
2. Seguir patrones existentes
3. Agregar documentación detallada
4. Escribir tests comprehensivos
5. Actualizar este documento si es necesario

### Para Corrección de Bugs

1. Escribir test que reproduzca el bug
2. Implementar la corrección
3. Verificar que el test pase
4. Ejecutar suite completa de tests
5. Documentar la corrección

## Herramientas de Desarrollo

### Testing

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest tests/test_integration.py

# Ejecutar con coverage
pytest --cov=src --cov-report=html

# Ejecutar tests marcados
pytest -m unit
pytest -m integration
```

### Linting

```bash
# Verificar estilo de código
flake8 src tests

# Formatear código
black src tests

# Verificar tipos
mypy src
```

### Coverage

```bash
# Generar reporte de coverage
coverage run -m pytest
coverage report
coverage html
```

## Recursos Adicionales

- [Documentación de pytest](https://docs.pytest.org/)
- [Guía de Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Convenciones de Python](https://pep8.org/)
- [Type Hints en Python](https://docs.python.org/3/library/typing.html)
