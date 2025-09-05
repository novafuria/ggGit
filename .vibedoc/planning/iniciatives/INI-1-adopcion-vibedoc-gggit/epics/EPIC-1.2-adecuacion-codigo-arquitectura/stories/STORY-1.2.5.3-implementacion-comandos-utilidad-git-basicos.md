# [HISTORIA] - Implementación de Comandos de Utilidad Git Básicos

## 🎯 Objetivo

Implementar los comandos de utilidad Git básicos (`gga`, `ggs`, `ggl`, `ggdif`, `ggunstage`, `ggreset`, `ggpl`, `ggpp`, `ggv`) migrando la funcionalidad existente de Bash a Python y aplicando Test-Driven Development (TDD) para garantizar calidad y cobertura de código.

## 🌎 Contexto

Esta historia migra los comandos de utilidad Git existentes en Bash a Python, manteniendo toda la funcionalidad actual pero aprovechando la nueva arquitectura. Los comandos de utilidad Git son esenciales para la productividad diaria de los desarrolladores y deben mantener la misma funcionalidad que los comandos Bash existentes.

Como parte de la épica "Adecuación de código a arquitectura", esta migración elimina la dualidad de implementaciones (Bash vs Python) y unifica todo bajo la arquitectura Python establecida.

La implementación debe seguir la metodología TDD para asegurar que cada comando mantenga la funcionalidad exacta de su contraparte Bash, mientras aprovecha las mejoras de la nueva arquitectura (colores, logging, configuración).

## 💡 Propuesta de Resolución

Se propone implementar los 9 comandos de utilidad Git básicos siguiendo el patrón establecido:

1. **Migración de funcionalidad**: Cada comando Python debe mantener la funcionalidad exacta de su contraparte Bash
2. **Estructura consistente**: Todos los comandos seguirán el patrón `BaseCommand` + `Click` establecido
3. **Test-Driven Development**: Implementación guiada por tests, escribiendo tests antes que el código
4. **Aprovechamiento de arquitectura**: Usar `GitInterface`, `ColorManager`, `LoggingManager`
5. **Mejoras visuales**: Aprovechar el sistema de colores unificado
6. **Configuración**: Integrar con el sistema de configuración jerárquica

**Patrón de implementación**:
```python
class GgaCommand(BaseCommand):
    def execute(self, files=None, all=False):
        git = GitInterface()
        if all:
            git.stage_all_changes()
        else:
            git.stage_files(files)
        return 0
```

**Metodología TDD**:
1. Escribir test que falle (Red)
2. Escribir código mínimo para que pase (Green)
3. Refactorizar manteniendo tests verdes (Refactor)
4. Repetir para cada funcionalidad

**Comandos a implementar**:
- `gga` - Git add simplificado
- `ggs` - Git status con formato mejorado
- `ggl` - Git log con formato compacto
- `ggdif` - Git diff con colores
- `ggunstage` - Git reset HEAD
- `ggreset` - Git reset --hard HEAD
- `ggpl` - Git pull
- `ggpp` - Git push
- `ggv` - Git version

## 📦 Artefactos

- 📦 Código fuente de los 9 comandos de utilidad Git
- 📦 Tests unitarios completos para cada comando con cobertura > 90%
- 📦 Tests de integración verificando flujos completos de cada comando
- 📦 Tests comparativos con comandos Bash existentes
- 📦 Documentación de uso actualizada en architecture.md
- 📦 Validación de que todos los comandos siguen el patrón arquitectónico establecido
- 📦 Eliminación de comandos Bash duplicados

## 🔍 Criterios de Aceptación

### Funcionalidad básica:
- Dado que un usuario ejecuta `gga`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer stage de todos los cambios (equivalente a `git add .`)

### Funcionalidad con parámetros:
- Dado que un usuario ejecuta `gga archivo.txt`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer stage solo del archivo especificado

### Formato mejorado:
- Dado que un usuario ejecuta `ggs`
- Cuando el comando se ejecuta exitosamente
- Entonces debe mostrar el status con colores y formato mejorado

### Funcionalidad de log:
- Dado que un usuario ejecuta `ggl`
- Cuando el comando se ejecuta exitosamente
- Entonces debe mostrar el log con formato compacto y colores

### Funcionalidad de diff:
- Dado que un usuario ejecuta `ggdif`
- Cuando el comando se ejecuta exitosamente
- Entonces debe mostrar el diff con colores

### Funcionalidad de unstage:
- Dado que un usuario ejecuta `ggunstage archivo.txt`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer unstage del archivo especificado

### Funcionalidad de reset:
- Dado que un usuario ejecuta `ggreset`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer reset --hard HEAD

### Funcionalidad de pull:
- Dado que un usuario ejecuta `ggpl`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer pull del repositorio remoto

### Funcionalidad de push:
- Dado que un usuario ejecuta `ggpp`
- Cuando el comando se ejecuta exitosamente
- Entonces debe hacer push al repositorio remoto

### Funcionalidad de version:
- Dado que un usuario ejecuta `ggv`
- Cuando el comando se ejecuta exitosamente
- Entonces debe mostrar la versión de Git

### Cobertura de código:
- Dado que se implementan 9 comandos nuevos
- Cuando se ejecuten las pruebas unitarias
- Entonces el porcentaje de cobertura deberá ser superior al 90%

### Consistencia arquitectónica:
- Dado que se implementan nuevos comandos
- Cuando se revise el código
- Entonces todos los comandos deben seguir el patrón `BaseCommand` + `GitInterface`

### Integración con sistema existente:
- Dado que se implementan comandos de utilidad Git
- Cuando se ejecuten los comandos
- Entonces deben usar el sistema de configuración jerárquica existente

### Compatibilidad con comandos Bash:
- Dado que se migran comandos de Bash a Python
- Cuando se ejecuten los comandos Python
- Entonces deben producir el mismo resultado que los comandos Bash

## 🔗 Dependencias y Recursos

### Dependencias

- STORY-1.2.5.1 y STORY-1.2.5.2 deben estar completadas (comandos de Conventional Commits)
- La implementación de `BaseCommand` y `GitInterface` debe estar completa y funcional
- El sistema de configuración jerárquica debe estar funcionando
- Los tests de comandos de Conventional Commits deben estar pasando

### Recursos

- Acceso al código fuente existente en `src/commands/` y `src/core/`
- Acceso a los comandos Bash existentes para comparación
- Framework de testing pytest configurado y funcionando
- Sistema de configuración jerárquica operativo
- Repositorio Git para testing de comandos
- Documentación de comandos Bash existentes
