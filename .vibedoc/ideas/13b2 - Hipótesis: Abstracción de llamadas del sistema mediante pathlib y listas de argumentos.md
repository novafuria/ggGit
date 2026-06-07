# 13b2 - Hipótesis: Abstracción de llamadas del sistema mediante pathlib y listas de argumentos

## Enunciado de la Hipótesis

**Dado** que Windows y Unix difieren radicalmente en el manejo de separadores de ruta (`\` vs `/`) y en el intérprete de comandos por defecto (`cmd`/`powershell` vs `bash`),  
**Si** refactorizamos `GitInterface` y la suite de comandos para utilizar la biblioteca estándar `pathlib` para la resolución de rutas, y realizamos la ejecución de subprocesos usando listas de argumentos (p. ej., `["git", "status"]`) con `shell=False` en lugar de strings con `shell=True`,  
**Entonces** el núcleo técnico de `ggGit` será 100% portable y capaz de ejecutarse nativamente en consolas de Windows (CMD y PowerShell) y Unix (Bash/Zsh) de forma idéntica, eliminando la necesidad de emulación o WSL.

## Justificación y Modelo Mental

El uso de `shell=True` en Python delega la interpretación del comando al shell del sistema operativo. Esto introduce fallos en Windows porque comandos Unix básicos o alias no existen de la misma forma, además de crear vulnerabilidades de inyección de comandos. Al usar listas y pasar los argumentos directamente al ejecutable, evitamos el intermediario (el shell) y garantizamos que Python invoque al ejecutable de Git de forma idéntica sin importar la plataforma.

## Validación Experimental

Para probar esta hipótesis, se plantea un experimento enfocado en auditar y simular las llamadas del sistema en entornos heterogéneos:

- [[13b2.1 - Experimento: Auditoría y simulación de llamadas del sistema Unix en entorno Windows]]

## Referencias

- [[2 - arquitectura unificada en python]]
- [[8 - sistema de integracion con git]]
- [[13b - Compatibilidad multiplataforma y entornos de terminal]]
