# 13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull

## Enunciado de la Hipótesis

**Dado** que el repositorio remoto utiliza un esquema de etiquetas móviles (Major, Minor, Patch) gestionado por automatización de CI,  
**Si** configuramos el comando `ggpl` (y el método `pull` de `GitInterface`) para que la operación de pull se ejecute por defecto con los flags de sincronización total y forzada: `git pull --all --tags --force --prune`,  
**Entonces** el espacio de trabajo local del desarrollador actualizará automáticamente las etiquetas móviles locales para coincidir con el remoto, eliminará las etiquetas que hayan sido borradas en el remoto y descargará todos los nuevos tags sin requerir intervención manual, garantizando la consistencia absoluta del versionado.

## Justificación y Modelo Mental

Un desarrollador espera que `ggpl` sea un sinónimo de "dejar mi espacio de trabajo exactamente igual que el remoto". Separar conceptualmente el pull de ramas del fetch forzado de tags es un residuo de la optimización histórica de ancho de banda de Git, pero en proyectos modernos con tags móviles es una fuente de bugs silenciosos (p. ej., construir un contenedor local apuntando a una versión `v2` desactualizada). Esta hipótesis asume que la sincronización total con forzado y poda (`--force --prune`) es el comportamiento intuitivo y correcto que `ggGit` debe proveer por defecto.

## Validación Experimental

Para probar esta hipótesis en un escenario real que emule las etiquetas móviles de la CI, se plantea el siguiente diseño de experimento:

- [[13d1.1 - Experimento: Implementación de descarga de tags automática en ggpl]]

## Referencias

- [[13d - El comando ggpl no obtiene las etiquetas o tags del remoto]]
- [[8 - sistema de integracion con git]]
