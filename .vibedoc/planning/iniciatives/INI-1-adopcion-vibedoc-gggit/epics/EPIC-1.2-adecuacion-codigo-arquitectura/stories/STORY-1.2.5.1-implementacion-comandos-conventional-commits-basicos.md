# [HISTORIA] - Implementación de Comandos Conventional Commits Básicos

## 🎯 Objetivo

Implementar los comandos de Conventional Commits básicos (`ggdocs`, `ggstyle`, `ggrefactor`, `ggtest`, `ggchore`) siguiendo la arquitectura establecida y aplicando Test-Driven Development (TDD) para garantizar calidad y cobertura de código.

## 🌎 Contexto

Esta historia es fundamental para completar la suite de comandos de Conventional Commits de ggGit. Actualmente solo tenemos implementados `ggfeat`, `ggfix` y `ggbreak`. Los comandos básicos restantes son esenciales para cubrir todos los tipos de commit según la especificación de Conventional Commits.

Como parte de la épica "Adecuación de código a arquitectura", necesitamos implementar estos comandos siguiendo el patrón establecido con `BaseCommand` y `CommitCommand`, manteniendo la consistencia arquitectónica y aprovechando la reutilización de código.

La implementación debe seguir la metodología TDD para asegurar que cada comando esté completamente probado y funcional antes de considerarse completo.

## 💡 Propuesta de Resolución

Se propone implementar los 5 comandos de Conventional Commits básicos siguiendo el patrón establecido:

1. **Reutilización de `CommitCommand`**: Cada comando utilizará `CommitCommand` con el tipo específico correspondiente
2. **Estructura consistente**: Todos los comandos seguirán el patrón `BaseCommand` + `Click` establecido
3. **Test-Driven Development**: Implementación guiada por tests, escribiendo tests antes que el código
4. **Validación de mensajes**: Integración con el sistema de validación existente
5. **Soporte para scope**: Mantener la funcionalidad de scope opcional
6. **Soporte para amend**: Mantener la funcionalidad de amend

**Patrón de implementación**:
```python
class DocsCommand(BaseCommand):
    def execute(self, message, scope=None, ai=False, amend=False):
        commit_cmd = CommitCommand("docs")
        return commit_cmd.execute(message, scope, amend)
```

**Metodología TDD**:
1. Escribir test que falle (Red)
2. Escribir código mínimo para que pase (Green)
3. Refactorizar manteniendo tests verdes (Refactor)
4. Repetir para cada funcionalidad

## 📦 Artefactos

- 📦 Código fuente de los 5 comandos: `ggdocs.py`, `ggstyle.py`, `ggrefactor.py`, `ggtest.py`, `ggchore.py`
- 📦 Tests unitarios completos para cada comando con cobertura > 90%
- 📦 Tests de integración verificando flujos completos de cada comando
- 📦 Documentación de uso actualizada en architecture.md
- 📦 Validación de que todos los comandos siguen el patrón arquitectónico establecido

## 🔍 Criterios de Aceptación

### Funcionalidad básica:
- Dado que un usuario ejecuta `ggdocs "actualizar README"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe crear un commit con mensaje `docs: actualizar README`

### Soporte para scope:
- Dado que un usuario ejecuta `ggdocs -s api "actualizar documentación"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe crear un commit con mensaje `docs(api): actualizar documentación`

### Soporte para amend:
- Dado que un usuario ejecuta `ggdocs -a "corregir documentación"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe modificar el último commit con el nuevo mensaje

### Validación de mensaje:
- Dado que un usuario ejecuta `ggdocs ""`
- Cuando el comando se ejecuta
- Entonces debe mostrar error de validación y no crear commit

### Cobertura de código:
- Dado que se implementan 5 comandos nuevos
- Cuando se ejecuten las pruebas unitarias
- Entonces el porcentaje de cobertura deberá ser superior al 90%

### Consistencia arquitectónica:
- Dado que se implementan nuevos comandos
- Cuando se revise el código
- Entonces todos los comandos deben seguir el patrón `BaseCommand` + `CommitCommand`

### Integración con sistema existente:
- Dado que se implementan comandos de Conventional Commits
- Cuando se ejecuten los comandos
- Entonces deben usar el sistema de configuración jerárquica existente

## 🔗 Dependencias y Recursos

### Dependencias

- La implementación de `BaseCommand` y `CommitCommand` debe estar completa y funcional
- El sistema de validación de mensajes debe estar implementado
- El sistema de configuración jerárquica debe estar funcionando
- Los tests de `ggfeat`, `ggfix` y `ggbreak` deben estar pasando para validar el patrón

### Recursos

- Acceso al código fuente existente en `src/commands/` y `src/core/`
- Framework de testing pytest configurado y funcionando
- Sistema de configuración jerárquica operativo
- Repositorio Git para testing de comandos
- Documentación de Conventional Commits para validación de tipos
