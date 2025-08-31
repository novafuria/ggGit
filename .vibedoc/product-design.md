# [product-design] - ggGit <!-- omit in toc -->

> Este documento debe ser una continuación del documento [02-research-of-references-and-collections](02-research-of-references-and-collections.md). Consiste en la creación de un diseño de producto que resuelva el problema planteado en el documento [01-research-and-assessment-of-the-problem](01-research-and-assessment-of-the-problem.md).
> Se compone de una combinación de metodología lienzo canvas y sketch de producto funcionales con flujos bpmn simplificados.
> Permite generar ideas de solución y validar las propuestas de valor con los interesados.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Descripción general](#descripción-general)
  - [Infografía de la Propuesta de Valor](#infografía-de-la-propuesta-de-valor)
  - [Texto Descriptivo de la Propuesta de Valor](#texto-descriptivo-de-la-propuesta-de-valor)
  - [Eventos y Actividades Clave](#eventos-y-actividades-clave)
  - [Explosión de Componentes](#explosión-de-componentes)
  - [Flexibilidad de Desarrollo por Comandos Independientes](#flexibilidad-de-desarrollo-por-comandos-independientes)
  - [Distribución de Vistas y Páginas](#distribución-de-vistas-y-páginas)
- [Glosario de términos y definiciones](#glosario-de-términos-y-definiciones)
- [Contexto: Terminal de Comandos](#contexto-terminal-de-comandos)
  - [Ciclo de vida](#ciclo-de-vida)
    - [Al iniciar el contexto](#al-iniciar-el-contexto)
    - [Al pasar a segundo plano](#al-pasar-a-segundo-plano)
    - [Al volver a primer plano](#al-volver-a-primer-plano)
    - [Al volver a la aplicación](#al-volver-a-la-aplicación)
    - [Al finalizar el contexto](#al-finalizar-el-contexto)
  - [Acciones](#acciones)
    - [Ejecutar comando ggGit](#ejecutar-comando-gggit)
      - [Descripción](#descripción)
      - [Beneficios](#beneficios)
      - [Casos de uso](#casos-de-uso)
        - [Desarrollador que necesita hacer un commit rápido](#desarrollador-que-necesita-hacer-un-commit-rápido)
        - [Tech Lead que quiere estandarizar commits del equipo](#tech-lead-que-quiere-estandarizar-commits-del-equipo)
    - [Configurar ggGit](#configurar-gggit)
      - [Descripción](#descripción-1)
      - [Beneficios](#beneficios-1)
      - [Casos de uso](#casos-de-uso-1)
        - [Nuevo desarrollador que se une al proyecto](#nuevo-desarrollador-que-se-une-al-proyecto)
        - [DevOps que necesita configurar el entorno](#devops-que-necesita-configurar-el-entorno)
    - [Gestionar configuración de módulos](#gestionar-configuración-de-módulos)
      - [Descripción](#descripción-2)
      - [Beneficios](#beneficios-2)
      - [Casos de uso](#casos-de-uso-2)
        - [Equipo que actualiza estándares de commit](#equipo-que-actualiza-estándares-de-commit)
        - [Integración con CI/CD pipeline](#integración-con-cicd-pipeline)
    - [Configurar repositorio específico](#configurar-repositorio-específico)
      - [Descripción](#descripción-3)
      - [Beneficios](#beneficios-3)
      - [Casos de uso](#casos-de-uso-3)
        - [Proyecto open source con configuración única](#proyecto-open-source-con-configuración-única)
        - [Repositorio de empresa con configuraciones específicas](#repositorio-de-empresa-con-configuraciones-específicas)
  - [Flujos de procesos](#flujos-de-procesos)
    - [Flujo de proceso 1: Commit con Conventional Commits](#flujo-de-proceso-1-commit-con-conventional-commits)
    - [Flujo de proceso 2: Configuración y gestión de módulos](#flujo-de-proceso-2-configuración-y-gestión-de-módulos)
    - [Flujo de proceso 3: Integración con CI/CD](#flujo-de-proceso-3-integración-con-cicd)


## Descripción general

> Consiste en una infografía de la propuesta de valor que representa la solución de software y una descripción textual de sus elementos y relaciones. La infografía debe ser una representación visual de la propuesta de valor que incluye en su interior diferentes recursos visuales necesarios dispuestos de una forma que permita visualizar la propuesta de valor y ser comprendida por cualquier actor involucrado en el proyecto.
> La infografía incluirá:
> - Sketch o wireframes de la propuesta de valor
> - Texto descriptivo de la propuesta de valor
> - Eventos y actividades clave
> - Diagramas de flujo de procesos BPMN asociados a cada evento y actividad clave
> - Explosión de componentes
> - Glosario de términos y definiciones
> - Distribución de vistas y páginas del sistema
> - Diagramas BPMN para procesos de negocio que son cubiertos por la solución de software

### Infografía de la Propuesta de Valor

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ggGit - Suite de Comandos Git Independientes           │
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│  │   Comandos      │    │  Configuración  │    │   Sistema de    │        │
│  │   Principales   │    │   Jerárquica    │    │   Validación    │        │
│  │                 │    │                 │    │                 │        │
│  │ • ggfeat (bash)│    │ • ~/.gggit/     │    │ • Convenciones  │        │
│  │ • ggfix (bash) │    │ • Módulos por   │    │   estándar      │        │
│  │ • ggbreak (bash)│   │   contexto      │    │ • Validación    │        │
│  │ • ggmerge (bash)│   │ • Config local  │    │   en la nube    │        │
│  │ • ggconfig (py)│    │ • Módulos       │    │ • Diferentes    │        │
│  │                 │    │ • Repositorio   │    │   tecnologías   │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│           │                       │                       │                │
│           ▼                       ▼                       ▼                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Terminal de Comandos                            │   │
│  │                                                                     │   │
│  │  $ ggfeat "nueva funcionalidad de login"                          │   │
│  │  → feat: nueva funcionalidad de login                              │   │
│  │                                                                     │   │
│  │  $ ggconfig show -m work-company-a                                │   │
│  │  → Configuración del módulo empresa A                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Flujos de Proceso                               │   │
│  │                                                                     │   │
│  │  1. Commit → 2. CI/CD → 3. Validación → 4. Release                 │   │
│  │     ↓           ↓           ↓         ↓                             │   │
│  │  Conventional  Pipeline   Validación Automático                     │   │
│  │  Commits      GitHub     en la nube Changelog                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │

└─────────────────────────────────────────────────────────────────────────────┘
```

### Texto Descriptivo de la Propuesta de Valor

ggGit es una suite de comandos independientes de línea de comandos que transforma la experiencia de trabajo con Git. La solución se compone de tres pilares principales:

1. **Comandos Principales**: Una colección de comandos independientes (no alias) que simplifican operaciones Git comunes, especialmente enfocados en Conventional Commits. Cada comando puede estar implementado en diferentes tecnologías según sus necesidades específicas.

2. **Sistema de Configuración Jerárquica**: Un mecanismo local que permite configuraciones específicas por contexto, incluyendo módulos por empresa/equipo, configuración de usuario, y configuraciones específicas de repositorio (con prioridad más alta), todo basado en archivos YAML locales.

3. **Sistema de Convenciones Estandarizadas**: Un sistema que genera commits con formato estándar usando comandos optimizados, asegurando consistencia en todos los entornos de desarrollo. La validación final se realiza en la nube (CI/CD, pull requests) donde se aplican los estándares del equipo.

### Eventos y Actividades Clave

- **Commit de Código**: El desarrollador ejecuta un comando ggGit que genera automáticamente un Conventional Commit válido
- **Configuración de Equipo**: El Tech Lead define estándares en archivos YAML que se comparten con el equipo
- **Gestión de Módulos**: El sistema detecta automáticamente el contexto de trabajo y aplica configuraciones específicas
- **Integración CI/CD**: Los commits estructurados activan automáticamente pipelines de build y deploy
- **Generación de Changelog**: El sistema genera automáticamente documentación de cambios basada en el historial de commits

### Explosión de Componentes

- **CLI Commands**: Comandos independientes ejecutables que encapsulan lógica Git compleja, cada uno implementado en la tecnología más apropiada (bash, Python, etc.)
- **Configuration Manager**: Sistema local que gestiona configuraciones jerárquicas basadas en archivos YAML
- **Template Engine**: Generador de mensajes de commit basado en templates configurables
- **Validation Engine**: Motor que valida configuraciones usando esquemas YAML
- **Convention Engine**: Motor que genera commits con formato estándar siguiendo Conventional Commits
- **Module System**: Sistema que detecta automáticamente el contexto de trabajo y aplica configuraciones específicas
- **Repository System**: Sistema que maneja configuraciones específicas de repositorio con prioridad más alta

### Flexibilidad de Desarrollo por Comandos Independientes

ggGit está diseñado como una suite de comandos independientes, no como un conjunto de alias Git. Esta arquitectura proporciona varias ventajas clave:

- **Tecnologías Específicas**: Cada comando puede estar implementado en la tecnología más apropiada (bash para comandos simples, Python para validación y configuración, etc.)
- **Desarrollo Independiente**: Los comandos pueden ser desarrollados, probados y mantenidos de forma independiente
- **Instalación Flexible**: El script de instalación maneja las dependencias específicas de cada comando
- **Mantenimiento Simplificado**: Cada comando tiene su propia lógica y responsabilidades claras
- **Extensibilidad**: Nuevos comandos pueden ser agregados sin afectar la funcionalidad existente

### Distribución de Vistas y Páginas

Como herramienta de línea de comandos, ggGit no tiene interfaces gráficas tradicionales, pero se organiza en:

- **Terminal de Comandos**: Interfaz principal donde se ejecutan todos los comandos
- **Archivos de Configuración**: Archivos YAML que definen comportamientos con validación de esquemas
- **Sistema de Ayuda**: Comandos de ayuda integrados con documentación
- **Logs y Feedback**: Salida visual que proporciona información sobre operaciones

## Glosario de términos y definiciones

- **ggGit**: Suite de comandos Git independientes que simplifica el flujo de trabajo de desarrollo
- **Conventional Commits**: Estándar para mensajes de commit que facilita la automatización y generación de changelogs
- **Comandos Independientes**: Comandos ejecutables separados (no alias) que pueden estar implementados en diferentes tecnologías
- **Sistema de Módulos**: Configuraciones específicas por contexto de trabajo (empresa, equipo, proyecto) basadas en archivos YAML
- **Sistema de Repositorio**: Configuraciones específicas por repositorio con prioridad más alta, almacenadas localmente en `.gggit/repo-config.yaml`
- **Validación de Esquemas**: Verificación automática de configuraciones YAML usando esquemas predefinidos
- **Pipeline CI/CD**: Flujo automatizado de integración continua y despliegue continuo
- **Changelog**: Documento que registra cambios, mejoras y correcciones en cada versión del software
- **Staging Area**: Área temporal donde se preparan los cambios antes de hacer commit
- **Branch**: Rama de desarrollo que permite trabajar en funcionalidades sin afectar el código principal
- **Merge**: Proceso de combinar cambios de diferentes ramas de desarrollo
- **Pull Request**: Solicitud para integrar cambios de una rama a otra, típicamente con revisión de código

## Contexto: Terminal de Comandos

> Con la información de la infografía se debe crear un texto extensivo que permita comprender la solución y sus dinámicas de forma completa solo con la lectura. Por cada pantalla, vista o proceso backend que se incluya en la infografía se debe incluir una imagen y una serie de secciones que describan las acciones y eventos, el ciclo de vida y los componentes involucrados. Estas secciones se llamarán contextos.

### Ciclo de vida

#### Al iniciar el contexto

Cuando el usuario abre una terminal y ejecuta un comando ggGit, el sistema inicializa el contexto de la terminal. El sistema verifica que Git esté disponible en el PATH, valida que el directorio actual sea un repositorio Git válido, y carga la configuración local del usuario. Se establece el entorno de trabajo con variables de entorno necesarias y se inicializa el sistema de logging para registrar todas las operaciones.

#### Al pasar a segundo plano

Cuando el usuario ejecuta un comando ggGit y este termina, el contexto pasa a segundo plano. El sistema mantiene en memoria la configuración cargada para futuras operaciones, persiste logs de la operación en archivos temporales, y libera recursos del sistema que ya no son necesarios. El contexto permanece activo pero inactivo, esperando el siguiente comando.

#### Al volver a primer plano

Cuando el usuario ejecuta otro comando ggGit, el contexto vuelve a primer plano. El sistema restaura la configuración desde la memoria, verifica que no haya cambios en la configuración del repositorio, y prepara el entorno para la nueva operación. Se cargan logs previos si son relevantes para la nueva operación.

#### Al volver a la aplicación

Cuando el usuario regresa a la terminal después de usar otras aplicaciones, el contexto se reactiva. El sistema verifica la integridad del repositorio Git, valida que la configuración siga siendo consistente, y restaura el estado de la sesión anterior si es necesario. Se mantiene la continuidad del flujo de trabajo.

#### Al finalizar el contexto

Cuando el usuario cierra la terminal o termina la sesión, el contexto se finaliza. El sistema limpia archivos temporales, guarda logs finales, libera memoria y recursos del sistema, y cierra conexiones a servicios externos si las hubiera. Se asegura que no queden procesos huérfanos.

### Acciones

#### Ejecutar comando ggGit
##### Descripción

El usuario ejecuta un comando ggGit desde la terminal, especificando la operación deseada y los parámetros necesarios. El sistema interpreta el comando, valida los parámetros, ejecuta la operación Git correspondiente, y proporciona feedback visual sobre el resultado. Esta es la acción principal que permite a los usuarios interactuar con ggGit.

##### Beneficios

- **Eficiencia**: Comandos más cortos y fáciles de recordar que los comandos Git nativos
- **Consistencia**: Todos los usuarios del equipo obtienen el mismo resultado con los mismos parámetros
- **Validación**: El sistema valida automáticamente la entrada y previene errores comunes
- **Feedback**: Información clara sobre el resultado de la operación y próximos pasos recomendados
- **Automatización**: Integración automática con configuraciones del equipo y estándares de commit

##### Casos de uso

###### Desarrollador que necesita hacer un commit rápido

María es una desarrolladora que acaba de terminar una corrección de bug. En lugar de recordar la sintaxis exacta de Git y escribir manualmente el mensaje siguiendo Conventional Commits, simplemente ejecuta `ggfix "corrige validación de email"`. El sistema automáticamente genera el commit con el formato correcto "fix: corrige validación de email", lo que le ahorra tiempo y asegura que el mensaje siga los estándares del equipo.

###### Tech Lead que quiere estandarizar commits del equipo

Carlos es Tech Lead de un equipo de 8 desarrolladores. Quiere asegurar que todos los commits sigan el mismo formato. Configura ggGit con templates personalizados y ejecuta `ggconfig setup -m work-team --interactive` para crear la configuración del equipo. Ahora todos los miembros del equipo pueden usar comandos como `ggfeat`, `ggfix`, y `ggbreak` que automáticamente generan commits consistentes, reduciendo la necesidad de revisar cada mensaje manualmente.

#### Configurar ggGit
##### Descripción

El usuario configura ggGit para su entorno específico usando el comando `ggconfig` con subcomandos y flags. El sistema permite mostrar, editar, crear y eliminar configuraciones tanto para el usuario principal como para módulos específicos (empresas, equipos). La configuración se basa en archivos YAML locales con validación de esquemas, proporcionando flexibilidad para diferentes contextos de trabajo.

##### Beneficios

- **Personalización**: Adapta la herramienta a las preferencias y flujo de trabajo del usuario
- **Estandarización**: Asegura que todos los miembros del equipo usen la misma configuración
- **Integración**: Conecta ggGit con herramientas existentes del entorno de desarrollo
- **Automatización**: Reduce la necesidad de configuración manual repetitiva
- **Consistencia**: Mantiene la configuración sincronizada entre diferentes máquinas del usuario

##### Casos de uso

###### Nuevo desarrollador que se une al proyecto

Ana es una nueva desarrolladora que se une al equipo. Simplemente ejecuta `ggconfig setup -m work-company-a --url https://company-a.com/gggit.yaml`. El sistema descarga automáticamente la configuración estándar del equipo, valida el esquema YAML, y la prepara para trabajar inmediatamente con los estándares del proyecto.

###### DevOps que necesita configurar el entorno

Roberto es DevOps y necesita configurar ggGit en un nuevo servidor de CI/CD. Ejecuta `ggconfig setup -m ci-cd --interactive` para crear una configuración optimizada para entornos automatizados. El sistema le guía a través de las opciones necesarias, valida la configuración con esquemas YAML, y establece la integración con el pipeline existente, todo sin intervención manual.

#### Gestionar configuración de módulos
##### Descripción

El usuario puede gestionar configuraciones específicas para diferentes contextos de trabajo (empresas, equipos, proyectos) usando el sistema de módulos. Cada vez que se ejecuta un comando ggGit, el sistema detecta automáticamente el contexto basándose en el directorio actual y aplica la configuración del módulo correspondiente. Esto permite usar diferentes configuraciones de IA y templates según el contexto de trabajo.

##### Beneficios

- **Contexto automático**: El sistema detecta automáticamente el contexto de trabajo sin intervención manual
- **Flexibilidad**: Diferentes configuraciones para diferentes contextos (personal, empresa, proyecto)
- **Separación de configuraciones**: Configuraciones de IA y templates específicos por contexto
- **Mantenimiento simple**: No hay sincronización automática, solo archivos YAML locales
- **Portabilidad**: Las configuraciones funcionan offline y son fáciles de respaldar

##### Casos de uso

###### Equipo que actualiza estándares de commit

El equipo decide agregar nuevos tipos de commit como "docs:" para documentación. El Tech Lead actualiza la configuración del módulo `work-company-a.yaml` y comparte el archivo con el equipo. Cada desarrollador ejecuta `ggconfig setup -m work-company-a --url <nueva-url>` para obtener la configuración actualizada, incluyendo el nuevo tipo de commit, templates actualizados, y configuraciones mejoradas.

###### Integración con CI/CD pipeline

El equipo actualiza las reglas de validación de commits para ser más estrictas. La nueva configuración se aplica localmente usando `ggconfig setup -m work-company-a --interactive`. Ahora todos los commits generados por ggGit seguirán automáticamente el nuevo formato estándar, asegurando que solo código de calidad pase a producción a través de la validación en la nube (CI/CD).

#### Configurar repositorio específico
##### Descripción

El usuario configura ggGit específicamente para el repositorio actual usando el comando `ggconfig setup --repo`. Esta configuración tiene la prioridad más alta en la jerarquía y se almacena localmente en `.gggit/repo-config.yaml` dentro del repositorio. Permite configuraciones muy específicas del proyecto que no se comparten con otros contextos de trabajo.

##### Beneficios

- **Especificidad máxima**: Configuraciones únicas para cada repositorio sin afectar otros proyectos
- **Prioridad alta**: Sobrescribe configuraciones de módulo y usuario cuando es necesario
- **Localización**: La configuración se mantiene dentro del repositorio para fácil portabilidad
- **Flexibilidad**: Permite configuraciones muy específicas del proyecto
- **Independencia**: No interfiere con configuraciones de otros contextos de trabajo

##### Casos de uso

###### Proyecto open source con configuración única

Elena mantiene un proyecto open source que requiere tipos de commit muy específicos como "docs:", "ci:", "build:", y "release:". Ejecuta `ggconfig setup --repo --interactive` para crear una configuración única del repositorio que incluye estos tipos personalizados, templates específicos para documentación, y configuraciones de IA optimizadas para el proyecto. Esta configuración se mantiene localmente y no afecta sus otros proyectos.

###### Repositorio de empresa con configuraciones específicas

Miguel trabaja en un repositorio de empresa que requiere integración con herramientas internas específicas. Ejecuta `ggconfig setup --repo --url https://internal.company.com/gggit-repo-config.yaml` para descargar la configuración específica del repositorio que incluye tokens de API internos, URLs de servicios corporativos, y templates que siguen los estándares específicos de la empresa para ese proyecto.

### Flujos de procesos

#### Flujo de proceso 1: Commit con Conventional Commits

```
[Usuario ejecuta ggfeat] → [Sistema valida parámetros] → [Genera mensaje] → [Ejecuta git add] → [Ejecuta git commit] → [Confirma éxito]
     ↓                              ↓                      ↓                ↓                ↓
[Comando inválido]           [Parámetros faltantes]  [Error en add]   [Error en commit] [Commit exitoso]
     ↓                              ↓                      ↓                ↓
[Mostrar error]              [Solicitar parámetros]  [Mostrar error]  [Mostrar error]   [Mostrar confirmación]
```

#### Flujo de proceso 2: Configuración y gestión de módulos

```
[Usuario ejecuta ggconfig] → [Sistema detecta subcomando] → [Procesa operación] → [Valida esquema YAML] → [Aplica cambios] → [Confirma aplicación]
     ↓                              ↓                        ↓                      ↓                ↓
[Comando inválido]             [Subcomando inválido]    [Error de operación] [Validación falla] [Error aplicación] [Configuración exitosa]
     ↓                              ↓                        ↓                      ↓                ↓
[Mostrar error]               [Mostrar ayuda]           [Reintentar]          [Reportar error]   [Rollback]         [Confirmar cambios]
```

#### Flujo de proceso 3: Integración con CI/CD

```
[Commit exitoso] → [Ejecuta tests] → [Pipeline CI/CD] → [Valida formato] → [Genera changelog] → [Deploy automático]
     ↓                   ↓                ↓                ↓                ↓                ↓
[Commit inválido]   [Tests fallan]   [Pipeline falla] [Validación falla] [Error changelog] [Deploy manual]
     ↓                   ↓                ↓                ↓                ↓
[Rechazar commit]   [Rechazar commit] [Notificar equipo] [Rechazar commit] [Generar manual] [Intervención manual]
```



