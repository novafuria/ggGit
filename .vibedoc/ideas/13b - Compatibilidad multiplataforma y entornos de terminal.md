# 13b - Compatibilidad multiplataforma y entornos de terminal

## Contexto y Problema

Durante el desarrollo de la Épica 2.1 (documentado en [[11a3 - compatibilidad-multiplataforma-zettelkasten]]), se descubrió que los nombres de archivo que incluían el caracter `:` bloqueaban la clonación e inicialización del repositorio en Windows, produciendo fallos catastróficos en comandos nativos de Git como `git checkout`. 

Esto reveló que los nombres de archivo en el zettelkasten son parte de la API e interfaces del sistema. Aunque se decidió desactivar Windows temporalmente del pipeline de CI/CD para priorizar los entornos Unix-native (Linux/macOS), la deuda técnica sigue abierta: asegurar que los usuarios de Windows puedan utilizar `ggGit` (vía WSL, Git Bash o nativamente) de forma estable y predecible.

## Evolución e Hipótesis

Para solventar esta deuda multiplataforma de forma estructurada, dividimos la solución en dos hipótesis fundamentales de diseño de archivos y diseño de abstracciones de sistema:

- [[13b1 - Hipótesis: Restricción de caracteres reservados en el Zettelkasten]]
- [[13b2 - Hipótesis: Abstracción de llamadas del sistema mediante pathlib y listas de argumentos]]

## Referencias

- [[6 - sistema de instalacion y distribucion]]
- [[8 - sistema de integracion con git]]
- [[11a3 - compatibilidad-multiplataforma-zettelkasten]]
