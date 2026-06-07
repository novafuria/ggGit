# [EXPERIMENTO] - Implementación de descarga de tags automática en ggpl

## 🎯 Objetivo

Modificar el método `pull` de `GitInterface` (y el flujo en `src/commands/ggpl.py`) para soportar la ejecución de pull con sincronización forzada y poda de etiquetas (`--all --tags --force --prune`), validando empíricamente que las etiquetas locales se actualicen y poden correctamente cuando el remoto sufra cambios o movimientos de tags mayores.

## 🌎 Contexto

La CI del proyecto genera tags mayores móviles (como `v2` apuntando al último release) que se desalinean constantemente en los entornos locales. Este experimento valida de forma práctica la hipótesis [[13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull]] para asegurar que `ggpl` resuelva este desalineamiento sin intervención del usuario.

## 💡 Diseño Experimental

1. **Refactorización Técnica**:
   - Modificar la llamada de `git.pull` en `src/core/git.py` para construir y ejecutar internamente la llamada equivalente a `git pull --all --tags --force --prune`.
   - Alternativamente, si la biblioteca de ejecución de subprocess requiere llamadas encadenadas, implementar un paso posterior inmediato de `git fetch --tags --force --prune` para asegurar la consistencia.
2. **Prueba de Simulación de Tags Móviles**:
   - Crear un repositorio local y un remoto de prueba simulado.
   - En el remoto, crear un tag `v2` apuntando al Commit A, y clonarlo localmente.
   - En el remoto, mover el tag `v2` para que apunte al Commit B (simulando una acción de la CI).
   - En el remoto, eliminar un tag obsoleto `v1.9-alpha`.
   - Ejecutar el comando `ggpl` modificado en el repositorio local.
3. **Métrica de éxito**: 
   - El tag local `v2` se actualiza exitosamente para apuntar al Commit B (forzado).
   - El tag local `v1.9-alpha` desaparece del repositorio local (poda).
   - El comando finaliza con código de salida `0`.

## 📦 Artefactos Esperados

- 📦 **GitInterface Modificado**: Cambios en `src/core/git.py` soportando los flags `--all --tags --force --prune`.
- 📦 **Pruebas de Sincronización Móvil**: Caso de prueba en `tests/test_git_utility_commands.py` (o un archivo dedicado `tests/test_git_tags_sync.py`) que simule movimiento de tags y poda.

## 🔍 Criterios de Éxito

### Actualización Forzada de Tags (Movable Tags):
- Dado que un tag mayor local como `v2` apunta a un commit desactualizado respecto al remoto
- Cuando se ejecute el comando `ggpl`
- Entonces el tag local `v2` debe actualizarse de forma forzada para apuntar al mismo commit que en el remoto.

### Poda de Tags Eliminados (Pruning):
- Dado que un tag ha sido borrado del servidor remoto
- Cuando se ejecute el comando `ggpl`
- Entonces el tag correspondiente debe ser eliminado del espacio de trabajo local de manera automática.

🔗 Referencias

- [[13d1 - Hipótesis: Sincronización automática de etiquetas en comando pull]]
