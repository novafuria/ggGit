# 3b11a1 - Propuesta de Solución: Implementar create_branch()

## Propuesta de Solución

**Fecha**: 2024-12-19  
**Componente**: Bug ggb (3b11a)  
**Tipo**: Propuesta técnica  
**Estado**: 💡 **PROPUESTA EN DEBATE**

## Solución Propuesta

### **Implementación del Método `create_branch()`**
```python
def create_branch(self, branch_name: str, start_point: Optional[str] = None) -> bool:
    """
    Create a new branch.
    
    Creates a new branch from the specified start point or current HEAD.
    Equivalent to running 'git branch <branch_name> [<start_point>]'.
    
    Args:
        branch_name (str): Name of the new branch
        start_point (Optional[str]): Starting point for the branch
        
    Returns:
        bool: True if branch was created successfully, False otherwise
        
    Raises:
        RuntimeError: If not in a Git repository
        ValueError: If branch name is invalid
        subprocess.CalledProcessError: If git branch command fails
    """
    if not self.is_git_repository():
        raise RuntimeError("Not a git repository")
    
    # Validate branch name
    if not self._is_valid_branch_name(branch_name):
        raise ValueError(f"Invalid branch name: {branch_name}")
    
    try:
        # Build git branch command
        cmd = ['git', 'branch', branch_name]
        if start_point:
            cmd.append(start_point)
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            raise subprocess.CalledProcessError(
                result.returncode,
                ' '.join(cmd),
                result.stderr
            )
        
        return True
        
    except subprocess.TimeoutExpired:
        raise subprocess.CalledProcessError(1, ' '.join(cmd), "Timeout")
    except subprocess.CalledProcessError as e:
        raise e
    except Exception as e:
        raise subprocess.CalledProcessError(1, ' '.join(cmd), str(e))

def _is_valid_branch_name(self, branch_name: str) -> bool:
    """Validate branch name format."""
    if not branch_name or not branch_name.strip():
        return False
    
    # Check length
    if len(branch_name) > 255:
        return False
    
    # Check for invalid characters
    invalid_chars = ['..', '~', '^', ':', '?', '*', '[', '\\']
    for char in invalid_chars:
        if char in branch_name:
            return False
    
    # Check for leading/trailing dots
    if branch_name.startswith('.') or branch_name.endswith('.'):
        return False
    
    # Check for consecutive dots
    if '..' in branch_name:
        return False
    
    return True
```

## Análisis de la Solución

### **Fortalezas de la Propuesta**
- ✅ **Uso de `git branch`**: Comando estándar para creación de ramas
- ✅ **Validación de nombre**: Verificación de formato antes de ejecutar
- ✅ **Manejo de errores robusto**: Diferentes tipos de error
- ✅ **Timeout apropiado**: Evita bloqueos indefinidos
- ✅ **Soporte para start_point**: Permite crear ramas desde puntos específicos
- ✅ **Validación previa**: Verifica que es repositorio Git

### **Consideraciones Técnicas**
- **`git branch` vs `git checkout -b`**: `git branch` solo crea, no cambia
- **Validación de nombres**: Sigue las reglas de Git para nombres de rama
- **Manejo de errores**: Diferentes códigos de error para diferentes situaciones
- **Timeout**: 30 segundos debería ser suficiente para la mayoría de casos

## Alternativas Consideradas

### **Alternativa 1: Usar `git checkout -b`**
```python
# Pros: Crea rama y cambia a ella en un comando
# Contras: Mezcla responsabilidades, menos flexible
```

### **Alternativa 2: Usar `git switch -c`**
```python
# Pros: Comando moderno, más específico
# Contras: Requiere Git 2.23+, menos compatible
```

### **Alternativa 3: Implementación híbrida**
```python
# Pros: Mejor experiencia de usuario
# Contras: Más complejo, requiere lógica adicional
```

## Validaciones Adicionales Propuestas

### **1. Verificar que la rama no existe**
```python
def branch_exists(self, branch_name: str) -> bool:
    """Check if branch exists locally"""
    # Implementar verificación de rama
```

### **2. Manejar conflictos de nombres**
```python
def _handle_branch_conflict(self, branch_name: str) -> str:
    """Handle branch name conflicts"""
    # Implementar resolución de conflictos
```

### **3. Validar start_point**
```python
def _validate_start_point(self, start_point: str) -> bool:
    """Validate start point exists"""
    # Implementar validación de punto de inicio
```

## Testing Requerido

### **Tests Unitarios**
- Test de creación exitosa de rama
- Test de error cuando rama ya existe
- Test de error cuando no es repositorio Git
- Test de error con nombre de rama inválido
- Test de timeout en operaciones lentas
- Test con start_point válido e inválido

### **Tests de Integración**
- Test completo del comando `ggb`
- Test con diferentes tipos de repositorios
- Test de creación y cambio de rama
- Test con ramas remotas

## Puntos de Debate

### **1. ¿Crear rama y cambiar automáticamente?**
- **Solo crear**: Mantiene responsabilidades separadas
- **Crear y cambiar**: Mejor experiencia de usuario
- **Propuesta**: Solo crear, dejar que `switch_branch()` maneje el cambio

### **2. ¿Validar existencia de rama antes de crear?**
- **Pros**: Mejor experiencia de usuario, mensajes más claros
- **Contras**: Operación adicional, más complejo
- **Propuesta**: Sí, validar existencia para mejor UX

### **3. ¿Manejar start_point opcional?**
- **Pros**: Más flexible, permite crear desde cualquier punto
- **Contras**: Más complejo, requiere validación adicional
- **Propuesta**: Sí, implementar start_point opcional

### **4. ¿Timeout de 30 segundos es apropiado?**
- **Pros**: Evita bloqueos indefinidos
- **Contras**: Puede ser muy corto para repositorios grandes
- **Propuesta**: 30 segundos es razonable, ajustar si es necesario

## Implementación Propuesta

### **Fase 1: Implementación Básica**
1. Implementar `create_branch()` con `git branch`
2. Validación básica de nombres de rama
3. Manejo básico de errores
4. Tests unitarios básicos

### **Fase 2: Validaciones Adicionales**
1. Validar existencia de rama antes de crear
2. Mejorar mensajes de error
3. Tests de integración

### **Fase 3: Optimizaciones**
1. Manejo de conflictos de nombres
2. Validación de start_point
3. Tests de rendimiento

## Integración con ggb

### **Flujo de Trabajo Propuesto**
1. `ggb` verifica si rama existe
2. Si existe: usa `switch_branch()` para cambiar
3. Si no existe: usa `create_branch()` para crear
4. Después de crear: usa `switch_branch()` para cambiar

### **Ventajas del Enfoque**
- **Separación de responsabilidades**: Cada método tiene una función específica
- **Reutilización**: `create_branch()` puede usarse en otros comandos
- **Flexibilidad**: Permite crear sin cambiar si es necesario

## Referencias

- **Zettel padre**: 3b11a - Bug específico de ggb
- **Archivo fuente**: `src/core/git.py:454-480`
- **Comando afectado**: `src/commands/ggb.py`
- **Documentación Git**: `git branch` command reference

## Conclusión

La propuesta de implementar `create_branch()` con `git branch` y validación de nombres es sólida y debería resolver el bug de `ggb`. La implementación por fases permite validar cada paso y ajustar según sea necesario.

**Estado**: 💡 **PROPUESTA EN DEBATE - PENDIENTE DE DECISIÓN**

