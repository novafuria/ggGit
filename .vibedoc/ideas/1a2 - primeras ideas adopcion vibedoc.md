# primeras ideas por adopcion de vibedoc

## Idea
Ya tenemos la documentación inicial de ggGit. Ahora necesitamos generar las primeras ideas para ggGit aplicando ***VibeDoc***. Las ideas deben ser coherentes con el concepto inicial y la documentación inicial.

Buscamos ideas de reconstrucción del código inicial de ggGit para alinear las caracteristicas con la documentación escrita hasta el momento. Esto se da de esta forma porque ya existe una implementación funcional de ggGit, y tras la incorporación de ***VibeDoc*** la solución fue adoptando objetivos diferentes y una arquitectura distinta. Sin embargo, este nuevo enfoque quedo restringido a la documentación pero no al código.

Asi que las siguientes ideas tendrán como objetivo reconstruir el código inicial de ggGit para adecuarlo a la documentación escrita hasta el momento.

> Al mismo tiempo vamos a estar evaluando el uso de ***VibeDoc*** para ggGit, haciendo especial foco en el flujo de trabajo de desarrollo basados en ideas, en la generación de codigo y en la documentación. Reflexionar sobre su uso nos permitira evaluar si seguimos trabajando de esta forma o no.

Cursor sugiere seguir este plan:

1. Estructura de Directorios Python
2. Abstracciones Base
  - `core/cli.py`
  - `core/config.py`
  - `core/git.py`
3. Utilidades Base
  - `utils/colors.py`
  - `utils/logging.py`
4. Comandos Base
  - `commands/base.py`
  - `commands/commit.py`
  - `commands/config.py`
5. Comandos Específicos 
  - `commands/ggfeat.py`
  - `commands/ggfix.py`
  - `commands/ggbreak.py`
  - `commands/ggdocs.py`
  - `commands/ggstyle.py`
  - `commands/ggrefactor.py`
  - `commands/ggtest.py`
  - `commands/ggchore.py`
  - `commands/ggperf.py`
  - `commands/ggci.py`
  - `commands/ggbuild.py`
  - `commands/ggconfig.py`
6. IA y Avanzados
  - `commands/ggai.py`

Ya veremos si el ajuste del codigo permite avanzar de esta forma
