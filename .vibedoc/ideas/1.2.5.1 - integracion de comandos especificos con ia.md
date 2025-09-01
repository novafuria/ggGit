# integracion de comandos especificos con ia

## Idea
Vamos a integrar los comandos especificos con la IA.

La IA es un componente clave de ggGit, y debe ser integrada en los comandos especificos. En esta oportunidad no se trata de hacer un nuevo comando con IA sino de integrar la capacidad de razonamiento y generacion de texto de los modelos LLM a los comando especificos ya existentes.

LA idea es simple, hasta ahora ggGit requeria generalmente de parametros para operar sin esos argumentos el comando fallaba. Pero ahora podemos delegar ciertos valores de parametros a la IA. El comando `ggfeat` es un buen ejemplo, ya que podemos delegar el mensaje de commit a la IA.

Los comandos que realizan un commit con conventional commits pueden incorporar este tipo de funcionalidad al ser ejecutados sin argumentos. Esto significa que se debe incorporar una logica para detectar cuando no se han proporcionado argumentos y generar un mensaje de commit con IA. El mensaje no puede ser cualquier mensaje, debe ser un mensaje valido para un commit con conventional commits y estar relacionado con los archivos modificados y los cambios realizados.

Que los comandos especificos se ejecuten sin parametros es una caracteristica nueva que podemos incorporar, pero habra que adecuar el documento de arquitectura ya que ahi indica que deberiamos usar flags para activar esta funcionalidad. En la practica resultará un poco mas natural de usar sin flags.

En el documento de [arquitectura](../architecture.md) y [product-design](../product-design.md) se explica algunas de las características que la IA puede usar para evaluar el tipo de cambio y redactar un mensaje:

- Categorización automática de archivos por tipo (source, test, docs, config, assets)
- Detección de patrones de cambios (bug fix, feature, refactor, docs)
- Análisis de diffs para determinar el tipo de cambio
- Sugerencia automática del tipo de commit

Se podría incorporar en la configuracion sobre IA, parametros para limitar el largo del mensaje por ejemplo. Habria que pensalo un poco mas.
