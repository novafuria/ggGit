# 13a1 - Hipótesis: Validación de consistencia en pipeline de CI

## Enunciado de la Hipótesis

**Dado** que los desarrolladores modifican o crean comandos en la suite de software (`src/commands/`),  
**Si** agregamos un Quality Gate automatizado en el pipeline de Integración Continua (CI) que valide la sincronización entre los comandos físicos existentes y el índice de documentación en `docs/commands.md`,  
**Entonces** el pipeline impedirá la integración de código que cause un desfase documental (evitando el "Patrón de Jon"), obligando al desarrollador a mantener la documentación principal sincronizada en el mismo Pull Request.

## Justificación y Modelo Mental

El "Patrón de Jon" ocurre por un sesgo de conveniencia temporal: documentar en la fase de diseño es estimulante, pero actualizar la referencia de comandos al finalizar el código se siente como una tarea secundaria o de baja prioridad. Al hacer que el pipeline sea el garante inflexible de esta consistencia (*"la documentación es el producto"*), elevamos la sincronización documental a un requisito técnico indispensable, igual que la compilación o el paso de pruebas unitarias.

## Validación Experimental

Para demostrar la validez de esta hipótesis, se ha diseñado un experimento detallado para implementar un validador automatizado:

- [[13a1a - Experimento: Implementar validador de consistencia de comandos en CI]]

## Referencias

- [[13a - Prevención del patrón de Jon en documentación]]
- [[11 - sistema de testing y calidad]]
