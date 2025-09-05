# [HISTORIA] - Configuración IA Básica

## 🎯 Objetivo

Extender el sistema de configuración existente para soportar funcionalidades de IA, permitiendo a los usuarios configurar proveedores de IA, modelos, límites de costo y análisis de complejidad a través del comando `ggconfig` existente.

## 🌎 Contexto

Esta historia es la base para la integración de IA en ggGit. Sin la configuración IA básica, no es posible implementar la funcionalidad de auto-generación de mensajes de commit. La historia se basa en las decisiones tomadas en los zettels 1.2.6.4, 1.2.6.7 y 1.2.6.8, donde se definió usar el sistema de configuración existente (`ggconfig`) en lugar de crear un comando separado.

La configuración IA debe integrarse con el ConfigManager existente y seguir la jerarquía repo > module > user > default ya implementada.

## 💡 Propuesta de Resolución

Se propone extender el esquema de configuración existente (`config-schema.yaml`) con una sección `ai` que incluya configuraciones básicas para habilitación, proveedor, credenciales, modelo y análisis de complejidad. Se implementará un método `_is_ai_configured()` en BaseCommand para verificar la disponibilidad de IA.

La implementación reutilizará el ConfigManager existente y el comando `ggconfig`, manteniendo la consistencia con el sistema de configuración actual.

## 📦 Artefactos

- 📦 **Esquema de configuración extendido**: Sección `ai` en `config-schema.yaml` con validaciones JSON Schema
- 📦 **Método de verificación IA**: `_is_ai_configured()` en BaseCommand para verificar disponibilidad
- 📦 **Tests unitarios**: Tests para ConfigManager con configuraciones IA
- 📦 **Documentación**: Ejemplos de configuración IA en documentación existente

## 🔍 Criterios de Aceptación

### **Configuración Básica**
- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggconfig set ai.enabled true`
- **Entonces** la configuración IA se habilita correctamente

- **Dado** que soy un desarrollador
- **Cuando** ejecuto `ggconfig get ai.provider`
- **Entonces** veo el proveedor de IA configurado

### **Configuraciones Requeridas**
- **Dado** que el esquema de configuración
- **Cuando** se validan configuraciones IA
- **Entonces** se aplican las validaciones JSON Schema apropiadas para:
  - `ai.enabled`: boolean
  - `ai.provider`: enum ["openai", "anthropic", "azure", "local"]
  - `ai.api_key_env`: string, no vacío
  - `ai.model`: string, no vacío
  - `ai.cost_limit`: number, > 0
  - `ai.analysis.max_files`: integer, > 0
  - `ai.analysis.max_diff_lines`: integer, > 0
  - `ai.analysis.max_file_size`: integer, > 0

### **Integración con Sistema Existente**
- **Dado** que el sistema de configuración existente
- **Cuando** se agregan configuraciones IA
- **Entonces** se mantiene la jerarquía repo > module > user > default

## 🔗 Dependencias y Recursos

### Dependencias
- Sistema de configuración existente (ConfigManager) debe estar implementado
- Comando ggconfig debe estar funcional
- Esquema de configuración existente debe estar definido

### Recursos
- Acceso al ConfigManager existente en `src/core/config.py`
- Acceso al comando ggconfig en `src/commands/ggconfig.py`
- Acceso al esquema de configuración en `config/config-schema.yaml`
