# 1.2.5.6.2 - Decisiones STORY-1.2.5.6

## Resumen de Decisiones

**Fecha**: 2024-12-19
**Historia**: STORY-1.2.5.6-implementacion-comandos-interactivos
**Objetivo**: Documentar decisiones arquitectónicas y de implementación

## Decisiones Tomadas

### 1. **Patrón de Implementación para Comandos Interactivos**

**Decisión**: Extender comandos existentes con funcionalidad interactiva

**Justificación**:
- Mantener consistencia con la arquitectura establecida
- Evitar duplicación de código
- Facilitar mantenimiento y testing
- Proporcionar funcionalidad progresiva (básica + interactiva)

**Implementación**:
```python
class GgmergeCommand(BaseCommand):
    def execute(self, branch=None, abort=False, continue_merge=False):
        """Execute the ggmerge command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            if branch:
                return self._merge_branch(branch)
            elif abort:
                return self._abort_merge()
            elif continue_merge:
                return self._continue_merge()
            else:
                return self._show_merge_options()  # Nueva funcionalidad interactiva
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
```

### 2. **Interfaz de Usuario Interactiva**

**Decisión**: Usar `input()` simple para selección de opciones

**Justificación**:
- Mantener simplicidad arquitectónica
- Evitar dependencias externas innecesarias
- Facilitar testing con mocking
- Suficiente para la funcionalidad requerida

**Implementación**:
```python
def _show_merge_options(self):
    """Show interactive list of branches for merge."""
    try:
        branches = self.git.get_mergeable_branches()
        
        if not branches:
            click.echo(ColorManager.warning("No hay ramas disponibles para merge"))
            return 0
        
        # Mostrar lista numerada
        click.echo(ColorManager.info("Ramas disponibles para merge:"))
        for i, branch in enumerate(branches, 1):
            click.echo(f"  {i}. {branch}")
        
        # Obtener selección del usuario
        while True:
            try:
                choice = input("\nSelecciona rama para merge (número): ").strip()
                
                if not choice:
                    click.echo(ColorManager.error("Selección requerida"))
                    continue
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(branches):
                    selected_branch = branches[choice_num - 1]
                    return self._merge_branch(selected_branch)
                else:
                    click.echo(ColorManager.error(f"Selección inválida. Ingresa un número entre 1 y {len(branches)}"))
                    
            except ValueError:
                click.echo(ColorManager.error("Selección inválida. Ingresa un número válido"))
            except KeyboardInterrupt:
                click.echo(ColorManager.warning("\nOperación cancelada"))
                return 1
                
    except Exception as e:
        click.echo(ColorManager.error(f"Error al mostrar opciones: {str(e)}"))
        return 1
```

### 3. **Validaciones Avanzadas**

**Decisión**: Implementar validaciones básicas de contexto (sin IA)

**Justificación**:
- Mantener simplicidad y simplicidad
- Evitar complejidad innecesaria
- Proporcionar funcionalidad útil sin dependencias externas
- Dejar elementos de IA para la próxima idea (1.2.6)

**Implementación**:
```python
def _validate_message_context(self, message: str, command_type: str) -> bool:
    """Validate message context and provide basic feedback."""
    # Validaciones básicas sin IA
    if not message or not message.strip():
        return False
    
    # Validaciones específicas por tipo de comando
    if command_type == "docs" and any(word in message.lower() for word in ["feature", "funcionalidad", "nueva"]):
        click.echo(ColorManager.warning("El mensaje sugiere una funcionalidad. Considera usar 'ggfeat' en su lugar"))
    
    return True
```

### 4. **Manejo de Entrada del Usuario**

**Decisión**: Manejo avanzado con reintentos y validación robusta

**Justificación**:
- Mejor experiencia de usuario
- Manejo robusto de errores
- Validación completa de entrada
- Feedback claro y descriptivo

**Implementación**:
```python
def _get_user_selection(self, options: List[str], prompt: str) -> str:
    """Get user selection with robust validation."""
    while True:
        try:
            choice = input(f"\n{prompt}: ").strip()
            
            if not choice:
                click.echo(ColorManager.error("Selección requerida"))
                continue
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                return options[choice_num - 1]
            else:
                click.echo(ColorManager.error(f"Selección inválida. Ingresa un número entre 1 y {len(options)}"))
                
        except ValueError:
            click.echo(ColorManager.error("Selección inválida. Ingresa un número válido"))
        except KeyboardInterrupt:
            click.echo(ColorManager.warning("\nOperación cancelada"))
            return None
```

