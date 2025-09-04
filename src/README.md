# ggGit - Patrones de Uso de Abstracciones

Este documento describe los patrones de uso de las abstracciones implementadas en ggGit.

## ColorManager

`ColorManager` proporciona un sistema unificado de colores para todos los comandos.

### Uso Básico

```python
from core.utils.colors import ColorManager
import click

# Mensajes de éxito
click.echo(ColorManager.success("Operación completada"))

# Mensajes de error
click.echo(ColorManager.error("Error en la operación"))

# Mensajes de advertencia
click.echo(ColorManager.warning("Advertencia importante"))

# Mensajes informativos
click.echo(ColorManager.info("Información adicional"))

# Mensajes de operación
click.echo(ColorManager.operation("Procesando..."))

# Texto destacado
click.echo(ColorManager.highlight("Texto importante"))

# Texto atenuado
click.echo(ColorManager.dim("Texto secundario"))
```

### Métodos Disponibles

- `success(message)`: Mensajes de éxito en verde
- `error(message)`: Mensajes de error en rojo
- `warning(message)`: Mensajes de advertencia en amarillo
- `info(message)`: Mensajes informativos en azul
- `operation(message)`: Mensajes de operación en cyan
- `highlight(message)`: Texto destacado en negrita
- `dim(message)`: Texto atenuado

## BaseCommand

`BaseCommand` es la clase base para todos los comandos de ggGit.

### Estructura de un Comando

```python
from core.base_commands.base import BaseCommand
from core.utils.colors import ColorManager
import click

class MiComando(BaseCommand):
    """Descripción del comando."""
    
    def execute(self, *args, **kwargs):
        """Implementar la lógica del comando."""
        # Acceso a componentes base
        config = self.config
        git = self.git
        validator = self.validator
        
        # Validar argumentos
        if not self.validate_args(args):
            return 1
        
        # Lógica del comando
        try:
            # Hacer algo
            click.echo(ColorManager.success("Comando ejecutado"))
            return 0
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {e}"))
            return 1

@click.command()
@click.option('--opcion', help='Descripción de la opción')
@click.argument('argumento', required=False)
def main(opcion, argumento):
    """Descripción del comando para Click."""
    try:
        cmd = MiComando()
        return cmd.run(argumento=argumento, opcion=opcion)
    except Exception as e:
        click.echo(ColorManager.error(f"Error: {e}"))
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
```

### Componentes Disponibles

- `self.config`: Instancia de `ConfigManager`
- `self.git`: Instancia de `GitInterface`
- `self.validator`: Instancia de `ArgumentValidator`

### Métodos Base

- `execute(*args, **kwargs)`: Método abstracto que debe implementarse
- `validate_args(args)`: Validación de argumentos (implementación por defecto)
- `setup_logging()`: Configuración de logging (implementación por defecto)
- `run(*args, **kwargs)`: Ejecuta el comando con manejo de errores

## Patrones de Implementación

### 1. Comando Simple

```python
class ComandoSimple(BaseCommand):
    def execute(self, mensaje):
        click.echo(ColorManager.info(f"Procesando: {mensaje}"))
        return 0
```

### 2. Comando con Validación

```python
class ComandoConValidacion(BaseCommand):
    def execute(self, mensaje):
        if not mensaje:
            click.echo(ColorManager.error("Mensaje requerido"))
            return 1
        
        self.validator.validate_commit_message(mensaje)
        click.echo(ColorManager.success("Validación exitosa"))
        return 0
```

### 3. Comando con Configuración

```python
class ComandoConConfig(BaseCommand):
    def execute(self, opcion):
        config_value = self.config.get_config('mi_config', 'default')
        click.echo(ColorManager.info(f"Configuración: {config_value}"))
        return 0
```

## Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Tests específicos
pytest tests/test_colors.py
pytest tests/test_base_command.py

# Con coverage
pytest --cov=src --cov-report=term-missing
```

### Estructura de Tests

```
tests/
├── conftest.py              # Configuración global
├── test_colors.py           # Tests para ColorManager
├── test_base_command.py     # Tests para BaseCommand
└── test_commands.py         # Tests para comandos específicos
```

## Configuración

### Dependencias

Las dependencias están definidas en `environment.yml`:

```yaml
dependencies:
  - python=3.12
  - click>=8.0.0
  - pyyaml>=6.0
  - pytest>=7.0.0
  - pytest-cov>=4.0.0
  - colorama
```

### Instalación

```bash
# Crear ambiente
conda env create -f environment.yml

# Activar ambiente
conda activate gggit

# Instalar en modo desarrollo
pip install -e .
```

## CI/CD

Los tests se ejecutan automáticamente en GitHub Actions en cada push y pull request.

### Configuración

- Archivo: `.github/workflows/test.yml`
- Python: 3.12
- Coverage: Mínimo 60%
- Reportes: HTML y XML