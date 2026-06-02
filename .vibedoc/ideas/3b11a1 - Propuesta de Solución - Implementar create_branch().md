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
        NotGitRepositoryError: If not in a Git repository
        ValueError: If branch name is invalid
        GitCommandError: If git branch command fails
    """
    if not self.is_git_repository():
        raise NotGitRepositoryError("Not a git repository")
    
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
            text=True
        )
        
        if result.returncode != 0:
            raise GitCommandError(f"Git branch command failed: {result.stderr}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        raise GitCommandError(f"Git branch failed: {e}")
    except NotGitRepositoryError:
        # Re-raise NotGitRepositoryError without wrapping
        raise
    except GitCommandError:
        # Re-raise GitCommandError without wrapping
        raise
    except Exception as e:
        raise GitInterfaceError(f"Unexpected error in create_branch: {e}")

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
- ✅ **Manejo de errores consistente**: Sigue patrones establecidos en GitInterface
- ✅ **Excepciones específicas**: Usa `NotGitRepositoryError`, `GitCommandError`, `GitInterfaceError`
- ✅ **Soporte para start_point**: Permite crear ramas desde puntos específicos
- ✅ **Validación previa**: Verifica que es repositorio Git

### **Consideraciones Técnicas**
- **`git branch` vs `git checkout -b`**: `git branch` solo crea, no cambia (separación de responsabilidades)
- **Validación de nombres**: Sigue las reglas de Git para nombres de rama
- **Manejo de errores**: Sigue el patrón establecido en GitInterface (3a1)
- **Sin timeout**: No es necesario para operaciones simples de Git
- **start_point**: Parámetro opcional para crear ramas desde commits específicos (ej: `git branch nueva-rama main`)

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

### **3. ¿Manejar archivos no committeados en switch?**
- **Pros**: Mejor experiencia de usuario, evita errores de Git
- **Contras**: Más complejo, requiere lógica adicional
- **Propuesta**: Sí, preguntar al usuario si quiere llevar archivos o descartarlos

### **4. ¿Usar git stash para archivos no committeados?**
- **Pros**: Preserva cambios del usuario, experiencia fluida
- **Contras**: Requiere manejo de stash, más complejo
- **Propuesta**: Sí, usar git stash para llevar archivos a la nueva rama

### **5. ¿Manejar start_point opcional?**
- **Pros**: Más flexible, permite crear desde cualquier punto
- **Contras**: Más complejo, requiere validación adicional
- **Propuesta**: Sí, implementar start_point opcional

## Implementación Propuesta

### **Fase 1: Implementación Básica**
1. Implementar `create_branch()` con `git branch`
2. Validación básica de nombres de rama
3. Manejo básico de errores siguiendo patrones GitInterface
4. Tests unitarios básicos

### **Fase 2: Validaciones Adicionales**
1. Validar existencia de rama antes de crear
2. Mejorar mensajes de error
3. Tests de integración

### **Fase 3: Manejo de Archivos No Committeados**
1. Detectar archivos no committeados antes del switch
2. Preguntar al usuario si quiere llevar archivos o descartarlos
3. Implementar git stash para preservar cambios
4. Tests de integración con archivos no committeados

### **Fase 4: Optimizaciones**
1. Validación de start_point
2. Manejo de conflictos de nombres
3. Tests de rendimiento

## Flujo de Trabajo Git

### **⚠️ IMPORTANTE: Mantener Rama de Trabajo**
Durante las pruebas y desarrollo, es **CRÍTICO** mantener el flujo de trabajo correcto:

1. **Trabajar en rama de trabajo**: `fix/ggb-not-checkout-neither-not-create-branch` (rama actual)
2. **Implementar en rama de trabajo**: Hacer cambios en la rama actual
3. **Probar en rama de trabajo**: Ejecutar tests y validaciones
4. **Commit en rama de trabajo**: Guardar cambios con mensaje descriptivo
5. **NO trabajar en ramas de prueba**: Evitar trabajar en `main` u otras ramas

### **Riesgos de No Seguir el Flujo**
- **Pérdida de código**: Cambios en ramas incorrectas pueden perderse
- **Historia confusa**: Commits en ramas de prueba crean historial desordenado
- **Conflictos de merge**: Cambios en múltiples ramas pueden causar conflictos
- **Dificultad de seguimiento**: No se puede rastrear el progreso del desarrollo

### **Proceso Recomendado**
```bash
# 1. Verificar rama actual
git branch

# 2. Si no estamos en fix/ggb-not-checkout-neither-not-create-branch, cambiar
git checkout fix/ggb-not-checkout-neither-not-create-branch

# 3. Implementar cambios
# ... código ...

# 4. Probar cambios
python src/commands/ggb.py nueva-rama

# 5. Commit cambios
git add .
git commit -m "feat: implement create_branch() method

- Add proper implementation using git branch
- Handle branch name validation
- Follow GitInterface error patterns
- Fix ggb command branch creation bug"

# 6. Continuar desarrollo en la misma rama
```

### **Validación del Flujo**
- **Antes de implementar**: Verificar que estamos en `fix/ggb-not-checkout-neither-not-create-branch`
- **Después de cada cambio**: Commit inmediato con mensaje descriptivo
- **Antes de probar**: Verificar que los cambios están committeados
- **Después de probar**: Documentar resultados en zettels

## Integración con ggb

### **Flujo de Trabajo Propuesto**
1. `ggb` verifica si rama existe
2. Si existe: 
   - Verifica si hay archivos no committeados
   - Si hay archivos: pregunta al usuario si quiere llevarlos o descartarlos
   - Usa `switch_branch()` para cambiar
3. Si no existe: 
   - Usa `create_branch()` para crear
   - Verifica si hay archivos no committeados
   - Si hay archivos: pregunta al usuario si quiere llevarlos o descartarlos
   - Usa `switch_branch()` para cambiar

### **Manejo de Archivos No Committeados**
```python
def _handle_uncommitted_changes(self, branch_name: str) -> bool:
    """Handle uncommitted changes before switching branches."""
    if self.git.has_uncommitted_changes():
        click.echo(ColorManager.warning("Tienes archivos sin commitear"))
        choice = input("¿Quieres llevarlos a la nueva rama? (s/n): ").strip().lower()
        
        if choice in ['s', 'si', 'y', 'yes']:
            # Stash changes
            self.git.stash_changes()
            click.echo(ColorManager.info("Cambios guardados en stash"))
            return True
        else:
            # Discard changes
            self.git.discard_changes()
            click.echo(ColorManager.info("Cambios descartados"))
            return True
    
    return False
```

### **Ventajas del Enfoque**
- **Separación de responsabilidades**: Cada método tiene una función específica
- **Reutilización**: `create_branch()` puede usarse en otros comandos
- **Flexibilidad**: Permite crear sin cambiar si es necesario
- **Experiencia de usuario**: Manejo inteligente de archivos no committeados

## Referencias

- **Zettel padre**: 3b11a - Bug específico de ggb
- **Archivo fuente**: `src/core/git.py:454-480`
- **Comando afectado**: `src/commands/ggb.py`
- **Documentación Git**: `git branch` command reference

## Conclusión

La propuesta de implementar `create_branch()` con `git branch` y validación de nombres es sólida y debería resolver el bug de `ggb`. La implementación por fases permite validar cada paso y ajustar según sea necesario.

**Estado**: 💡 **PROPUESTA EN DEBATE - PENDIENTE DE DECISIÓN**

