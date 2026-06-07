# 13a - Prevención del patrón de Jon en documentación

## Contexto y Problema

Durante el análisis de la rama `session-bugs` (documentado en [[3b15-inconsistencias-documentacion-session-bugs]] y [[3b15a-reflexion-reoinspeccion-documentacion-completada]]), se descubrió una tendencia crítica denominada **"El Patrón de Jon"**: el desarrollo técnico avanza de forma sobresaliente (implementación real de IA, comandos de navegación, etc.), pero la documentación principal (`architecture.md`, `product-design.md`, README.md) se queda rezagada, rompiendo el principio fundamental de Vibedoc de *"la documentación es el producto"*.

La corrección de estas inconsistencias requirió una fase tardía y costosa de reoinspección manual. Necesitamos un mecanismo preventivo para evitar el desfase documental sistemático.

## Evolución e Hipótesis

Para abordar este desafío conceptual, formulamos dos hipótesis de validación y gobernanza que se detallan a continuación:

- [[13a1 - Hipótesis: Validación de consistencia en pipeline de CI]]
- [[13a2 - Hipótesis: Autodisciplina asistida mediante Git Hooks interactivos]]

## Referencias

- [[1 - vibedoc]]
- [[3b15-inconsistencias-documentacion-session-bugs]]
- [[3b15a-reflexion-reoinspeccion-documentacion-completada]]
