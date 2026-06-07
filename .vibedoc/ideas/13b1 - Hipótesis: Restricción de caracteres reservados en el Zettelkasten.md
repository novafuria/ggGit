# 13b1 - Hipótesis: Restricción de caracteres reservados en el Zettelkasten

## Enunciado de la Hipótesis

**Dado** que los sistemas de archivos de Windows (NTFS, FAT) prohíben estrictamente el uso de ciertos caracteres especiales en los nombres de archivo (como `:`, `*`, `?`, `"`, `<`, `>`, `|`),  
**Si** aplicamos una restricción arquitectónica absoluta que obligue a que todos los nombres de archivos documentales (zettels, planes, readme) usen únicamente caracteres alfanuméricos, espacios, tildes, guiones medios y guiones bajos,  
**Entonces** restauraremos la compatibilidad universal de clonación, checkout y navegación de git en todos los sistemas operativos (Linux, macOS, Windows nativo) sin perjudicar el valor conceptual de la documentación.

## Justificación y Modelo Mental

Un repositorio de Git distribuido debe ser agnóstico del sistema operativo del desarrollador. El "incidente de los dos puntos" ocurrió porque en sistemas Unix-like los archivos con `:` son perfectamente válidos, lo que cegó al equipo ante las restricciones del Kernel de Windows. Esta hipótesis asume que la compatibilidad universal es una regla de diseño de interfaz técnica y que su cumplimiento elimina fallos de bajo nivel en las herramientas de control de versiones.

## Resultados Empíricos (Confirmados)

Esta hipótesis **ha sido probada con éxito rotundo** en la Épica 2.1. Al remover y renombrar todos los zettels que contenían `:` (como `2.2.1-bug-ggb-create-branch-not-implemented.md`), se confirmó que el repositorio se puede clonar y operar en Windows sin errores de `invalid path` en Git.

## Referencias

- [[11a3 - compatibilidad-multiplataforma-zettelkasten]]
- [[13b - Compatibilidad multiplataforma y entornos de terminal]]
