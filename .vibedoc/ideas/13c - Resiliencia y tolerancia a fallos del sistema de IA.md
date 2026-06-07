# 13c - Resiliencia y tolerancia a fallos del sistema de IA

## Contexto y Problema

Con la unificación de los comandos de commit (como `ggfeat`, `ggfix`, etc.) para usar automáticamente la inteligencia artificial cuando no se proporciona un mensaje manual (introducido en el commit `9c6755a`), el flujo de trabajo del desarrollador se ha vuelto altamente dependiente de la disponibilidad de la API de IA (sea local con Ollama o en la nube con OpenAI/Anthropic).

Actualmente, si el generador de mensajes de IA (`_generate_ai_message` en `BaseCommand`) se encuentra con una API caída, una falta de conexión a red o si la instancia local de Ollama está apagada, el sistema captura la excepción, imprime un mensaje de error genérico como `Error generando mensaje con IA: ...` y finaliza con código de salida `1`, bloqueando completamente la posibilidad de realizar el commit en ese instante. Esto representa una falta de tolerancia a fallos en una herramienta de CLI que debería ser resiliente por diseño.

## Hipótesis

### Hipótesis 1 (Degradación Graciosa / Fallback Manual Interactivo):
Si el intento de generación de mensaje con IA falla por problemas de conectividad o indisponibilidad del servicio, entonces el sistema debería realizar una "degradación graciosa" (graceful degradation) en lugar de abortar, preguntando interactivamente al usuario en la terminal si desea escribir un mensaje manual en ese momento (o abrir un editor como `nano`/`vim` estilo git tradicional), manteniendo el flujo de trabajo ininterrumpido.

### Hipótesis 2 (Caché local de contexto o Diagnóstico Proactivo):
Si el sistema detecta que el servicio de IA está caído, antes de fallar debería comprobar si hay una firma de error conocida (ej. `ConnectionRefusedError` en el puerto 11434 de Ollama) y proponer en el mismo mensaje de error el comando exacto de diagnóstico (p. ej., `ollama serve` o `ggai test`) reduciendo la carga cognitiva del desarrollador para arreglar su entorno.

## Experimentos Propuestos

### Experimento 1 (Manejo de Excepciones Específicas en BaseCommand):
1. Modificar el bloque `try...except` en `_generate_ai_message` en `src/core/base_commands/base.py`.
2. Si se captura una excepción de tipo conexión (`requests.exceptions.ConnectionError`, `urllib3.exceptions.MaxRetryError`), capturarla de forma específica.
3. En lugar de retornar `1` directamente, implementar un prompt interactivo de `click.confirm("¿Deseas ingresar un mensaje manual para continuar?")`. Si el usuario acepta, invocar `click.prompt` para capturar el mensaje y proceder con `_execute_manual_commit`.
4. **Métrica de éxito**: Un corte de red o la caída de Ollama no detiene el flujo de commits del desarrollador; el sistema se degrada graciosamente a un flujo manual guiado.

## Referencias

- [[5 - sistema de interfaz de usuario cli]]
- [[9 - sistema de ia para generacion de commits]]
- [[3b15a-reflexion-reoinspeccion-documentacion-completada]]
