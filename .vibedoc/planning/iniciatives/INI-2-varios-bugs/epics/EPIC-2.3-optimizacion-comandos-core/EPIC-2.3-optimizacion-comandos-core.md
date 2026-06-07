# [EPICA] - Optimización y Resiliencia de los Comandos Core de Git y Configuración

## 🎯 Objetivo de la Épica

Optimizar la suite de comandos principales de `ggGit` y su sistema de configuración eliminando deuda técnica, mejorando la resiliencia en fallos de red/IA, simplificando los perfiles de configuración a nivel de usuario, e incorporando un asistente interactivo de configuración de IA, garantizando un flujo de trabajo confiable y de baja fricción cognitiva.

## 🌎 Contexto y Justificación

Tras estabilizar la infraestructura de CI/CD y dependencias, hemos identificado cuatro grandes focos de mejora funcional que impactan directamente en la usabilidad y mantenibilidad de la aplicación a largo plazo (documentados bajo el Sistema 13 del Zettelkasten):
1. El comando `ggpl` no sincroniza tags móviles de forma robusta ni poda tags eliminados.
2. El tracking de uso de tokens (`AiUsageTracker`) genera complejidad accidental y escrituras redundantes.
3. El sistema de configuración jerárquico es excesivo; un único perfil a nivel de usuario es suficiente y más fácil de razonar.
4. El proceso de configuración manual de la IA tiene una alta fricción técnica y cognitiva.

Al agrupar estas optimizaciones en una sola épica, mantenemos una estructura de planeación limpia y secuencial, evitando la dispersión de carpetas de épica individuales para tareas pequeñas pero altamente conectadas.

## 💡 Visión de la Solución

Se implementarán de forma iterativa cuatro historias de usuario que resuelvan cada uno de los problemas identificados. Comenzaremos con la sincronización automática de tags en `ggpl` (Story 2.3.1), seguida de la simplificación del tracker, la unificación del ConfigManager y la creación del asistente interactivo `ggconfigia`.

## 🚀 Alcance de la Épica

### Debe Tener
- **Sincronización robusta de tags (`ggpl`)**: Forzado y poda de tags remotos.
- **Remoción de AiUsageTracker**: Deprecación y eliminación física del tracker y sus dependencias.
- **Simplificación de ConfigManager**: Centralización de configuraciones en un único perfil global de usuario.
- **Asistente Interactivo de IA (`ggconfigia`)**: Wizard paso a paso para la inicialización y testeo de proveedores.

### Podría Tener
- **Validación automática de consistencia de comandos**: Implementación de checks en la CI.

### Fuera de Alcance
- **Cambio de frameworks de CLI**: Se mantiene Click como biblioteca core.

## Referencias a Zettels
- [[13 - bugs y deuda tecnica de software]]
- [[13d - El comando ggpl no obtiene las etiquetas o tags del remoto]]
- [[13e - Remoción del sistema de tracking de consumo de IA]]
- [[13f - Simplificación del alcance de configuración a nivel de usuario]]
- [[13g - Interfaz interactiva de configuración de IA]]

## 📋 Historias de la Épica

### 🔄 Historias En Proceso
1. **STORY-2.3.1b**: [Solución de Doble Comando para Sobreescritura de Tags en ggpl](stories/STORY-2.3.1b-sobreescritura-tags-ggpl.md)

### ✅ Historias Completadas
- **STORY-2.3.1**: [Sincronización de Etiquetas Robustas en ggpl](stories/STORY-2.3.1-sincronizacion-tags-ggpl.md)

### 📋 Historias Pendientes
2. **STORY-2.3.2**: Remoción del sistema de tracking de uso de IA
3. **STORY-2.3.3**: Centralización de la configuración en un solo perfil de usuario
4. **STORY-2.3.4**: Implementación de asistente interactivo ggconfigia
