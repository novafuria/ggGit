# 13b - Compatibilidad multiplataforma y entornos de terminal

## Contexto y Problema

Durante el desarrollo de la Épica 2.1 (documentado en [[11a3 - compatibilidad-multiplataforma-zettelkasten]]), se descubrió que los nombres de archivo que incluían el caracter `:` bloqueaban la clonación e inicialización del repositorio en Windows, produciendo fallos catastróficos en comandos nativos de Git como `git checkout`. 

Esto reveló que los nombres de archivo en el zettelkasten son parte de la API e interfaces del sistema. Aunque se decidió desactivar Windows temporalmente del pipeline de CI/CD para priorizar los entornos Unix-native (Linux/macOS), la deuda técnica sigue abierta: asegurar que los usuarios de Windows puedan utilizar `ggGit` (vía WSL, Git Bash o nativamente) de forma estable y predecible.

## Hipótesis

### Hipótesis 1 (Compatibilidad de Archivos):
Si establecemos una regla de diseño estricta en el sistema de documentación que prohíba el uso de caracteres reservados de Windows (como `*`, `?`, `:`, `"`, `<`, `>`, `|`) en todos los archivos del repositorio, garantizaremos la clonación y navegación fluida en sistemas NTFS/FAT sin mermar la legibilidad de la documentación. (Esta hipótesis fue probada y confirmada con éxito al renombrar los archivos con `:`).

### Hipótesis 2 (Ejecución de Subprocesos Portables):
Si modificamos la clase `GitInterface` para que todas las llamadas de sistema usen `subprocess` pasándole los comandos como listas de argumentos (p. ej., `["git", "status"]`) en lugar de strings crudos que dependen del parsing del shell, y si empleamos el módulo `pathlib` para manipular rutas, entonces `ggGit` funcionará nativamente en Windows CMD y PowerShell sin necesidad de recurrir a WSL o capas de emulación Bash.

## Experimentos Propuestos

### Experimento 1 (Auditoría de Llamadas de Sistema):
1. Inspeccionar `src/core/git.py` y `src/core/base_commands/` en busca de construcciones que asuman entornos Unix (como `/` hardcodeados, uso de comandos shell nativos como `chmod` o variables de entorno dependientes de la terminal).
2. Desarrollar un test unitario que simule la ejecución en un entorno Windows (usando mocks del módulo `os` y `sys.platform`).
3. **Métrica de éxito**: Cero asunciones específicas de entorno Unix en la capa de abstracción del sistema.

## Referencias

- [[6 - sistema de instalacion y distribucion]]
- [[8 - sistema de integracion con git]]
- [[11a3 - compatibilidad-multiplataforma-zettelkasten]]
