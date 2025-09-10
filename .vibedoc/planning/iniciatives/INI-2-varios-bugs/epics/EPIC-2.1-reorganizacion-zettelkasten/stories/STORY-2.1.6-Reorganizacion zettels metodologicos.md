# [HISTORIA] - Reorganización Zettels Metodológicos

## 🎯 Objetivo

Reubicar los zettels metodológicos (actualmente numerados como 13.x) bajo el Sistema 1 (Vibedoc) con numeración 1h.x, ya que representan mejoras de metodología y procesos Vibedoc, no bugs de software ggGit.

## 🌎 Contexto

Durante la implementación de las historias 2.1.1-2.1.4, se identificó una inconsistencia conceptual: los zettels `13 - varios bugs` y sus reflexiones (`13a`, `13b`, `13c`, `13d`) contienen mejoras metodológicas de Vibedoc y procesos de documentación, no bugs del software ggGit.

Estos zettels documentan:
- Reflexiones sobre metodología Vibedoc aplicada
- Mejoras de procesos de documentación zettelkasten
- Evolución de la práctica metodológica
- Decisiones sobre reorganización estructural

Por coherencia conceptual, deben ubicarse bajo el Sistema 1 (Vibedoc) como mejoras metodológicas, siguiendo el principio Luhmann de que la numeración refleje la construcción temporal del conocimiento dentro de cada sistema.

## 💡 Propuesta de Resolución

Se propone migrar los zettels metodológicos con el siguiente mapeo:
- `13 - varios bugs.md` → `1h - mejoras estructura zettelkasten.md`
- `13a - reflexion story-2.1.1.md` → `1h1 - reflexion story-2.1.1.md`
- `13b - reflexion story-2.1.2.md` → `1h2 - reflexion story-2.1.2.md`
- `13c - reflexion story-2.1.3.md` → `1h3 - reflexion story-2.1.3.md`
- `13d - reflexion story-2.1.4.md` → `1h4 - reflexion story-2.1.4.md`

Actualizar todas las referencias internas y validar que la navegación sigue funcionando correctamente.

## 📦 Artefactos

- **Script de migración**: Comandos `mv` para reubicar archivos metodológicos
- **Referencias actualizadas**: Todos los enlaces internos corregidos
- **Zettel de entrada actualizado**: `1h - mejoras estructura zettelkasten.md` con contexto correcto
- **Validación de navegación**: Confirmación de que los enlaces funcionan
- **Zettel de reflexión**: Documentando la corrección conceptual realizada

## 🔍 Criterios de Aceptación

### Zettels Metodológicos Reubicados Correctamente
- Dado que los zettels 13.x contienen metodología Vibedoc
- Cuando se muevan a la numeración 1h.x
- Entonces deben estar bajo el Sistema 1 (Vibedoc)

### Coherencia Conceptual Restaurada
- Dado que el Sistema 1 agrupa todo lo relacionado con Vibedoc
- Cuando se revise la organización de zettels metodológicos
- Entonces debe ser evidente que pertenecen a mejoras de metodología

### Referencias Internas Actualizadas
- Dado que existen referencias cruzadas a estos zettels
- Cuando se actualicen las referencias de 13.x a 1h.x
- Entonces todos los enlaces deben funcionar correctamente

### Navegación Funcional Preservada
- Dado que la navegación debe mantenerse operativa
- Cuando se prueben los enlaces después de la migración
- Entonces no debe haber enlaces rotos

### Zettel de Entrada Coherente
- Dado que `1h` será el nuevo zettel de entrada metodológico
- Cuando se revise su contenido
- Entonces debe reflejar claramente que trata mejoras de Vibedoc

### Historia Temporal Preservada
- Dado que las reflexiones mantienen su secuencia cronológica
- Cuando se revise la numeración 1h1, 1h2, 1h3, 1h4
- Entonces debe reflejar la evolución temporal de las historias 2.1.1-2.1.4

### Limpieza del Sistema 13
- Dado que el Sistema 13 quedará sin contenido metodológico
- Cuando se complete la migración
- Entonces el Sistema 13 debe quedar disponible para verdaderos bugs de software

## 🔗 Dependencias y Recursos

### Dependencias

- **STORY-2.1.4 completada**: Referencias ya actualizadas y sistema estable
- **Estructura migrada estable**: Base sólida para realizar la corrección conceptual
- **Conocimiento de referencias**: Comprensión de qué enlaces necesitan actualización

### Recursos

- **Herramientas de migración**: Scripts `mv` y `sed` para automatización
- **Validación sistemática**: Verificación de que todos los enlaces funcionan
- **Conocimiento conceptual**: Comprensión de la diferencia entre metodología y bugs de software
- **Tiempo dedicado**: Aproximadamente 1 hora para migración, actualización y validación

## 🎯 Justificación Adicional

Esta reorganización es importante porque:

1. **Coherencia conceptual**: Los zettels metodológicos pertenecen al Sistema 1 (Vibedoc)
2. **Claridad para usuarios**: Es más intuitivo buscar mejoras metodológicas bajo Vibedoc
3. **Sistema 13 disponible**: Queda libre para verdaderos bugs de software ggGit
4. **Completitud de reorganización**: Cierra correctamente la épica EPIC-2.1
5. **Principio Luhmann**: La numeración debe reflejar la construcción conceptual del conocimiento

Esta historia completa la reorganización iniciada en EPIC-2.1 con coherencia conceptual total.
