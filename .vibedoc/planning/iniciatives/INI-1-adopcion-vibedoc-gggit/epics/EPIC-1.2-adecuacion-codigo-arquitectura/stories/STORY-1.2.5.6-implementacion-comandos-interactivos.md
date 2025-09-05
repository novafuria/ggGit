# [HISTORIA] - Implementación de Comandos Interactivos

## 🎯 Objetivo

Implementar los comandos interactivos (`ggmerge` interactivo, validaciones avanzadas) siguiendo la arquitectura establecida y aplicando Test-Driven Development (TDD) para garantizar calidad y cobertura de código.

## 🌎 Contexto

Esta historia implementa la funcionalidad más avanzada de ggGit: comandos interactivos que mejoran significativamente la experiencia del desarrollador. El comando `ggmerge` interactivo permite seleccionar ramas para merge desde una lista, mientras que las validaciones avanzadas proporcionan feedback inteligente sobre el contexto de los commits.

Como parte de la épica "Adecuación de código a arquitectura", estos comandos representan la culminación de la funcionalidad de ggGit, proporcionando una experiencia de usuario superior que diferencia ggGit de otras herramientas similares.

La implementación debe seguir la metodología TDD para asegurar que cada funcionalidad interactiva esté completamente probada y funcional, especialmente el manejo de entrada del usuario y la validación de selecciones.

## 💡 Propuesta de Resolución

Se propone implementar los comandos interactivos siguiendo el patrón establecido:

1. **Reutilización de `GitInterface`**: Cada comando utilizará `GitInterface` para operaciones Git
2. **Estructura consistente**: Todos los comandos seguirán el patrón `BaseCommand` + `Click` establecido
3. **Test-Driven Development**: Implementación guiada por tests, escribiendo tests antes que el código
4. **Interfaz interactiva**: Implementar selección de opciones desde lista
5. **Validaciones inteligentes**: Proporcionar feedback contextual sobre commits
6. **Manejo de errores**: Integración con el sistema de logging y manejo de errores

**Patrón de implementación**:
```python
class GgmergeCommand(BaseCommand):
    def execute(self, branch_name=None):
        if branch_name:
            return self._merge_branch(branch_name)
        else:
            return self._show_merge_options()
    
    def _show_merge_options(self):
        git = GitInterface()
        branches = git.get_mergeable_branches()
        
        # Mostrar lista numerada
        for i, branch in enumerate(branches, 1):
            print(f"{i}. {branch}")
        
        # Permitir selección
        choice = input("Selecciona rama para merge (número): ")
        selected_branch = branches[int(choice) - 1]
        
        return self._merge_branch(selected_branch)
```

**Metodología TDD**:
1. Escribir test que falle (Red)
2. Escribir código mínimo para que pase (Green)
3. Refactorizar manteniendo tests verdes (Refactor)
4. Repetir para cada funcionalidad

**Funcionalidades a implementar**:
- `ggmerge` (sin parámetros) - Lista interactiva de ramas para merge
- Validaciones avanzadas para comandos de Conventional Commits
- Feedback contextual sobre el tipo de commit apropiado

## 📦 Artefactos

- 📦 Código fuente de los comandos interactivos
- 📦 Tests unitarios completos para cada comando con cobertura > 90%
- 📦 Tests de integración verificando flujos completos de cada comando
- 📦 Tests para funcionalidad interactiva (selección de opciones)
- 📦 Tests para validaciones avanzadas
- 📦 Tests para manejo de errores (selección inválida, entrada vacía)
- 📦 Documentación de uso actualizada en architecture.md
- 📦 Validación de que todos los comandos siguen el patrón arquitectónico establecido

## 🔍 Criterios de Aceptación

### Funcionalidad de ggmerge interactivo:
- Dado que un usuario ejecuta `ggmerge`
- Cuando el comando se ejecuta exitosamente
- Entonces debe mostrar una lista numerada de ramas disponibles para merge

### Selección de rama:
- Dado que un usuario ejecuta `ggmerge` y selecciona una opción
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer merge de la rama seleccionada

### Manejo de selección inválida:
- Dado que un usuario ejecuta `ggmerge` y selecciona una opción inválida
- Cuando el comando se ejecuta
- Entonces debe mostrar error descriptivo y permitir nueva selección

### Manejo de entrada vacía:
- Dado que un usuario ejecuta `ggmerge` y presiona Enter sin seleccionar
- Cuando el comando se ejecuta
- Entonces debe mostrar error descriptivo y permitir nueva selección

### Validaciones avanzadas:
- Dado que un usuario ejecuta `ggperf "agregar nueva funcionalidad"`
- Cuando el comando se ejecuta
- Entonces puede mostrar advertencia sobre el contexto del mensaje

### Feedback contextual:
- Dado que un usuario ejecuta `ggdocs` con mensaje que sugiere feature
- Cuando el comando se ejecuta
- Entonces puede sugerir usar `ggfeat` en su lugar

### Cobertura de código:
- Dado que se implementan comandos interactivos
- Cuando se ejecuten las pruebas unitarias
- Entonces el porcentaje de cobertura deberá ser superior al 90%

### Consistencia arquitectónica:
- Dado que se implementan nuevos comandos
- Cuando se revise el código
- Entonces todos los comandos deben seguir el patrón `BaseCommand` + `GitInterface`

### Integración con sistema existente:
- Dado que se implementan comandos interactivos
- Cuando se ejecuten los comandos
- Entonces deben usar el sistema de configuración jerárquica existente

### Experiencia de usuario:
- Dado que se implementan comandos interactivos
- Cuando se ejecuten los comandos
- Entonces deben proporcionar una experiencia de usuario superior a los comandos Git nativos

## 🔗 Dependencias y Recursos

### Dependencias

- STORY-1.2.5.1, STORY-1.2.5.2, STORY-1.2.5.3, STORY-1.2.5.4 y STORY-1.2.5.5 deben estar completadas
- La implementación de `BaseCommand` y `GitInterface` debe estar completa y funcional
- El sistema de configuración jerárquica debe estar funcionando
- Los tests de comandos anteriores deben estar pasando

### Recursos

- Acceso al código fuente existente en `src/commands/` y `src/core/`
- Framework de testing pytest configurado y funcionando
- Sistema de configuración jerárquica operativo
- Repositorio Git para testing de comandos
- Documentación de comandos Git para validación de funcionalidad
- Ejemplos de flujos de trabajo para testing de funcionalidad interactiva
