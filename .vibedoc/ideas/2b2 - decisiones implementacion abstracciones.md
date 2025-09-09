# Decisiones: Implementación de Abstracciones

## Contexto
Este zettel documenta las decisiones consensuadas para la implementación de abstracciones basadas en el análisis de la idea [1.2.2 - implementacion de abstracciones](1.2.2 - implementacion de abstracciones.md).

## Decisiones Técnicas

### 1. Validación de Esquemas YAML
**Decisión:** Usar PyYAML + jsonschema
- **PyYAML** para cargar archivos YAML
- **jsonschema** para validar contra esquemas en `config/`
- Mantener esquemas existentes en `config-schema.yaml` y `commit-schema.yaml`

### 2. Integración con Git
**Decisión:** Usar subprocess (no GitPython)
**Justificación:**
- Mantiene compatibilidad con mensajes de error originales de Git
- Sin dependencias adicionales
- Control total sobre la ejecución
- Consistente con la filosofía de ggGit original

**Manejo de errores:**
- Capturar stderr y stdout de subprocess
- Preservar mensajes de error originales de Git
- Mapear códigos de salida a códigos de error estándar de ggGit

### 3. Framework de Testing
**Decisión:** pytest + TDD
- **pytest** como framework principal
- Integración con GitHub Actions
- Implementar TDD para nuevas funcionalidades
- Cobertura de código objetivo: 80%

### 4. Resolución de Inconsistencias Arquitectónicas

#### 4.1 Unificación de Sistema de Colores
**Problema:** Los comandos usan directamente `click.echo(click.style())` en lugar de las abstracciones
**Decisión:** 
- Mantener solo `ColorManager` con métodos estáticos
- Eliminar `CLIBase` (redundante con ColorManager)
- Refactorizar comandos para usar `ColorManager` en lugar de `click.style()` directo

#### 4.2 Patrón de Inicialización
**Problema:** Comandos instancian componentes individualmente en lugar de usar `BaseCommand`
**Decisión:**
- Refactorizar comandos para usar `BaseCommand` como base
- Centralizar inicialización en `BaseCommand.__init__()`
- Comandos específicos solo implementan `execute()`

#### 4.3 Implementaciones Pendientes (se resolverán en ideas posteriores)
**Nota:** Las siguientes "inconsistencias" son en realidad implementaciones pendientes:
- `ConfigManager` vacío → Se implementará en **1.2.4 - comando de configuracion**
- `GitInterface` vacío → Se implementará en **1.2.3 - comandos base**
- `LoggingManager` no usado → Se implementará en **1.2.3 - comandos base**
- `CommitCommand.execute()` vacío → Se implementará en **1.2.3 - comandos base**

## Estrategia de Implementación

### Fase 1: Corrección de Inconsistencias Reales (3-5 días)
1. **Unificar sistema de colores:**
   - Eliminar `CLIBase` (redundante)
   - Refactorizar comandos para usar `ColorManager` en lugar de `click.style()` directo
   - Actualizar `BaseCommand` para usar `ColorManager`

2. **Refactorizar patrón de inicialización:**
   - Migrar comandos para usar `BaseCommand` como base
   - Eliminar instanciación individual de componentes
   - Centralizar inicialización en `BaseCommand.__init__()`

### Fase 2: Preparación para Ideas Posteriores (2-3 días)
1. **Estructura base sólida:**
   - Asegurar que `BaseCommand` esté bien diseñado
   - Preparar interfaces para futuras implementaciones
   - Documentar patrones de uso

2. **Testing básico:**
   - Configurar pytest
   - Tests para las abstracciones actuales
   - GitHub Actions básico

### Nota sobre Implementaciones Pendientes
Las siguientes funcionalidades se implementarán en ideas posteriores según el plan original:
- **1.2.3 - comandos base**: `GitInterface`, `LoggingManager`, `CommitCommand.execute()`
- **1.2.4 - comando de configuracion**: `ConfigManager` funcional
- **1.2.5 - comandos especificos**: Integración completa con abstracciones

## Criterios de Éxito

### Funcionales (para esta idea)
- [ ] Comandos usan `ColorManager` en lugar de `click.style()` directo
- [ ] Comandos usan `BaseCommand` como base
- [ ] Sistema de colores unificado y consistente
- [ ] Patrón de inicialización consistente

### Técnicos (para esta idea)
- [ ] pytest configurado y funcionando
- [ ] Tests básicos para abstracciones actuales
- [ ] GitHub Actions configurado
- [ ] Sin código duplicado en sistema de colores

### Arquitecturales (para esta idea)
- [ ] `CLIBase` eliminado (redundante)
- [ ] `ColorManager` como única fuente de colores
- [ ] `BaseCommand` como base para todos los comandos
- [ ] Interfaces preparadas para futuras implementaciones

### Pendientes para Ideas Posteriores
- [ ] `ConfigManager` funcional (1.2.4)
- [ ] `GitInterface` funcional (1.2.3)
- [ ] `LoggingManager` integrado (1.2.3)
- [ ] `CommitCommand.execute()` funcional (1.2.3)

## Próximos Pasos

1. **Aprobar decisiones** con el equipo
2. **Crear planificación detallada** en carpeta `planning/`
3. **Implementar Fase 1** - Corrección de inconsistencias
4. **Seguir metodología TDD** para nuevas funcionalidades
5. **Integrar con GitHub Actions** para CI/CD

## Consideraciones Adicionales

### Dependencias
- Agregar `jsonschema` a `environment.yml`
- Mantener `PyYAML` como dependencia principal
- No agregar `GitPython` (usar subprocess)

### Compatibilidad
- Preservar comportamiento de ggGit original
- Mantener mensajes de error familiares para usuarios
- Asegurar compatibilidad con scripts existentes

### Mantenibilidad
- Documentar patrones de uso de abstracciones
- Crear ejemplos de implementación de comandos
- Establecer guías de contribución claras
