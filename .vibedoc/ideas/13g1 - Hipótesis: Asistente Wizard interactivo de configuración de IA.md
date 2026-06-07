# 13g1 - Hipótesis: Asistente Wizard interactivo de configuración de IA

## Enunciado de la Hipótesis

**Dado** que el usuario final desea configurar la generación de mensajes con IA de forma ágil y sin memorizar nombres de variables de configuración,  
**Si** implementamos un comando interactivo nuevo llamado `ggconfigia` que actúe como un asistente (Wizard) paso a paso, guiando al usuario para seleccionar su proveedor (Ollama, OpenAI, Anthropic, etc.), solicitando interactivamente el token o credenciales, y sugiriendo valores por defecto inteligentes (p. ej., endpoint de Ollama en `http://localhost:11434` y modelo `gemma3:4b`),  
**Entonces** el tiempo de inicialización de la IA se reducirá de minutos a segundos, prevendremos fallos de sintaxis en la configuración de disco y elevaremos exponencialmente la experiencia del desarrollador desde el primer comando.

## Justificación y Modelo Mental

Un desarrollador valora las herramientas listas para usar (Out-of-the-box experience). El dolor de comenzar a usar React antes de "Create React App" era la interminable configuración manual de Webpack. Lo mismo ocurre con la IA local: la CLI debe actuar como un puente amable que desmitifique la complejidad de conexión. Un asistente paso a paso con valores por defecto inteligentes y explicaciones en línea reduce el esfuerzo y la "fricción de entrada" para nuevos miembros del equipo.

## Validación Experimental

Para validar empíricamente esta propuesta de experiencia interactiva de usuario, se diseña un experimento detallado para implementar el Wizard:

- [[13g1a - Experimento: Implementación de comando interactivo ggconfigia]]

## Referencias

- [[13g - Interfaz interactiva de configuración de IA]]
- [[4a5 - reflexion implementacion configcommand-execute]]