### 5. **Testing de Funcionalidad Interactiva**

**Decisión**: Mockear entrada del usuario en tests unitarios

**Justificación**:
- Tests unitarios rápidos y confiables
- Control total sobre entrada del usuario
- Fácil de mantener y debuggear
- Separación clara entre tests unitarios e integración

**Implementación**:
```python
@patch('builtins.input', return_value='1')
def test_show_merge_options_success(self, mock_input):
    """Test successful interactive merge selection."""
    cmd = GgmergeCommand()
    
    with patch.object(cmd.git, 'is_git_repository', return_value=True):
        with patch.object(cmd.git, 'get_mergeable_branches', return_value=['feature/test']):
            with patch.object(cmd, '_merge_branch', return_value=0) as mock_merge:
                result = cmd._show_merge_options()
                
                assert result == 0
                mock_merge.assert_called_once_with('feature/test')
```

### 6. **Extensión de GitInterface**

**Decisión**: Agregar métodos específicos para funcionalidad interactiva

**Justificación**:
- Centralizar funcionalidad Git en un solo lugar
- Mantener simplicidad arquitectónica
- Facilitar testing y mantenimiento
- Proporcionar funcionalidad específica para comandos interactivos

**Métodos a Implementar**:
```python
def get_mergeable_branches(self) -> List[str]:
    """Get list of branches that can be merged."""
    
def get_branch_info(self, branch_name: str) -> Dict[str, Any]:
    """Get detailed information about a branch."""
    
def is_branch_mergeable(self, branch_name: str) -> bool:
    """Check if branch can be merged."""
```

## Impacto en la Implementación

### **Archivos a Crear/Modificar**:
- **`src/core/git.py`**: Extender GitInterface con métodos interactivos
- **`src/commands/ggmerge.py`**: Extender con funcionalidad interactiva
- **`src/commands/ggb.py`**: Extender con funcionalidad interactiva
- **`src/commands/[otros].py`**: Agregar validaciones avanzadas básicas

### **Tests a Crear**:
- **`tests/test_git_interface_interactive.py`**: Tests para métodos nuevos de GitInterface
- **`tests/test_git_interactive_commands.py`**: Tests parametrizados para comandos interactivos
- **`tests/test_advanced_validations.py`**: Tests para validaciones avanzadas

### **Patrón de Implementación**:
- Todos los comandos mantendrán compatibilidad con funcionalidad básica
- Funcionalidad interactiva se activa cuando no se proporcionan parámetros
- Validaciones avanzadas se integran en comandos existentes
- Tests unitarios con mocking de entrada del usuario

## Consideraciones Especiales

### **1. Compatibilidad con Funcionalidad Existente**
- **Funcionalidad básica**: Mantener intacta para compatibilidad
- **Funcionalidad interactiva**: Agregar como extensión
- **Parámetros**: Funcionalidad interactiva se activa sin parámetros
- **Comportamiento**: Mismo comportamiento para casos existentes

### **2. Experiencia de Usuario**
- **Feedback claro**: Mensajes descriptivos para cada acción
- **Validación robusta**: Manejo de errores con reintentos
- **Cancelación**: Soporte para Ctrl+C para cancelar operaciones
- **Colores**: Uso consistente de ColorManager para mejor experiencia

### **3. Testing**
- **Tests unitarios**: Mocking de entrada del usuario
- **Tests de integración**: Verificación de funcionalidad real
- **Cobertura >90%**: Mantener estándar de calidad establecido
- **Tests parametrizados**: Eficiencia para comandos similares

### **4. Elementos de IA Diferidos**
- **Validaciones inteligentes**: Para la próxima idea (1.2.6)
- **Sugerencias avanzadas**: Para la próxima idea (1.2.6)
- **Feedback contextual**: Para la próxima idea (1.2.6)
- **Funcionalidad básica**: Implementar ahora sin IA

## Conclusión

Estas decisiones aseguran:
1. **Funcionalidad interactiva** sin complejidad innecesaria
2. **Compatibilidad** con funcionalidad existente
3. **Experiencia de usuario** mejorada con validación robusta
4. **Testing eficiente** con mocking de entrada del usuario
5. **Preparación** para elementos de IA en la próxima idea

La implementación procederá siguiendo estas decisiones establecidas, proporcionando funcionalidad interactiva básica pero efectiva, manteniendo la simplicidad arquitectónica y preparando el terreno para elementos más avanzados en la próxima idea.
