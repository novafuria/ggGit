# Guía de Etapa 5: Arquitectura de Software

Bienvenido a la sexta y última etapa de ***Vibedoc***. Con un diseño de producto completo y validado, ahora nos enfocamos en definir la arquitectura técnica que hará realidad la solución. Esta etapa es fundamental para traducir los requisitos funcionales y de diseño en una estructura técnica sólida, escalable y mantenible.

El objetivo aquí es crear una arquitectura de software que se adapte al tipo específico de proyecto, considerando que no todos los proyectos requieren los mismos componentes (frontend, backend, base de datos, etc.). La arquitectura debe ser flexible y evolucionar según las necesidades específicas del proyecto.

## 🎯 Objetivo de esta Etapa

Al finalizar esta etapa, tendrás un documento (`/.vibedoc/05_architecture/ARCHITECTURE_TEMPLATE.md` completado) que responde a las siguientes preguntas fundamentales:

- ¿Cuál es la estructura técnica general de la solución? (Arquitectura General)
- ¿Qué componentes específicos necesita este proyecto? (Componentes del Sistema)
- ¿Cómo se comunican e integran los diferentes elementos? (Comunicación e Integración)
- ¿Qué patrones arquitectónicos y tecnologías son más apropiados? (Patrones y Tecnologías)
- ¿Cómo se asegura la calidad, seguridad y observabilidad del sistema? (Calidad y Operaciones)

## 📜 Artefactos de esta Etapa

`/.vibedoc/05_architecture/ARCHITECTURE_TEMPLATE.md`: La plantilla principal que incluye:
- Descripción general de la arquitectura
- Componentes específicos del sistema (adaptables al proyecto)
- Patrones de comunicación e integración
- Consideraciones de seguridad y observabilidad
- Integraciones con sistemas externos

## 🤖 Cómo Trabajar en esta Etapa (El Diálogo ***Vibedoc***)

El proceso continúa siendo una conversación colaborativa. Utiliza a tu asistente de IA como un arquitecto de software experto que te ayuda a diseñar una solución técnica que se adapte perfectamente a las necesidades específicas de tu proyecto.

1. **Usa el Contexto Previo:** Los documentos de las etapas anteriores son tu base:
   - `/.vibedoc/00_project/project.md` (visión del proyecto)
   - `/.vibedoc/01_research-and-assessment-of-the-problem/research-and-assessment-of-the-problem.md` (análisis del problema)
   - `/.vibedoc/02_research-of-references-and-collections/research-of-references-and-collections.md` (investigación de referencias)
   - `/.vibedoc/03_value-proposition/VALUE_PROPOSITION_CANVAS_TEMPLATE.md` (propuesta de valor)
   - `/.vibedoc/04_product-design/PRODUCT_DESIGN_TEMPLATE.md` (diseño del producto)

2. **Abre un Chat con tu IA:** Inicia una conversación con tu asistente.

3. **Selecciona el Artifex adecuado:** Elige un Artifex especializado en arquitectura de software, patrones de diseño, o la tecnología específica de tu proyecto.

4. **Usa un Prompt Inicial Fuerte:** Establece el nuevo marco de la conversación.

> Basado en nuestro diseño de producto, ahora necesito tu ayuda para definir la arquitectura técnica de la solución. Actúa como un arquitecto de software experto. Tu rol es guiarme para crear una arquitectura que se adapte perfectamente al tipo de proyecto que estamos desarrollando, considerando que no todos los proyectos necesitan los mismos componentes. Usaremos la plantilla `/.vibedoc/05_architecture/ARCHITECTURE_TEMPLATE.md` como base, pero la adaptaremos según las necesidades específicas. ¡Empecemos!

5. **Itera y Refina:** A través del diálogo, la IA te ayudará a:
   - Identificar qué componentes son realmente necesarios para tu proyecto
   - Adaptar la plantilla de arquitectura a tus necesidades específicas
   - Elegir patrones arquitectónicos apropiados
   - Definir tecnologías y herramientas específicas
   - Generar diagramas de arquitectura cuando sea útil

## 🏗️ Tipos de Proyectos y Adaptación de la Arquitectura

### **Aplicaciones Web Tradicionales**
- **Componentes típicos:** Frontend, Backend, Base de datos, Sistema de autenticación
- **Adaptaciones:** Arquitectura cliente-servidor, APIs REST/GraphQL, SPA o SSR

### **Aplicaciones Móviles**
- **Componentes típicos:** App nativa/híbrida, Backend, Base de datos, APIs
- **Adaptaciones:** Arquitectura móvil-first, sincronización offline, push notifications

### **APIs y Microservicios**
- **Componentes típicos:** Servicios individuales, Gateway API, Base de datos distribuida
- **Adaptaciones:** Arquitectura de microservicios, comunicación asíncrona, service mesh

### **Librerías y SDKs**
- **Componentes típicos:** Código fuente, documentación, tests, ejemplos
- **Adaptaciones:** Arquitectura modular, interfaces claras, versionado semántico

### **Sistemas Embebidos/IoT**
- **Componentes típicos:** Firmware, sensores/actuadores, comunicación de red
- **Adaptaciones:** Arquitectura en tiempo real, gestión de recursos limitados

