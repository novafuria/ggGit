# [HISTORIA] - Solución de Doble Comando para Sobreescritura de Tags en ggpl

## 🎯 Objetivo

Corregir el bug funcional en el comando `ggpl` donde las etiquetas locales (tags) no se sobreescriben con las nuevas posiciones del remoto a pesar de usar `--force` en el pull. Se implementará una estrategia de doble comando ejecutando un `git fetch --tags --force --prune` complementario, garantizando que el espacio local refleje fielmente y de forma forzada los tags móviles de la CI.

## 🌎 Contexto

Durante la validación de la Story 2.3.1, se observó que `git pull --all --tags --force --prune` descarga los tags nuevos pero **no reemplaza** ni sobreescribe los tags locales existentes (como el tag mayor `v1`) cuando la CI los mueve en el remoto. Esto se debe a que en Git, el flag `--force` de `git pull` se interpreta en el contexto de la fusión (merge), ignorando el forzado de referencias en el fetch de tags. Este hallazgo se documenta en el Zettel [[13d1b - Reflexión: Limitaciones de git pull --force y solución de doble comando]].

## 💡 Propuesta de Resolución

Se propone modificar el método `pull` de `GitInterface` para que, si los parámetros `tags` o `force` están habilitados, ejecute un segundo subproceso complementario: `git fetch <remote> --tags --force --prune` (o con `--all` si aplica), forzando la sobreescritura de los tags locales y podando los eliminados en una sola transacción fluida.

## 📦 Artefactos

- 📦 **GitInterface Modificado**: `src/core/git.py`.
- 📦 **Zettel de Reflexión**: `.vibedoc/ideas/13d1b - Reflexión: Limitaciones de git pull --force y solución de doble comando.md`.

## 🔍 Criterios de Aceptación

### Sobreescritura Real de Tags (Movable Tags):
- Dado que un tag local `v1` apunta a un commit antiguo y en el remoto `v1` ha sido movido a un nuevo commit
- Cuando se ejecute el comando `ggpl`
- Entonces el tag local `v1` debe ser forzado a actualizarse, apuntando exactamente al mismo commit que en el remoto.

### Poda de Tags:
- Dado que un tag fue eliminado en el remoto
- Cuando se ejecute el comando `ggpl`
- Entonces el tag local correspondiente debe ser eliminado de forma automática.

### Suite de Tests en Verde:
- Dado que agregamos un paso de fetch complementario
- Cuando se corran las pruebas unitarias y de integración
- Entonces todas deben pasar en verde (580+ tests) y los mocks de `subprocess.run` deben validar el doble comando.

🔗 Referencias

- [[13d1b - Reflexión: Limitaciones de git pull --force y solución de doble comando]]
