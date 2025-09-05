# 1.2.6.4 - Decisiones: Comando sin Argumentos = IA por Defecto

## Resumen de la Decisión

**Fecha**: 2024-12-19
**Idea Padre**: 1.2.6 - el comando ggai
**Objetivo**: Documentar decisión sobre comportamiento de comandos sin argumentos con IA

## Propuesta Analizada

### **Comportamiento Propuesto**
```bash
# En lugar de:
ggfeat --ai

# Simplemente:
ggfeat
# (Si IA está configurado, genera mensaje automáticamente)
```

### **Lógica de Decisión**
- **Si mensaje proporcionado**: Usar mensaje del usuario
- **Si sin mensaje + IA configurado**: Generar mensaje con IA
- **Si sin mensaje + IA no configurado**: Mostrar error descriptivo

## Análisis de Compatibilidad

### **✅ Estado Actual Compatible**

#### **1. Argumentos Click Configurados Correctamente**
```python
@click.argument('message', required=False)  # ✅ Ya es opcional
def main(scope, ai, amend, message):
```

**Comandos con `message` opcional**:
- ✅ `ggfeat` - `required=False`
- ✅ `ggfix` - `required=False`
- ✅ `ggdocs` - `required=False`
- ✅ `ggstyle` - `required=False`
- ✅ `ggrefactor` - `required=False`
- ✅ `ggtest` - `required=False`
- ✅ `ggchore` - `required=False`
- ✅ `ggperf` - `required=False`
- ✅ `ggci` - `required=False`
- ✅ `ggbuild` - `required=False`

**Comando con `message` obligatorio**:
- ❌ `ggbreak` - `required=True` (necesita ajuste)

#### **2. Lógica de Ejecución Preparada**
```python
def execute(self, message, scope=None, ai=False, amend=False):
    # If no message and AI is enabled, generate automatically
    if not message and ai:
        # TODO: Implement AI message generation
        click.echo(ColorManager.warning("AI functionality not yet implemented"))
        return 1
```

**Estado actual**: Ya está preparado para manejar `message=None` y `ai=True`

### **⚠️ Ajustes Necesarios**

#### **1. Cambiar Lógica de Activación de IA**
**Actual**:
```python
if not message and ai:  # Requiere flag --ai
```

**Propuesto**:
```python
if not message and self._is_ai_configured():  # IA por defecto si está configurado
```

#### **2. Ajustar ggbreak para Consistencia**
**Actual**:
```python
@click.argument('message', required=True)
```

**Propuesto**:
```python
@click.argument('message', required=False)
```

#### **3. Agregar Verificación de Configuración IA**
```python
def _is_ai_configured(self) -> bool:
    """Check if AI is configured and available."""
    # Verificar configuración en ConfigManager
    # Verificar disponibilidad de servicios IA
    # Verificar API keys, etc.
    return True  # Placeholder
```

## Ventajas de la Propuesta

### **1. Experiencia de Usuario Simplificada**
- **Menos teclas**: No necesita recordar flag `--ai`
- **Más intuitivo**: Comando sin argumentos = IA automática
- **Consistente**: Mismo comportamiento en todos los comandos

### **2. Compatibilidad con Flujo de Trabajo Existente**
- **Sin cambios breaking**: Comandos con mensaje siguen funcionando igual
- **Progresivo**: IA se activa solo cuando está configurado
- **Fallback claro**: Error descriptivo si IA no está disponible

### **3. Implementación Limpia**
- **Menos flags**: Elimina necesidad de `--ai` en comandos
- **Configuración centralizada**: IA se controla desde configuración global
- **Mantenimiento simple**: Una sola lógica para todos los comandos

## Consideraciones de Implementación

### **1. Configuración de IA**
```yaml
# .gggit/config.yaml
ai:
  enabled: true
  provider: "openai"  # openai, claude, local
  auto_generate: true  # Generar automáticamente si no hay mensaje
  api_key: "${OPENAI_API_KEY}"
  model: "gpt-4"
```

