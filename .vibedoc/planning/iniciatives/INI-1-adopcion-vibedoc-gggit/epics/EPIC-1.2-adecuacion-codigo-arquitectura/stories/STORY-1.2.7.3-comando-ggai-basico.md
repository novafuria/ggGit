# [HISTORIA] - Comando ggai Básico

## 🎯 Objetivo

Implementar comando `ggai` con subcomandos básicos para gestión de IA, incluyendo generación de mensajes, tracking de consumo y prueba de conexión, integrado con el análisis de complejidad existente.

## 🌎 Contexto

Esta historia implementa el comando central de IA definido en los zettels 1.2.6.6, 1.2.6.7 y 1.2.6.8. El comando `ggai` actúa como centro de control para la funcionalidad de IA, proporcionando subcomandos para uso, tracking y testing.

La historia se basa en la decisión de usar `ggai usage reset` en lugar de `ggai reset` para mayor claridad, y en la integración con el sistema de tracking de consumo definido en el zettel 1.2.6.7.

## 💡 Propuesta de Resolución

Se propone crear el comando `ggai` con subcomandos `usage`, `usage reset` y `test`, integrado con el análisis de complejidad para generar mensajes automáticamente. Se implementará un sistema de tracking de consumo en archivo `.gggit/ai-usage.yaml` con métricas de requests, tokens y costos.

La implementación seguirá el patrón BaseCommand existente y se integrará con el sistema de configuración para verificar disponibilidad de IA.

## 📦 Artefactos

- 📦 **Comando ggai**: Implementación en `src/commands/ggai.py` con subcomandos básicos
- 📦 **Sistema de tracking**: Archivo `.gggit/ai-usage.yaml` para tracking de consumo
- 📦 **Integración con análisis**: Uso de ComplexityAnalyzer para decisión IA vs. fallback
- 📦 **Tests unitarios**: Tests para comando ggai y subcomandos

## 🔍 Criterios de Aceptación

### **Comando Principal**
- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggai` sin argumentos
- **Entonces** se genera un mensaje de commit con IA (si cambios son simples) o se muestra fallback educativo (si cambios son complejos)

### **Subcomandos**
- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggai usage`
- **Entonces** veo el consumo de IA y costos en formato:
  ```
  📊 Consumo de IA - Período: 2024-12-19
  ├── Requests: 15
  ├── Tokens usados: 2,450
  └── Costo estimado: $0.12/$5.00
  ```

- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggai usage reset`
- **Entonces** se reinicia el contador de consumo y se muestra confirmación

- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggai test`
- **Entonces** se prueba la conexión con IA y se muestra el estado

### **Integración con Análisis**
- **Dado** que ejecuto `ggai` con cambios simples
- **Cuando** se analiza complejidad
- **Entonces** se genera mensaje con IA

- **Dado** que ejecuto `ggai` con cambios complejos
- **Cuando** se analiza complejidad
- **Entonces** se muestra fallback educativo

## 🔗 Dependencias y Recursos

### Dependencias
- Configuración IA básica (STORY-1.2.7.1) debe estar implementada
- Análisis de complejidad (STORY-1.2.7.2) debe estar implementado
- Servicios de IA (OpenAI, Claude, etc.) deben estar configurados

### Recursos
- Acceso a BaseCommand existente en `src/core/base_commands/base.py`
- Acceso a ComplexityAnalyzer para integración
- Acceso a configuraciones IA para verificación de disponibilidad
