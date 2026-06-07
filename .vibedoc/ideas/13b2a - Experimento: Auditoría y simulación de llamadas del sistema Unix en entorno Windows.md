# [EXPERIMENTO] - Auditoría y simulación de llamadas del sistema Unix en entorno Windows

## 🎯 Objetivo

Auditar la totalidad del código fuente de `ggGit` (en particular la clase `GitInterface` en `src/core/git.py` y `BaseCommand` en `src/core/base_commands/base.py`) para identificar asunciones exclusivas de entornos Unix (como `/` crudos, llamadas directas a comandos bash, comandos como `chmod` o variables dependientes), proponiendo un diseño portable basado en la librería `pathlib` y listas de argumentos.

## 🌎 Contexto

Actualmente, las pruebas automatizadas de Windows están deshabilitadas en CI debido a la fricción de dependencias y entornos. Para habilitar un soporte multiplataforma real y duradero, debemos validar experimentalmente la hipótesis [[13b2 - Hipótesis: Abstracción de llamadas del sistema mediante pathlib y listas de argumentos]] sin necesidad de contar con infraestructura física de Windows en una fase inicial de análisis.

## 💡 Diseño Experimental

1. **Análisis Estático (Grepping)**:
   - Buscar llamadas a subprocesos que utilicen `shell=True` o pasen comandos en formato string.
   - Buscar concatenaciones manuales de rutas usando strings en lugar de `pathlib.Path` u `os.path.join`.
2. **Creación de Mocking de Plataforma**:
   - Crear una suite de pruebas unitarias (`tests/test_platform_portability.py`) que mockee `sys.platform` a `win32` y `os.name` a `nt`.
   - Validar que los métodos clave de `GitInterface` sigan construyendo las llamadas de forma correcta y que los comandos no intenten ejecutar instrucciones Unix-exclusive (como permisos de archivo).
3. **Métrica de éxito**: Cero asunciones específicas de Unix detectadas en la capa de persistencia y llamadas. Los tests simulados en Windows deben arrojar código de salida `0`.

## 📦 Artefactos Esperados

- 📦 **Reporte de Auditoría**: Archivo `.md` detallando las líneas y archivos que requieren refactorización multiplataforma.
- 📦 **Suite de Simulación**: `tests/test_platform_portability.py` ejecutándose en la suite actual de pytest.

## 🔍 Criterios de Éxito

### Cobertura de la Auditoría:
- Dado que existen llamadas de sistema en `src/core/git.py`
- Cuando se ejecute la suite de simulación multiplataforma mockeando un entorno Windows
- Entonces el sistema no debe arrojar errores de rutas no encontradas ni invocar comandos de shell de Linux.

### Aislamiento de Comandos de Inicialización:
- Dado que los instaladores (`install.sh` e `install.ps1`) difieren por plataforma
- Cuando el software esté en ejecución regular
- Entonces ninguna clase del núcleo (`src/core/`) debe invocar scripts de bash nativos (`.sh`).

🔗 Referencias

- [[13b2 - Hipótesis: Abstracción de llamadas del sistema mediante pathlib y listas de argumentos]]
