# [HISTORIA] - Implementación de GitInterface básico

## 🎯 Objetivo

Implementar la funcionalidad completa del GitInterface especificada en la arquitectura para permitir que los comandos ggfeat, ggfix y ggbreak puedan realizar operaciones Git reales. Esta historia establece la base completa para que los comandos de commit funcionen correctamente y proporciona funcionalidad adicional para gestión de archivos.

## 🌎 Contexto

Esta historia es fundamental para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" y específicamente para la idea 1.2.3 - comandos base. Actualmente, el GitInterface tiene todos sus métodos marcados como TODO, lo que impide que los comandos realicen commits reales.

Sin un GitInterface funcional, los comandos ggfeat, ggfix y ggbreak no pueden cumplir su propósito principal: hacer commits con mensajes formateados según Conventional Commits. Esta historia implementa todos los 7 métodos especificados en la arquitectura para tener comandos completamente funcionales.

La implementación debe seguir la especificación de la arquitectura (architecture.md) y usar subprocess para mantener compatibilidad con Git nativo.

## 💡 Propuesta de Resolución

Se propone implementar los 7 métodos del GitInterface especificados en la arquitectura usando subprocess para ejecutar comandos Git nativos:

**Métodos básicos (críticos para comandos funcionales):**
1. **is_git_repository()**: Verificar si el directorio actual es un repositorio Git válido
2. **stage_all_changes()**: Ejecutar `git add .` para stagear todos los cambios
3. **commit(message)**: Ejecutar `git commit -m "message"` para hacer commit
4. **get_current_branch()**: Ejecutar `git branch --show-current` para obtener rama actual

**Métodos adicionales (especificados en architecture.md):**
5. **stage_files(files)**: Ejecutar `git add <files>` para stagear archivos específicos
6. **get_staged_files()**: Ejecutar `git diff --cached --name-only` para obtener archivos staged
7. **get_unstaged_files()**: Ejecutar `git diff --name-only` para obtener archivos modificados no staged

La implementación incluirá:
- Manejo de errores con subprocess.CalledProcessError
- Validación de que Git esté disponible en el sistema
- Mensajes de error descriptivos y accionables
- Retorno de valores booleanos para operaciones de escritura
- Retorno de strings para operaciones de lectura

## 📦 Artefactos

- 📦 **Código fuente del GitInterface**: Implementación completa de los 7 métodos especificados en `src/core/git.py`
- 📦 **Pruebas unitarias**: Tests para cada método implementado en `tests/test_git_interface.py`
- 📦 **Documentación actualizada**: Docstrings completos y ejemplos de uso
- 📦 **Validación de funcionamiento**: Script de prueba que demuestre que los comandos funcionan

## 🔍 Criterios de Aceptación

### Verificación de repositorio Git:
- Dado que se debe verificar si estamos en un repositorio Git
- Cuando se ejecute `is_git_repository()`
- Entonces debe retornar `True` si estamos en un repo Git válido y `False` en caso contrario

### Stage de cambios:
- Dado que se deben stagear todos los cambios
- Cuando se ejecute `stage_all_changes()`
- Entonces debe ejecutar `git add .` y retornar `True` si es exitoso

### Realización de commit:
- Dado que se debe hacer commit con un mensaje
- Cuando se ejecute `commit("feat: add new feature")`
- Entonces debe ejecutar `git commit -m "feat: add new feature"` y retornar `True` si es exitoso

### Obtención de rama actual:
- Dado que se debe obtener la rama actual
- Cuando se ejecute `get_current_branch()`
- Entonces debe retornar el nombre de la rama actual o `None` si no está en una rama

### Stage de archivos específicos:
- Dado que se deben stagear archivos específicos
- Cuando se ejecute `stage_files(['file1.py', 'file2.py'])`
- Entonces debe ejecutar `git add file1.py file2.py` y retornar `True` si es exitoso

### Obtención de archivos staged:
- Dado que se deben obtener archivos staged
- Cuando se ejecute `get_staged_files()`
- Entonces debe retornar una lista de archivos staged o lista vacía si no hay archivos

### Obtención de archivos unstaged:
- Dado que se deben obtener archivos modificados no staged
- Cuando se ejecute `get_unstaged_files()`
- Entonces debe retornar una lista de archivos modificados o lista vacía si no hay cambios

### Manejo de errores:
- Dado que Git no esté disponible o no sea un repositorio
- Cuando se ejecuten los métodos
- Entonces debe lanzar excepciones descriptivas con mensajes accionables

### Tests unitarios:
- Dado que se debe validar la funcionalidad
- Cuando se ejecuten las pruebas unitarias
- Entonces debe tener cobertura del 100% para los métodos implementados

## 🔗 Dependencias y Recursos

### Dependencias

- **Estructura de directorios**: La estructura `src/core/` debe estar implementada (STORY-1.2.1 completada)
- **Git instalado**: El sistema debe tener Git instalado y disponible en PATH
- **Repositorio de prueba**: Acceso a un repositorio Git de prueba para testing

### Recursos

- **Conocimiento de subprocess**: Comprensión de cómo ejecutar comandos del sistema desde Python
- **Conocimiento de Git**: Entendimiento de los comandos Git básicos y sus códigos de salida
- **Entorno de testing**: Acceso a un repositorio Git para probar la funcionalidad
- **Documentación de Git**: Referencia para códigos de error y comportamientos esperados
