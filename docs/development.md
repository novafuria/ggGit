# Guía de Desarrollo

Esta guía está dirigida a desarrolladores que quieren contribuir a ggGit o entender su arquitectura interna.

## Arquitectura del Proyecto

ggGit está construido siguiendo principios de arquitectura limpia y modularidad. El proyecto se organiza en capas bien definidas que separan las responsabilidades y facilitan el mantenimiento.

### Estructura de Directorios

```
src/
├── commands/          # Comandos CLI individuales
├── core/             # Lógica central del sistema
│   ├── ai/           # Módulos de integración con IA
│   ├── base_commands/ # Comandos base y abstracciones
│   └── utils/        # Utilidades compartidas
└── __init__.py       # Inicialización del paquete
```

### Capas de la Arquitectura

**Capa de Comandos**: Cada comando CLI es un módulo independiente en `src/commands/`. Estos comandos actúan como puntos de entrada y orquestan la funcionalidad.

**Capa de Lógica de Negocio**: La lógica central reside en `src/core/` y se organiza por responsabilidades. Los módulos de IA, comandos base y utilidades están claramente separados.

**Capa de Utilidades**: Funciones auxiliares y helpers compartidos se encuentran en `src/core/utils/`, incluyendo manejo de colores, logging y validaciones.

## Configuración del Entorno de Desarrollo

### Requisitos del Sistema

- Python 3.7 o superior
- Git (para operaciones de repositorio)
- Ollama (opcional, para características de IA)

### Instalación del Entorno

```bash
# Clonar el repositorio
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Instalar en modo desarrollo
pip install -e .
```

### Dependencias de Desarrollo

El archivo `requirements-dev.txt` incluye todas las herramientas necesarias para el desarrollo:

- **pytest**: Framework de testing
- **pytest-cov**: Cobertura de código
- **black**: Formateo de código
- **flake8**: Linting de código
- **mypy**: Verificación de tipos
- **pre-commit**: Hooks de git

## Estructura de Comandos

### Patrón de Comando Base

Todos los comandos siguen un patrón consistente basado en la clase `BaseCommand`:

```python
from src.core.base_commands.base import BaseCommand
from click import command, option

@command()
@option('--message', '-m', help='Mensaje personalizado')
def ggfeat(message=None):
    """Comando para commits de funcionalidad."""
    cmd = BaseCommand('feat', message)
    cmd.execute()
```

### Comandos de Conventional Commits

Los comandos de conventional commits extienden `CommitCommand` que proporciona funcionalidad específica para commits:

```python
from src.core.base_commands.commit import CommitCommand
from click import command, option

@command()
@option('--message', '-m', help='Mensaje personalizado')
def ggfix(message=None):
    """Comando para commits de corrección."""
    cmd = CommitCommand('fix', message)
    cmd.execute()
```

### Comandos de Git

Los comandos de Git utilizan la interfaz `GitInterface` para ejecutar operaciones de Git:

```python
from src.core.git import GitInterface
from click import command

@command()
def ggs():
    """Comando para mostrar estado de Git."""
    git = GitInterface()
    git.status()
```

## Sistema de IA

### Arquitectura de IA

El sistema de IA está diseñado para ser modular y extensible. Los componentes principales son:

**MessageGenerator**: Genera mensajes de commit usando diferentes proveedores de IA.

**ComplexityAnalyzer**: Analiza la complejidad de los cambios para generar mensajes más precisos.

**UsageTracker**: Rastrea el uso de IA para optimización y debugging.

### Agregar Nuevo Proveedor de IA

Para agregar un nuevo proveedor de IA:

1. Crear clase que implemente la interfaz `AIProvider`
2. Registrar el proveedor en `MessageGenerator`
3. Agregar configuración en el sistema de configuración
4. Agregar tests para el nuevo proveedor

```python
class NuevoProveedor(AIProvider):
    def generate_message(self, changes, commit_type):
        # Implementar lógica de generación
        pass
    
    def test_connection(self):
        # Implementar prueba de conexión
        pass
```

## Sistema de Configuración

### Jerarquía de Configuración

El sistema de configuración utiliza un patrón de cadena de responsabilidad:

1. **Configuración de proyecto** (`.gggit/config.yaml`)
2. **Configuración de usuario** (`~/.gggit/config.yaml`)
3. **Configuración global** (valores por defecto)

### Agregar Nueva Configuración

Para agregar una nueva opción de configuración:

1. Definir el valor por defecto en `ConfigManager`
2. Agregar validación en el esquema de configuración
3. Documentar la nueva opción
4. Agregar tests de configuración

```python
# En ConfigManager
DEFAULT_CONFIG = {
    'nueva_opcion': {
        'default': 'valor_por_defecto',
        'type': 'string',
        'description': 'Descripción de la nueva opción'
    }
}
```

## Testing

### Estructura de Tests

Los tests están organizados en el directorio `tests/` siguiendo la estructura del código fuente:

