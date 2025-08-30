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

Desarrollar y mantener una suite de comandos de línea de comandos que simplifique y acelere el trabajo con Git, con especial énfasis en la implementación y uso de Conventional Commits. El objetivo es reducir el tiempo de desarrollo dedicado a operaciones Git repetitivas y aumentar la adopción de Conventional Commits en equipos de desarrollo.

## 📖 Contexto

Actualmente, los desarrolladores dedican una cantidad significativa de tiempo a escribir comandos Git verbosos y recordar la sintaxis correcta para Conventional Commits. Esto resulta en:

- **Pérdida de productividad**: Comandos Git largos y repetitivos que ralentizan el flujo de trabajo
- **Inconsistencia en commits**: Diferentes formatos de mensajes entre desarrolladores del mismo equipo
- **Curva de aprendizaje**: Nuevos desarrolladores deben aprender tanto Git como Conventional Commits desde cero
- **Errores frecuentes**: Sintaxis incorrecta en commits que rompe la consistencia del historial

La competencia actual se limita principalmente a alias básicos de Git o herramientas que no están específicamente diseñadas para Conventional Commits. ggGit busca llenar este vacío proporcionando una experiencia unificada y optimizada.

## 🔮 Visión de la Solución

Se propone crear una suite de comandos cortos, mnemotécnicos y cross-platform que transforme la experiencia de trabajo con Git. La solución incluirá:

- **Comandos abreviados**: Transformación de comandos Git verbosos en comandos cortos y fáciles de recordar
- **Automatización de Conventional Commits**: Generación automática de mensajes de commit siguiendo la especificación de Conventional Commits
- **Feedback visual mejorado**: Salidas coloridas y estructuradas que faciliten la comprensión del estado del repositorio
- **Instalación automática**: Scripts de instalación que configuren automáticamente el PATH y permisos en diferentes sistemas operativos
- **Consistencia cross-platform**: Funcionamiento idéntico en Linux, macOS y Windows

La herramienta se integrará perfectamente en el flujo de trabajo existente de los desarrolladores, proporcionando una capa de abstracción que simplifica Git sin ocultar su funcionalidad.

## 📐 Alcance

### ✅ Debe Tener

- **Comandos básicos de Git**: `gga` (add), `ggs` (status), `ggl` (log), `ggdif` (diff), `ggunstage`, `ggreset`
- **Gestión de ramas**: `ggmain`, `ggmaster`, `ggmerge`
- **Operaciones remotas**: `ggpl` (pull), `ggpp` (push)
- **Conventional Commits**: `ggfeat`, `ggfix`, `ggbreak` con soporte para scope
- **Información del sistema**: `ggv` (version), `ggconfig`
- **Instalación automática**: Scripts para Linux/macOS (`install.sh`) y Windows (`install.ps1`)
- **Soporte cross-platform**: Funcionamiento en Bash (Linux/macOS) y PowerShell (Windows)
- **Integración con PATH**: Configuración automática de variables de entorno

### 🤔 Podría Tener

- **Sistema de alias personalizables**: Permitir a los usuarios definir sus propios comandos abreviados
- **Templates de commit personalizables**: Configuración de formatos de commit específicos por proyecto
- **Integración con hooks de Git**: Automatización de validaciones de Conventional Commits
- **Sistema de plugins**: Arquitectura extensible para comandos adicionales
- **Documentación interactiva**: Comando de ayuda que muestre ejemplos de uso
- **Validación de mensajes**: Verificación automática del formato de Conventional Commits antes del commit
- **Integración con IDEs**: Extensiones para VSCode, IntelliJ, etc.
- **Sistema de autenticación**: No manejará credenciales o tokens de acceso para herramientas de IA.

### ❌ Fuera de Alcance

- **Interfaz gráfica**: La herramienta será exclusivamente de línea de comandos
- **Gestión de repositorios remotos**: No incluirá funcionalidades de GitHub, GitLab, etc. más allá de push/pull
- **Backup automático**: No incluirá funcionalidades de respaldo de repositorios
- **Integración con sistemas de CI/CD**: No automatizará pipelines de integración continua
- **Gestión de dependencias**: No manejará paquetes o dependencias del proyecto
- **Soporte para otros VCS**: Solo Git, no Mercurial, SVN, etc.

## ⚠️ Riesgos y Supuestos

### 🚨 Riesgos

- **Cambios en la API de Git**: Las nuevas versiones de Git podrían introducir cambios que rompan la funcionalidad de ggGit
- **Incompatibilidades de shell**: Diferentes versiones de Bash o PowerShell podrían comportarse de manera diferente
- **Resistencia al cambio**: Los desarrolladores podrían preferir usar comandos Git nativos por costumbre
- **Fragmentación de la comunidad**: Diferentes forks podrían crear confusión sobre cuál es la versión "oficial"
- **Dependencia de Git**: Si Git cambia drásticamente, ggGit podría requerir reescrituras significativas

### 🤷 Supuestos

- **Git seguirá siendo el VCS dominante**: Se asume que Git mantendrá su posición de liderazgo en el mercado
- **Conventional Commits seguirán siendo estándar**: Se asume que la especificación de Conventional Commits se mantendrá estable
- **Compatibilidad de shells**: Se asume que Bash y PowerShell mantendrán compatibilidad hacia atrás
- **Adopción del equipo**: Se asume que los equipos de desarrollo estarán dispuestos a adoptar nuevas herramientas
- **Recursos de mantenimiento**: Se asume que habrá recursos disponibles para mantener y actualizar la herramienta

## 🔑 Recursos Clave

- **Especificación de Conventional Commits**: https://www.conventionalcommits.org/
- **Documentación oficial de Git**: https://git-scm.com/doc
