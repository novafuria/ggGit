# 13e1 - Hipótesis: Simplificación del núcleo mediante remoción de tracking de uso de IA

## Enunciado de la Hipótesis

**Dado** que el módulo `AiUsageTracker` añade complejidad y escrituras redundantes al repositorio de configuración local,  
**Si** eliminamos por completo la clase `AiUsageTracker` y removemos todas sus importaciones e invocaciones dentro de `BaseCommand`, `AiMessageGenerator` y la suite de comandos de configuración,  
**Entonces** reduciremos significativamente el tamaño del código fuente del núcleo, eliminaremos operaciones de disco innecesarias que causan ruido en el espacio de trabajo del usuario y quitaremos una carga inútil de mantenimiento técnico (cálculo de costos y tokens), sin degradar ninguna funcionalidad de generación de mensajes de commit.

## Justificación y Modelo Mental

Un principio guía de la ingeniería es que *"el mejor código es el código que no existe"*. Si una característica añade coste de mantenimiento sin aportar un valor real percibido por el usuario (quien ya tiene un panel de costos oficial en OpenAI/Anthropic o usa Ollama gratis), lo mejor es removerla para reducir la superficie de errores del sistema. Esto simplifica drásticamente el flujo del comando `_generate_ai_message` en `BaseCommand`, haciéndolo más limpio y legible.

## Validación Experimental

Para validar y ejecutar la remoción de forma segura y sin romper la suite de pruebas del proyecto, se propone el siguiente diseño experimental:

- [[13e1a - Experimento: Deprecación y remoción segura de AiUsageTracker]]

## Referencias

- [[13e - Remoción del sistema de tracking de consumo de IA]]
- [[11 - sistema de testing y calidad]]
