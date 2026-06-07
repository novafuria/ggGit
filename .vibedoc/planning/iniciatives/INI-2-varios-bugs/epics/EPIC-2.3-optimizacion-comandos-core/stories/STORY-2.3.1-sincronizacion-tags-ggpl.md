# [HISTORIA] - Sincronización de Etiquetas Robustas en ggpl

## 🎯 Objetivo

Modificar el flujo del comando `ggpl` para que sincronice de forma automática, forzada y con poda todas las etiquetas del servidor remoto (ejecutando la lógica equivalente a `git pull --all --tags --force --prune`), garantizando que las etiquetas mayores móviles de la CI y los tags eliminados se reflejen instantáneamente en el entorno local del desarrollador sin pasos manuales.

## 🌎 Contexto

Actualmente, el comando `ggpl` no actualiza etiquetas de manera robusta. Dado que la CI del equipo genera tags semánticos móviles (como `v2` apuntando al commit más reciente de producción), el Git local de los desarrolladores suele bloquear su actualización local, provocando desalineamientos graves de versión. La historia se basa en el problema [[13d - El comando ggpl no obtiene las etiquetas o tags del remoto]].

## 💡 Propuesta de Resolución

Se propone modificar el método `pull` en `src/core/git.py` para invocar subprocesos de git que incluyan los parámetros `--all --tags --force --prune`. Se actualizará `src/commands/ggpl.py` para habilitar este comportamiento por defecto. Adicionalmente, se escribirá una prueba de integración unitaria que emule el movimiento y eliminación de etiquetas en repositorios locales y remotos de prueba.

## 📦 Artefactos

- 📦 **GitInterface Modificado**: `src/core/git.py`.
- 📦 **Comando ggpl Modificado**: `src/commands/ggpl.py`.
- 📦 **Pruebas de Sincronización**: Caso de prueba de tags en la suite de pruebas (`tests/`).

## 🔍 Criterios de Aceptación

### Sincronización Forzada (Movable Tags):
- Dado que existe una etiqueta local `v2` apuntando a un commit desactualizado respecto al remoto
- Cuando el desarrollador ejecute el comando `ggpl`
- Entonces la etiqueta local `v2` debe ser sobreescrita y apuntar de forma correcta al mismo commit del servidor remoto.

### Poda de Tags Eliminados (Pruning):
- Dado que una etiqueta fue borrada en el remoto
- Cuando el desarrollador ejecute el comando `ggpl`
- Entonces la etiqueta local correspondiente debe desaparecer del repositorio local de forma automática.

### Éxito General:
- Dado que se ejecuta el pull completo
- Cuando finalice la operación
- Entonces el comando debe retornar código de salida `0` y la suite de pytest debe pasar al 100%.

🔗 Dependencias y Recursos

### Dependencias
- Ninguna.

### Recursos
- Repositorio de prueba simulado dentro de la suite de tests.
