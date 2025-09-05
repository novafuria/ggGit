# [project] - ggGit

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [\[project\] - ggGit](#project---gggit)
  - [🎯 Objetivo](#-objetivo)
  - [📖 Contexto](#-contexto)
  - [🔮 Visión de la Solución](#-visión-de-la-solución)
  - [📐 Alcance](#-alcance)
    - [✅ Debe Tener](#-debe-tener)
    - [🤔 Podría Tener](#-podría-tener)
    - [❌ Fuera de Alcance](#-fuera-de-alcance)
  - [⚠️ Riesgos y Supuestos](#️-riesgos-y-supuestos)
    - [🚨 Riesgos](#-riesgos)
    - [🤷 Supuestos](#-supuestos)
  - [🔑 Recursos Clave](#-recursos-clave)

## 🎯 Objetivo

Desarrollar y mantener una suite de 26 comandos Python independientes que simplifique y acelere el trabajo con Git, con especial énfasis en la implementación y uso de Conventional Commits e integración de inteligencia artificial. El objetivo es reducir el tiempo de desarrollo dedicado a operaciones Git repetitivas, aumentar la adopción de Conventional Commits en equipos de desarrollo, y proporcionar generación automática de mensajes de commit usando IA con análisis de complejidad y tracking de uso.

## 📖 Contexto

Actualmente, los desarrolladores dedican una cantidad significativa de tiempo a escribir comandos Git verbosos y recordar la sintaxis correcta para Conventional Commits. Esto resulta en:

- **Pérdida de productividad**: Comandos Git largos y repetitivos que ralentizan el flujo de trabajo
- **Inconsistencia en commits**: Diferentes formatos de mensajes entre desarrolladores del mismo equipo
- **Curva de aprendizaje**: Nuevos desarrolladores deben aprender tanto Git como Conventional Commits desde cero
- **Errores frecuentes**: Sintaxis incorrecta en commits que rompe la consistencia del historial
- **Generación manual de mensajes**: Escribir mensajes de commit descriptivos consume tiempo valioso de desarrollo
- **Falta de herramientas de IA**: No hay herramientas integradas que analicen cambios automáticamente y sugieran mensajes de commit inteligentes
- **Resistencia cultural a la consola**: Muchos desarrolladores prefieren herramientas gráficas pero necesitan la potencia de la línea de comandos

La competencia actual se limita principalmente a alias básicos de Git, herramientas gráficas que no se integran bien con terminales, o herramientas de IA que están atadas a IDEs específicos. ggGit busca llenar este vacío proporcionando una experiencia unificada y optimizada con 26 comandos Python independientes, sistema de configuración jerárquica, e integración de IA para generación automática de mensajes de commit.

## 🔮 Visión de la Solución

Se propone crear una suite de 26 comandos Python independientes, mnemotécnicos y cross-platform que transforme la experiencia de trabajo con Git. La solución incluirá:

- **26 Comandos Python Independientes**: Suite completa de comandos ejecutables independientes implementados en Python para consistencia y mantenimiento
- **Comandos abreviados**: Transformación de comandos Git verbosos en comandos cortos y fáciles de recordar
- **Sistema de Configuración Jerárquica**: Configuraciones locales por contexto (repositorio > módulo > usuario > default) con validación JSON Schema
- **Sistema de IA Integrado**: Inteligencia artificial integrada para generación automática de mensajes de commit con análisis de complejidad
- **Análisis Inteligente**: Evaluación automática de complejidad de cambios para decidir entre IA y fallback educativo
- **Tracking de Uso de IA**: Monitoreo de consumo de IA, costos y límites para control de gastos
- **Feedback visual mejorado**: Salidas coloridas y estructuradas que faciliten la comprensión del estado del repositorio
- **Instalación automática**: Scripts de instalación Python que configuren automáticamente aliases y variables de entorno
- **Consistencia cross-platform**: Funcionamiento idéntico en Linux, macOS y Windows

La herramienta se integrará perfectamente en el flujo de trabajo existente de los desarrolladores, proporcionando una capa de abstracción que simplifica Git sin ocultar su funcionalidad. ggGit incluye capacidades de IA integradas que analizan automáticamente los cambios y sugieren mensajes de commit inteligentes, con análisis de complejidad que decide cuándo usar IA y cuándo proporcionar feedback educativo, similar a las funcionalidades de autocompletado de los IDEs modernos pero con la flexibilidad de la línea de comandos.

## 📐 Alcance

### ✅ Debe Tener

- **26 Comandos Python Independientes**: Suite completa de comandos ejecutables independientes
- **Comandos básicos de Git**: `gga` (add), `ggs` (status), `ggl` (log), `ggdif` (diff), `ggunstage`, `ggreset`
- **Gestión de ramas**: `ggmain`, `ggdevelop`, `ggb`, `ggmerge` con selección interactiva
- **Operaciones remotas**: `ggpl` (pull), `ggpp` (push)
- **Conventional Commits**: `ggfeat`, `ggfix`, `ggdocs`, `ggstyle`, `ggchore`, `ggbuild`, `ggci`, `ggperf`, `ggtest`, `ggbreak` con soporte para scope
- **Sistema de IA Integrado**: `ggai` con subcomandos para generación, uso y testing
- **Información del sistema**: `ggv` (version), `ggconfig` con gestión jerárquica
- **Instalación automática**: Scripts Python para Linux/macOS (`install.py`) y Windows (`install.ps1`)
- **Soporte cross-platform**: Funcionamiento en Python en Linux, macOS y Windows
- **Sistema de aliases**: Configuración automática de aliases y variables de entorno
- **Sistema de configuración jerárquica**: Configuraciones locales por contexto (repositorio > módulo > usuario > default) con validación JSON Schema
- **Análisis de complejidad**: Evaluación automática de cambios para decidir entre IA y fallback educativo
- **Tracking de uso de IA**: Monitoreo de consumo de IA, costos y límites

### 🤔 Podría Tener

- **Sistema de plugins**: Arquitectura extensible para comandos adicionales
- **Documentación interactiva**: Comando de ayuda que muestre ejemplos de uso
- **Validación en la nube**: Verificación del formato de Conventional Commits en CI/CD y pull requests
- **Integración con IDEs**: Extensiones para VSCode, IntelliJ, etc.
- **Sistema de autenticación**: No manejará credenciales o tokens de acceso para herramientas de IA
- **Configuraciones avanzadas de IA**: Límites de costo personalizables por proyecto, modelos específicos por contexto
- **Análisis de complejidad avanzado**: Criterios personalizables para decidir cuándo usar IA
- **Integración con más proveedores de IA**: Soporte para modelos locales adicionales, APIs empresariales
- **Métricas de productividad**: Análisis de uso de comandos y mejora de productividad del equipo
- **Sistema de notificaciones**: Alertas sobre límites de costo de IA, actualizaciones de configuración

### ❌ Fuera de Alcance

- **Interfaz gráfica**: La herramienta será exclusivamente de línea de comandos
- **Gestión de repositorios remotos**: No incluirá funcionalidades de GitHub, GitLab, etc. más allá de push/pull
- **Backup automático**: No incluirá funcionalidades de respaldo de repositorios
- **Integración con sistemas de CI/CD**: No automatizará pipelines de integración continua
- **Gestión de dependencias**: No manejará paquetes o dependencias del proyecto
- **Soporte para otros VCS**: Solo Git, no Mercurial, SVN, etc.
- **Modelos de IA propietarios**: No incluirá modelos de IA propietarios o entrenados específicamente para ggGit
- **Sincronización automática de configuraciones**: Las configuraciones se mantienen locales sin sincronización automática
- **Gestión de credenciales**: No manejará credenciales de IA, solo variables de entorno

## ⚠️ Riesgos y Supuestos

### 🚨 Riesgos

- **Cambios en la API de Git**: Las nuevas versiones de Git podrían introducir cambios que rompan la funcionalidad de ggGit
- **Incompatibilidades de shell**: Diferentes versiones de Bash o PowerShell podrían comportarse de manera diferente
- **Resistencia al cambio**: Los desarrolladores podrían preferir usar comandos Git nativos por costumbre
- **Fragmentación de la comunidad**: Diferentes forks podrían crear confusión sobre cuál es la versión "oficial"
- **Dependencia de Git**: Si Git cambia drásticamente, ggGit podría requerir reescrituras significativas
- **Costos de IA**: Los servicios de IA pueden ser costosos y los límites de costo pueden no ser suficientes
- **Disponibilidad de IA**: Los servicios de IA pueden tener interrupciones o cambios en sus APIs
- **Complejidad de configuración**: El sistema de configuración jerárquica puede ser complejo para usuarios nuevos
- **Dependencia de Python**: Cambios en Python o sus dependencias pueden afectar la funcionalidad

### 🤷 Supuestos

- **Git seguirá siendo el VCS dominante**: Se asume que Git mantendrá su posición de liderazgo en el mercado
- **Conventional Commits seguirán siendo estándar**: Se asume que la especificación de Conventional Commits se mantendrá estable
- **Compatibilidad de shells**: Se asume que Bash y PowerShell mantendrán compatibilidad hacia atrás
- **Adopción del equipo**: Se asume que los equipos de desarrollo estarán dispuestos a adoptar nuevas herramientas
- **Recursos de mantenimiento**: Se asume que el desarrollador principal podrá mantener el proyecto como actividad personal
- **Infraestructura de Novafuria**: Se asume que la infraestructura de desarrollo seguirá disponible sin costos adicionales
- **Disponibilidad de IA**: Se asume que los servicios de IA seguirán disponibles y con precios estables
- **Adopción de IA**: Se asume que los desarrolladores estarán dispuestos a usar herramientas de IA para generar mensajes de commit
- **Compatibilidad de Python**: Se asume que Python mantendrá compatibilidad hacia atrás y estabilidad
- **Efectividad de IA**: Se asume que la IA será efectiva para generar mensajes de commit descriptivos y útiles

## 🔑 Recursos Clave

El proyecto se basa en recursos existentes y gratuitos, aprovechando la infraestructura de desarrollo disponible.

- **Especificación de Conventional Commits**: https://www.conventionalcommits.org/
- **Documentación oficial de Git**: https://git-scm.com/doc
- **Infraestructura de Novafuria**: Herramientas de desarrollo y testing existentes
- **GitHub**: Repositorio público y CI/CD gratuito para proyectos open source
- **Comunidad de desarrolladores**: Usuarios activos en equipos de trabajo y Novafuria
- **APIs de IA**: OpenAI, Anthropic, Azure OpenAI, Ollama para generación de mensajes de commit
- **Python y ecosistema**: Click, PyYAML, jsonschema, colorama para funcionalidades core
- **Metodología Vibedoc**: Documentación estructurada y metodología de desarrollo
- **Testing y CI/CD**: pytest, GitHub Actions para calidad y automatización
- **Documentación técnica**: Arquitectura, diseño de producto, perfiles de usuario actualizados
