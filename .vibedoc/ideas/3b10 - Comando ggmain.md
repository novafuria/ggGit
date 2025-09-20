# 3b10 - Comando ggmain

## Descripción del Comando

**Fecha**: 2024-12-19  
**Componente**: Sistema de comandos específicos (3b)  
**Comando**: `ggmain`  
**Estado**: 🔍 **EN ANÁLISIS**

## Propósito

El comando `ggmain` está diseñado para facilitar el cambio a la rama principal (`main`) del repositorio Git actual. Es un comando de utilidad básica que debería simplificar la navegación entre ramas para los usuarios.

## Funcionalidad Esperada

### **Comportamiento Ideal**
1. **Verificar** que estamos en un repositorio Git válido
2. **Cambiar** a la rama `main` 
3. **Confirmar** el cambio exitoso
4. **Mostrar** feedback visual al usuario

### **Flujo de Ejecución**
```bash
$ ggmain
# Debería cambiar a la rama main y mostrar:
# "Cambiado a rama main"
```

## Implementación Actual

### **Archivo**: `src/commands/ggmain.py`
```python
class GgmainCommand(BaseCommand):
    def execute(self):
        try:
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("Not a git repository"))
                return 1
            
            result = self.git.switch_branch("main")
            
            if result:
                click.echo(ColorManager.success("Cambiado a rama main"))
                return 0
            else:
                click.echo(ColorManager.error("Error al cambiar a rama main"))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error: {str(e)}"))
            return 1
```

### **Dependencias**
- **GitInterface**: Método `switch_branch()`
- **BaseCommand**: Clase base para comandos
- **ColorManager**: Gestión de colores en terminal

## Análisis de la Implementación

### **Fortalezas**
- ✅ **Patrón consistente**: Sigue el patrón BaseCommand
- ✅ **Manejo de errores**: Try-catch apropiado
- ✅ **Feedback visual**: Mensajes claros al usuario
- ✅ **Validación**: Verifica que es un repositorio Git

### **Debilidades Identificadas**
- ❌ **Dependencia no implementada**: `switch_branch()` es un TODO
- ❌ **Falta de validación**: No verifica que la rama `main` existe
- ❌ **Manejo de errores limitado**: No distingue tipos de error

## Casos de Uso

### **Caso 1: Cambio Exitoso**
```bash
$ git branch
* feature/nueva-funcionalidad
  main
$ ggmain
Cambiado a rama main
$ git branch
  feature/nueva-funcionalidad
* main
```

### **Caso 2: No es Repositorio Git**
```bash
$ ggmain
Not a git repository
```

### **Caso 3: Rama main no Existe**
```bash
$ ggmain
Error: La rama 'main' no existe
```

### **Caso 4: Cambios no Committeados**
```bash
$ ggmain
Error: No se puede cambiar de rama. Tienes cambios sin commitear
```

## Integración con el Sistema

### **Relación con Otros Comandos**
- **Comandos de navegación**: Futuros comandos `ggdevelop`, `ggfeature`
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
- Test de cambio exitoso
- Test de error cuando no es repositorio
- Test de error cuando rama no existe
- Test de error con cambios no committeados

## Evolución del Comando

### **Versión Actual**
- Implementación básica con dependencia no resuelta
- Feedback visual implementado
- Manejo de errores básico

### **Versión Futura (Propuesta)**
- Validación completa de precondiciones
- Manejo específico de diferentes tipos de error
- Integración con sistema de logging
- Soporte para diferentes nombres de rama principal

## Referencias

- **Zettel padre**: 3b - Comandos específicos
- **Zettel hijo**: 3b10a - Bug específico de ggmain
- **Archivo fuente**: `src/commands/ggmain.py`
- **Dependencia**: `src/core/git.py:switch_branch()`

## Conclusión

El comando `ggmain` tiene una implementación sólida en términos de estructura y patrón, pero depende de una funcionalidad core (`switch_branch()`) que no está implementada. Una vez resuelta esta dependencia, será un comando robusto y útil para la navegación entre ramas.

**Estado**: 🔍 **EN ANÁLISIS - PENDIENTE DE RESOLUCIÓN DE DEPENDENCIAS**
