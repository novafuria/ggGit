# 13d - El comando ggpl no obtiene las etiquetas o tags del remoto

## Contexto y Problema

El comando `ggpl` es el encargado de descargar y fusionar cambios desde el repositorio remoto (equivalente a `git pull`). Sin embargo, en flujos de trabajo profesionales modernos que usan integración continua (CI/CD) para automatizar la gestión de versiones, se genera una arquitectura de etiquetado semántico complejo que un simple `git pull` no puede gestionar correctamente:

1.  **Etiquetas Móviles (Movable Major Tags)**: La CI genera tres niveles de tags: Major, Minor y Patch (p. ej., `v2`, `v2.1`, `v2.1.0`). Cuando se lanza una nueva versión menor o parche, el tag mayor (p. ej., `v2`) es *reapuntado* o movido en el remoto para que siempre coincida con la última versión liberada.
2.  **Conflicto en Workspace Local**: Git, por defecto, se niega a actualizar un tag local si este ya existe en el espacio de trabajo del desarrollador (drift de etiquetas). Esto provoca que el desarrollador local se quede con el tag `v2` apuntando a un commit antiguo, mientras que en el remoto `v2` ya apunta al último hotfix.
3.  **Falta de Sincronización y Tags Huérfanos**: Las etiquetas eliminadas en el remoto no se eliminan localmente, dejando tags huérfanos que confunden el historial y bloquean tareas de empaquetado o builds locales.

Para solucionar esto, el desarrollador se ve obligado a ejecutar comandos verbosos y avanzados como `git pull --all --tags --force --prune` de manera recurrente, lo cual incrementa la carga cognitiva y contradice la propuesta de valor de `ggGit`.

## Evolución e Hipótesis

Para resolver este escenario avanzado de forma elegante y automatizada, proponemos la siguiente hipótesis de sincronización robusta:

- [[13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull]]

## Referencias

- [[3 - sistema de comandos independientes]]
- [[8 - sistema de integracion con git]]
