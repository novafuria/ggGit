# [EPICA] - <name>

## 🎯 Objetivo de la Épica

> Describe el propósito principal de este épica. ¿Qué valor de negocio busca entregar? ¿Qué problema resuelve o qué oportunidad aprovecha? Sé conciso y enfócate en el resultado deseado.
> P. ej. (Pagos Fraccionados): Permitir a los usuarios cargar, editar y buscar pagos fraccionados
> P. ej. (DataIngester): Implementar los flujos pre-persistencia del sistema DataIngester
> P. ej. (Framework de Transacciones Paralelas): Recopilar y preparar los lineamientos generales para la construcción de un framework para transacciones paralelas distribuidas
> P. ej. (Configuración del Sistema - UX): Abordar el diseño de la experiencia de usuario para la configuración del sistema desde el punto de vista del administrador

## 🌎 Contexto y Justificación

> Proporciona el trasfondo necesario para entender esta épica. ¿Cuál es la situación actual que justifica este desarrollo? ¿Qué datos o insights respaldan la necesidad de esta épica? ¿Quiénes son los usuarios o segmentos de clientes afectados?
> P. ej. (Pagos Fraccionados): Actualmente, muchos usuarios abandonan sus carritos debido a la falta de opciones de pago flexible para compras de alto valor. Un estudio de mercado … indica que el 30% de los carritos abandonados tienen un valor superior a $500 y los usuarios expresan interés en planes de pago…
> P. ej. (DataIngester): En la actualidad existen muchos frameworks que buscan facilitar la ingesta de datos priorizando diferentes experiencias de desarrollo y arquitecturas técnicas. Propuestas No-Code, como el DTSX abordado en los últimos años en el Banco Galicia, presentan severos problemas a la hora de inyectar un gran número de datos. No sólo encontramos un impacto negativo al momento de persistir, sino támbien limitaciones al abordar el desarrollo de los procesos pre-persistencia. Estas limitaciones sugieren afrontar la ingesta de datos desde una nueva perspectiva que…
> P. ej. (Framework de Transacciones Paralelas): Las entidades financieras suelen trabajar continuamente con grandes cantidades transacciones y metadata asociada que requieren un procesamiento inmediato. A lo largo de los años en Cedeira se han propuesto diferentes arquitecturas que a pesar de sus ventajas y desventajas, quedan embebidos en soluciones específicas. Esto causa que cada vez que nos enfrentamos a una situación similar terminemos construyendo muchos elementos desde cero. Un marco común de desarrollo para el tratamiento de grandes lotes de información en ecosistemas distribuidos permitiría reducir gran carga del diseño de sistemas, y centrar los esfuerzos en el desarrollo de lógicas de negocio que aporten valor diferencial al cliente. Para lograr esta propuesta  será necesario realizar un relevamiento que… 
> P. ej. (Configuración del Sistema - UX): Desde un inicio surgió la necesidad de permitirle a un rol administrador realizar operaciones de configuración del sistema en tiempo real. La necesidad, planteada por el cliente, cubre aspectos de la consultas, construcción de reportes, categorización de tipos de facturación y bloqueo de permisos. Por el contrario la gestión de usuario queda delegado a servicios de autenticación de terceros. Esta flexibilidad busca darle la capacidad al cliente de poder reaccionar de manera inmediata a las fluctuaciones en las normativas y regulaciones provenientes de las entidades gubernamentales. La experiencia atravesada durante la implementación de una nueva reglamentación en Marzo del 2025, en sistemas que no soportaban estas características causó una cadena de incidentes que…

## 💡 Visión de la Solución

