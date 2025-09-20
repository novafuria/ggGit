# [planning] - <name> <!-- omit in toc -->

Este documento describe la estructura de carpetas y archivos para operar con las iniciativas, epics y stories.

## Tabla de Contenidos

- [Tabla de Contenidos](#tabla-de-contenidos)
- [Estructura de carpetas](#estructura-de-carpetas)
- [Iniciativas](#iniciativas)
- [Epics](#epics)
- [Stories](#stories)

## Estructura de carpetas

```bash
.
├── iniciatives/
│   ├── INI-<zettelkasten-identifier>-<title>/ # Cada iniciativa tiene su propio archivo de especificación.
│   │   ├── epics/
│   │   │   ├── EPIC-<zettelkasten-identifier>-<title>.md # Cada epic tiene su propio archivo de especificación.
│   │   │   └── stories/
│   │   │       ├── STORY-<zettelkasten-identifier>-<title>.md # Cada story tiene su propio archivo de especificación.
│   └── INI-<zettelkasten-identifier>-<title>.md # Cada iniciativa tiene su propio archivo de especificación.
```

> [!NOTE]
> **Zettelkasten-identifier** sigue la numeración Luhmann (ej: 2.1, 2.1.1, 2.1.2) que refleja la construcción temporal del conocimiento y se alinea con los sistemas arquitectónicos del proyecto.

## Iniciativas

Una iniciativa representa una etapa de desarrollo que tiene un objetivo y una duración definida. Permite agrupar epicas e historias asignando a un responsable del proyecto o equipo de trabajo. Puede durar desde 1 mes, varios meses o incluso hasta 1 año. Las iniciativas abarcan una amplia variedad de areas en Cedeira, pueden existir iniciativas de desarrollo de Software, iniciativas de mejoras de procesos en RRHH, iniciativas de pruebas de concepto, iniciativas de capacitación, etc.

Cada iniciativa:

- Se identifica con un código interno `INI-<zettelkasten-identifier>-<title>`.
- En la estructura de carpetas de este repositorio, se encuentra en la carpeta `iniciatives`.
- Tiene su propio archivo de especificación `iniciatives/INI-<zettelkasten-identifier>-<title>/iniciative.md`.
- Se completa siguiendo la plantilla de especificación de iniciativas disponible en `templates/iniciative.md`.

> [!NOTE]
> No debería quedar ninguna sección vacía en el archivo de especificación de la iniciativa.

## Epics

Un epic representa una tarea compleja que se divide en varias stories. Cada epica debe estar dentro de una iniciativa.

Cada epica:

- Se identifica con un código interno `EPIC-<zettelkasten-identifier>-<title>`.
- En la estructura de carpetas de este repositorio, se encuentra en la carpeta `iniciatives/INI-<zettelkasten-identifier>-<title>/epics`.
- Tiene su propio archivo de especificación `iniciatives/INI-<zettelkasten-identifier>-<title>/epics/EPIC-<zettelkasten-identifier>-<title>.md`.
- Se completa siguiendo la plantilla de especificación de epics disponible en `templates/epic.md`.

> [!NOTE]
> Es posible que alguna sección de dependencias, recursos o supuestos clave, queden vacías. Si alguna sección de la plantilla va a quedar vacía, porque no se aplica a la epica, se completa con un `No aplica`.

## Stories

Una story representa una tarea concreta que se realiza en una iniciativa.

Cada story:

- Se identifica con un código interno `STORY-<zettelkasten-identifier>-<title>`.
- En la estructura de carpetas de este repositorio, se encuentra en la carpeta `iniciatives/INI-<zettelkasten-identifier>-<title>/epics/EPIC-<zettelkasten-identifier>-<title>/stories`.
- Tiene su propio archivo de especificación `iniciatives/INI-<zettelkasten-identifier>-<title>/epics/EPIC-<zettelkasten-identifier>-<title>/stories/STORY-<zettelkasten-identifier>-<title>.md`.
- Se completa siguiendo la plantilla de especificación de stories disponible en `templates/story.md`.

> [!NOTE]
> Es posible que alguna sección de dependencias, recursos o supuestos clave, queden vacías. Si alguna sección de la plantilla va a quedar vacía, porque no se aplica a la historia, se completa con un `No aplica`.

## Reflexiones y Retrorevisión

### Reflexiones de Historia

Cada historia debe generar un **zettel de reflexión** que documente:
- Logros principales y artefactos generados
- Aprendizajes técnicos y metodológicos
- Preparación para la siguiente historia
- Contexto temporal para futuras referencias

**Ubicación**: `.vibedoc/ideas/<zettelkasten-id> - reflexion <story-identifier>.md`  
**Ejemplo**: `1h2 - reflexion story-2.1.1-preparacion-zettels-entrada.md`

### Reflexión de Épica

Al completar una épica, crear una **reflexión épica** que incluya:
- Evaluación completa de logros vs objetivos
- Métricas de éxito y lecciones aprendidas
- Impacto en el proyecto y preparación futura
- Validación de metodología aplicada

### Retrorevisión de Documentación

Post-épica, realizar **retrorevisión** de documentación:
1. **README Vibedoc**: Actualizar con nuevos aprendizajes metodológicos
2. **Architecture.md**: Verificar alineación con cambios estructurales
3. **Templates**: Incorporar mejoras basadas en experiencia práctica
4. **Validación**: Confirmar coherencia documental completa

Esta fase asegura que el conocimiento generado se preserve y beneficie futuras iniciativas.
