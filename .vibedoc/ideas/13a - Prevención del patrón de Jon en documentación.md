# 13a - Prevención del patrón de Jon en documentación

## Contexto y Problema

Durante el análisis de la rama `session-bugs` (documentado en [[3b15-inconsistencias-documentacion-session-bugs]] y [[3b15a-reflexion-reoinspeccion-documentacion-completada]]), se descubrió una tendencia crítica denominada **"El Patrón de Jon"**: el desarrollo técnico avanza de forma sobresaliente (implementación real de IA, comandos de navegación, etc.), pero la documentación principal (`architecture.md`, `product-design.md`, README.md) se queda rezagada, rompiendo el principio fundamental de Vibedoc de *"la documentación es el producto"*.

La corrección de estas inconsistencias requirió una fase tardía y costosa de reoinspección manual. Necesitamos un mecanismo preventivo para evitar el desfase documental sistemático.

## Hipótesis

### Hipótesis 1 (Validación por Pipeline de CI):
Si agregamos una validación automatizada en la CI que compare las fechas de modificación o las firmas de los comandos en `src/commands/` con sus secciones correspondientes en `docs/commands.md`, entonces el pipeline fallará si un programador introduce un nuevo comando sin documentarlo, forzando la actualización en el mismo commit.

### Hipótesis 2 (Gobernanza de Proceso - Git Hooks / Templates):
Si implementamos un template de Pull Request estructurado y un Git pre-push hook que escanee recursivamente los archivos `.py` modificados y pregunte interactivamente al desarrollador si actualizó los zettels y documentos correspondientes, entonces reduciremos la deriva documental en un 90% mediante autodisciplina asistida.

## Experimentos Propuestos

### Experimento 1 (Script de Validación de Consistencia de Comandos):
1. Desarrollar un script simple en Python (`scripts/validate_docs_sync.py`) que:
   - Escanee `src/commands/*.py` para listar los comandos reales.
   - Analice `docs/commands.md` y verifique la existencia de secciones o menciones explícitas para cada comando.
2. Integrar este script en el pipeline de GitHub Actions como un Quality Gate.
3. **Métrica de éxito**: 100% de comandos de código tienen correspondencia documental exacta. El pipeline previene fusiones inconsistentes de manera confiable.

## Referencias

- [[1 - vibedoc]]
- [[3b15-inconsistencias-documentacion-session-bugs]]
- [[3b15a-reflexion-reoinspeccion-documentacion-completada]]
