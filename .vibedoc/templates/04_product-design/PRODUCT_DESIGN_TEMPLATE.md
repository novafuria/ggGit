# [product-design] - <name> <!-- omit in toc -->

> Este documento debe ser una continuación del documento [02-research-of-references-and-collections](02-research-of-references-and-collections.md). Consiste en la creación de un diseño de producto que resuelva el problema planteado en el documento [01-research-and-assessment-of-the-problem](01-research-and-assessment-of-the-problem.md).
> Se compone de una combinación de métodología lienzo canvas y sketch de producto funcionales con flujos bpmn simplificados.
> Permite generar ideas de solución y validar las propuestas de valor con los interesados.

## 📋 Tabla de Contenidos <!-- omit in toc -->

- [Descripción general](#descripción-general)
- [Glosario de términos y definiciones](#glosario-de-términos-y-definiciones)
- [Contexto: \<nombre de la pantalla, vista o proceso backend\>](#contexto-nombre-de-la-pantalla-vista-o-proceso-backend)
  - [Ciclo de vida](#ciclo-de-vida)
    - [Al iniciar el contexto](#al-iniciar-el-contexto)
    - [Al pasar a segundo plano](#al-pasar-a-segundo-plano)
    - [Al volver a primer plano](#al-volver-a-primer-plano)
    - [Al volver a la aplicación](#al-volver-a-la-aplicación)
    - [Al finalizar el contexto](#al-finalizar-el-contexto)
  - [Acciones](#acciones)
    - [\<nombre de la acción\>](#nombre-de-la-acción)
      - [Descripción](#descripción)
      - [Beneficios](#beneficios)
      - [Casos de uso](#casos-de-uso)
        - [Título descriptivo del caso de uso (p. ej., Confirmar la creación de un nuevo grupo para auditores)](#título-descriptivo-del-caso-de-uso-p-ej-confirmar-la-creación-de-un-nuevo-grupo-para-auditores)
        - [Título descriptivo de otro caso de uso (p. ej, Ver rápidamente los tipos de objeto que puede filtrar)](#título-descriptivo-de-otro-caso-de-uso-p-ej-ver-rápidamente-los-tipos-de-objeto-que-puede-filtrar)
  - [Flujos de procesos](#flujos-de-procesos)
    - [Flujo de proceso 1](#flujo-de-proceso-1)
    - [Flujo de proceso 2](#flujo-de-proceso-2)

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

## Glosario de términos y definiciones

> Consiste en una lista de términos y definiciones propios del producto y que reflejan el enfoque de la solución.

## Contexto: <nombre de la pantalla, vista o proceso backend>

> Con la información de la infografía se debe crear un texto extensivo que permita comprender la solución y sus dinámicas de forma completa solo con la lectura. Por cada pantalla, vista o proceso backend que se incluya en la infografía se debe incluir una imagen y una serie de secciones que describan las acciones y eventos, el ciclo de vida y los componentes involucrados. Estas secciones se llamarán contextos.

### Ciclo de vida

#### Al iniciar el contexto

> Qué sucede con el contexto cuando el usuario persibe que se inicia por primera vez?

#### Al pasar a segundo plano

> Qué sucede con el contexto cuando el usuario persibe que se pasa a segundo plano, por ejemplo, cuando se navega a otra pantalla?

#### Al volver a primer plano

> Qué sucede con el contexto cuando el usuario persibe que se vuelve a primer plano, por ejemplo, cuando se vuelve a la pantalla anterior?

#### Al volver a la aplicación

> Qué sucede con el contexto cuando el usuario persibe que se vuelve a la aplicación, por ejemplo, cuando se vuelve a la pantalla principal?

#### Al finalizar el contexto

> Qué sucede con el contexto cuando el usuario persibe que se finaliza, cierra o cancela el contexto?

### Acciones

> Consiste en una serie de acciones que se pueden realizar en el contexto. Estas acciones se pueden realizar por el usuario o por el sistema. Generalmente implica un cambio de estado del contexto. Si el flujo de la acción es complejo, se puede contemplar la creación de un diagrama BPMN. En caso contrario, una descripción textual de la acción es suficiente.

#### <nombre de la acción>
##### Descripción

> Describe el problema o la necesidad puntual del usuario que esta funcionalidad busca resolver (p.ej, En la columna de "Acción", el usuario puede hacer clic en "Ver acciones" para abrir un diálogo. En este diálogo, los permisos del usuario se muestran agrupados por sección en un acordeón. Cada permiso indica si está asignado o no, y se muestra su descripción).
 
##### Beneficios

> Una lista o descripción con los beneficios claves que obtiene el usuario al poder realizar esta acción
> - p. ej., Logra mantener sincronizados los grupos de usuarios evitando fugas de seguridad
> - p. ej., Al redactar en la caja de texto del filtro, logra ver por medio de las sugerencias, nuevas opciones de consulta que le ayudarán a aplicar nuevas reglas de filtrado rápidamente

##### Casos de uso

> Son una serie de narraciones reales o simuladas que relatan situaciones que llevan al usuario a ejecutar la acción. Permite a los lectores entender desde el punto de vista del usuario, el contexto en el que la acción se ejecutará.

###### Título descriptivo del caso de uso (p. ej., Confirmar la creación de un nuevo grupo para auditores)

> Narración de la situación que lleva al usuario a ejecutar la acción, sus decisiones y sus consecuencias. (p. ej., Un nuevo equipo de contadores es creado en el cliente para auditar las operaciones realizadas por los usuarios operadores con el sistema. El Administrador debe otorgarles acceso a la aplicación, pero debe asegurarse de que sólo puedan ver los datos a auditar y que no puedan modificar o eliminar ningún registro. Para eso el Administrador decide crear un grupo específico para los auditores, asignando solo los permisos de lectura y consulta. Una vez que creo el grupo y visualiza en el resumen de la configuración decide ejecutar el guardado. Si todo sale bien, observará el cartel verde de confirmación.

###### Título descriptivo de otro caso de uso (p. ej, Ver rápidamente los tipos de objeto que puede filtrar)

> Narración de la situación que lleva al usuario a ejecutar la acción, sus decisiones y sus consecuencias. (p. ej., Encargaron a un usuario obtener un reporte de las operaciones muy particular. El usuario es nuevo, y no recuerda exactamente los valores que debe usar en las reglas de filtrados paraobtener los datos deseados. Antes que consultar la documentación decide probar suerte y ayudar a refrescar su memoria escribiendo en el filtro rápido el nombre del campo que necesita filtrar. Espera que, al ir escribiendo el nombre de la columna en la caja de texto del filtro, las sugerencias automáticas del sistema le muestre diferentes valores que el campo tipo de objeto puede contener y de esta forma si tiene suerte encontrar el valor que necesita).

### Flujos de procesos

> Consiste en una serie de flujos de procesos que se pueden realizar en el contexto. Estos flujos de procesos se pueden realizar por el usuario o por el sistema. Generalmente tienen un correlato con los flujos descriptos en el documento [02-research-of-references-and-collections](02-research-of-references-and-collections.md). Estos nuevos flujos permiten entender como las mejoras que trae la solución resuelven los problemas de los usuarios.

#### Flujo de proceso 1

> Diagrama: [flujo-proceso-1.png](flujo-proceso-1.png)
> Describe el flujo de proceso 1.

#### Flujo de proceso 2

> Diagrama: [flujo-proceso-2.png](flujo-proceso-2.png)
> Describe el flujo de proceso 2.
