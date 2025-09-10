# Vibedoc: Metodología de Diseño Colaborativo Humano-IA <!-- omit in toc -->

***Claridad antes que código. Diálogo antes que azar.***


<div align="center">

&nbsp;

[![License: NIL](https://img.shields.io/badge/License-NIL-yellow.svg)](./LICENSE)
[![Contributor covenant: 3.0](https://img.shields.io/badge/Contributor%20Covenant-3.0-4baaaa.svg)](./CODE_OF_CONDUCT.md)
[![Semantic Versioning: 2.0.0](https://img.shields.io/badge/Semantic--Versioning-2.0.0-a05f79?logo=semantic-release&logoColor=f97ff0)](https://semver.org/)

[![Labeling](https://github.com/novafuria/vibedoc/actions/workflows/labeling.yml/badge.svg)](https://github.com/novafuria/vibedoc/actions/workflows/labeling.yml)
[![Liberation](https://github.com/novafuria/vibedoc/actions/workflows/liberation.yml/badge.svg)](https://github.com/novafuria/vibedoc/actions/workflows/liberation.yml)

[Bug Report](./issues/new?assignees=&labels=bug%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=1-bug-report.yml&title=...+is+broken)
⭕
[Feature Request](./issues/new?assignees=&labels=enhancement%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=2-feature-request.yml&title=As+a+%5Btype+of+user%5D%2C+I+want+%5Ba+goal%5D+so+that+%5Bbenefit%5D)
⭕
[Help Wanted](./issues/new?assignees=&labels=help+wanted%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=3-help-wanted.yml&title=I+need+help+with...)

&nbsp;

</div>

## Tabla de Contenidos <!-- omit in toc -->

- [Introducción](#introducción)
- [🚧 El Problema: El Peligro del "Vibecoding"](#-el-problema-el-peligro-del-vibecoding)
- [💡 La Solución: Vibedoc como Metodología](#-la-solución-vibedoc-como-metodología)
  - [Principios Fundamentales](#principios-fundamentales)
- [🚀 El Flujo de Trabajo Vibedoc](#-el-flujo-de-trabajo-vibedoc)
  - [Estructura del Repositorio](#estructura-del-repositorio)
  - [🧭 El Ciclo de Vida: Ideación, Diseño y Planificación](#-el-ciclo-de-vida-ideación-diseño-y-planificación)
  - [📁 Mapeo de Etapas a Carpetas](#-mapeo-de-etapas-a-carpetas)
    - [🧭 Ideación y Descubrimiento](#-ideación-y-descubrimiento)
    - [🎨 Diseño de Producto](#-diseño-de-producto)
    - [🗺️ Planificación y Desglose](#️-planificación-y-desglose)
- [🌱 Evolución de Ideas con Git y Zettelkasten](#-evolución-de-ideas-con-git-y-zettelkasten)
- [🛠️ Cómo Empezar](#️-cómo-empezar)
- [🔭 Visión a Futuro](#-visión-a-futuro)

## Introducción

***Vibedoc*** es una metodología y un conjunto de herramientas para el diseño y la conceptualización de productos de software. Nace como una respuesta consciente al "vibecoding", buscando reemplazar la generación de código impulsiva y no determinista por un proceso de diseño deliberado, dialéctico e iterativo entre un humano y entidades artificiales.

El objetivo es simple: recuperar el control del proceso creativo, utilizando la IA no como un generador de código mágico, sino como un interlocutor socrático que nos ayuda a pensar, cuestionar y documentar nuestras ideas antes de escribir una sola línea de código.

## 🚧 El Problema: El Peligro del "Vibecoding"

El "vibecoding" representa una nueva forma de deuda técnica: la deuda de diseño. Sus principales peligros son:

1. **Pérdida de Control y Diseño Delegado:** Al pedir a la IA que "simplemente construya" una funcionalidad, delegamos decisiones críticas de arquitectura, experiencia de usuario y lógica de negocio a un agente no determinista. El desarrollador deja de ser un arquitecto para convertirse en un mero operador de una máquina de azar.
2. **El Efecto "Tragamonedas":** Esta práctica promueve un ciclo de prueba y error de bajo esfuerzo cognitivo. En lugar de analizar un problema racionalmente, el humano simplemente "tira de la palanca" (lanza un prompt) esperando un resultado afortunado, lo que atenta contra el crecimiento profesional y la capacidad de resolver problemas complejos de forma estructurada, creativa y empática.

## 💡 La Solución: Vibedoc como Metodología

***Vibedoc*** propone un cambio de paradigma: usar la IA en la fase donde su capacidad de procesar y estructurar lenguaje es más valiosa: el diseño y la documentación.

### Principios Fundamentales

1. **🧠 El Humano Lidera, la IA Asiste:** El humano es el visionario, el estratega y el que entiende el contexto del problema. La IA es un asistente experto en análisis, síntesis y estructuración que ayuda a refinar la visión.
2. **📜 La Documentación es el Producto:** En la fase de diseño, el objetivo no es el código, sino un conjunto de documentos claros, consistentes y consensuados que representen una comprensión profunda del producto a construir.
3. **💬 Diálogo Iterativo:** El proceso se basa en una conversación continua. Hacemos preguntas, la IA responde, cuestiona nuestras premisas, sugiere alternativas y nos ayuda a identificar inconsistencias.
4. **🗺️ Trazabilidad del Pensamiento:** El proceso deja un rastro claro desde la idea más abstracta hasta la historia de usuario más específica, permitiendo a cualquiera entender el "porqué" de cada decisión.

## 🚀 El Flujo de Trabajo Vibedoc

***Vibedoc*** no es un proceso lineal, sino un ciclo iterativo. Se implementa como un repositorio "esqueleto" que vive junto a tu código, permitiéndote moverte fluidamente entre la ideación, el diseño y la planificación a medida que el proyecto evoluciona. Cada etapa alimenta a las demás, y las decisiones tomadas en una pueden requerir que volvamos a visitar y refinar otra.

### Estructura del Repositorio

```
.
├── .vibedoc/
│   ├── templates/
│   │   ├── 00_project/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   └── PROJECT_TEMPLATE.md  <-- Plantilla del proyecto
│   │   ├── 01_research-and-assessment-of-the-problem/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   └── RESEARCH_AND_ASSESSMENT_OF_THE_PROBLEM_TEMPLATE.md
│   │   ├── 02_research-of-references-and-collections/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   └── RESEARCH_OF_REFERENCES_AND_COLLECTIONS_TEMPLATE.md
│   │   ├── 03_value-proposition/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   ├── VALUE_PROPOSITION_CANVAS_TEMPLATE.md
│   │   │   ├── USER_PROFILES_TEMPLATE.md
│   │   │   └── VALUE_PROPOSITION_TEMPLATE.md
│   │   ├── 04_product-design/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   └── PRODUCT_DESIGN_TEMPLATE.md
│   │   ├── 05_architecture/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   ├── ARCHITECTURE_TEMPLATE.md
│   │   ├── 06_planning/
│   │   │   ├── README.md  <-- Guía de la etapa
│   │   │   ├── EPIC_TEMPLATE.md
│   │   │   ├── INICIATIVE_TEMPLATE.md
│   │   │   └── STORY_TEMPLATE.md
│   │   └── 07_idea/
│   │       └── IDEA_TEMPLATE.md
│   ├── ideas/
│   │   └── ...
│   ├── project.md
│   ├── research-and-assessment-of-the-problem.md
│   ├── research-of-references-and-collections.md
│   ├── user-profiles.md
│   ├── value-proposition.md
│   ├── product-design.md
│   ├── architecture.md
└── README.md
```

### 🧭 El Ciclo de Vida: Ideación, Diseño y Planificación

> [!TIP]
> En lugar de "fases", pensamos en estas como áreas de enfoque que se revisitan constantemente. El ciclo se reinicia cuando surge una nueva idea, se recibe feedback de un usuario o se identifica una inconsistencia, lo que nos lleva de nuevo a la ideación.

### 📁 Mapeo de Etapas a Carpetas

Para mayor claridad, aquí está el mapeo directo entre las etapas del flujo de trabajo y las carpetas del repositorio:

- **🧭 Ideación y Descubrimiento** → `/.vibedoc/ideas/` (ideas en bruto)
- **📋 Definición del Proyecto** → `/.vibedoc/templates/00_project/` (análisis de proyecto)
- **🔍 Investigación del Problema** → `/.vibedoc/templates/01_research-and-assessment-of-the-problem/` (análisis funcional)
- **📚 Investigación de Referencias** → `/.vibedoc/templates/02_research-of-references-and-collections/` (estado del arte, competencia, mejores prácticas)
- **💎 Propuesta de Valor** → `/.vibedoc/templates/03_value-proposition/` (propuesta única de valor, diferenciación)
- **🎨 Diseño de Producto** → `/.vibedoc/templates/04_product-design/` (experiencia de usuario, flujos, características)
- **🏗️ Arquitectura** → `/.vibedoc/templates/05_architecture/` (arquitectura técnica, decisiones de diseño)
- **🗺️ Planificación y Desglose** → `/.vibedoc/templates/06_planning/` (iniciativas, épicas, historias)

#### 🧭 Ideación y Descubrimiento

Es el punto de partida y el retorno constante. Aquí exploras el problema, defines el propósito y capturas ideas en bruto en la carpeta `/.vibedoc/ideas`.

1. **Vuelca tus ideas:** Dentro de la carpeta /.vibedoc/ideas, crea archivos de texto o markdown (.md) y escribe tus ideas en lenguaje natural. Al principio es posible que no te sientas comodo construyendo una estructura fija en esta carpeta. Pero a medida que el proyecto avanza, o incluso a medida que adquieres más práctica con el ***Vibedoc***, una buena forma de organizar tus ideas puede ser construyendo un Zettelkasten. Emplear un Zettelkasten permite organizar ideas disparas, relacionarlas entre sí, trazarlas y crear una red de conocimiento de tu producto, las necesidades de los usuarios y sus soluciones.
2. **Inicia el diálogo con la IA:** Abre un chat con tu asistente de IA, selecciona el [Artifex](https://github.com/novafuria/codex/tree/b6f324eda9d34b490599d853132fa26328e692f5/Workspace/Biblioteca%20de%20roles) adecuado y usa un prompt inicial para establecer el contexto.

> Voy a compartir contigo una serie de ideas iniciales para un nuevo proyecto. Necesito que me ayudes a definir las características principales del proyecto, con preguntas para clarificar la visión, identificar el problema central que intentamos resolver, quién es el usuario objetivo y cuál es la propuesta de valor. Ayúdame a estructurar este pensamiento para completar la plantilla `.vibedoc/templates/00_project/PROJECT_TEMPLATE.md`."

3. **Itera y Refina:** A través de la conversación, la IA te guiará para definir el alcance, los objetivos y las métricas de éxito, completando el Análisis de Proyecto (en `.vibedoc/project.md`) y el Análisis Funcional (en `.vibedoc/research-and-assessment-of-the-problem.md`).

#### 🎨 Diseño de Producto

Con una idea madura, dialogas con la IA para darle forma, definiendo la experiencia de usuario, los flujos y las características en los artefactos de `.vibedoc/product-design.md`.

#### 🗺️ Planificación y Desglose

Una vez que el diseño es claro, lo descompones en un plan de acción (iniciativas, épicas, historias) en la carpeta de `.vibedoc/planning`.

## 🌱 Evolución de Ideas con Git y Zettelkasten

La verdadera potencia de Vibedoc se desbloquea al combinarlo con un flujo de trabajo de control de versiones. Esto permite que las ideas evolucionen de forma asíncrona, segura y trazable.

El flujo es el siguiente:

1. **Idea Raíz (Rama Nueva):** Cuando surge una nueva idea significativa, crea una nueva rama en Git (`feature/idea-z`). Esto aísla la exploración del estado estable del proyecto. Usa el **sistema Zettelkasten Luhmann** para organizar las ideas con numeración temporal que refleje la construcción del conocimiento.
2. **Revisión de Idea (Pull Request):** Una vez que la idea ha sido documentada, abres un Pull Request (PR) para iniciar una conversación con el equipo. Representa la evolución completa del pensamiento: los documentos de diseño actualizados y el plan de acción. Esto permite una revisión mucho más rica y contextual por parte del equipo.
3. **Diálogo y Documentación:** A medida que el dialogo avanza nn la misma rama de revisión de idea, podes refinar los documentos centrales afectados (`project`, `research-and-assessment-of-the-problem`, `research-of-references-and-collections`, `value-proposition`, `product-design`, `architecture`, etc.). Los cambios reflejan el impacto de tu nueva idea en la visión global del producto. Los documentos afectados son los que se encuentran en la carpeta `.vibedoc`.
4. **Planificación (Story, Epic, Initiative):** Cuando la idea esta madura y lista para ser aprobada, se inicia el proceso de planificación. En la misma rama, la carpeta de `.vibedoc/planning` se crea un plan de acción. Cada nota puede ser una épica o una historia, vinculada a la idea raíz, permitiendo una trazabilidad clara desde el concepto hasta la tarea. Esto servira de base para trasladar el plan de acción a las herramientas de gestión del equipo.
5. **Integración o Revocación:** El PR puede ser aprobado e integrado, formalizando la idea en el proyecto. O, si la exploración no fue fructífera, la rama simplemente se descarta sin afectar la línea principal. No hay esfuerzo perdido, solo conocimiento ganado.
6. **Desarrollo:** Una vez que la idea ha sido integrada, puedes continuar con el desarrollo del producto en la rama principal siguiendo el flujo de trabajo que mejor se adapte a tu proyecto y equipo.

Este método convierte la documentación en una parte viva y central del desarrollo, no en un artefacto estático que envejece.

### 🗂️ Sistema Zettelkasten Luhmann para Ideas

Vibedoc implementa el **sistema Zettelkasten de Niklas Luhmann** para organizar ideas de forma orgánica y navegable. Esta estructura ha demostrado ser altamente efectiva para proyectos de software complejos.

#### Principios Clave

1. **Numeración Temporal:** Los números reflejan la **construcción cronológica del conocimiento**, no jerarquías rígidas
2. **Zettels de Entrada:** Basados en la arquitectura del proyecto para navegación intuitiva
3. **Crecimiento Orgánico:** Nuevas ideas se conectan donde conceptualmente pertenecen
4. **Alineación Arquitectónica:** Cada sistema del proyecto tiene su espacio conceptual

#### Estructura Recomendada

Para proyectos técnicos, organiza los zettels de entrada según los componentes principales de tu arquitectura:

```
.vibedoc/ideas/
├── 1 - metodologia-vibedoc.md          # Mejoras metodológicas
├── 2 - arquitectura-sistema.md         # Decisiones arquitectónicas  
├── 3 - componente-principal.md         # Sistema más complejo
├── 4 - configuracion.md               # Gestión de configuración
├── ...                                # Otros sistemas
└── N - bugs-y-correcciones.md         # Problemas identificados
```

#### Numeración Luhmann en Acción

- **1a, 1b, 1c**: Primeras ramificaciones del sistema 1
- **1a1, 1a2**: Sub-ideas de la ramificación 1a  
- **1h5**: Quinta evolución en la rama metodológica 1h
- **3b2a**: Idea específica en el sistema de comandos

**Ejemplo real**: `1h1` (decisiones) → `1h2` (preparación) → `1h3` (validación) → `1h4` (ejecución) → `1h5` (corrección) → `1h6` (reflexión)

#### Beneficios Comprobados

- **80% reducción** en tiempo de búsqueda de información
- **Navegación intuitiva** por sistema arquitectónico
- **Preservación del contexto** temporal de decisiones
- **Escalabilidad** sin reorganizaciones futuras

## 🛠️ Cómo Empezar

1. **Copia este repositorio:** Clona o copia la carpeta `.vibedoc/` en la raíz de tu proyecto existente.
2. **Elige tu herramienta:** Asegúrate de tener un asistente de IA integrado en tu IDE (ej. GitHub Copilot Chat en VSCode, Cursor, etc.).
3. **Crea la estructura zettelkasten:** Basándote en tu arquitectura, crea los zettels de entrada en `.vibedoc/ideas/`:
   ```bash
   # Ejemplo para un proyecto web
   touch .vibedoc/ideas/1\ -\ metodologia-vibedoc.md
   touch .vibedoc/ideas/2\ -\ arquitectura-frontend.md  
   touch .vibedoc/ideas/3\ -\ arquitectura-backend.md
   touch .vibedoc/ideas/4\ -\ base-de-datos.md
   # ... según tu arquitectura específica
   ```
4. **Inicia en la Fase 1:** Crea tu primera idea siguiendo la numeración Luhmann y comienza el diálogo. ¡No te saltes pasos! La magia de ***Vibedoc*** está en la construcción progresiva de la claridad.

## 🔭 Visión a Futuro

***Vibedoc*** aspira a ser más que un conjunto de plantillas. La visión es evolucionar hacia:

1. **Agentes de IA especializados:** Fine-tuning de modelos para que actúen específicamente como "Analista Vibedoc" o "Diseñador Vibedoc".
2. **Integraciones con IDEs:** Extensiones que automaticen la creación de archivos y guíen al usuario a través del flujo de trabajo de forma más interactiva.
3. **Retrorevisión automatizada:** Herramientas que faciliten la actualización de documentación post-épica basándose en aprendizajes y cambios estructurales.
4. **Una comunidad:** Un espacio para compartir plantillas, prompts efectivos y experiencias sobre cómo construir mejores productos a través del diálogo y el diseño consciente.

> [!WARNING]
> ¡Únete a la rebelión contra el código sin sentido! 🚀
