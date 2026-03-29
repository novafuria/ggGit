# 3b12a - Bug: ggmerge usa fast-forward perdiendo rastro de rama mergeada

## Problema Identificado
El comando `ggmerge` está usando `git merge` sin la opción `--no-ff`, lo que causa que se haga fast-forward cuando es posible, perdiendo el rastro de la rama mergeada en el historial.

## Comportamiento Actual (Incorrecto)
```bash
# Cuando se puede hacer fast-forward
git merge feature-branch
# Resultado: Fast-forward, no hay commit de merge explícito
# El historial se ve como si los commits fueran directos en la rama principal
```

## Comportamiento Esperado (Correcto)
```bash
# Siempre generar commit de merge explícito
git merge --no-ff feature-branch
# Resultado: Commit de merge explícito que mantiene el rastro de la rama
# El historial muestra claramente que se mergeó una rama
```

## Impacto del Bug
- **Pérdida de contexto**: No se puede ver claramente qué commits pertenecían a la rama mergeada
- **Historial confuso**: Los commits aparecen como si fueran directos en la rama principal
- **Falta de trazabilidad**: No se puede identificar fácilmente qué cambios vinieron de qué rama
- **Inconsistencia con el propósito**: El comando se llama "ggmerge" pero no hace merge real

## Evidencia del Problema
En `src/core/git.py` línea 1048:
```python
cmd = ['git', 'merge', branch_name]  # ❌ Falta --no-ff
```

## Casos Afectados
1. **Merge de feature branches**: Cuando se puede hacer fast-forward
2. **Merge de hotfix branches**: Cuando se puede hacer fast-forward  
3. **Merge de release branches**: Cuando se puede hacer fast-forward
4. **Cualquier merge**: Donde Git determine que se puede hacer fast-forward

## Severidad
**CRÍTICA** - El comando no cumple su propósito principal de mantener el rastro de las ramas mergeadas.
