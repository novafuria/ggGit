# 13d - El comando ggpl no obtiene las etiquetas o tags del remoto

## Contexto y Problema

El comando `ggpl` es el encargado de descargar y fusionar cambios desde el repositorio remoto (equivalente a `git pull`). Sin embargo, en flujos de trabajo profesionales donde el etiquetado (tags) es crítico para el versionado, lanzamientos (releases) y disparadores de pipelines de CI/CD, el comando `git pull` básico no siempre garantiza la descarga de las etiquetas correspondientes desde el remoto. 

Esto provoca que el espacio de trabajo local del desarrollador quede desincronizado respecto a los tags existentes en GitHub/GitLab, forzándolo a ejecutar comandos manuales adicionales como `git fetch --tags`, lo cual contradice la propuesta de valor de `ggGit` de simplificar las operaciones diarias de Git.

## Evolución e Hipótesis

Para resolver esta desincronización de forma limpia y transparente, proponemos la siguiente hipótesis:

- [[13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull]]

## Referencias

- [[3 - sistema de comandos independientes]]
- [[8 - sistema de integracion con git]]
