# [EXPERIMENTO] - Implementación de comando interactivo ggconfigia

## 🎯 Objetivo

Diseñar, codificar y probar un nuevo comando ejecutable independiente `src/commands/ggconfigia.py` que guíe al usuario en un flujo interactivo de terminal para configurar su proveedor de IA, validando las entradas en caliente e inyectando valores por defecto según el proveedor seleccionado.

## 🌎 Contexto

La configuración interactiva disminuye de manera sustancial la tasa de error del desarrollador. Este experimento es la culminación práctica de la hipótesis [[13g1 - Hipótesis: Asistente Wizard interactivo de configuración de IA]] y depende directamente de la simplificación arquitectónica realizada en [[13f1.1 - Experimento: Refactorización y unificación de ConfigManager en un solo nivel de usuario]].

## 💡 Diseño Experimental

1. **Creación del Comando (`src/commands/ggconfigia.py`)**:
   - Crear el script Click configurando prompts e inputs interactivos:
     - Preguntar: *¿Qué proveedor deseas utilizar? [Ollama (local) / OpenAI / Anthropic / Azure]* (Selección de opción).
     - Si es Ollama: Ofrecer por defecto el endpoint `http://localhost:11434` y el modelo `gemma3:4b` sin requerir token (o preconfigurar `GGGIT_AI_KEY=ollama`).
     - Si es OpenAI u otro cloud: Solicitar el nombre de la variable de entorno o directamente la API key e inyectarla de forma persistente.
     - Confirmar con un test de conexión simulado (invocando internamente lógica de `ggai test`).
   - Escribir la configuración resultante directamente en el archivo unificado de usuario (`~/.gggit/config.json`).
2. **Registro de la Herramienta**:
   - Agregar el alias de comando `ggconfigia` en el script de instalación `install.py` y `install.sh`.
3. **Métrica de éxito**: Al ejecutar `python src/commands/ggconfigia.py`, el usuario es guiado paso a paso en menos de 10 segundos, guardando una configuración 100% válida en disco y lista para usar con `ggfeat`.

## 📦 Artefactos Esperados

- 📦 **Nuevo Comando CLI**: Archivo `src/commands/ggconfigia.py`.
- 📦 **Pruebas de la Interfaz**: `tests/test_ggconfigia_command.py` que valide el flujo interactivo usando `click.testing.CliRunner` y mocks de inputs de terminal.
- 📦 **Scripts de Instalación Actualizados**: Actualización en `install.py` e `install.sh` para incluir el nuevo comando en el path del usuario.

## 🔍 Criterios de Éxito

### Flujo Guiado y Predecible:
- Dado que el usuario inicia la configuración interactiva de IA ejecuntado `ggconfigia`
- Cuando selecciona "Ollama" de la lista de proveedores
- Entonces el sistema debe autocompletar el puerto `11434` y el modelo recomendado, confirmando de forma visual que la configuración fue escrita con éxito y está lista para su testeo.

### Validación de Credenciales:
- Dado que el usuario selecciona un proveedor en la nube como "OpenAI"
- Cuando no proporciona una API Key o variable válida
- Entonces el asistente interactivo debe emitir una advertencia en rojo y permitirle reintentar el ingreso o cancelar el flujo sin escribir datos corruptos o vacíos en la configuración.

🔗 Referencias

- [[13g1 - Hipótesis: Asistente Wizard interactivo de configuración de IA]]
