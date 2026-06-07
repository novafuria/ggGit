# 13e - Remoción del sistema de tracking de consumo de IA

## Contexto y Problema

Actualmente, `ggGit` cuenta con un sistema de tracking de consumo de IA (`src/core/ai/usage_tracker.py`, `AiUsageTracker`) diseñado para monitorear las llamadas, los límites de tokens, costos y cuotas de uso de los modelos de lenguaje. Sin embargo, en el entorno real de desarrollo, este sistema introduce múltiples problemas:

1.  **Complejidad Accidental**: Genera escrituras constantes en archivos de configuración locales del usuario, introduciendo ruido y potenciales problemas de concurrencia o bloqueos de archivos en la terminal.
2.  **Mantenimiento Imposible**: Los esquemas de precios de tokens de los proveedores (OpenAI, Anthropic, Azure, etc.) cambian constantemente y varían de forma drástica entre modelos. Intentar mantener un calculador de precios actualizado localmente es una batalla perdida y una fuente interminable de parches de código.
3.  **Redundancia**: Los usuarios que consumen modelos locales con Ollama no tienen costos asociados (consumo gratuito), y quienes usan APIs en la nube (OpenAI) ya cuentan con dashboards de facturación precisos, límites y tracking de costos en tiempo real provistos por la propia plataforma del proveedor.

## Evolución e Hipótesis

Para eliminar esta complejidad innecesaria y mejorar la mantenibilidad del software, proponemos la siguiente hipótesis:

- [[13e1 - Hipótesis: Simplificación del núcleo mediante remoción de tracking de uso de IA]]

## Referencias

- [[9 - sistema de ia para generacion de commits]]
- [[10 - sistema de observabilidad y logging]]