>Describe a alto nivel cómo se planea lograr el objetivo de la épica. ¿Cuál es la idea principal de la solución? ¿Qué componentes clave podría incluir? No es necesario detallar las historias de usuario aquí. Piensa en la arquitectura general o el enfoque funcional.
> P. ej. (Pagos Fraccionados): Se implementará un módulo de financiación en la pasarela de pago existente, permitiendo la selección de planes de cuotas. Esto incluirá cambios en el flujo de checkout, la integración con un proveedor de financiación externo y la visualización de opciones de pago en la página del producto.
> P. ej. (DataIngester): Se diseñará y construirá un microservicio de ingesta de datos con una arquitectura basada en eventos, utilizando Apache Kafka para la cola de mensajes y un motor de reglas personalizable para las transformaciones pre-persistencia. Este servicio será escalable y resiliente, permitiendo la definición de pipelines de ingesta a través de una API REST.
> P. ej. (Framework de Transacciones Paralelas): Se realizará un relevamiento de soluciones existentes y se propondrá un diseño arquitectónico para un framework distribuido que soporte transacciones paralelas de alto volumen. Esto incluirá la identificación de patrones de concurrencia, mecanismos de consenso (ej. Two-Phase Commit simplificado) y la selección de tecnologías clave (ej. bases de datos distribuidas, sistemas de mensajería). El entregable será un documento de diseño conceptual y un prototipo inicial de la infraestructura.
> P. ej. (Configuración del Sistema - UX): Se elaborarán wireframes, flujos de usuario y prototipos interactivos para las pantallas de configuración del sistema desde la perspectiva del administrador. Se hará énfasis en la claridad de la información, la facilidad de navegación y la retroalimentación visual. Esto incluirá el diseño de interfaces para la gestión de categorías de facturación, definición de reportes y asignación de permisos a roles predefinidos, excluyendo la gestión individual de usuarios.

## 🚀 Alcance de la Épica

### Debe Tener

> Enumera las funcionalidades y requisitos esenciales que deben ser entregados para que esta épica se considere completa y cumpla su objetivo principal. Sin esto, la épica no tendría valor significativo.
> P. ej. (Pagos Fraccionados): “Carga inicial de planes de pago ofrecidos por el proveedor externo.”, “Selección y aplicación de un plan de pago en el checkout.”, “Visualización del resumen de cuotas antes de confirmar la compra.”
> P. ej. (DataIngester): “Capacidad para recibir datos vía API REST y encolarlos en Kafka.” “Implementación de un conector básico para una fuente de datos (ej. CSV).” “Definición de un esquema de datos inicial para la validación pre-persistencia.”
> P. ej. (Framework de Transacciones Paralelas): “Documento de arquitectura conceptual con patrones identificados.” “Prototipo de un mecanismo básico de coordinación entre nodos. “Benchmarking inicial de rendimiento en un entorno de pruebas con datos simulados.”
> P. ej. (Configuración del Sistema - UX): “Flujos de usuario completos para la creación y edición de categorías de facturación.” “Wireframes de alta fidelidad para las pantallas de configuración de reportes básicos.” “Guías de estilo y componentes de UI para la sección de administración.”

- ✅ 

### Podría Tener

>Enumera las funcionalidades o mejoras deseables que, si bien aportan valor, no son críticas para la primera la épica. Podrían ser consideradas en futuras épicas o si el tiempo y los recursos lo permiten.
> P. ej. (Pagos Fraccionados): “Notificaciones al usuario sobre el estado de sus pagos fraccionados.”, “Integración con un segundo proveedor de financiación para comparación.”
> P. ej. (DataIngester): “Un panel de monitoreo básico para los flujos de ingesta.”, “Implementación de un conector para una base de datos relacional.”
> P. ej. (Framework de Transacciones Paralelas): “Un ejemplo de implementación de un caso de uso simple usando el framework.”, “Análisis de costo/beneficio de las tecnologías propuestas.”
> P. ej. (Configuración del Sistema - UX): “Diseño de microinteracciones para la retroalimentación de acciones.”, “Prototipo funcional navegable de la sección de permisos.” 

- ✨ 

## Fuera de Alcance

> Especifica claramente lo que NO será parte de esta épica. Esto ayuda a gestionar las expectativas y evitar malentendidos sobre lo que se entregará.
> P. ej. (Pagos Fraccionados): “Gestión de reclamos o disputas de pagos fraccionados.”, “Modificación de planes de pago una vez confirmada la compra.”
> P. ej. (DataIngester): “Persistencia final de los datos transformados en la base de datos de destino.”, ”Un editor gráfico de flujos de transformación (no-code).”
> P. ej. (Framework de Transacciones Paralelas): “Desarrollo de componentes de lógica de negocio específicos del cliente.”, ”Implementación completa de un sistema de mensajería desde cero.”
> P. ej. (Configuración del Sistema - UX): “Diseño de la gestión de usuarios (roles, permisos individuales).”, “Desarrollo front-end o back-end de la sección de administración.”

