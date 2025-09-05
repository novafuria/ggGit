# [HISTORIA] - Implementación de Comandos Conventional Commits Especializados

## 🎯 Objetivo

Implementar los comandos de Conventional Commits especializados (`ggperf`, `ggci`, `ggbuild`) siguiendo la arquitectura establecida y aplicando Test-Driven Development (TDD) para garantizar calidad y cobertura de código.

## 🌎 Contexto

Esta historia completa la implementación de todos los tipos de commit según la especificación de Conventional Commits. Los comandos especializados (`perf`, `ci`, `build`) son menos comunes que los básicos pero son importantes para equipos que siguen estrictamente la especificación.

Como parte de la épica "Adecuación de código a arquitectura", estos comandos siguen el mismo patrón establecido pero representan tipos de commit más específicos que requieren un entendimiento más profundo del contexto del desarrollo.

La implementación debe seguir la metodología TDD para asegurar que cada comando esté completamente probado y funcional, manteniendo la consistencia con los comandos básicos implementados en STORY-1.2.5.1.

## 💡 Propuesta de Resolución

Se propone implementar los 3 comandos de Conventional Commits especializados siguiendo el patrón establecido:

1. **Reutilización de `CommitCommand`**: Cada comando utilizará `CommitCommand` con el tipo específico correspondiente
2. **Estructura consistente**: Todos los comandos seguirán el patrón `BaseCommand` + `Click` establecido
3. **Test-Driven Development**: Implementación guiada por tests, escribiendo tests antes que el código
4. **Validación de mensajes**: Integración con el sistema de validación existente
5. **Soporte para scope**: Mantener la funcionalidad de scope opcional
6. **Soporte para amend**: Mantener la funcionalidad de amend

**Patrón de implementación**:
```python
class PerfCommand(BaseCommand):
    def execute(self, message, scope=None, ai=False, amend=False):
        commit_cmd = CommitCommand("perf")
        return commit_cmd.execute(message, scope, amend)
```

**Metodología TDD**:
1. Escribir test que falle (Red)
2. Escribir código mínimo para que pase (Green)
3. Refactorizar manteniendo tests verdes (Refactor)
4. Repetir para cada funcionalidad

**Consideraciones especiales**:
- Los comandos especializados pueden requerir validaciones adicionales específicas del contexto
- `ggperf` debe validar que realmente se trate de mejoras de rendimiento
- `ggci` debe validar que se trate de cambios en CI/CD
- `ggbuild` debe validar que se trate de cambios en sistema de build

## 📦 Artefactos

- 📦 Código fuente de los 3 comandos: `ggperf.py`, `ggci.py`, `ggbuild.py`
- 📦 Tests unitarios completos para cada comando con cobertura > 90%
- 📦 Tests de integración verificando flujos completos de cada comando
- 📦 Tests específicos para validaciones de contexto de cada tipo de commit
- 📦 Documentación de uso actualizada en architecture.md
- 📦 Validación de que todos los comandos siguen el patrón arquitectónico establecido

## 🔍 Criterios de Aceptación

### Funcionalidad básica:
- Dado que un usuario ejecuta `ggperf "optimizar algoritmo de búsqueda"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe crear un commit con mensaje `perf: optimizar algoritmo de búsqueda`

### Soporte para scope:
- Dado que un usuario ejecuta `ggci -s pipeline "actualizar configuración"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe crear un commit con mensaje `ci(pipeline): actualizar configuración`

### Soporte para amend:
- Dado que un usuario ejecuta `ggbuild -a "corregir script de build"`
- Cuando el comando se ejecuta exitosamente
- Entonces debe modificar el último commit con el nuevo mensaje

### Validación de mensaje:
- Dado que un usuario ejecuta `ggperf ""`
- Cuando el comando se ejecuta
- Entonces debe mostrar error de validación y no crear commit

### Validación de contexto (opcional):
- Dado que un usuario ejecuta `ggperf "agregar nueva funcionalidad"`
- Cuando el comando se ejecuta
- Entonces puede mostrar advertencia sobre el contexto del mensaje

### Cobertura de código:
- Dado que se implementan 3 comandos nuevos
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

### Compatibilidad con especificación:
- Dado que se implementan comandos especializados
- Cuando se ejecuten los comandos
- Entonces deben generar mensajes compatibles con la especificación de Conventional Commits

## 🔗 Dependencias y Recursos

### Dependencias

- STORY-1.2.5.1 debe estar completada (comandos básicos implementados)
- La implementación de `BaseCommand` y `CommitCommand` debe estar completa y funcional
- El sistema de validación de mensajes debe estar implementado
- El sistema de configuración jerárquica debe estar funcionando
- Los tests de comandos básicos deben estar pasando para validar el patrón

### Recursos

- Acceso al código fuente existente en `src/commands/` y `src/core/`
- Framework de testing pytest configurado y funcionando
- Sistema de configuración jerárquica operativo
- Repositorio Git para testing de comandos
- Documentación de Conventional Commits para validación de tipos especializados
- Ejemplos de commits especializados para testing
