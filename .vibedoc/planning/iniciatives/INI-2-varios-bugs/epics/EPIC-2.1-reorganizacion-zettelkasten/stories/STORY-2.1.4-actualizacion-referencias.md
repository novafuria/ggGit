# [HISTORIA] - Actualización de Referencias

## 🎯 Objetivo

Buscar y actualizar todas las referencias cruzadas en archivos migrados, actualizar enlaces en planning que referencien zettels antiguos, y validar que la navegación funciona correctamente en la nueva estructura.

## 🌎 Contexto

Esta historia implementa la Fase 4 del plan de reorganización documentado en [4.1 - decisiones reorganizacion estructura zettelkasten](../../../ideas/4.1 - decisiones reorganizacion estructura zettelkasten.md). Es crítica para mantener la integridad de las conexiones entre zettels, que es fundamental en el sistema Zettelkasten.

Los archivos migrados contienen múltiples referencias internas usando la numeración antigua (1.2.3.4) que deben actualizarse a la nueva numeración Luhmann (2a1). También hay referencias desde la carpeta de planning hacia zettels específicos.

## 💡 Propuesta de Resolución

Se propone realizar una búsqueda sistemática de todas las referencias usando patrones regex, actualizar manualmente cada referencia para preservar el contexto, y validar que los enlaces funcionan correctamente. Se incluirá actualización de referencias bidireccionales y validación de navegación completa.

## 📦 Artefactos

- **Referencias actualizadas**: Todos los enlaces internos corregidos en archivos migrados
- **Planning actualizado**: Enlaces desde historias/épicas hacia zettels corregidos
- **Mapa de referencias**: Documento con todas las referencias encontradas y actualizadas
- **Validación de navegación**: Reporte confirmando que todos los enlaces funcionan

## 🔍 Criterios de Aceptación

### Referencias Internas Actualizadas
- Dado que los archivos migrados contienen referencias con numeración antigua
- Cuando se busquen patrones como `[1.2.3.4 - nombre](archivo.md)`
- Entonces deben actualizarse a la nueva numeración como `[2a1 - nombre](archivo.md)`

### Referencias desde Planning Actualizadas
- Dado que las historias/épicas referencian zettels específicos
- Cuando se revisen archivos en `.vibedoc/planning/`
- Entonces todas las referencias a zettels deben usar la nueva numeración

### Referencias Bidireccionales Mantenidas
- Dado que algunos zettels se referencian mutuamente
- Cuando se actualice una referencia en un archivo
- Entonces la referencia inversa también debe actualizarse si existe

### Navegación Funcional Validada
- Dado que necesitamos una estructura navegable
- Cuando se pruebe la navegación siguiendo enlaces
- Entonces todos los enlaces deben llevar a archivos existentes

### Sintaxis de Markdown Correcta
- Dado que las referencias usan sintaxis de enlaces Markdown
- Cuando se actualicen las referencias
- Entonces la sintaxis `[texto](ruta)` debe mantenerse correcta

### No Hay Enlaces Rotos
- Dado que no podemos tener referencias que no funcionan
- Cuando se valide la estructura completa
- Entonces no debe haber enlaces que apunten a archivos inexistentes

## 🔗 Dependencias y Recursos

### Dependencias

- **Historia anterior completada**: STORY-2.1.3 con migración ejecutada y commiteada
- **Estructura migrada estable**: Todos los archivos en sus ubicaciones finales
- **Mapeo de migración**: Lista completa de cambios de nombres para referencia

### Recursos

- **Herramientas de búsqueda**: grep, sed, o herramientas de find/replace para patrones
- **Editor de texto avanzado**: Para búsqueda y reemplazo con regex
- **Conocimiento de estructura**: Comprensión de las conexiones entre zettels
- **Tiempo dedicado**: Aproximadamente 4 horas para búsqueda, actualización y validación
