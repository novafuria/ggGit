# [HISTORIA] - Corrección de Inconsistencias Reales en Abstracciones

## 🎯 Objetivo

Corregir las inconsistencias arquitectónicas reales identificadas en las abstracciones base de ggGit, específicamente la duplicación del sistema de colores y el patrón de inicialización inconsistente, para establecer una base sólida y coherente para el desarrollo futuro.

## 🌎 Contexto

Esta historia es fundamental para la épica "Adecuación del Código a la Nueva Arquitectura Documentada" ya que resuelve inconsistencias reales que impiden el uso correcto de las abstracciones definidas. Sin esta corrección, las ideas posteriores (1.2.3 - comandos base, 1.2.4 - comando de configuracion) no podrán implementarse correctamente.

Las inconsistencias identificadas son:
- **Sistema de colores duplicado**: Los comandos usan `click.echo(click.style())` directo en lugar de `ColorManager`
- **Patrón de inicialización inconsistente**: Comandos instancian componentes individualmente en lugar de usar `BaseCommand`

Referencias: [1.2.2.2 - decisiones implementacion abstracciones](.vibedoc/ideas/1.2.2.2 - decisiones implementacion abstracciones.md)

## 💡 Propuesta de Resolución

Se propone realizar un refactoring sistemático de los comandos existentes para:

1. **Unificar sistema de colores:**
   - Eliminar la clase `CLIBase` (redundante con `ColorManager`)
   - Refactorizar todos los comandos para usar `ColorManager` en lugar de `click.style()` directo
   - Actualizar `BaseCommand` para usar `ColorManager` internamente

2. **Estandarizar patrón de inicialización:**
   - Migrar comandos para usar `BaseCommand` como clase base
   - Eliminar la instanciación individual de componentes (`ConfigManager`, `GitInterface`, `ArgumentValidator`)
   - Centralizar la inicialización en `BaseCommand.__init__()`

3. **Configurar testing básico:**
   - Configurar pytest como framework de testing
   - Crear tests básicos para las abstracciones actuales
   - Configurar GitHub Actions para CI/CD

## 📦 Artefactos

- **Código fuente refactorizado**: Comandos `ggfeat.py`, `ggfix.py`, `ggbreak.py` usando `BaseCommand` y `ColorManager`
- **Clase `CLIBase` eliminada**: Archivo `src/core/cli.py` removido del proyecto
- **`BaseCommand` actualizado**: Clase base mejorada con `ColorManager` integrado
- **Tests unitarios**: Archivos de test para `ColorManager` y `BaseCommand`
- **Configuración pytest**: Archivo `pytest.ini` y estructura de tests
- **GitHub Actions**: Archivo `.github/workflows/test.yml` para CI/CD
- **Documentación actualizada**: README de `src/` con patrones de uso

## 🔍 Criterios de Aceptación

### Unificación de Sistema de Colores
- **Dado que** los comandos necesitan mostrar mensajes con colores
- **Cuando** se ejecute cualquier comando
- **Entonces** debe usar `ColorManager` en lugar de `click.style()` directo

### Patrón de Inicialización Consistente
- **Dado que** los comandos necesitan acceso a abstracciones comunes
- **Cuando** se implemente un nuevo comando
- **Entonces** debe extender `BaseCommand` y usar los componentes centralizados

### Testing Básico
- **Dado que** las abstracciones son críticas para el funcionamiento
- **Cuando** se ejecuten las pruebas unitarias
- **Entonces** debe haber al menos 60% de cobertura en `ColorManager` y `BaseCommand`

### Eliminación de Duplicación
- **Dado que** existe duplicación en el sistema de colores
- **Cuando** se complete el refactoring
- **Entonces** no debe existir código duplicado entre `CLIBase` y `ColorManager`

## 🔗 Dependencias y Recursos

### Dependencias

- **Decisión de abstracciones**: Las decisiones sobre abstracciones deben estar consensuadas (completada en zettel 1.2.2.2)
- **Estructura de directorios**: La estructura `src/core/` y `src/commands/` debe estar implementada (completada)
- **Abstracciones base**: Las clases `ColorManager` y `BaseCommand` deben existir (completada)

### Recursos

- **Desarrollador Python**: Experiencia en refactoring y testing en Python
- **Conocimiento de Click**: Comprensión de la biblioteca Click para CLI
- **Entorno de testing**: Acceso a Python 3.12 y pytest
- **GitHub Actions**: Acceso a configuración de CI/CD en el repositorio
