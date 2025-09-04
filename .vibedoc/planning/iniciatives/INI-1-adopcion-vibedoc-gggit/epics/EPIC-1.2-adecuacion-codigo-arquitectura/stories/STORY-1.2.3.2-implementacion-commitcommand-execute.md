# [HISTORIA] - Implementación de CommitCommand.execute()

## 🎯 Objetivo

Implementar la funcionalidad principal del CommitCommand.execute() para que los comandos ggfeat, ggfix y ggbreak puedan realizar commits reales con mensajes formateados según Conventional Commits.

## 🌎 Contexto

Esta historia es crítica para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" y la idea 1.2.3 - comandos base. Actualmente, CommitCommand.execute() solo tiene un TODO y retorna 0 sin hacer nada real.

El CommitCommand es el corazón de los comandos de commit (ggfeat, ggfix, ggbreak) y debe:
1. Validar el mensaje y scope proporcionados
2. Formatear el mensaje según Conventional Commits
3. Usar GitInterface para hacer el commit real
4. Manejar errores y proporcionar feedback al usuario

Esta implementación debe seguir la especificación de la arquitectura y usar las abstracciones ya implementadas (GitInterface, ArgumentValidator, ColorManager).

## 💡 Propuesta de Resolución

Se propone implementar CommitCommand.execute() con la siguiente lógica:

1. **Validación de entrada**: Usar ArgumentValidator para validar mensaje y scope
2. **Formateo de mensaje**: Aplicar formato Conventional Commits usando el método existente
3. **Verificación de repositorio**: Usar GitInterface.is_git_repository() para verificar que estamos en un repo Git
4. **Stage de cambios**: Usar GitInterface.stage_all_changes() para stagear cambios
5. **Realización de commit**: Usar GitInterface.commit() con el mensaje formateado
6. **Manejo de errores**: Capturar excepciones y proporcionar feedback apropiado

La implementación debe:
- Seguir el patrón de retorno de códigos de salida (0 = éxito, 1 = error)
- Usar ColorManager para mensajes de éxito/error
- Manejar el flag --amend si está presente
- Validar que hay cambios para hacer commit

## 📦 Artefactos

- 📦 **Código fuente de CommitCommand.execute()**: Implementación completa del método en `src/core/base_commands/commit.py`
- 📦 **Pruebas unitarias**: Tests para CommitCommand.execute() en `tests/test_commit_command.py`
- 📦 **Pruebas de integración**: Tests que demuestren que los comandos ggfeat, ggfix, ggbreak funcionan end-to-end
- 📦 **Documentación actualizada**: Docstrings y ejemplos de uso actualizados

## 🔍 Criterios de Aceptación

### Validación de entrada:
- Dado que se proporciona un mensaje válido
- Cuando se ejecute CommitCommand.execute()
- Entonces debe validar el mensaje usando ArgumentValidator

### Formateo de mensaje:
- Dado que se proporciona un mensaje y scope
- Cuando se ejecute CommitCommand.execute()
- Entonces debe formatear el mensaje como "type(scope): message"

### Verificación de repositorio:
- Dado que no estamos en un repositorio Git
- Cuando se ejecute CommitCommand.execute()
- Entonces debe retornar código de error 1 y mostrar mensaje apropiado

### Stage de cambios:
- Dado que hay cambios sin stagear
- Cuando se ejecute CommitCommand.execute()
- Entonces debe stagear todos los cambios antes del commit

### Realización de commit:
- Dado que hay cambios staged
- Cuando se ejecute CommitCommand.execute()
- Entonces debe hacer commit con el mensaje formateado y retornar código de éxito

### Manejo de flag --amend:
- Dado que se proporciona el flag --amend
- Cuando se ejecute CommitCommand.execute()
- Entonces debe usar `git commit --amend` en lugar de `git commit`

### Tests unitarios:
- Dado que se debe validar la funcionalidad
- Cuando se ejecuten las pruebas unitarias
- Entonces debe tener cobertura del 100% para el método execute()

### Tests de integración:
- Dado que se debe validar el flujo completo
- Cuando se ejecuten los comandos ggfeat, ggfix, ggbreak
- Entonces deben hacer commits reales con mensajes formateados correctamente

## 🔗 Dependencias y Recursos

### Dependencias

- **GitInterface básico**: STORY-1.2.3.1 debe estar completada para tener GitInterface funcional
- **ArgumentValidator**: Debe estar implementado para validación de entrada
- **ColorManager**: Debe estar implementado para mensajes de salida
- **BaseCommand**: Debe estar implementado para la estructura base

### Recursos

- **Conocimiento de Conventional Commits**: Entendimiento del formato estándar de mensajes de commit
- **Conocimiento de Git**: Comprensión de los comandos git add, git commit y git commit --amend
- **Entorno de testing**: Repositorio Git de prueba para validar commits reales
- **Documentación de ArgumentValidator**: Referencia para métodos de validación disponibles
