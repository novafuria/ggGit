# [EXPERIMENTO] - Refactorización y unificación de ConfigManager en un solo nivel de usuario

## 🎯 Objetivo

Refactorizar la clase `ConfigManager` en `src/core/config.py` para erradicar la lógica de alcances jerárquicos (repositorio, módulo) y unificarla en un único archivo de configuración del usuario (perfil global), asegurando la compatibilidad de lectura, simplificando los tests asociados y eliminando el código heredado innecesario.

## 🌎 Contexto

Actualmente, el sistema de validación y la jerarquía complican innecesariamente el mantenimiento (como se documenta en [[13f1 - Hipótesis: Centralización de configuración en perfil único de usuario]]). Este experimento simplificará la base técnica de configuración de `ggGit` antes de afrontar el diseño del Wizard interactivo de configuración de IA.

## 💡 Diseño Experimental

1. **Refactorización de ConfigManager (`src/core/config.py`)**:
   - Modificar la clase para que solo cargue la configuración por defecto de la aplicación y la fusione directamente con el archivo de configuración global del usuario localizado en `~/.gggit/config.json` (o similar).
   - Eliminar el escaneo recursivo de directorios ascendentes para buscar configuraciones locales de repositorio o módulo.
   - Simplificar el método `set_config` para que siempre escriba en la ruta de configuración global de usuario.
2. **Actualización de Schema Validation (`src/core/validation.py`)**:
   - Simplificar el JSON Schema si fuera necesario para ajustarse únicamente al perfil del usuario.
3. **Refactorización de Tests**:
   - Actualizar `tests/test_config_manager.py` y `tests/test_config_validation.py` para remover las pruebas de herencia de alcances locales y certificar que la lectura y escritura global funciona de forma impecable.
4. **Métrica de éxito**: Todos los comandos de configuración (`ggconfig`) y la suite de tests pasan con éxito total utilizando únicamente el archivo de configuración global del usuario.

## 📦 Artefactos Esperados

- 📦 **ConfigManager Simplificado**: Código fuente reducido en `src/core/config.py`.
- 📦 **Esquema de Validación Consolidado**: Cambios en `src/core/validation.py`.
- 📦 **Suite de Tests Actualizada**: `tests/test_config_manager.py` simplificado.

## 🔍 Criterios de Éxito

### Sencillez de Configuración:
- Dado que modificamos una propiedad usando `ggconfig set ai.enabled true`
- Cuando se consulte dicha propiedad desde cualquier directorio o repositorio del sistema
- Entonces la propiedad se resolverá con el valor unificado `true`, demostrando que el estado de la configuración no depende de la carpeta desde la que se invoque.

### Reducción de Complejidad de Código:
- Dado que simplificamos el código de `src/core/config.py`
- Cuando se compare la cantidad de líneas antes/después del refactor
- Entonces se debe registrar una reducción de al menos un 40% de líneas de código y de un 50% de complejidad ciclomática en la lógica de resolución de paths de configuración.

🔗 Referencias

- [[13f1 - Hipótesis: Centralización de configuración en perfil único de usuario]]
