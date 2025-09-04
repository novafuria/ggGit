# [HISTORIA] - Implementación de ConfigManager básico

## 🎯 Objetivo

Implementar la funcionalidad básica del ConfigManager para gestionar la configuración jerárquica de ggGit, permitiendo que los comandos puedan acceder y modificar configuraciones según la especificación de la arquitectura.

## 🌎 Contexto

Esta historia es fundamental para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" y específicamente para la idea 1.2.4 - comando de configuración. Actualmente, ConfigManager tiene todos sus métodos marcados como TODO, lo que impide que los comandos accedan a configuraciones personalizadas.

El ConfigManager es el corazón del sistema de configuración jerárquica que permite configuraciones específicas por contexto con prioridad repositorio > módulo > usuario > default. Sin esta funcionalidad, los comandos no pueden personalizar su comportamiento según las preferencias del usuario o las configuraciones del proyecto.

Esta implementación debe seguir la especificación de la arquitectura (architecture.md) y usar PyYAML para el manejo de archivos de configuración YAML.

## 💡 Propuesta de Resolución

Se propone implementar los 3 métodos básicos del ConfigManager:

1. **load_hierarchical_config()**: Cargar configuración siguiendo jerarquía de prioridad
2. **get_config(key, default=None)**: Obtener valor de configuración usando dot notation
3. **set_config(key, value, level='user')**: Establecer valor de configuración en nivel específico

La implementación incluirá:
- Carga de archivos YAML desde las 4 ubicaciones jerárquicas
- Merge de configuraciones respetando prioridad (repositorio > módulo > usuario > default)
- Acceso a configuraciones anidadas usando dot notation (ej: 'commit.format')
- Escritura de configuraciones en archivos YAML con formato preservado
- Manejo de errores para archivos YAML corruptos o inaccesibles
- Creación automática de directorios de configuración si no existen

## 📦 Artefactos

- 📦 **Código fuente del ConfigManager**: Implementación completa de los 3 métodos básicos en `src/core/config.py`
- 📦 **Pruebas unitarias**: Tests para cada método implementado en `tests/test_config_manager.py`
- 📦 **Archivos de configuración de ejemplo**: Creación de archivos de configuración por defecto
- 📦 **Documentación actualizada**: Docstrings completos y ejemplos de uso
- 📦 **Validación de funcionamiento**: Script que demuestre la carga y escritura de configuraciones

## 🔍 Criterios de Aceptación

### Carga de configuración jerárquica:
- Dado que existen archivos de configuración en diferentes niveles
- Cuando se ejecute `load_hierarchical_config()`
- Entonces debe cargar y mergear configuraciones respetando la prioridad repositorio > módulo > usuario > default

### Acceso con dot notation:
- Dado que existe una configuración anidada como `commit.format: "conventional"`
- Cuando se ejecute `get_config('commit.format', 'simple')`
- Entonces debe retornar "conventional" o el valor por defecto si no existe

### Escritura de configuración:
- Dado que se debe establecer una configuración en nivel de usuario
- Cuando se ejecute `set_config('ui.colors.enabled', True, 'user')`
- Entonces debe escribir el valor en `~/.gggit/user-config.yaml` y retornar sin errores

### Manejo de archivos inexistentes:
- Dado que no existen archivos de configuración
- Cuando se ejecute `load_hierarchical_config()`
- Entonces debe retornar configuración vacía sin errores

### Creación de directorios:
- Dado que el directorio `~/.gggit/` no existe
- Cuando se ejecute `set_config()` por primera vez
- Entonces debe crear el directorio automáticamente

### Manejo de errores YAML:
- Dado que existe un archivo YAML corrupto
- Cuando se ejecute `load_hierarchical_config()`
- Entonces debe manejar el error gracefully y continuar con otros archivos

### Tests unitarios:
- Dado que se debe validar la funcionalidad
- Cuando se ejecuten las pruebas unitarias
- Entonces debe tener cobertura del 100% para los métodos implementados

## 🔗 Dependencias y Recursos

### Dependencias

- **Estructura de directorios**: La estructura `src/core/` debe estar implementada (STORY-1.2.1 completada)
- **PyYAML**: Dependencia debe estar instalada para manejo de archivos YAML
- **LoggingManager**: Debe estar implementado para logging de cambios de configuración (STORY-1.2.3.3 completada)
- **Sistema de archivos**: Acceso de escritura al directorio home del usuario

### Recursos

- **Conocimiento de PyYAML**: Comprensión del manejo de archivos YAML en Python
- **Conocimiento de dot notation**: Entendimiento de acceso a diccionarios anidados
- **Entorno de testing**: Directorio temporal para pruebas de configuración
- **Documentación de PyYAML**: Referencia para manejo de errores y formato de archivos
