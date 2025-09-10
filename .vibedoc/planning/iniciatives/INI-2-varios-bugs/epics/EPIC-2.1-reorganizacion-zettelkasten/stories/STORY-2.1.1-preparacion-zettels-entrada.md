# [HISTORIA] - Preparación Zettels de Entrada

## 🎯 Objetivo

Crear los 13 zettels de entrada basados en la arquitectura documentada y generar el script completo de migración hardcodeado para revisión manual, estableciendo la base para la reorganización del zettelkasten.

## 🌎 Contexto

Esta historia implementa la Fase 1 del plan de reorganización documentado en [4.1 - decisiones reorganizacion estructura zettelkasten](../../../ideas/4.1 - decisiones reorganizacion estructura zettelkasten.md). Es la historia fundamental que establece la nueva estructura antes de migrar el contenido existente.

La creación de zettels de entrada con `touch` no generará conflictos con nombres existentes, ya que la numeración actual usa formato decimal (1.2.3) mientras que la nueva usa formato simple (1, 2, 3).

## 💡 Propuesta de Resolución

Se propone crear una rama de trabajo específica y generar los 13 zettels de entrada usando comandos `touch` simples. Cada zettel de entrada contendrá una descripción básica del sistema correspondiente según la arquitectura documentada. Simultáneamente, se generará un script de migración completo con todos los comandos `mv` hardcodeados para revisión posterior.

## 📦 Artefactos

- **Rama de trabajo**: `feature/reorganizacion-zettelkasten` creada y configurada
- **13 Zettels de entrada**: Archivos creados con contenido básico descriptivo
  - `1 - vibedoc.md`
  - `2 - arquitectura unificada en python.md`
  - `3 - sistema de comandos independientes.md`
  - `4 - sistema de configuracion jerarquica.md`
  - `5 - sistema de interfaz de usuario cli.md`
  - `6 - sistema de instalacion y distribucion.md`
  - `7 - sistema de validacion y esquemas.md`
  - `8 - sistema de integracion con git.md`
  - `9 - sistema de ia para generacion de commits.md`
  - `10 - sistema de observabilidad y logging.md`
  - `11 - sistema de testing y calidad.md`
  - `12 - integraciones con terceros.md`
  - `13 - varios bugs.md`
- **Script de migración**: `migrate_zettelkasten.sh` con lista completa hardcodeada de comandos `mv`

## 🔍 Criterios de Aceptación

### Rama de Trabajo Preparada
- Dado que necesitamos aislar la reorganización del trabajo principal
- Cuando se cree la rama `feature/reorganizacion-zettelkasten`
- Entonces debe estar basada en la rama actual y sin conflictos

### Zettels de Entrada Creados
- Dado que necesitamos establecer la nueva estructura
- Cuando se ejecuten los comandos `touch` para los 13 zettels de entrada
- Entonces cada archivo debe existir con contenido básico descriptivo del sistema correspondiente

### Script de Migración Generado
- Dado que necesitamos migrar 75+ archivos de forma controlada
- Cuando se genere el script de migración
- Entonces debe contener todos los comandos `mv` hardcodeados con origen y destino correctos

### Sin Conflictos de Nombres
- Dado que la numeración actual es diferente a la nueva
- Cuando se creen los zettels de entrada
- Entonces no debe haber conflictos con archivos existentes

## 🔗 Dependencias y Recursos

### Dependencias

- **Decisiones aprobadas**: Zettel 4.1 con decisiones de reorganización validadas
- **Arquitectura estable**: Documento `architecture.md` sin cambios pendientes
- **Repositorio limpio**: Working directory sin cambios sin commitear

### Recursos

- **Acceso al repositorio**: Permisos para crear ramas y archivos
- **Lista completa de archivos**: Inventario de todos los zettels existentes para migración
- **Tiempo dedicado**: Aproximadamente 2 horas para preparación completa
