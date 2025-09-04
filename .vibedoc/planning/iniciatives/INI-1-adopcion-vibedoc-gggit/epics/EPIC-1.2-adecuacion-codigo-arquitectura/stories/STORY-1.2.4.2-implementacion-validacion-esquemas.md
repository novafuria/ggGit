# [HISTORIA] - Implementación de validación y esquemas

## 🎯 Objetivo

Implementar el sistema de validación de configuraciones usando JSON Schema para asegurar que todas las configuraciones de ggGit cumplan con la estructura y tipos definidos en la arquitectura.

## 🌎 Contexto

Esta historia es crítica para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" y la idea 1.2.4 - comando de configuración. Sin validación de esquemas, las configuraciones pueden contener errores que causen fallos silenciosos o comportamientos inesperados en los comandos.

El sistema de validación debe verificar que las configuraciones cumplan con los esquemas definidos en `config-schema.yaml`, `commit-schema.yaml` y `module-schema.yaml`. Esto es especialmente importante para la configuración jerárquica donde diferentes niveles pueden tener estructuras inconsistentes.

Esta implementación debe integrarse con ConfigManager y proporcionar mensajes de error descriptivos para facilitar la corrección de configuraciones inválidas.

## 💡 Propuesta de Resolución

Se propone implementar la validación de esquemas con las siguientes funcionalidades:

1. **validate_config(config)**: Validar configuración contra esquema apropiado
2. **Integración con jsonschema**: Usar la librería jsonschema para validación
3. **Mensajes de error descriptivos**: Proporcionar información clara sobre errores de validación
4. **Fallback a configuración por defecto**: En caso de error, usar configuración por defecto
5. **Validación automática**: Validar configuraciones al cargar en ConfigManager

La implementación incluirá:
- Carga de esquemas JSON desde archivos en `config/`
- Validación de tipos, formatos y valores requeridos
- Mensajes de error específicos con ubicación del problema
- Logging de errores de validación para debugging
- Validación de configuraciones de módulos específicos
- Validación de mensajes de commit según Conventional Commits

## 📦 Artefactos

- 📦 **Código fuente de validación**: Implementación completa del método `validate_config()` en `src/core/config.py`
- 📦 **Esquemas JSON actualizados**: Archivos de esquema completos y validados en `config/`
- 📦 **Pruebas unitarias**: Tests para validación de esquemas en `tests/test_config_validation.py`
- 📦 **Casos de prueba**: Archivos de configuración válidos e inválidos para testing
- 📦 **Documentación de esquemas**: Documentación de la estructura de configuraciones
- 📦 **Script de validación**: Herramienta para validar configuraciones existentes

## 🔍 Criterios de Aceptación

### Validación de configuración válida:
- Dado que existe una configuración que cumple con el esquema
- Cuando se ejecute `validate_config(config)`
- Entonces debe retornar `True` sin errores

### Validación de configuración inválida:
- Dado que existe una configuración con tipos incorrectos
- Cuando se ejecute `validate_config(config)`
- Entonces debe lanzar `jsonschema.ValidationError` con mensaje descriptivo

### Validación de valores requeridos:
- Dado que falta un campo requerido en la configuración
- Cuando se ejecute `validate_config(config)`
- Entonces debe indicar específicamente qué campo falta

### Validación de tipos:
- Dado que un campo tiene un tipo incorrecto (ej: string en lugar de boolean)
- Cuando se ejecute `validate_config(config)`
- Entonces debe indicar el tipo esperado y el tipo actual

### Validación de formatos:
- Dado que un campo tiene formato incorrecto (ej: versión inválida)
- Cuando se ejecute `validate_config(config)`
- Entonces debe indicar el formato esperado

### Fallback a configuración por defecto:
- Dado que la configuración es inválida
- Cuando se ejecute `load_hierarchical_config()`
- Entonces debe usar configuración por defecto y loggear el error

### Validación de módulos:
- Dado que se valida configuración de módulo específico
- Cuando se ejecute `validate_config(config, schema_type='module')`
- Entonces debe usar el esquema de módulo apropiado

### Tests unitarios:
- Dado que se debe validar la funcionalidad
- Cuando se ejecuten las pruebas unitarias
- Entonces debe tener cobertura del 100% para la validación

## 🔗 Dependencias y Recursos

### Dependencias

- **ConfigManager básico**: STORY-1.2.4.1 debe estar completada para tener `load_hierarchical_config()`
- **jsonschema**: Dependencia debe estar instalada para validación de esquemas
- **Esquemas JSON**: Archivos de esquema deben estar definidos en `config/`
- **LoggingManager**: Debe estar implementado para logging de errores de validación

### Recursos

- **Conocimiento de JSON Schema**: Comprensión de la especificación JSON Schema
- **Conocimiento de jsonschema**: Entendimiento de la librería jsonschema de Python
- **Esquemas de referencia**: Ejemplos de esquemas JSON Schema para configuraciones
- **Entorno de testing**: Archivos de configuración de prueba para validación
