# 3b12a1 - Propuesta de Solución: Implementar --no-ff y mensaje automático

## Solución Propuesta
Modificar el método `merge_branch()` en `GitInterface` para usar `git merge --no-ff` y aceptar automáticamente el mensaje por defecto del commit de merge.

## Cambios Requeridos

### 1. Modificar `GitInterface.merge_branch()`
**Archivo**: `src/core/git.py`
**Línea**: ~1048

**Cambio actual**:
```python
cmd = ['git', 'merge', branch_name]
```

**Cambio propuesto**:
```python
cmd = ['git', 'merge', '--no-ff', branch_name]
```

### 2. Aceptar mensaje por defecto automáticamente
**Opción 1**: Usar `--no-edit` para aceptar el mensaje por defecto
```python
cmd = ['git', 'merge', '--no-ff', '--no-edit', branch_name]
```

**Opción 2**: Usar `-m` con mensaje personalizado
```python
cmd = ['git', 'merge', '--no-ff', '-m', f'Merge branch \'{branch_name}\' into {current_branch}']
```

## Implementación Recomendada

### Opción 1: --no-edit (Más simple)
```python
def merge_branch(self, branch_name: str) -> bool:
    try:
        if not self.is_git_repository():
            raise NotGitRepositoryError("Not a git repository")
        
        cmd = ['git', 'merge', '--no-ff', '--no-edit', branch_name]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise GitCommandError(f"Git merge failed: {result.stderr}")
        
        return True
    # ... resto del manejo de errores
```

### Opción 2: Mensaje personalizado (Más control)
```python
def merge_branch(self, branch_name: str) -> bool:
    try:
        if not self.is_git_repository():
            raise NotGitRepositoryError("Not a git repository")
        
        # Obtener rama actual
        current_branch = self.get_current_branch()
        
        cmd = ['git', 'merge', '--no-ff', '-m', f'Merge branch \'{branch_name}\' into {current_branch}']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise GitCommandError(f"Git merge failed: {result.stderr}")
        
        return True
    # ... resto del manejo de errores
```

## Ventajas de la Solución

### ✅ **Mantiene el rastro de la rama**
- Siempre genera un commit de merge explícito
- El historial muestra claramente qué rama se mergeó
- Preserva el contexto de los commits de la rama mergeada

### ✅ **Comportamiento consistente**
- Siempre hace merge real, nunca fast-forward
- Cumple con el propósito del comando "ggmerge"
- Comportamiento predecible y confiable

### ✅ **Experiencia de usuario mejorada**
- No requiere interacción para el mensaje del commit
- Proceso automático y eficiente
- Feedback claro sobre el resultado

## Consideraciones

### **Casos edge**
- **Merge conflictos**: Se manejan igual que antes
- **Ramas ya mergeadas**: Git maneja automáticamente
- **Ramas inexistentes**: Se mantiene el manejo de errores actual

### **Compatibilidad**
- No afecta las opciones `--abort` y `--continue`
- Mantiene la funcionalidad interactiva
- No requiere cambios en el comando principal

## Recomendación
**Usar Opción 1** (`--no-edit`) por simplicidad y porque el mensaje por defecto de Git es generalmente apropiado y descriptivo.
