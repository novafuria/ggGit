# 13c - Resiliencia y tolerancia a fallos del sistema de IA

## Contexto y Problema

Con la unificación de los comandos de commit (como `ggfeat`, `ggfix`, etc.) para usar automáticamente la inteligencia artificial cuando no se proporciona un mensaje manual (introducido en el commit `9c6755a`), el flujo de trabajo del desarrollador se ha vuelto altamente dependiente de la disponibilidad de la API de IA (sea local con Ollama o en la nube con OpenAI/Anthropic).

Actualmente, si el generador de mensajes de IA (`_generate_ai_message` en `BaseCommand`) se encuentra con una API caída, una falta de conexión a red o si la instancia local de Ollama está apagada, el sistema captura la excepción, imprime un mensaje de error genérico como `Error generando mensaje con IA: ...` y finaliza con código de salida `1`, bloqueando completamente la posibilidad de realizar el commit en ese instante. Esto representa una falta de tolerancia a fallos en una herramienta de CLI que debería ser resiliente por diseño.

## Evolución e Hipótesis

Para solventar esta debilidad de resiliencia y asegurar que el desarrollador nunca quede bloqueado, planteamos dos hipótesis de mitigación interactiva y diagnóstica:

- [[13c1 - Hipótesis: Degradación graciosa con fallback manual interactivo]]
- [[13c2 - Hipótesis: Mensajes de diagnóstico proactivo para APIs de IA]]

## Referencias

- [[5 - sistema de interfaz de usuario cli]]
- [[9 - sistema de ia para generacion de commits]]
- [[3b15a-reflexion-reoinspeccion-documentacion-completada]]
