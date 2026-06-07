# 13c2 - Hipótesis: Mensajes de diagnóstico proactivo para APIs de IA

## Enunciado de la Hipótesis

**Dado** que los desarrolladores noveles pueden no comprender la arquitectura de Ollama (ej. que requiere un demonio local escuchando en el puerto 11434),  
**Si** el sistema detecta que la API de IA local falló debido a una conexión rechazada (`ConnectionRefusedError` en el host configurado),  
**Entonces** el mensaje de error de la CLI debe incluir de forma proactiva instrucciones claras y procesables de diagnóstico (como sugerir ejecutar `ollama serve` o `ollama pull <modelo>`), reduciendo la frustración y el tiempo medio de resolución de problemas de entorno en un 50%.

## Justificación y Modelo Mental

Un sistema con buena experiencia de desarrollador no solo reporta que algo salió mal; explica *qué* salió mal y *cómo* solucionarlo en su contexto inmediato. El síndrome del impostor y la fricción de herramientas ocurren cuando el programador se encuentra ante un error opaco (como un timeout de socket largo e inescrutable) sin saber por dónde empezar a depurar. Al empoderar a la CLI para que realice una introspección proactiva de la configuración, convertimos un mensaje de error seco en un mentor amigable.

## Validación Experimental Propuesta

El experimento se basaría en mapear las firmas de las excepciones de red conocidas en la capa del cliente de IA (`src/core/ai/message_generator.py`) y enriquecer las salidas de error usando `ColorManager` para resaltar comandos exactos de solución según el proveedor de IA configurado.

## Referencias

- [[9 - sistema de ia para generacion de commits]]
- [[13c - Resiliencia y tolerancia a fallos del sistema de IA]]