### **Aplicaciones de Escritorio**
- **Componentes típicos:** Interfaz de usuario, lógica de negocio, almacenamiento local
- **Adaptaciones:** Arquitectura monolítica, gestión de estado local, actualizaciones

## 🔧 Componentes Adaptables del Sistema

### **1. Descripción General**
- Visión de alto nivel de la arquitectura
- Principios y decisiones arquitectónicas clave
- Restricciones técnicas y del proyecto

### **2. Sistema de Almacenamiento de Datos**
- **Aplicable cuando:** El proyecto requiere persistencia de datos
- **Alternativas:** Base de datos relacional, NoSQL, archivos, memoria, blockchain
- **Consideraciones:** Escalabilidad, consistencia, disponibilidad

### **3. Frontend (Solo si es necesario)**
- **Aplicable cuando:** El proyecto requiere interfaz de usuario
- **Alternativas:** Web, móvil, escritorio, línea de comandos, API
- **Consideraciones:** Framework, responsividad, accesibilidad

### **4. Backend (Solo si es necesario)**
- **Aplicable cuando:** El proyecto requiere lógica de servidor
- **Alternativas:** API REST, GraphQL, microservicios, serverless
- **Consideraciones:** Escalabilidad, rendimiento, mantenibilidad

### **5. Sistema de Seguridad**
- **Aplicable cuando:** El proyecto maneja datos sensibles o usuarios
- **Alternativas:** Autenticación, autorización, encriptación, auditoría
- **Consideraciones:** Compliance, amenazas, vulnerabilidades

### **6. Sistema de Observabilidad**
- **Aplicable cuando:** El proyecto requiere monitoreo y debugging
- **Alternativas:** Logging, métricas, tracing, alertas
- **Consideraciones:** Visibilidad, troubleshooting, performance

### **7. Comunicación Interna**
- **Aplicable cuando:** El proyecto tiene múltiples componentes
- **Alternativas:** APIs, mensajería, eventos, RPC
- **Consideraciones:** Latencia, confiabilidad, consistencia

### **8. Integraciones con Terceros**
- **Aplicable cuando:** El proyecto se conecta con sistemas externos
- **Alternativas:** APIs, webhooks, SDKs, protocolos estándar
- **Consideraciones:** Confiabilidad, rate limiting, fallbacks

## 🎨 Patrones Arquitectónicos Recomendados

### **Arquitectura Monolítica**
- **Cuándo usar:** Proyectos pequeños a medianos, equipos pequeños
- **Ventajas:** Simplicidad, desarrollo rápido, testing fácil
- **Desventajas:** Escalabilidad limitada, acoplamiento alto

### **Arquitectura de Microservicios**
- **Cuándo usar:** Proyectos grandes, equipos grandes, alta escalabilidad
- **Ventajas:** Escalabilidad, independencia de equipos, tecnologías diversas
- **Desventajas:** Complejidad, testing distribuido, operaciones complejas

### **Arquitectura Event-Driven**
- **Cuándo usar:** Sistemas reactivos, procesamiento asíncrono
- **Ventajas:** Desacoplamiento, escalabilidad, resiliencia
- **Desventajas:** Complejidad, debugging difícil, consistencia eventual

### **Arquitectura Serverless**
- **Cuándo usar:** Cargas variables, desarrollo rápido, bajo mantenimiento
- **Ventajas:** Escalabilidad automática, sin gestión de infraestructura
- **Desventajas:** Vendor lock-in, cold starts, debugging limitado

## 💡 Consejos para una Arquitectura Efectiva

1. **Adapta al Proyecto:** No uses componentes que no necesites.
2. **Piensa en el Futuro:** Diseña para escalar, pero no sobre-diseñes.
3. **Considera el Equipo:** La arquitectura debe ser comprensible para tu equipo.
4. **Documenta las Decisiones:** Cada decisión arquitectónica debe tener una justificación.
5. **Valida con Stakeholders:** Asegúrate de que la arquitectura cumple con los requisitos no funcionales.

## 🔄 Adaptación de la Plantilla

### **Paso 1: Identificar el Tipo de Proyecto**
- Determina qué componentes son realmente necesarios
- Elimina secciones que no aplican a tu caso

### **Paso 2: Personalizar las Secciones**
- Adapta el contenido a tu tecnología específica
- Agrega consideraciones particulares de tu dominio

### **Paso 3: Generar Diagramas**
- Crea diagramas de arquitectura específicos para tu proyecto
- Usa herramientas como Mermaid, Draw.io, o Lucidchart

### **Paso 4: Validar y Refinar**
- Revisa la arquitectura con el equipo técnico
- Asegúrate de que cumple con los requisitos del proyecto

## 🚀 Siguiente Paso

Una vez completada esta etapa, tendrás una arquitectura técnica sólida y adaptada a tu proyecto específico. Esto te preparará para comenzar la implementación real del producto, con una base técnica clara y bien documentada.

> [!TIP]
> Recuerda: La mejor arquitectura es la más simple que resuelve tu problema. No agregues complejidad innecesaria solo porque "es lo que se hace".

> [!WARNING]
> No copies arquitecturas de otros proyectos sin entender por qué funcionan. Cada proyecto tiene necesidades únicas que requieren soluciones únicas.

> [!NOTE]
> Esta plantilla es un punto de partida. Adáptala, modifícala y hazla tuya según las necesidades específicas de tu proyecto.
