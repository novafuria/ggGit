# 13c1 - Hipótesis: Degradación graciosa con fallback manual interactivo

## Enunciado de la Hipótesis

**Dado** que el desarrollador invoca un comando de commit sin mensaje (p. ej., `ggfeat`) esperando que la IA lo autogenere,  
**Si** el servicio de IA falla por caída del servidor local (Ollama) o error de red (OpenAI/Anthropic),  
**Entonces** el sistema no debe abortar la ejecución con código de salida `1`, sino degradarse graciosamente ofreciendo al desarrollador un flujo interactivo de entrada (p. ej., un prompt de terminal o abriendo un editor interactivo) para capturar el mensaje de commit de forma manual, completando el flujo con éxito.

## Justificación y Modelo Mental

Un desarrollador no debería sufrir por las herramientas de las que depende. La automatización con IA es un acelerador, no un cuello de botella. Si Ollama está apagado, el desarrollador ya experimenta fricción conceptual al ver el error; impedirle hacer su commit de forma manual añade una "frustración accidental" inaceptable. Una herramienta resiliente asume que sus dependencias externas pueden fallar en cualquier momento, y siempre proporciona una salida elegante para cumplir el objetivo de negocio (hacer el commit).

## Validación Experimental

Para validar y calibrar este comportamiento de tolerancia a fallos, se propone implementar un flujo experimental interactivo detallado en el siguiente Zettel:

- [[13c1.1 - Experimento: Implementación de fallback interactivo ante indisponibilidad de Ollama]]

## Referencias

- [[3b15a-reflexion-reoinspeccion-documentacion-completada]]
- [[13c - Resiliencia y tolerancia a fallos del sistema de IA]]
