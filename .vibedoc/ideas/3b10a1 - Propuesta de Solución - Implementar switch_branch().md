# 3b10a1 - Propuesta de Solución: Implementar switch_branch()

## Propuesta de Solución

**Fecha**: 2024-12-19  
**Componente**: Bug ggmain (3b10a)  
**Tipo**: Propuesta técnica  
**Estado**: 💡 **PROPUESTA EN DEBATE**

## Solución Propuesta

### **Implementación del Método `switch_branch()`**
```python
def switch_branch(self, branch_name: str) -> bool:
    """
    Switch to a different branch.
    
    Switches to the specified branch. Equivalent to running
    'git checkout <branch_name>' or 'git switch <branch_name>'.
    
    Args:
        branch_name (str): Name of the branch to switch to
        
    Returns:
        bool: True if switch was successful, False otherwise
        
    Raises:
        NotGitRepositoryError: If not in a Git repository
        GitCommandError: If git checkout/switch command fails
    """
    if not self.is_git_repository():
        raise NotGitRepositoryError("Not a git repository")
    
    try:
        # Use git switch (preferred) or fallback to git checkout
        result = subprocess.run(
            ['git', 'switch', branch_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            # Fallback to git checkout if git switch fails
            result = subprocess.run(
                ['git', 'checkout', branch_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                raise GitCommandError(f"Failed to switch to branch '{branch_name}': {result.stderr}")
        
        return True
        
    except subprocess.TimeoutExpired:
        raise GitCommandError(f"Timeout switching to branch '{branch_name}'")
    except subprocess.CalledProcessError as e:
        raise GitCommandError(f"Git switch failed: {e}")
    except Exception as e:
        raise GitInterfaceError(f"Unexpected error in switch_branch: {e}")
```

## Análisis de la Solución

### **Fortalezas de la Propuesta**
- ✅ **Uso de `git switch`**: Comando moderno y preferido
- ✅ **Fallback a `git checkout`**: Compatibilidad con versiones antiguas
- ✅ **Manejo de errores robusto**: Diferentes tipos de error
- ✅ **Timeout apropiado**: Evita bloqueos indefinidos
- ✅ **Validación previa**: Verifica que es repositorio Git

### **Consideraciones Técnicas**
- **`git switch` vs `git checkout`**: `git switch` es más específico para cambio de ramas
- **Manejo de errores**: Diferentes códigos de error para diferentes situaciones
- **Timeout**: 30 segundos debería ser suficiente para la mayoría de casos
- **Compatibilidad**: Fallback asegura funcionamiento en versiones antiguas

## Alternativas Consideradas

### **Alternativa 1: Solo `git checkout`**
```python
# Pros: Más compatible, más simple
# Contras: Menos específico, puede confundir con checkout de archivos
```

### **Alternativa 2: Solo `git switch`**
```python
# Pros: Más moderno, más específico
# Contras: Requiere Git 2.23+, puede fallar en versiones antiguas
```

### **Alternativa 3: Detección automática**
```python
# Pros: Mejor experiencia de usuario
# Contras: Más complejo, requiere verificación de versión Git
```

## Validaciones Adicionales Propuestas

### **1. Verificar que la rama existe**
```python
def branch_exists(self, branch_name: str) -> bool:
    """Check if branch exists locally or remotely"""
    # Implementar verificación de rama
```

### **2. Manejar cambios no committeados**
```python
def has_uncommitted_changes(self) -> bool:
    """Check if there are uncommitted changes"""
    # Implementar verificación de cambios
```

### **3. Validar nombre de rama**
```python
def is_valid_branch_name(self, branch_name: str) -> bool:
    """Validate branch name format"""
    # Implementar validación de nombre
```

## Testing Requerido

### **Tests Unitarios**
- Test de switch exitoso a rama existente
- Test de error cuando rama no existe
- Test de error cuando no es repositorio Git
- Test de timeout en operaciones lentas
- Test de fallback a `git checkout`

### **Tests de Integración**
- Test completo del comando `ggmain`
- Test con diferentes tipos de repositorios
- Test con ramas locales y remotas
- Test con cambios no committeados

## Puntos de Debate

### **1. ¿Usar `git switch` o `git checkout`?**
- **`git switch`**: Más moderno, más específico
- **`git checkout`**: Más compatible, más conocido
- **Propuesta**: Usar `git switch` con fallback a `git checkout`

### **2. ¿Validar existencia de rama antes del switch?**
- **Pros**: Mejor experiencia de usuario, mensajes más claros
- **Contras**: Operación adicional, más complejo
- **Propuesta**: Sí, validar existencia para mejor UX

### **3. ¿Manejar cambios no committeados?**
- **Pros**: Evita errores de Git, mejor experiencia
- **Contras**: Más complejo, puede no ser responsabilidad del comando
- **Propuesta**: Dejar que Git maneje, pero mejorar mensajes de error

### **4. ¿Timeout de 30 segundos es apropiado?**
- **Pros**: Evita bloqueos indefinidos
- **Contras**: Puede ser muy corto para repositorios grandes
- **Propuesta**: 30 segundos es razonable, ajustar si es necesario

## Implementación Propuesta

### **Fase 1: Implementación Básica**
1. Implementar `switch_branch()` con `git switch` y fallback
2. Manejo básico de errores
3. Tests unitarios básicos

### **Fase 2: Validaciones Adicionales**
1. Validar existencia de rama
2. Mejorar mensajes de error
3. Tests de integración

### **Fase 3: Optimizaciones**
1. Manejo de cambios no committeados
2. Validación de nombres de rama
3. Tests de rendimiento

## Referencias

- **Zettel padre**: 3b10a - Bug específico de ggmain
- **Archivo fuente**: `src/core/git.py:483-509`
- **Comando afectado**: `src/commands/ggmain.py`
- **Documentación Git**: `git switch` vs `git checkout`

## Conclusión

La propuesta de implementar `switch_branch()` con `git switch` y fallback a `git checkout` es sólida y debería resolver el bug de `ggmain`. La implementación por fases permite validar cada paso y ajustar según sea necesario.

**Estado**: 💡 **PROPUESTA EN DEBATE - PENDIENTE DE DECISIÓN**
