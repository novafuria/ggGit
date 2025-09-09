# 1.2.3.1 - Patrones de Manejo de Errores para GitInterface

## Decisión Arquitectónica

**Fecha**: 2024-12-19
**Historia**: STORY-1.2.3.1-implementacion-gitinterface-basico
**Contexto**: Implementación de GitInterface básico para comandos ggfeat, ggfix y ggbreak

## Problema

La arquitectura no especifica patrones específicos para el manejo de errores en GitInterface, pero los criterios de aceptación requieren:
- Manejo de errores con subprocess.CalledProcessError
- Validación de que Git esté disponible en el sistema
- Mensajes de error descriptivos y accionables

## Decisión Tomada

Implementar patrones estándar de Python para subprocess con excepciones personalizadas:

### 1. Excepciones Personalizadas
```python
class GitInterfaceError(Exception):
    """Excepción base para errores de GitInterface"""
    pass

class GitNotAvailableError(GitInterfaceError):
    """Git no está disponible en el sistema"""
    pass

class NotGitRepositoryError(GitInterfaceError):
    """No es un repositorio Git válido"""
    pass

class GitCommandError(GitInterfaceError):
    """Error al ejecutar comando Git"""
    pass
```

### 2. Manejo de subprocess.CalledProcessError
- Capturar `subprocess.CalledProcessError` en cada método
- Convertir a excepciones específicas con contexto
- Incluir comando ejecutado y código de salida en el mensaje

### 3. Validación de Git Disponible
- Verificar que `git` esté en PATH al inicializar GitInterface
- Lanzar `GitNotAvailableError` si no está disponible

### 4. Mensajes Descriptivos y Accionables
- Incluir comando ejecutado en mensajes de error
- Sugerir acciones correctivas cuando sea posible
- Mantener consistencia con el patrón de la arquitectura

## Justificación

- **Consistencia**: Sigue patrones estándar de Python
- **Trazabilidad**: Excepciones específicas permiten mejor debugging
- **Usabilidad**: Mensajes descriptivos ayudan al usuario
- **Mantenibilidad**: Patrón claro y documentado para futuras implementaciones

## Impacto

Esta decisión establece el patrón base para:
- Todos los métodos de GitInterface
- Futuras implementaciones de interfaces con sistemas externos
- Manejo de errores en otros componentes core

## Referencias

- [STORY-1.2.3.1-implementacion-gitinterface-basico.md](../planning/iniciatives/INI-1-adopcion-vibedoc-gggit/epics/EPIC-1.2-adecuacion-codigo-arquitectura/stories/STORY-1.2.3.1-implementacion-gitinterface-basico.md)
- [architecture.md](../architecture.md)
- [1.2.3 - comandos base.md](1.2.3%20-%20comandos%20base.md)