### **2. Comportamiento por Comando**
```bash
# Comportamiento con IA configurado:
ggfeat                    # → Genera mensaje con IA
ggfeat "mensaje manual"   # → Usa mensaje manual
ggfeat --ai "mensaje"     # → Usa mensaje manual (flag ignorado)

# Comportamiento sin IA configurado:
ggfeat                    # → Error: "Mensaje requerido o configure IA"
ggfeat "mensaje manual"   # → Usa mensaje manual
```

### **3. Mensajes de Error Descriptivos**
```python
if not message and not self._is_ai_configured():
    click.echo(ColorManager.error("Mensaje requerido. Configure IA para generación automática."))
    click.echo(ColorManager.info("Ejecute 'ggconfig set ai.enabled true' para habilitar IA"))
    return 1
```

## Impacto en Arquitectura

### **1. Cambios en Comandos Existentes**
- **Eliminar parámetro `ai`**: Ya no necesario en CLI
- **Agregar verificación IA**: Método `_is_ai_configured()`
- **Ajustar lógica**: Cambiar condición de activación

### **2. Configuración Global**
- **ConfigManager**: Agregar sección `ai`
- **Validación**: Verificar configuración al inicializar
- **Fallback**: Manejo de errores cuando IA no disponible

### **3. Experiencia de Usuario**
- **Documentación**: Actualizar help de comandos
- **Tutoriales**: Guías de configuración de IA
- **Feedback**: Mensajes claros sobre estado de IA

## Decisión Tomada

### **✅ APROBADO: Comando sin Argumentos = IA por Defecto**

**Justificación**:
1. **Compatibilidad total**: No rompe funcionalidad existente
2. **UX simplificada**: Menos flags, más intuitivo
3. **Implementación limpia**: Lógica centralizada
4. **Progresivo**: IA se activa solo cuando está configurado

### **Implementación Propuesta**:

#### **Fase 1: Ajustes Básicos**
1. Cambiar lógica de activación de IA en todos los comandos
2. Ajustar `ggbreak` para consistencia (`required=False`)
3. Agregar verificación de configuración IA

#### **Fase 2: Configuración**
1. Extender ConfigManager con sección `ai`
2. Implementar verificación de disponibilidad IA
3. Agregar mensajes de error descriptivos

#### **Fase 3: Integración IA**
1. Implementar generación automática de mensajes
2. Integrar con servicios de IA
3. Testing y validación

## Próximos Pasos

1. **Implementar MVP con UX mejorada**:
   - Análisis inteligente de cambios (git diff + staging)
   - Criterios de complejidad para decidir IA vs. mensaje default
   - Comando `ggai` con subcomandos (`usage`, `reset`, `config`)

2. **Sistema de tracking de consumo**:
   - Archivo `.gggit/ai-usage.yaml`
   - Comandos `ggai usage` y `ggai reset`
   - Control de costos y límites

3. **Integración con comandos existentes**:
   - Ajustar `ggbreak` (message opcional)
   - Lógica de activación IA mejorada
   - Fallbacks robustos

4. **Fase 3 futura** (documentada en 3.1):
   - Prompts personalizables
   - Modo offline avanzado
   - Aprendizaje del proyecto

## Referencias
- **MVP detallado**: 1.2.6.6 - mvp-ia-con-ux-mejorada.md
- **Fase 3 futura**: 3.1 - ia-avanzada-futuro.md
- **Configuraciones**: 1.2.6.5 - configuraciones-ia-detalladas.md

## Preguntas Pendientes

1. **¿Qué servicios de IA priorizar** para implementación inicial?
2. **¿Cómo manejar costos** de llamadas a IA?
3. **¿Qué nivel de personalización** permitir en configuración?
4. **¿Cómo validar mensajes generados** por IA?
