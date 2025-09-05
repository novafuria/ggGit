# [HISTORIA] - Integración con Comandos Existentes

## 🎯 Objetivo

Integrar funcionalidad IA con todos los comandos de commit existentes, implementando la lógica de "comando sin argumentos = IA por defecto" y ajustando la consistencia de argumentos requeridos.

## 🌎 Contexto

Esta historia implementa la decisión clave del zettel 1.2.6.4 de usar comandos sin argumentos para activar IA automáticamente, resolviendo la deuda técnica identificada en el zettel 1.2.6.1 del parámetro `--ai` no implementado.

La historia se basa en la decisión de cambiar la lógica de activación de `if not message and ai:` a `if not message and self._is_ai_configured()`, y en ajustar `ggbreak` para consistencia con otros comandos.

## 💡 Propuesta de Resolución

Se propone modificar la lógica de activación IA en todos los comandos de commit existentes, cambiando de la verificación de flag `--ai` a la verificación de configuración IA. Se ajustará `ggbreak` para hacer el argumento `message` opcional y se integrará con el análisis de complejidad para decisión automática.

La implementación mantendrá compatibilidad total con el uso manual de mensajes y proporcionará fallbacks educativos cuando IA no esté disponible.

## 📦 Artefactos

- 📦 **Lógica de activación IA**: Modificación en todos los comandos de commit para usar `_is_ai_configured()`
- 📦 **Ajuste de ggbreak**: Cambio de `message` de `required=True` a `required=False`
- 📦 **Integración con análisis**: Uso de ComplexityAnalyzer en comandos existentes
- 📦 **Tests de integración**: Tests para comandos con funcionalidad IA

## 🔍 Criterios de Aceptación

### **Activación IA Automática**
- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggfeat` sin argumentos
- **Entonces** se activa la generación de mensaje con IA (si está configurado) o se muestra error descriptivo (si no está configurado)

- **Dado** que soy un desarrollador
- **Cuando** ejecuto cualquier comando de commit sin argumentos
- **Entonces** se activa la generación de mensaje con IA automáticamente

### **Compatibilidad con Argumentos**
- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggfeat "mensaje manual"`
- **Entonces** se usa el mensaje manual (no IA)

- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggbreak` sin argumentos
- **Entonces** se activa la generación de mensaje con IA (consistente con otros comandos)

### **Integración con Análisis**
- **Dado** que ejecuto un comando con cambios simples
- **Cuando** se analiza complejidad
- **Entonces** se genera mensaje con IA

- **Dado** que ejecuto un comando con cambios complejos
- **Cuando** se analiza complejidad
- **Entonces** se muestra fallback educativo

### **Mensajes de Error Descriptivos**
- **Dado** que IA no está configurado
- **Cuando** ejecuto un comando sin argumentos
- **Entonces** se muestra error descriptivo con instrucciones de configuración

## 🔗 Dependencias y Recursos

### Dependencias
- Configuración IA básica (STORY-1.2.7.1) debe estar implementada
- Análisis de complejidad (STORY-1.2.7.2) debe estar implementado
- Comando ggai básico (STORY-1.2.7.3) debe estar implementado
- Todos los comandos de commit existentes deben estar funcionales

### Recursos
- Acceso a todos los comandos de commit en `src/commands/`
- Acceso a BaseCommand para implementar `_is_ai_configured()`
- Acceso a ComplexityAnalyzer para integración
- Acceso a configuraciones IA para verificación