- 🚫 

##⚠️ Riesgos y Supuestos

### Riesgos Identificados

> Enumera los posibles riesgos que podrían impactar la entrega o el éxito de esta épica. Piensa en riesgos técnicos, de mercado, de recursos, etc.
> P. ej. (Pagos Fraccionados): “Baja adopción por parte de los usuarios si la interfaz no es clara.”, “Problemas de seguridad o cumplimiento con la normativa de pagos.”
> P. ej. (DataIngester): “Cuellos de botella en el rendimiento de Kafka si el volumen de datos excede las estimaciones iniciales.”, “Complejidad inesperada en la implementación de reglas de transformación.”
> P. ej. (Framework de Transacciones Paralelas): “Falta de compatibilidad entre las tecnologías candidatas identificadas.”, “La curva de aprendizaje del nuevo framework es demasiado alta para los equipos actuales.”
> P. ej. (Configuración del Sistema - UX): “Interpretación incorrecta de los requisitos del cliente para el flujo de configuración.”, “Dificultad para mantener la consistencia visual con el resto de la aplicación.”

- ❗

### Supuestos Clave

> Detalla los supuestos clave bajo los cuales se está planificando esta épica. Si estos supuestos resultan ser incorrectos, podría afectar el alcance, el tiempo o el costo.
> P. ej. (Pagos Fraccionados): “Asumimos que la API del proveedor de financiación es estable y está bien documentada.”, “Asumimos que los usuarios están familiarizados con el concepto de pagos fraccionados.”
> P. ej. (DataIngester): “Asumimos que el equipo de Infraestructura puede provisionar los recursos de Kafka en el plazo esperado.”, “Asumimos que los volúmenes de datos iniciales no superarán X terabytes por día.”
> P. ej. (Framework de Transacciones Paralelas): “Asumimos que los equipos de desarrollo tienen una base de conocimientos sólida en programación concurrente.”, “Asumimos que habrá tiempo disponible para investigar soluciones de código abierto.”
> P. ej. (Configuración del Sistema - UX): “Asumimos que la gestión de usuarios seguirá siendo externa y no será parte del alcance de administración.”, “Asumimos que las decisiones de diseño se basarán en las necesidades identificadas por el equipo de Producto.”

- ❓ 

## 🔗 Dependencias y Recursos Clave

### Dependencias

> Identifica cualquier dependencia externa o interna que pueda afectar el progreso de esta épica. ¿Qué otros equipos o proyectos necesitan entregar algo antes de que esta épica pueda avanzar?
> P. ej. (Pagos Fraccionados): “Equipo de Backend: Integración con la API del proveedor de pagos fraccionados.”, “Equipo de Legal: Aprobación de los términos y condiciones de los planes de pago.”
> P. ej. (DataIngester): “Equipo de Infraestructura: Configuración de los clústeres de Kafka y servidores para el microservicio.”, “Equipo de Arquitectura de Datos: Definición de los esquemas finales de destino de los datos.”
> P. ej. (Framework de Transacciones Paralelas): “Acceso a bases de conocimiento internas sobre sistemas distribuidos.”, “Aprobación del presupuesto para pruebas de concepto con tecnologías específicas.”
> P. ej. (Configuración del Sistema - UX): “Equipo de Producto: Definición final de los atributos de los reportes.”, “Equipo de Backend: Especificación de las APIs REST para la configuración.”

- 

### Recursos Clave Necesarios

> Lista los recursos críticos (personas, sistemas, herramientas, licencias, información) que son esenciales para la ejecución de esta épica.
> P. ej. (Pagos Fraccionados): “Experto en pasarelas de pago.”, “Documentación API del proveedor de financiación.”
> P. ej. (DataIngester): “Ingeniero de Datos con experiencia en Kafka.”, “Acceso a entornos de desarrollo y pruebas con Kafka.”
> P. ej. (Framework de Transacciones Paralelas): “Arquitecto de Software Senior con experiencia en sistemas distribuidos.”, “Acceso a literatura científica y papers sobre transacciones distribuidas.”
> P. ej. (Configuración del Sistema - UX): “Diseñador UX/UI Senior.”, “Herramienta de prototipado (ej. Figma, Sketch).”

- 
