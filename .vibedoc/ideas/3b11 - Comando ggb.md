# 3b11 - Comando ggb

## Descripción del Comando

**Fecha**: 2024-12-19  
**Componente**: Sistema de comandos específicos (3b)  
**Comando**: `ggb`  
**Estado**: 🔍 **EN ANÁLISIS**

## Propósito

El comando `ggb` está diseñado para facilitar la gestión de ramas Git, permitiendo tanto la creación de nuevas ramas como el cambio a ramas existentes. Es un comando de utilidad básica que debería simplificar la navegación y creación de ramas para los usuarios.

## Funcionalidad Esperada

### **Comportamiento Ideal**
1. **Crear nueva rama**: Si la rama no existe, crearla y cambiar a ella
2. **Cambiar a rama existente**: Si la rama ya existe, cambiar a ella
3. **Validar parámetros**: Verificar que se proporciona nombre de rama
4. **Mostrar feedback**: Confirmar la operación realizada

### **Flujo de Ejecución**
```bash
# Crear nueva rama
$ ggb nueva-rama
# Debería crear la rama y cambiar a ella

# Cambiar a rama existente  
$ ggb main
# Debería cambiar a la rama existente
```

## Implementación Actual

### **Archivo**: `src/commands/ggb.py`
```python
class GgbCommand(BaseCommand):
    def execute(self, branch_name):
        """Execute the ggb command."""
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            # Check if branch exists
            if self.git.branch_exists(branch_name):
                # Switch to existing branch
                result = self.git.switch_branch(branch_name)
                if result:
                    click.echo(ColorManager.success(f"Cambiado a rama '{branch_name}'"))
                    return 0
                else:
                    click.echo(ColorManager.error(f"Error al cambiar a rama '{branch_name}'"))
                    return 1
            else:
                # Create new branch
                result = self.git.create_branch(branch_name)
                if result:
                    click.echo(ColorManager.success(f"Rama '{branch_name}' creada y cambiado a ella"))
                    return 0
                else:
                    click.echo(ColorManager.error(f"Error al crear rama '{branch_name}'"))
                    return 1
                    
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
```

### **Dependencias**
- **GitInterface**: Métodos `branch_exists()`, `create_branch()`, `switch_branch()`
- **BaseCommand**: Clase base para comandos
- **ColorManager**: Gestión de colores en terminal

## Análisis de la Implementación

### **Fortalezas**
- ✅ **Lógica clara**: Distingue entre crear y cambiar rama
- ✅ **Patrón consistente**: Sigue el patrón BaseCommand
- ✅ **Manejo de errores**: Try-catch apropiado
- ✅ **Feedback visual**: Mensajes claros al usuario
- ✅ **Validación**: Verifica que es un repositorio Git

### **Debilidades Identificadas**
- ❌ **Dependencias no implementadas**: `branch_exists()` y `create_branch()` son TODOs
- ❌ **Falta de validación**: No verifica formato de nombre de rama
- ❌ **Manejo de errores limitado**: No distingue tipos de error específicos

## Casos de Uso

### **Caso 1: Crear Nueva Rama**
```bash
$ ggb feature/nueva-funcionalidad
Rama 'feature/nueva-funcionalidad' creada y cambiado a ella
$ git branch
  main
* feature/nueva-funcionalidad
```

### **Caso 2: Cambiar a Rama Existente**
```bash
$ ggb main
Cambiado a rama 'main'
$ git branch
* main
  feature/nueva-funcionalidad
```

### **Caso 3: No es Repositorio Git**
```bash
$ ggb nueva-rama
Not a git repository
```

### **Caso 4: Nombre de Rama Inválido**
```bash
$ ggb "rama con espacios"
Error: Nombre de rama inválido
```

## Integración con el Sistema

### **Relación con Otros Comandos**
- **Comandos de navegación**: `ggmain`, `ggdevelop`
- **Comandos de gestión**: `ggmerge`, `ggreset`
- **Comandos de utilidad**: `ggstatus`, `gglog`

### **Patrón Arquitectónico**
- **BaseCommand**: Herencia para consistencia
- **GitInterface**: Delegación de operaciones Git
- **ColorManager**: Consistencia visual

## Métricas de Calidad

### **Cobertura de Código**
- **Objetivo**: >90%
- **Actual**: Pendiente de implementación completa

### **Tests Requeridos**
- Test de creación de nueva rama
- Test de cambio a rama existente
- Test de error cuando no es repositorio
- Test de error con nombre de rama inválido

## Evolución del Comando

### **Versión Actual**
- Implementación básica con dependencias no resueltas
- Feedback visual implementado
- Manejo de errores básico

### **Versión Futura (Propuesta)**
- Validación completa de precondiciones
- Manejo específico de diferentes tipos de error
- Integración con sistema de logging
- Soporte para ramas remotas

## Referencias

- **Zettel padre**: 3b - Comandos específicos
- **Zettel hijo**: 3b11a - Bug específico de ggb
- **Archivo fuente**: `src/commands/ggb.py`
- **Dependencias**: `src/core/git.py:branch_exists()`, `create_branch()`

## Conclusión

El comando `ggb` tiene una implementación sólida en términos de estructura y patrón, pero depende de funcionalidades core (`branch_exists()` y `create_branch()`) que no están implementadas. Una vez resueltas estas dependencias, será un comando robusto y útil para la gestión de ramas.

**Estado**: 🔍 **EN ANÁLISIS - PENDIENTE DE RESOLUCIÓN DE DEPENDENCIAS**

