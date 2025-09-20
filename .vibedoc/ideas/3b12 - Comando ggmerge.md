# 3b12 - Comando ggmerge

## Descripción
Comando para realizar merge de ramas sin fast-forward, manteniendo el historial de commits y generando un commit de merge explícito.

## Funcionalidad Esperada
- **Merge sin fast-forward**: Usar `git merge --no-ff` para mantener el rastro de la rama mergeada
- **Commit de merge automático**: Aceptar el mensaje por defecto del commit de merge
- **Validación de parámetros**: Verificar que la rama existe y es mergeable
- **Feedback claro**: Mostrar mensajes de éxito/error apropiados
- **Funcionalidad interactiva**: Listar ramas disponibles para merge cuando no se especifica rama

## Implementación Actual
- ✅ Comando base implementado con opciones `--abort` y `--continue`
- ✅ Funcionalidad interactiva para listar ramas disponibles
- ✅ Manejo de errores básico
- ❌ **Problema crítico**: Usa `git merge` sin `--no-ff`, perdiendo el rastro de la rama mergeada
- ❌ No acepta automáticamente el mensaje por defecto del commit de merge

## Dependencias
- `GitInterface.merge_branch()` - Implementado pero sin `--no-ff`
- `GitInterface.get_mergeable_branches()` - Implementado
- `GitInterface.merge_abort()` - Implementado
- `GitInterface.merge_continue()` - Implementado

## Casos de Uso
1. **Merge explícito**: `ggmerge feature-branch` → merge con commit explícito
2. **Merge interactivo**: `ggmerge` → listar ramas y seleccionar
3. **Abortar merge**: `ggmerge --abort` → cancelar merge en progreso
4. **Continuar merge**: `ggmerge --continue` → continuar después de resolver conflictos

## Debilidades Identificadas
- **Fast-forward por defecto**: No mantiene el rastro de la rama mergeada
- **Falta de opción --no-ff**: No genera commit de merge explícito
- **Mensaje de merge manual**: Requiere interacción para el mensaje del commit de merge