```
tests/
├── test_commands.py          # Tests de comandos CLI
├── test_core/               # Tests de lógica central
├── test_ai/                 # Tests de integración con IA
└── conftest.py             # Configuración de pytest
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con cobertura
pytest --cov=src

# Ejecutar tests específicos
pytest tests/test_commands.py

# Ejecutar tests en modo verbose
pytest -v
```

### Escribir Tests

Los tests siguen el patrón AAA (Arrange, Act, Assert):

```python
def test_commit_command_generation():
    # Arrange
    cmd = CommitCommand('feat', None)
    
    # Act
    result = cmd.generate_message()
    
    # Assert
    assert result.startswith('feat:')
    assert len(result) > 10
```

## Linting y Formateo

### Herramientas de Calidad de Código

El proyecto utiliza varias herramientas para mantener la calidad del código:

- **Black**: Formateo automático de código
- **Flake8**: Detección de errores y problemas de estilo
- **MyPy**: Verificación de tipos estáticos
- **Pre-commit**: Hooks de git para validación automática

### Configuración de Pre-commit

```bash
# Instalar pre-commit
pip install pre-commit

# Instalar hooks
pre-commit install

# Ejecutar en todos los archivos
pre-commit run --all-files
```

### Formateo de Código

```bash
# Formatear con Black
black src/ tests/

# Verificar con Flake8
flake8 src/ tests/

# Verificar tipos con MyPy
mypy src/
```

## Documentación

### Documentación de Código

El proyecto utiliza docstrings en formato Google para documentar funciones y clases:

```python
def generate_commit_message(changes, commit_type):
    """Genera un mensaje de commit usando IA.
    
    Args:
        changes: Lista de archivos modificados
        commit_type: Tipo de commit (feat, fix, etc.)
    
    Returns:
        str: Mensaje de commit generado
        
    Raises:
        AIError: Si hay problemas con el proveedor de IA
    """
    pass
```

### Actualizar Documentación

Cuando agregues nuevas funcionalidades:

1. Actualiza docstrings en el código
2. Actualiza la documentación de usuario en `docs/`
3. Actualiza ejemplos de uso
4. Verifica que todos los enlaces funcionen

## Flujo de Contribución

### Proceso de Desarrollo

1. **Crear rama de feature**: `git checkout -b feature/nueva-funcionalidad`
2. **Desarrollar con TDD**: Escribir tests antes que código
3. **Ejecutar validaciones**: Tests, linting, formateo
4. **Crear commit**: Usar `ggfeat` o `ggfix` según corresponda
5. **Crear Pull Request**: Con descripción detallada

### Estándares de Código

- **Nombres descriptivos**: Variables y funciones deben ser claras
- **Funciones pequeñas**: Máximo 20-30 líneas por función
- **Comentarios útiles**: Explicar el "por qué", no el "qué"
- **Manejo de errores**: Usar excepciones apropiadas
- **Tests completos**: Cobertura mínima del 80%

### Revisión de Código

Antes de crear un Pull Request:

1. Ejecutar todos los tests: `pytest`
2. Verificar linting: `flake8 src/ tests/`
3. Verificar tipos: `mypy src/`
4. Formatear código: `black src/ tests/`
5. Actualizar documentación si es necesario

## Debugging

### Herramientas de Debug

```bash
# Ejecutar con logging detallado
GGGIT_LOG_LEVEL=DEBUG ggfeat

# Ejecutar con modo verbose
ggfeat --verbose

# Ver configuración actual
ggconfig --verbose
```

### Logs de Desarrollo

Los logs se almacenan en `~/.gggit/gggit.log` y incluyen:

- Operaciones de Git ejecutadas
- Llamadas a APIs de IA
- Errores y excepciones
- Información de configuración

### Debugging de IA

```bash
# Probar conexión de IA
ggai test --verbose

# Ver configuración de IA
ggai config

# Generar mensaje con debug
ggai generate --debug
```

## Optimización

### Performance

Para optimizar el rendimiento:

1. **Cache de IA**: Los mensajes generados se cachean automáticamente
2. **Lazy Loading**: Los módulos se cargan solo cuando se necesitan
3. **Validación eficiente**: Las validaciones se ejecutan solo cuando es necesario

### Monitoreo

El sistema incluye métricas básicas de uso:

- Número de comandos ejecutados
- Tiempo de respuesta de IA
- Errores y excepciones
- Uso de memoria

## Despliegue

### Versionado

El proyecto sigue Semantic Versioning (SemVer):

- **MAJOR**: Cambios incompatibles
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs

### Release Process

1. Actualizar versión en `__init__.py`
2. Actualizar CHANGELOG.md
3. Crear tag de versión
4. Generar release en GitHub
5. Actualizar documentación

### Distribución

El proyecto se distribuye a través de:

- **GitHub Releases**: Archivos binarios y código fuente
- **PyPI**: Para instalación con pip (futuro)
- **Homebrew**: Para usuarios de macOS (futuro)

Esta guía proporciona una base sólida para contribuir al desarrollo de ggGit. Para preguntas específicas o dudas sobre la implementación, consulta los issues existentes o crea uno nuevo en el repositorio.
