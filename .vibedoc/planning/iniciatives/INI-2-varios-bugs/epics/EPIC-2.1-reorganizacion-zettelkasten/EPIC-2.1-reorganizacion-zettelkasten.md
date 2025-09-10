# [EPICA] - Reorganización Estructura Zettelkasten

## 🎯 Objetivo de la Épica

Reorganizar la estructura del zettelkasten de ideas implementando el sistema Luhmann clásico alineado con la arquitectura documentada de ggGit, mejorando significativamente la navegación, comprensión y mantenimiento del conocimiento acumulado durante INI-1 (Adopción de Vibedoc).

## 🌎 Contexto y Justificación

Tras completar INI-1 (Adopción de Vibedoc en ggGit), el zettelkasten de ideas ha crecido a más de 75 archivos con una estructura jerárquica profunda (hasta 1.2.5.1.1) que dificulta la navegación y comprensión. La experiencia práctica ha revelado varios problemas críticos:

- **Navegación compleja**: La numeración jerárquica profunda requiere explorar múltiples archivos para entender el contexto
- **Desalineación con arquitectura**: Los zettels no reflejan la estructura modular documentada en `architecture.md`
- **Dificultad para ubicar información**: Especialmente sobre comandos específicos que están dispersos en múltiples niveles
- **Pérdida de la esencia Zettelkasten**: La estructura actual no refleja la evolución temporal del conocimiento

Esta épica es fundamental para establecer una base sólida que facilite el trabajo futuro en la iniciativa varios-bugs y permita el crecimiento orgánico del conocimiento siguiendo principios Zettelkasten auténticos.

## 💡 Visión de la Solución

Se implementará una reorganización completa basada en el sistema Luhmann clásico, donde la numeración refleje la construcción temporal del conocimiento en lugar de jerarquías rígidas. La solución incluirá:

- **Zettels de entrada alineados con arquitectura**: 13 zettels principales basados en el índice del documento de arquitectura
- **Sistema de numeración temporal**: Implementación del principio "la numeración es historia del pensamiento"
- **Migración controlada**: Script simple de revisión manual para mover archivos preservando la historia
- **Estructura orgánica**: Capacidad de crecimiento natural sin reorganizaciones futuras

La nueva estructura permitirá navegación intuitiva, ubicación rápida de información por sistema, y evolución orgánica del conocimiento.

## 🚀 Alcance de la Épica

### Debe Tener

- ✅ **13 Zettels de entrada**: Basados en sistemas de arquitectura (Vibedoc, Arquitectura Python, Comandos, Configuración, CLI, Instalación, Validación, Git, IA, Logging, Testing, Integraciones, Varios Bugs)
- ✅ **Migración completa**: Todos los 75+ archivos existentes migrados a nueva estructura
- ✅ **Script de migración**: Lista hardcodeada de comandos `mv` para revisión manual
- ✅ **Preservación de contenido**: Todo el conocimiento y historia preservados
- ✅ **Referencias actualizadas**: Enlaces internos corregidos en archivos migrados
- ✅ **Validación de estructura**: Verificación que la nueva estructura funciona correctamente

### Podría Tener

- ✨ **Herramientas de navegación**: Scripts para generar índices automáticos
- ✨ **Validador de consistencia**: Herramienta para detectar referencias rotas
- ✨ **Documentación de patrones**: Guías para crear nuevos zettels siguiendo la nueva estructura
- ✨ **Métricas de navegación**: Análisis de mejora en navegabilidad

## Fuera de Alcance

- 🚫 **Modificación de contenido**: No se cambiará el contenido de los zettels, solo su ubicación
- 🚫 **Herramientas automatizadas complejas**: No se desarrollarán scripts complejos de migración
- 🚫 **Reorganización de planning**: La estructura de planning se mantendrá sin cambios en esta épica
- 🚫 **Nuevas funcionalidades**: Esta épica es puramente organizacional

## ⚠️ Riesgos y Supuestos

### Riesgos Identificados

- ❗ **Referencias rotas**: Migración manual puede generar enlaces internos incorrectos
- ❗ **Pérdida de contexto**: Cambio de numeración puede confundir referencias históricas
- ❗ **Adopción del equipo**: Nueva estructura requiere adaptación de patrones mentales
- ❗ **Complejidad de migración**: 75+ archivos requieren revisión manual cuidadosa

### Supuestos Clave

- ❓ **Asumimos que la estructura de arquitectura es estable** y no cambiará durante la migración
- ❓ **Asumimos que el sistema Luhmann es apropiado** para el tipo de conocimiento que manejamos
- ❓ **Asumimos que la migración manual es más segura** que scripts automatizados complejos
- ❓ **Asumimos que el beneficio de navegación** justifica el esfuerzo de migración

## 🔗 Dependencias y Recursos Clave

### Dependencias

- **Documentación de arquitectura estable**: Requiere que `architecture.md` esté actualizado y no cambie durante migración
- **Decisiones validadas**: Necesita aprobación final de las decisiones documentadas en zettel 4.1
- **Rama de trabajo limpia**: Requiere rama `feature/reorganizacion-zettelkasten` sin conflictos

### Recursos Clave Necesarios

- **Tiempo dedicado para migración manual**: Aproximadamente 4-6 horas para migración completa
- **Conocimiento de estructura actual**: Comprensión profunda de la organización existente
- **Acceso completo al repositorio**: Permisos para crear ramas y mover archivos
- **Herramientas de validación**: Scripts básicos para verificar consistencia post-migración

## Referencias a Zettels

- **Zettel de idea**: [4 - reorganizacion estructura zettelkasten](../../../ideas/4 - reorganizacion estructura zettelkasten.md)
- **Zettel de decisiones**: [4.1 - decisiones reorganizacion estructura zettelkasten](../../../ideas/4.1 - decisiones reorganizacion estructura zettelkasten.md)
- **Arquitectura de referencia**: [architecture.md](../../../architecture.md)
- **Reflexión INI-1**: [1.3 - reflexion-final-iniciativa-adopcion-vibedoc](../../../ideas/1.3 - reflexion-final-iniciativa-adopcion-vibedoc.md)

## 📋 Historias de la Épica

### ✅ Historias Completadas

1. **STORY-2.1.1**: [Preparación Zettels de Entrada](stories/STORY-2.1.1-preparacion-zettels-entrada.md) - Crear 13 zettels de entrada y script de migración
2. **STORY-2.1.2**: [Revisión y Validación del Script](stories/STORY-2.1.2-revision-validacion-script.md) - Validar script en entorno de prueba
3. **STORY-2.1.3**: [Ejecución de Migración](stories/STORY-2.1.3-ejecucion-migracion.md) - Ejecutar migración real con preservación de historia
4. **STORY-2.1.4**: [Actualización de Referencias](stories/STORY-2.1.4-actualizacion-referencias.md) - Corregir 72+ referencias internas post-migración

### 🔄 Historias En Proceso

6. **STORY-2.1.6**: [Reorganización Zettels Metodológicos](stories/STORY-2.1.6-reorganizacion-zettels-metodologicos.md) - Reubicar zettels metodológicos bajo Sistema 1 (Vibedoc)

### 📋 Historias Pendientes

5. **STORY-2.1.5**: [Validación Final y Reflexión](stories/STORY-2.1.5-validacion-final-reflexion.md) - Validación completa y reflexión de épica
