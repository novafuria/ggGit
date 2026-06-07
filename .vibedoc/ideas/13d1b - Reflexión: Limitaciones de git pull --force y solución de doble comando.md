# 13d1b - Reflexión: Limitaciones de git pull --force y solución de doble comando

## Contexto del Descubrimiento

Durante las pruebas en condiciones reales tras fusionar la Story 2.3.1 (donde implementamos `git pull --all --tags --force --prune` por defecto para `ggpl`), se constató el siguiente comportamiento anómalo:
*   `ggpl` descargaba con éxito los tags nuevos (como `v1.5.0` y `v1.5`).
*   Sin embargo, **no sobreescribía los tags existentes** que se habían movido en el remoto (como el tag mayor `v1`), dejándolos localmente apuntados a commits obsoletos y sin reportar ningún error de ejecución.

## Análisis de la Causa Raíz

En la arquitectura interna de Git, `git pull` es un comando de alto nivel que realiza dos operaciones secuenciales: `git fetch` y `git merge` (o `rebase`). 

Cuando ejecutamos `git pull --force`, el flag `--force` se asocia semánticamente a la fase de **merge** (forzando la integración de commits o pisando ramas locales), pero **no se propaga** con el comportamiento de "forzado de sobreescritura" a las referencias de etiquetas descargadas durante la fase interna de fetch. Git asume que las etiquetas son punteros estáticos del historial de commits, por lo que bloquea silenciosamente cualquier actualización de etiquetas locales preexistentes para evitar la pérdida de referencias locales históricas.

Para que Git fuerce la sobreescritura de un tag móvil, se requiere explícitamente invocar el comando de bajo nivel `git fetch` pasándole de forma combinada los flags `--tags --force`.

## La Solución de Doble Comando

La única manera de garantizar la sincronía absoluta de los tags de forma segura y portable es implementar una **estrategia de doble comando** en el método `pull` de `GitInterface`:

1.  **Paso 1: Pull de Commits y Ramas**: Ejecutar el `git pull` estándar de forma normal para integrar el código de la rama de trabajo.
2.  **Paso 2: Fetch Forzado de Tags**: Si los parámetros `tags` o `force` están activos, ejecutar inmediatamente después un `git fetch --tags --force --prune` (o con `--all` si se especificó pull de todos los remotes). 

Este paso complementario barre y machaca cualquier discrepancia local de etiquetas, forzando a que coincidan 1:1 con el estado exacto del servidor remoto y podando las eliminadas.

## Referencias

- [[13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull]]
- [[13d1a - Experimento: Implementación de descarga de tags automática en ggpl]]
