# [research-and-assessment-of-the-problem] - <name> <!-- omit in toc -->

> Este documento debe ser una continuación del documento de contexto del proyecto. Consiste en una descripción detallada de los procesos del problema actual que se busca resolver con la solución de software, los actores involucrados y las integraciones con otros sistemas. No busca aportar soluciones, sino describir el problema tal como es. Invita a los diseñadores de producto a entender el problema, generar actividades de investigación y relevamiento de forma proactiva e iterativamente. Se trata de un documento que debe ser leído por todos los miembros del equipo de producto. Debe estar enfocado en la comprensión del problema, la identificación de los factores que lo afectan.
> El documento completo será la base para la generación y discusión iterativa de soluciones de software.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Introducción al problema](#introducción-al-problema)
- [👥 Actores](#-actores)
  - [Diagrama de Flujo de Datos del problema de Nivel 0](#diagrama-de-flujo-de-datos-del-problema-de-nivel-0)
- [⚙️ Procesos del problema](#️-procesos-del-problema)
  - [Diagrama de Flujo de Datos del problema de Nivel 1](#diagrama-de-flujo-de-datos-del-problema-de-nivel-1)
- [🔍 Flujos detallados de procesos del problema seleccionados](#-flujos-detallados-de-procesos-del-problema-seleccionados)
- [🔗 Integraciones con otros sistemas](#-integraciones-con-otros-sistemas)
- [🌐 Entorno de Implementación](#-entorno-de-implementación)

## Introducción al problema

> En esta sección se debe describir el propósito del análisis funcional del problema. Se debe explicar qué se busca analizar y qué se espera obtener como resultado. Se debe explicar el contexto del problema que busca resolver al incluir soluciones de software.
> Explica en razgos generales los procesos funcionales involucrados, los actores y las integraciones con otros sistemas. Deja entrever los desafios que se deben resolver para que la solución sea efectiva a partir de un entendimiento general de la naturaleza del problema. Se trata de una narrativa extensa. Es una continuación de la sección de contexto del proyecto, que incorpora más detalles sobre los elementos fucnionales involucrados en sus procesos.
>  P. ej. (E-commerce): Los procesos actuales de venta son manuales y no permiten la personalización de la experiencia del cliente. Las ventas se dividen en dos canales: ventas por catálogo y ventas por distribuidores externos. La venta por catálogo es la que genera más ingresos, pero la red de promotores y líderes de áreas dificulta en gran medida la actualización de información de precios y productos. Para que una venta por catálogo llege a concretarse, el proceso es largo y complejo. En una primera etapa...
>  P. ej. (Sistema de Gestión Interna): El proceso actual para la gestión de RRHH en Novafuria es manual y se basa en hojas de cálculo y correos electrónicos. Esto genera errores frecuentes, retrasos en las aprobaciones y una gran carga de trabajo para el personal administrativo. Con el crecimiento de la empresa, este sistema se ha vuelto insostenible y está afectando negativamente la moral de los empleados y la eficiencia operativa. Entre las gestiones más frecuentes se encuentran las solicitudes de vacaciones, que son gestionadas por el personal administrativo. Por lo general, cada departamento realiza una solicitud de vacaciones, y el personal administrativo debe...

## 👥 Actores

> En esta sección se explica narrativamente quienes son las entidades del problema, entidades externas y quien/s es el/los actor/es. Identifica y describe todos los actores (personas, entidades, sistemas) que interactuarán con los procesos que se busca analizar. Para cada actor, se debe especificar qué tipo de interacción tiene con el sistema y cuáles son sus responsabilidades, restricciones y capacidades principales. Esto ayuda a entender quiénes son los usuarios y qué pueden hacer. Se debe especificar si el actor es interno o externo al sistema.

### Diagrama de Flujo de Datos del problema de Nivel 0

> En esta sección incluiremos uno o más Diagramas de Flujo de Datos (DFD) de Nivel 0, también conocido como Diagrama de Contexto. Este diagrama ofrece una vista panorámica del sistema, mostrando sus fronteras, las entidades externas con las que interactúa y los flujos de información principales entre ellos. Este diagrama es fundamental y sirve como punto de partida para todo el análisis posterior. Permite establecer el alcance funcional de los procesos actuales que se están analizando y permite identificar los límites del sistema que hay que diseñar.
> Se sugiere usar la herramienta [Mermaid](https://mermaid.js.org/) para generar los diagramas. Con estilos y colores se puede mejorar la legibilidad. 
> El siguiente es un ejemplo de diagrama de flujo de datos de alto nivel para un sistema de e-commerce.
> ```mermaid
> graph TD
>     %% --- Proceso Central (El Sistema como un todo) ---
>     P0((Sistema E-commerce))
>     style P0 fill:#ccf,stroke:#333,stroke-width:4px,color:#000
> 
>     %% --- Actores Externos ---
>     A_Visitante(["fa:fa-user Visitante"])
>     style A_Visitante fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     
>     A_Cliente(["fa:fa-user Cliente Registrado"])
>     style A_Cliente fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     
>     A_Admin(["fa:fa-user-cog Administrador"])
>     style A_Admin fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     
>     A_Pagos(["fa:fa-credit-card Sistema de Pagos"])
>     style A_Pagos fill:#5a5,stroke:#333,stroke-width:4px,color:#000
> 
>     %% --- Flujos de Datos Externos ---
>     A_Visitante -- "Consultas del catálogo" --> P0
>     P0 -- "Información de productos" --> A_Visitante
> 
>     A_Cliente -- "Gestión de cuenta y compras" --> P0
>     P0 -- "Confirmaciones y datos de cuenta" --> A_Cliente
> 
>     A_Admin -- "Solicitudes de gestión y reportes" --> P0
>     P0 -- "Reportes de ventas y stock" --> A_Admin
> 
>     P0 -- "Datos de la transacción" --> A_Pagos
>     A_Pagos -- "Resultado del pago" --> P0
> ```

## ⚙️ Procesos del problema

> Aquí se describen los flujos de trabajo o casos de uso clave del sistema desde una perspectiva funcional. Se debe detallar el paso a paso de las interacciones más importantes entre los actores y las acciones que se realizan actualmente y las fuentes de información que se utilizan sin entrar en detalles técnicos de implementación. Este mapa servira como base para determinar que procesos se podrán mejorar con la solución de software y cuales no. El objetivo es definir "qué" hace el sistema actual, no "cómo" lo hace.

### Diagrama de Flujo de Datos del problema de Nivel 1

> En esta sección incluiremos uno o más Diagramas de Flujo de Datos (DFD) de Nivel 1 que muestran los procesos del problema de manera más detallada. Permite conocer cuales son las funciones principales del problema, cómo colaboran entre sí estas funciones y qué información fundamental es gestionada. Esta información será especialmente útil para los jefes de producto y los arquitectos de software, ya que permite entender el problema desde una perspectiva funcional y sistematica.
> Se sugiere usar la herramienta [Mermaid](https://mermaid.js.org/) para generar los diagramas. Con estilos y colores se puede mejorar la legibilidad. 
> El siguiente es un ejemplo de diagrama de flujo de datos de alto nivel para un sistema de e-commerce.
> ```mermaid
> graph TD;
>     %% --- 1. Actores (Entidades Externas) ---
>     A_Visitante(["fa:fa-user Visitante"])
>     style A_Visitante fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     A_Cliente(["fa:fa-user Cliente Registrado"])
>       style A_Cliente fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     A_Admin(["fa:fa-user-cog Administrador"])
>     style A_Admin fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     A_Pagos(["fa:fa-credit-card Sistema de Pagos"])
>     style A_Pagos fill:#5a5,stroke:#333,stroke-width:4px,color:#000
>     %% --- 2. Procesos (Funciones Principales) ---
>     P1a((Consultar producto))
>     P1b((Leer información de producto))
>     P1c((Leer stock y precio))
>     P2a((Consultar cuenta))
>     P2b((Crear/Actualizar cuenta))
>     P3a((Agregar al carrito / Finalizar compra))
>     P3b((Verificar datos del cliente))
>     P3c((Verificar stock del producto))
>     P3d((Crear/Actualizar orden))
>     P3e((Enviar datos de transacción))
>     P3f((Confirmar orden))
>     P4a((Solicitar reporte))
>     P4b((Leer datos de venta))
>     P4c((Leer datos de inventario))
>     P4d((Generar reporte de ventas y stock))
>     %% --- 3. Almacenes de Datos (Cajas) ---
>     D1[("fa:fa-database D1: Productos")]
>     style D1 fill:#f55,stroke:#333,stroke-width:4px,color:#000
>     D2[("fa:fa-database D2: Clientes")]
>     style D2 fill:#f55,stroke:#333,stroke-width:4px,color:#000
>     D3[("fa:fa-database D3: Pedidos")]
>     style D3 fill:#f55,stroke:#333,stroke-width:4px,color:#000
>     subgraph "1.0 Gestionar Catálogo"
>         A_Visitante --> P1a
>         P1b --> A_Visitante
>         P1c --> D1
>         D1 --> P1b
>     end
>     subgraph "2.0 Gestionar Cuentas"
>        A_Cliente --> P2a
>         P2b --> D2
>         D2 --> P2b
>     end
>     subgraph "3.0 Procesar Pedidos"
>         A_Cliente --> P3a
>         P3b --> D2
>         P3c --> D1
>         P3d --> D3
>         D3 --> P3d
>         P3e --> A_Pagos
>         A_Pagos --> P3f
>         P3f --> D3
>     end
>     subgraph "4.0 Generar Reportes"
>         A_Admin --> P4a
>         P4b --> D3
>         P4c --> D1
>         D3 --> P4b
>         D1 --> P4c
>         P4d --> A_Admin
>     end
> ```

## 🔍 Flujos detallados de procesos del problema seleccionados

> En esta sección se describen los flujos de trabajo o casos de uso clave del problema desde una perspectiv procedural. Aborda uan selección de flujos y procesos que serán mejorados por la solución de software. Esta primer selección se logra tras la identificacion de puntos de dolor en el proceso actual, identificados en los diagramas de flujo de datos de nivel 1.
> Se debe detallar el paso a paso de las interacciones más importantes entre los actores y las acciones que se realizan actualmente y las fuentes de información que se utilizan sin entrar en detalles técnicos de implementación. Estos flujos, junto al mapa conceptual de procesos del problema, permiten identificar puntos de dolor en el proceso actual y por tanto alcanzar una comprensión completa y coherente de los procesos que se deberían mejorar con la solución de software.
> Se sugiere crear una sección por cada flujo y completarlo con un diagrama BPMN, insertando un enlace a un diagrama BPMN.io o Darw.io. Debe ir acompañado por una explicación narrativa. A modo de ejemplo, se muestra el flujo de compra de un cliente registrado.
> 
> ### Flujo de compra de un cliente registrado
>
> [Diagrama BPMN.io](https://bpmn.io/editor/index.html)
>
> Cuando un promotor visita el domicilio de un cliente registrado, deja el catálogo de productos por unos días. Durante ese periodo el cliente selecciona los productos que desea comprar comparando precios, características y recordando el número de identificación de los productos. Si surge alguna duda, el cliente puede...

## 🔗 Integraciones con otros sistemas

> En esta sección se listan y describen todos los sistemas externos con los que la solución necesitará comunicarse. Para cada integración, se debe especificar el propósito de la misma, qué tipo de datos se intercambian y, si es posible, el método de comunicación (ej. API REST, SOAP, Webhooks, etc.).
> P. ej. (E-commerce): El sistema de e-commerce de Naturastore necesita integrar con una pasarela de pagos (Mercado Pago) para procesar las transacciones de compra. También necesita enviar correos electrónicos de confirmación de compra y envío de pedido a los clientes. Las credenciales de acceso...
> P. ej. (Sistema de Gestión Interna): El sistema de gestión interna de RRHH de Novafuria necesita integrar con un sistema de liquidación de sueldos (Tango Gestión) para obtener la información de los recibos de sueldo de los empleados. También necesita integrar con el Directorio Activo local para autenticar a los usuarios del sistema. Se espera que...

## 🌐 Entorno de Implementación

> Aquí se describen los requisitos y características técnicas de los recursos físicos y lógicos con los que cuenta los actores involucrados en el problema actualmente. Consiste en una descripción del entorno en el que se espera que la solución de software debe operar y en el que se debe implementar la solución. Esto incluye detalles sobre los servidores, bases de datos, servicios en la nube y cualquier otra dependencia de infraestructura necesaria para que la solución funcione correctamente. Debe incluir cualquier detalle que sea relevante para la implementación de la solución de software, como la ubicación de los servidores, la red de comunicaciones, la seguridad, etc.
> P. ej. (E-commerce): El sistema de e-commerce de Naturastore opera en un entorno cloud, con una plataforma de pago en línea (Mercado Pago) y un sistema de gestión de inventario (ERP Interno). El sistema se ejecuta en contenedores Docker y utiliza AWS como proveedor de servicios en la nube.
> P. ej. (Sistema de Gestión Interna): El sistema de gestión interna de RRHH de Novafuria opera en un entorno on-premise, con un servidor de aplicaciones Java (Apache Tomcat) y una base de datos Microsoft SQL Server 2019. El sistema se ejecuta en servidores virtualizados con VMware y utiliza el Directorio Activo local como sistema de autenticación. La aplicación será accesible internamente a través de la URL `http://portalrrhh.cedeira.local`. No tendrá exposición a internet. Aunque si emplean una base de datos Microsoft SQL Server 2019, utilizando una instancia existente en la infraestructura de la empresa.
