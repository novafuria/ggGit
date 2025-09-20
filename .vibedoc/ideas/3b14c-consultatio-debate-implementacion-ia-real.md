# 3b14c - Consultatio: Debate sobre implementación de IA real

## Pregunta Central
¿Cómo implementar la IA real en `AiMessageGenerator` para reemplazar la funcionalidad mock actual?

## Contexto del Debate

### **Situación Actual**
- `AiMessageGenerator` es solo mock con análisis estático
- Ollama funcionando correctamente en `http://localhost:11434`
- Modelo `gemma3:4b` disponible y generando respuestas de calidad
- Configuración de usuario correcta pero ignorada

### **Objetivo**
Implementar IA real que use la configuración del usuario y genere mensajes de commit contextuales y descriptivos.

## Puntos de Debate

### **1. Estrategia de Implementación**

#### **Opción A: Reemplazo Completo**
- Reemplazar completamente la implementación mock
- Implementar IA real desde cero
- Mantener fallback a mock solo en caso de error

**Ventajas:**
- Implementación limpia y directa
- Cumple completamente con las especificaciones
- Mejor experiencia de usuario

**Desventajas:**
- Cambio más disruptivo
- Requiere más testing
- Posibles problemas de compatibilidad

#### **Opción B: Implementación Híbrida**
- Mantener mock como base
- Agregar IA real como opción
- Permitir configuración para elegir entre mock e IA

**Ventajas:**
- Transición más gradual
- Mantiene funcionalidad existente
- Permite testing A/B

**Desventajas:**
- Código más complejo
- Mantiene funcionalidad mock innecesaria
- Configuración más compleja

### **2. Manejo de Errores y Fallback**

#### **Pregunta: ¿Qué hacer cuando IA falla?**
- ¿Fallback a mock?
- ¿Mostrar error y pedir mensaje manual?
- ¿Reintentar con diferentes parámetros?

#### **Pregunta: ¿Cómo manejar timeouts?**
- ¿Timeout corto (10s) con fallback rápido?
- ¿Timeout largo (30s) para mejor calidad?
- ¿Timeout configurable por usuario?

### **3. Construcción de Prompts**

#### **Pregunta: ¿Qué información incluir en el prompt?**
- ¿Solo archivos y diff?
- ¿Incluir contexto del repositorio?
- ¿Incluir historial de commits recientes?

#### **Pregunta: ¿Cómo estructurar el prompt?**
- ¿Prompt simple y directo?
- ¿Prompt con ejemplos?
- ¿Prompt con instrucciones detalladas?

### **4. Tracking y Monitoreo**

#### **Pregunta: ¿Cómo trackear uso real?**
- ¿Tokens reales o estimados?
- ¿Costo real o simulado?
- ¿Métricas de calidad de respuestas?

#### **Pregunta: ¿Qué métricas recopilar?**
- ¿Tiempo de respuesta?
- ¿Calidad de mensajes generados?
- ¿Tasa de fallback a mock?

### **5. Configuración y Personalización**

#### **Pregunta: ¿Qué parámetros hacer configurables?**
- ¿Temperature del modelo?
- ¿Max tokens?
- ¿Timeout de API?
- ¿Prompt personalizado?

#### **Pregunta: ¿Cómo manejar diferentes proveedores?**
- ¿Solo Ollama por ahora?
- ¿Implementar OpenAI también?
- ¿Sistema de plugins para proveedores?

## Preguntas Específicas para el Debate

### **1. Implementación Inmediata**
¿Implementamos IA real ahora o esperamos a tener más tiempo para testing?

### **2. Estrategia de Rollout**
¿Implementamos para todos los usuarios o solo para testing interno?

### **3. Compatibilidad**
¿Mantenemos compatibilidad con la implementación mock actual?

### **4. Testing**
¿Cómo probamos la calidad de los mensajes generados por IA?

### **5. Documentación**
¿Actualizamos la documentación para reflejar la implementación real?

## Propuestas para Discutir

### **Propuesta 1: Implementación Mínima Viable**
- Implementar IA real básica con Ollama
- Fallback a mock en caso de error
- Testing con casos reales
- Iterar basado en feedback

### **Propuesta 2: Implementación Completa**
- Implementar IA real con todas las características
- Soporte para múltiples proveedores
- Configuración avanzada
- Testing exhaustivo antes del release

### **Propuesta 3: Implementación Gradual**
- Implementar IA real para comandos específicos
- Expandir gradualmente a todos los comandos
- A/B testing entre mock e IA
- Feedback continuo de usuarios

## Conclusión del Debate
Este debate debe resultar en una decisión clara sobre cómo proceder con la implementación de IA real, considerando el balance entre funcionalidad, calidad, y tiempo de implementación.
