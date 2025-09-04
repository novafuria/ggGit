# [HISTORIA] - Implementación de LoggingManager básico

## 🎯 Objetivo

Implementar la funcionalidad básica del LoggingManager para proporcionar logging y debugging a los comandos ggGit, facilitando el mantenimiento y troubleshooting del sistema.

## 🌎 Contexto

Esta historia es importante para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" y la idea 1.2.3 - comandos base. Actualmente, LoggingManager tiene todos sus métodos marcados como TODO, lo que impide el logging funcional.

El LoggingManager es esencial para:
1. **Debugging**: Registrar información detallada durante la ejecución de comandos
2. **Monitoreo**: Trackear el uso y rendimiento de los comandos
3. **Troubleshooting**: Identificar problemas cuando los comandos fallan
4. **Auditoría**: Mantener registro de operaciones realizadas

Esta implementación debe seguir la especificación de la arquitectura (architecture.md) y crear logs estructurados en `~/.gggit/logs/`.

## 💡 Propuesta de Resolución

Se propone implementar los métodos básicos del LoggingManager:

1. **_setup_logging()**: Configurar el sistema de logging con archivos y consola
2. **log_command_execution()**: Registrar la ejecución de comandos con argumentos
3. **log_error()**: Registrar errores con contexto y stack trace
4. **get_logger()**: Crear loggers específicos para módulos

La implementación incluirá:
- Configuración de logging con rotación de archivos
- Logs estructurados con timestamps y niveles
- Directorio de logs en `~/.gggit/logs/`
- Formato consistente: `YYYY-MM-DD HH:MM:SS - gggit.<module> - LEVEL - message`
- Manejo de diferentes niveles de log (DEBUG, INFO, WARNING, ERROR)

## 📦 Artefactos

- 📦 **Código fuente del LoggingManager**: Implementación completa de los métodos básicos en `src/core/utils/logging.py`
- 📦 **Pruebas unitarias**: Tests para cada método implementado en `tests/test_logging_manager.py`
- 📦 **Configuración de logging**: Archivo de configuración de logging con rotación
- 📦 **Documentación actualizada**: Docstrings y ejemplos de uso
- 📦 **Validación de funcionamiento**: Script que demuestre que el logging funciona correctamente

## 🔍 Criterios de Aceptación

### Configuración de logging:
- Dado que se debe configurar el sistema de logging
- Cuando se ejecute `_setup_logging()`
- Entonces debe crear el directorio `~/.gggit/logs/` y configurar handlers de archivo y consola

### Logging de comandos:
- Dado que se ejecuta un comando
- Cuando se llame `log_command_execution("ggfeat", ["add feature"])`
- Entonces debe registrar la ejecución con timestamp y argumentos en el archivo de log

### Logging de errores:
- Dado que ocurre un error
- Cuando se llame `log_error(ValueError("test"), "test_function")`
- Entonces debe registrar el error con stack trace y contexto en el archivo de log

### Creación de loggers:
- Dado que se necesita un logger específico
- Cuando se llame `get_logger("command")`
- Entonces debe retornar un logger configurado con namespace `gggit.command`

### Formato de logs:
- Dado que se registra un mensaje
- Cuando se examine el archivo de log
- Entonces debe seguir el formato: `YYYY-MM-DD HH:MM:SS - gggit.<module> - LEVEL - message`

### Rotación de archivos:
- Dado que se configuran logs con rotación
- Cuando se generen múltiples logs
- Entonces debe crear archivos separados por fecha y mantener un número limitado de archivos

### Tests unitarios:
- Dado que se debe validar la funcionalidad
- Cuando se ejecuten las pruebas unitarias
- Entonces debe tener cobertura del 100% para los métodos implementados

### Integración con comandos:
- Dado que se ejecuta un comando ggGit
- Cuando se examine el archivo de log
- Entonces debe registrar la ejecución del comando con sus argumentos

## 🔗 Dependencias y Recursos

### Dependencias

- **Estructura de directorios**: La estructura `src/core/utils/` debe estar implementada (STORY-1.2.1 completada)
- **BaseCommand**: Debe estar implementado para usar LoggingManager en comandos
- **Sistema de archivos**: Acceso de escritura al directorio home del usuario

### Recursos

- **Conocimiento de logging**: Comprensión del módulo logging de Python y configuración de handlers
- **Conocimiento de rotación de logs**: Entendimiento de RotatingFileHandler y TimedRotatingFileHandler
- **Entorno de testing**: Acceso a directorio temporal para pruebas de logging
- **Documentación de logging**: Referencia para configuración avanzada de logging en Python
