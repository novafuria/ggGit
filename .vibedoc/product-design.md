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
  - [Flujos de procesos](#flujos-de-procesos)
    - [Flujo de proceso 1: Commit con Conventional Commits](#flujo-de-proceso-1-commit-con-conventional-commits)
    - [Flujo de proceso 2: Configuración y gestión de módulos](#flujo-de-proceso-2-configuración-y-gestión-de-módulos)
    - [Flujo de proceso 3: Integración con CI/CD](#flujo-de-proceso-3-integración-con-cicd)
- [Contexto: Sistema de Configuración](#contexto-sistema-de-configuración)
  - [Ciclo de vida](#ciclo-de-vida-1)
    - [Al iniciar el contexto](#al-iniciar-el-contexto-1)
    - [Al pasar a segundo plano](#al-pasar-a-segundo-plano-1)
    - [Al volver a primer plano](#al-volver-a-primer-plano-1)
    - [Al volver a la aplicación](#al-volver-a-la-aplicación-1)
    - [Al finalizar el contexto](#al-finalizar-el-contexto-1)
  - [Acciones](#acciones-1)
    - [Crear configuración de equipo](#crear-configuración-de-equipo)
      - [Descripción](#descripción-3)
      - [Beneficios](#beneficios-3)
      - [Casos de uso](#casos-de-uso-3)
        - [Tech Lead que define estándares del proyecto](#tech-lead-que-define-estándares-del-proyecto)
    - [Distribuir configuración](#distribuir-configuración)
      - [Descripción](#descripción-4)
      - [Beneficios](#beneficios-4)
      - [Casos de uso](#casos-de-uso-4)
        - [Onboarding de nuevos desarrolladores](#onboarding-de-nuevos-desarrolladores)
  - [Flujos de procesos](#flujos-de-procesos-1)
    - [Flujo de proceso 4: Gestión de configuraciones](#flujo-de-proceso-4-gestión-de-configuraciones)
- [Contexto: Futuro Sistema de IA](#contexto-futuro-sistema-de-ia)
  - [Ciclo de vida](#ciclo-de-vida-2)
    - [Al iniciar el contexto](#al-iniciar-el-contexto-2)
    - [Al pasar a segundo plano](#al-pasar-a-segundo-plano-2)
    - [Al volver a primer plano](#al-volver-a-primer-plano-2)
    - [Al volver a la aplicación](#al-volver-a-la-aplicación-2)
    - [Al finalizar el contexto](#al-finalizar-el-contexto-2)
  - [Acciones](#acciones-2)
    - [Generar mensaje de commit con IA](#generar-mensaje-de-commit-con-ia)
      - [Descripción](#descripción-5)
      - [Beneficios](#beneficios-5)
      - [Casos de uso](#casos-de-uso-5)
        - [Desarrollador que no sabe qué escribir en el commit](#desarrollador-que-no-sabe-qué-escribir-en-el-commit)
    - [Autocompletar mensaje de commit](#autocompletar-mensaje-de-commit)
      - [Descripción](#descripción-6)
      - [Beneficios](#beneficios-6)
      - [Casos de uso](#casos-de-uso-6)
        - [Desarrollador que quiere acelerar su flujo de trabajo](#desarrollador-que-quiere-acelerar-su-flujo-de-trabajo)
  - [Flujos de procesos](#flujos-de-procesos-2)
    - [Flujo de proceso 5: Generación de mensajes con IA](#flujo-de-proceso-5-generación-de-mensajes-con-ia)

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
│  │ • ggfeat (bash)│    │ • ~/.gggit/     │    │ • Esquemas YAML │        │
│  │ • ggfix (bash) │    │ • Módulos por   │    │ • Validación    │        │
│  │ • ggbreak (bash)│   │   contexto      │    │   automática    │        │
│  │ • ggmerge (bash)│   │ • Config local  │    │ • Diferentes    │        │
│  │ • ggconfig (py)│    │ • Módulos       │    │   tecnologías   │        │
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
│  │  1. Commit → 2. Validación → 3. CI/CD → 4. Release                 │   │
│  │     ↓           ↓           ↓         ↓                             │   │
│  │  Conventional  Hooks      Pipeline  Automático                     │   │
│  │  Commits      Git         GitHub    Changelog                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Futuro: Sistema de IA                           │   │
│  │                                                                     │   │
│  │  $ ggai "analiza cambios y sugiere mensaje"                        │   │
│  │  → feat: implementa autenticación OAuth2 con refresh tokens        │   │
│  │                                                                     │
│  │  Análisis automático de archivos staged → Sugerencia inteligente   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Texto Descriptivo de la Propuesta de Valor

ggGit es una suite de comandos independientes de línea de comandos que transforma la experiencia de trabajo con Git. La solución se compone de tres pilares principales:

1. **Comandos Principales**: Una colección de comandos independientes (no alias) que simplifican operaciones Git comunes, especialmente enfocados en Conventional Commits. Cada comando puede estar implementado en diferentes tecnologías según sus necesidades específicas.

2. **Sistema de Configuración Jerárquica**: Un mecanismo local que permite configuraciones específicas por contexto, incluyendo módulos por empresa/equipo, configuración de usuario, y configuraciones específicas de repositorio, todo basado en archivos YAML locales.

3. **Sistema de Validación Robusto**: Un sistema que valida configuraciones usando esquemas YAML, asegurando consistencia y robustez en todos los entornos de desarrollo sin necesidad de sincronización automática.

### Eventos y Actividades Clave

- **Commit de Código**: El desarrollador ejecuta un comando ggGit que genera automáticamente un Conventional Commit válido
- **Configuración de Equipo**: El Tech Lead define estándares en archivos YAML que se comparten con el equipo
- **Gestión de Módulos**: El sistema detecta automáticamente el contexto de trabajo y aplica configuraciones específicas
- **Integración CI/CD**: Los commits estructurados activan automáticamente pipelines de build y deploy
- **Generación de Changelog**: El sistema genera automáticamente documentación de cambios basada en el historial de commits

### Explosión de Componentes

- **CLI Commands**: Comandos independientes ejecutables que encapsulan lógica Git compleja, cada uno implementado en la tecnología más apropiada (bash, Python, etc.)
- **Configuration Manager**: Sistema local que gestiona configuraciones jerárquicas basadas en archivos YAML
- **Hook System**: Integración con Git hooks para validación automática de commits
- **Template Engine**: Generador de mensajes de commit basado en templates configurables
- **Validation Engine**: Motor que valida configuraciones usando esquemas YAML y valida formato de commits
- **Module System**: Sistema que detecta automáticamente el contexto de trabajo y aplica configuraciones específicas

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
- **Git Hooks**: Scripts que se ejecutan automáticamente en eventos específicos de Git
- **Comandos Independientes**: Comandos ejecutables separados (no alias) que pueden estar implementados en diferentes tecnologías
- **Sistema de Módulos**: Configuraciones específicas por contexto de trabajo (empresa, equipo, proyecto) basadas en archivos YAML
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
- **Automatización**: Integración automática con hooks y configuraciones del equipo

##### Casos de uso

###### Desarrollador que necesita hacer un commit rápido

María es una desarrolladora que acaba de terminar una corrección de bug. En lugar de recordar la sintaxis exacta de Git y escribir manualmente el mensaje siguiendo Conventional Commits, simplemente ejecuta `ggfix "corrige validación de email"`. El sistema automáticamente genera el commit con el formato correcto "fix: corrige validación de email", lo que le ahorra tiempo y asegura que el mensaje siga los estándares del equipo.

###### Tech Lead que quiere estandarizar commits del equipo

Carlos es Tech Lead de un equipo de 8 desarrolladores. Quiere asegurar que todos los commits sigan el mismo formato. Configura ggGit con templates personalizados y ejecuta `ggconfig --team` para distribuir la configuración. Ahora todos los miembros del equipo pueden usar comandos como `ggfeat`, `ggfix`, y `ggbreak` que automáticamente generan commits consistentes, reduciendo la necesidad de revisar cada mensaje manualmente.

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

Ana es una nueva desarrolladora que se une al equipo. En lugar de configurar manualmente todos los alias Git, hooks, y configuraciones, simplemente ejecuta `ggconfig setup -m work-company-a --url https://company-a.com/gggit.yaml`. El sistema descarga automáticamente la configuración estándar del equipo, valida el esquema YAML, instala todos los hooks necesarios, y la prepara para trabajar inmediatamente con los estándares del proyecto.

###### DevOps que necesita configurar el entorno

Roberto es DevOps y necesita configurar ggGit en un nuevo servidor de CI/CD. Ejecuta `ggconfig setup -m ci-cd --interactive` para crear una configuración optimizada para entornos automatizados. El sistema le guía a través de las opciones necesarias, valida la configuración con esquemas YAML, y establece la integración con el pipeline existente, todo sin intervención manual.

#### Gestionar configuración de módulos
##### Descripción

El usuario puede gestionar configuraciones específicas para diferentes contextos de trabajo (empresas, equipos, proyectos) usando el sistema de módulos. Cada vez que se ejecuta un comando ggGit, el sistema detecta automáticamente el contexto basándose en el directorio actual y aplica la configuración del módulo correspondiente. Esto permite usar diferentes configuraciones de IA, hooks, y templates según el contexto de trabajo.

##### Beneficios

- **Contexto automático**: El sistema detecta automáticamente el contexto de trabajo sin intervención manual
- **Flexibilidad**: Diferentes configuraciones para diferentes contextos (personal, empresa, proyecto)
- **Separación de configuraciones**: Configuraciones de IA, hooks y templates específicos por contexto
- **Mantenimiento simple**: No hay sincronización automática, solo archivos YAML locales
- **Portabilidad**: Las configuraciones funcionan offline y son fáciles de respaldar

##### Casos de uso

###### Equipo que actualiza estándares de commit

El equipo decide agregar nuevos tipos de commit como "docs:" para documentación. El Tech Lead actualiza la configuración del módulo `work-company-a.yaml` y comparte el archivo con el equipo. Cada desarrollador ejecuta `ggconfig setup -m work-company-a --url <nueva-url>` para obtener la configuración actualizada, incluyendo el nuevo tipo de commit, templates actualizados, y validaciones mejoradas.

###### Integración con CI/CD pipeline

El equipo actualiza las reglas de validación de commits para ser más estrictas. La nueva configuración se aplica localmente usando `ggconfig setup -m work-company-a --interactive`. Ahora todos los commits que no cumplan con las nuevas reglas serán rechazados automáticamente por los hooks locales, asegurando que solo código de calidad pase a producción.

### Flujos de procesos

#### Flujo de proceso 1: Commit con Conventional Commits

```
[Usuario ejecuta ggfeat] → [Sistema valida parámetros] → [Genera mensaje] → [Ejecuta git add] → [Ejecuta git commit] → [Valida formato] → [Confirma éxito]
     ↓                              ↓                      ↓                ↓                ↓                ↓
[Comando inválido]           [Parámetros faltantes]  [Error en add]   [Error en commit] [Formato inválido] [Commit exitoso]
     ↓                              ↓                      ↓                ↓                ↓
[Mostrar error]              [Solicitar parámetros]  [Mostrar error]  [Mostrar error]   [Corregir formato] [Mostrar confirmación]
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
[Commit exitoso] → [Git hook ejecuta] → [Valida formato] → [Ejecuta tests] → [Pipeline CI/CD] → [Genera changelog] → [Deploy automático]
     ↓                   ↓                ↓                ↓                ↓                ↓                ↓
[Commit inválido]   [Hook falla]     [Validación falla] [Tests fallan]   [Pipeline falla] [Error changelog] [Deploy manual]
     ↓                   ↓                ↓                ↓                ↓                ↓
[Rechazar commit]   [Reportar error] [Rechazar commit] [Rechazar commit] [Notificar equipo] [Generar manual] [Intervención manual]
```

## Contexto: Sistema de Configuración

> Con la información de la infografía se debe crear un texto extensivo que permita comprender la solución y sus dinámicas de forma completa solo con la lectura. Por cada pantalla, vista o proceso backend que se incluya en la infografía se debe incluir una imagen y una serie de secciones que describan las acciones y eventos, el ciclo de vida y los componentes involucrados. Estas secciones se llamarán contextos.

### Ciclo de vida

#### Al iniciar el contexto

Cuando se inicia el sistema de configuración, el contexto se inicializa cargando la configuración base desde el repositorio central del equipo. El sistema verifica la conectividad con el repositorio de configuración, valida las credenciales de acceso, y descarga la configuración más reciente. Se establece el contexto de trabajo con todas las configuraciones disponibles y se prepara para responder a solicitudes de configuración.

#### Al pasar a segundo plano

Cuando el sistema de configuración no está procesando solicitudes activas, pasa a segundo plano. El sistema mantiene en memoria la configuración cargada, monitorea cambios en el repositorio central, y mantiene conexiones activas para respuestas rápidas. Se ejecutan procesos de limpieza y optimización en segundo plano.

#### Al volver a primer plano

Cuando se recibe una nueva solicitud de configuración, el contexto vuelve a primer plano. El sistema valida que la configuración en memoria esté actualizada, verifica la integridad de los archivos de configuración, y prepara el entorno para procesar la nueva solicitud. Se restauran las conexiones necesarias.

#### Al volver a la aplicación

Cuando el usuario regresa a la aplicación después de usar otras herramientas, el contexto se reactiva. El sistema verifica que no haya cambios en la configuración del repositorio central, valida la consistencia de la configuración local, y restaura el estado de la sesión anterior si es necesario.

#### Al finalizar el contexto

Cuando se finaliza el sistema de configuración, el contexto se cierra. El sistema guarda logs de todas las operaciones realizadas, cierra conexiones a repositorios externos, libera memoria y recursos del sistema, y asegura que no queden procesos activos. Se realiza una limpieza completa del entorno.

### Acciones

#### Crear configuración de equipo
##### Descripción

El Tech Lead o administrador del proyecto crea una nueva configuración de equipo que define estándares, templates, y reglas de validación. El sistema presenta un formulario de configuración, valida las entradas del usuario, genera archivos de configuración en formato estándar, y los sube al repositorio central del equipo. Esta configuración se convierte en la base para todos los miembros del equipo.

##### Beneficios

- **Estandarización**: Define reglas claras que todos los miembros del equipo deben seguir
- **Consistencia**: Asegura que todos los entornos de desarrollo tengan la misma configuración
- **Evolución**: Permite que el equipo mejore y refine sus estándares de manera colaborativa
- **Automatización**: Reduce la necesidad de configurar manualmente cada entorno
- **Calidad**: Establece estándares que mejoran la calidad del código y la documentación

##### Casos de uso

###### Tech Lead que define estándares del proyecto

Sofía es Tech Lead de un proyecto de e-commerce. Quiere establecer estándares claros para commits que faciliten la generación automática de changelogs. Crea una configuración que define tipos de commit específicos como "feat:", "fix:", "docs:", "style:", "refactor:", "test:", y "chore:". También define templates para cada tipo y reglas de validación que aseguran que los mensajes sean descriptivos y útiles. Una vez creada, la configuración se distribuye automáticamente a todo el equipo.

#### Distribuir configuración
##### Descripción

El sistema distribuye automáticamente la configuración del equipo a todos los entornos de desarrollo. Cuando se detecta un cambio en la configuración central, el sistema notifica a todos los usuarios registrados, descarga la nueva configuración, y la aplica automáticamente. Los usuarios pueden también forzar una sincronización manual cuando lo deseen.

##### Beneficios

- **Distribución automática**: Los usuarios reciben nuevas configuraciones sin intervención manual
- **Sincronización**: Todos los entornos mantienen la misma configuración actualizada
- **Notificación**: Los usuarios son informados de cambios en la configuración
- **Rollback**: Posibilidad de revertir a configuraciones anteriores si es necesario
- **Auditoría**: Registro completo de todas las distribuciones y cambios de configuración

##### Casos de uso

###### Onboarding de nuevos desarrolladores

Lucas es un nuevo desarrollador que se une al equipo. En lugar de configurar manualmente su entorno Git con todos los alias, hooks, y configuraciones del proyecto, simplemente ejecuta `ggconfig --team`. El sistema detecta automáticamente que es un nuevo usuario, descarga la configuración estándar del equipo, instala todos los componentes necesarios, y lo prepara para trabajar inmediatamente con los estándares del proyecto. El proceso completo toma menos de 2 minutos.

### Flujos de procesos

#### Flujo de proceso 4: Gestión de configuraciones

```
[Cambio en configuración] → [Sistema detecta cambio] → [Valida configuración] → [Notifica usuarios] → [Distribuye cambios] → [Confirma aplicación]
     ↓                           ↓                        ↓                      ↓                ↓                ↓
[Configuración inválida]   [Error de detección]     [Validación falla]    [Notificación falla] [Distribución falla] [Aplicación exitosa]
     ↓                           ↓                        ↓                      ↓                ↓
[Rechazar cambio]          [Reportar error]          [Rechazar cambio]     [Reintentar]         [Rollback]          [Confirmar distribución]
```

## Contexto: Futuro Sistema de IA

> Con la información de la infografía se debe crear un texto extensivo que permita comprender la solución y sus dinámicas de forma completa solo con la lectura. Por cada pantalla, vista o proceso backend que se incluya en la infografía se debe incluir una imagen y una serie de secciones que describan las acciones y eventos, el ciclo de vida y los componentes involucrados. Estas secciones se llamarán contextos.

### Ciclo de vida

#### Al iniciar el contexto

Cuando se inicia el sistema de IA, el contexto se inicializa cargando modelos de lenguaje pre-entrenados, configurando APIs de servicios de IA, y estableciendo conexiones con repositorios de código. El sistema verifica la disponibilidad de recursos de IA, valida las credenciales de acceso a servicios externos, y prepara el entorno para análisis de código y generación de mensajes.

#### Al pasar a segundo plano

Cuando el sistema de IA no está procesando solicitudes activas, pasa a segundo plano. El sistema mantiene los modelos de IA en memoria para respuestas rápidas, monitorea el uso de recursos, y ejecuta procesos de optimización y limpieza. Se mantienen conexiones activas con servicios de IA externos.

#### Al volver a primer plano

Cuando se recibe una nueva solicitud de análisis de código o generación de mensaje, el contexto vuelve a primer plano. El sistema valida que los modelos de IA estén actualizados, verifica la disponibilidad de servicios externos, y prepara el entorno para procesar la nueva solicitud. Se restauran las conexiones necesarias.

#### Al volver a la aplicación

Cuando el usuario regresa a la aplicación después de usar otras herramientas, el contexto se reactiva. El sistema verifica que no haya cambios en los modelos de IA, valida la consistencia de las configuraciones, y restaura el estado de la sesión anterior si es necesario.

#### Al finalizar el contexto

Cuando se finaliza el sistema de IA, el contexto se cierra. El sistema guarda logs de todas las operaciones realizadas, cierra conexiones a servicios externos de IA, libera memoria y recursos del sistema, y asegura que no queden procesos activos. Se realiza una limpieza completa del entorno.

### Acciones

#### Generar mensaje de commit con IA
##### Descripción

El sistema analiza automáticamente los cambios en los archivos staged para commit y genera un mensaje de commit descriptivo y bien estructurado usando inteligencia artificial. El usuario ejecuta un comando como `ggai` y el sistema analiza el código modificado, identifica el tipo de cambio, y sugiere un mensaje que sigue los estándares de Conventional Commits.

##### Beneficios

- **Automatización**: Elimina la necesidad de escribir manualmente mensajes de commit
- **Consistencia**: Asegura que todos los mensajes sigan los mismos estándares
- **Calidad**: Genera mensajes más descriptivos y útiles que los escritos manualmente
- **Eficiencia**: Acelera el flujo de trabajo al reducir el tiempo de escritura de commits
- **Aprendizaje**: Los usuarios aprenden mejores prácticas observando los mensajes generados

##### Casos de uso

###### Desarrollador que no sabe qué escribir en el commit

Diego está trabajando en una nueva funcionalidad pero no está seguro de cómo describir los cambios en el mensaje de commit. En lugar de escribir algo vago como "cambios varios", ejecuta `ggai`. El sistema analiza los archivos modificados, detecta que se agregó autenticación OAuth2, y sugiere el mensaje "feat: implementa autenticación OAuth2 con refresh tokens". Diego puede aceptar la sugerencia o modificarla según sus preferencias.

#### Autocompletar mensaje de commit
##### Descripción

El sistema proporciona autocompletado inteligente mientras el usuario escribe un mensaje de commit. A medida que el usuario escribe, el sistema analiza el contexto del código modificado y sugiere completaciones basadas en patrones comunes y mejores prácticas. El usuario puede aceptar las sugerencias o continuar escribiendo manualmente.

##### Beneficios

- **Asistencia**: Ayuda al usuario a escribir mensajes más completos y descriptivos
- **Flexibilidad**: Permite al usuario mantener control total sobre el mensaje final
- **Aprendizaje**: Enseña mejores prácticas a través de sugerencias contextuales
- **Eficiencia**: Acelera la escritura sin eliminar la creatividad del usuario
- **Consistencia**: Sugiere formatos que siguen los estándares del equipo

##### Casos de uso

###### Desarrollador que quiere acelerar su flujo de trabajo

Valentina está escribiendo un mensaje de commit y comienza con "feat:". El sistema detecta que está trabajando en una nueva funcionalidad y sugiere "feat: implementa sistema de notificaciones push". Valentina puede aceptar la sugerencia completa o modificar solo la parte descriptiva. El sistema continúa sugiriendo mejoras mientras escribe, como agregar el scope del cambio o detalles adicionales sobre la implementación.

### Flujos de procesos

#### Flujo de proceso 5: Generación de mensajes con IA

```
[Usuario ejecuta ggai] → [Sistema analiza cambios] → [IA genera mensaje] → [Usuario revisa] → [Usuario acepta/modifica] → [Commit exitoso]
     ↓                        ↓                        ↓                ↓                ↓                ↓
[Comando inválido]      [Error en análisis]      [IA falla]        [Usuario rechaza] [Usuario modifica] [Commit exitoso]
     ↓                        ↓                        ↓                ↓                ↓
[Mostrar error]         [Reintentar análisis]    [Fallback manual] [Solicitar input] [Regenerar con IA] [Confirmar commit]
```