# [EPICA] - Adecuación del Código a la Nueva Arquitectura Documentada

## 🎯 Objetivo de la Épica

Reconstruir el código inicial de ggGit para alinearlo con la documentación de arquitectura creada mediante Vibedoc, migrando de la implementación actual en Bash a una arquitectura Python moderna, modular y bien estructurada.

## 🌎 Contexto y Justificación

Actualmente existe una implementación funcional de ggGit en Bash que cumple con las funcionalidades básicas, pero presenta limitaciones significativas para el mantenimiento y evolución del producto. Tras la incorporación de Vibedoc, se generó una documentación completa que define una nueva arquitectura, objetivos diferentes y una visión más amplia del producto.

La brecha entre la documentación (que refleja la nueva visión) y el código existente (que mantiene la implementación original) representa un riesgo para la sostenibilidad del proyecto. Esta épica busca cerrar esa brecha, transformando ggGit en un producto que refleje fielmente la arquitectura documentada.

La migración a Python permitirá aprovechar las capacidades de IA integradas, mejorar la mantenibilidad del código, facilitar el testing y crear una base sólida para futuras funcionalidades.

## 💡 Visión de la Solución

Se implementará una arquitectura Python unificada que siga la estructura de directorios definida en las decisiones tomadas (src/core/ para abstracciones, src/commands/ para ejecutables). La solución incluirá:

- **Estructura de directorios coherente**: Implementación de la estructura src/core/ y src/commands/ definida en las decisiones
- **Abstracciones reutilizables**: Módulos core para configuración, Git, validación y utilidades
- **Comandos independientes**: Scripts Python ejecutables que reutilizan las abstracciones comunes
- **Sistema de configuración jerárquica**: Implementación del ConfigManager con prioridad repositorio > módulo > usuario > default
- **Integración con IA**: Base para funcionalidades de IA integradas en comandos existentes
- **Testing y CI/CD**: Estructura de pruebas unitarias y integración con GitHub Actions

## 🚀 Alcance de la Épica

### Debe Tener

- ✅ **Estructura de directorios Python**: Implementación completa de la estructura src/core/ y src/commands/ definida en las decisiones
- ✅ **Abstracciones base**: Implementación de ConfigManager, GitInterface, ArgumentValidator y BaseCommand
- ✅ **Utilidades core**: Sistema de colores y logging unificado
- ✅ **Comandos base**: Implementación de comandos base reutilizables (base.py, commit.py, config.py)
- ✅ **Comando de configuración**: Implementación del comando ggconfig para gestión de configuración
- ✅ **Comandos específicos básicos**: Implementación de ggfeat, ggfix, ggbreak como prueba de concepto
- ✅ **Sistema de testing**: Estructura de pruebas unitarias y configuración de GitHub Actions
- ✅ **Scripts de instalación**: Actualización de install.sh e install.ps1 para la nueva estructura

### Podría Tener

- ✨ **Comandos específicos completos**: Implementación de todos los comandos específicos (ggdocs, ggstyle, etc.)
- ✨ **Integración con IA**: Implementación básica de funcionalidades de IA en comandos existentes
- ✨ **Comando ggai**: Implementación del comando conversacional con IA
- ✨ **Sistema de plugins**: Arquitectura extensible para comandos adicionales
- ✨ **Documentación interactiva**: Comando de ayuda mejorado con ejemplos

## Fuera de Alcance

- 🚫 **Interfaz gráfica**: La herramienta seguirá siendo exclusivamente de línea de comandos
- 🚫 **Gestión de repositorios remotos**: No incluirá funcionalidades de GitHub, GitLab, etc. más allá de push/pull
- 🚫 **Backup automático**: No incluirá funcionalidades de respaldo de repositorios
- 🚫 **Integración con sistemas de CI/CD**: No automatizará pipelines de integración continua
- 🚫 **Gestión de dependencias**: No manejará paquetes o dependencias del proyecto
- 🚫 **Soporte para otros VCS**: Solo Git, no Mercurial, SVN, etc.

## ⚠️ Riesgos y Supuestos

### Riesgos Identificados

- ❗ **Complejidad de migración**: La migración de Bash a Python podría introducir bugs o comportamientos diferentes
- ❗ **Pérdida de funcionalidad**: Riesgo de no replicar exactamente el comportamiento de la implementación actual
- ❗ **Resistencia al cambio**: Los usuarios podrían preferir la implementación actual en Bash
- ❗ **Dependencias de Python**: Nuevas dependencias podrían complicar la instalación
- ❗ **Curva de aprendizaje**: El equipo podría necesitar tiempo para adaptarse a la nueva arquitectura

### Supuestos Clave

- ❓ **Compatibilidad de Python**: Asumimos que Python 3.8+ estará disponible en los entornos objetivo
- ❓ **Estabilidad de Git**: Asumimos que la API de Git se mantendrá estable durante la migración
- ❓ **Adopción del equipo**: Asumimos que el equipo estará dispuesto a adoptar la nueva implementación
- ❓ **Recursos de desarrollo**: Asumimos que habrá tiempo suficiente para completar la migración
- ❓ **Funcionalidad equivalente**: Asumimos que es posible replicar toda la funcionalidad actual en Python

## 🔗 Dependencias y Recursos Clave

### Dependencias

- **Decisión de estructura**: La estructura de directorios debe estar definida y documentada (completada en zettel 1.2.1.1)
- **Documentación de arquitectura**: La arquitectura debe estar actualizada y coherente (completada)
- **Implementación actual**: La implementación en Bash debe estar documentada para referencia
- **Entorno de desarrollo**: Python 3.8+ y Git deben estar disponibles

### Recursos Clave Necesarios

- **Desarrollador Python**: Experiencia en desarrollo de herramientas CLI en Python
- **Conocimiento de Git**: Comprensión profunda de la API de Git y sus comandos
- **Entorno de testing**: Acceso a diferentes sistemas operativos para testing cross-platform
- **Documentación de referencia**: Acceso a la implementación actual en Bash para comparación
