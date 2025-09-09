# 1.2.6.7 - Propuesta Ajustada con Configuración Existente

## Resumen de Ajustes

**Fecha**: 2024-12-19
**Idea Padre**: 1.2.6 - el comando ggai
**Objetivo**: Ajustar propuesta IA usando sistema de configuración existente

## Análisis de Configuración Existente

### **✅ Sistema Ya Implementado**
- **ConfigManager**: Jerarquía `repo > module > user > default`
- **Comando `ggconfig`**: `get`, `set`, `list`, `reset`
- **Esquema IA**: Ya incluye sección `ai` en `config-schema.yaml`

### ** Configuración IA Existente**
```yaml
ai:
  enabled: true/false
  provider: "openai", "anthropic", "azure", "local"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  base_url: "opcional"
```

## Propuesta Ajustada

### **1. Usar `ggconfig` para Configuración IA**

#### **Comandos de Configuración**
```bash
# Ver configuración IA actual
ggconfig get ai.enabled
ggconfig get ai.provider
ggconfig get ai.model

# Configurar IA
ggconfig set ai.enabled true
ggconfig set ai.provider openai
ggconfig set ai.model gpt-4
ggconfig set ai.api_key_env OPENAI_API_KEY

# Ver toda la configuración IA
ggconfig list --level user | grep "ai\."
```

#### **Configuración Extendida para Tracking**
```yaml
# Extensión del esquema existente
ai:
  # Configuración básica (ya existe)
  enabled: true
  provider: "openai"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-4"
  base_url: "opcional"
  
  # Nuevas configuraciones para tracking
  cost_limit: 5.00  # USD por período
  tracking_enabled: true
  usage_file: ".gggit/ai-usage.yaml"
  
  # Análisis inteligente
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000
    complexity_threshold: 0.7
```

### **2. Comando `ggai` Simplificado**

#### **Estructura Ajustada**
```bash
ggai                    # Generar mensaje IA (comando principal)
ggai usage             # Ver consumo y costos
ggai usage reset       # Reiniciar contador de consumo
ggai test              # Probar conexión IA
```

#### **Subcomando `ggai usage`**
```bash
$ ggai usage
📊 Consumo de IA - Período: 2024-12-19
├── Requests: 15
├── Tokens usados: 2,450
├── Costo estimado: $0.12/$5.00
└── Última actualización: 14:30

💡 Comandos disponibles:
   ggai usage reset    # Reiniciar contador
   ggconfig get ai.*   # Ver configuración
```

#### **Subcomando `ggai usage reset`**
```bash
$ ggai usage reset
✅ Contador de consumo reiniciado
📊 Nuevo período iniciado: 2024-12-19 15:00
```

### **3. Archivo de Tracking Ajustado**

#### **Estructura del Archivo**
```yaml
# .gggit/ai-usage.yaml
period:
  start_date: "2024-12-19"
  end_date: "2024-12-26"
  
daily_usage:
  "2024-12-19":
    requests: 15
    tokens: 2450
    cost: 0.12
    commands:
      - "ggfeat": 8
      - "ggfix": 4
      - "ggperf": 2
      - "ggdocs": 1
  
totals:
  requests: 15
  tokens: 2450
  cost: 0.12
  
limits:
  cost_limit: 5.00  # USD por período
  tracking_enabled: true
```

### **4. Flujo de Uso Ajustado**

#### **Configuración Inicial**
```bash
# 1. Configurar IA
ggconfig set ai.enabled true
ggconfig set ai.provider openai
ggconfig set ai.model gpt-4
ggconfig set ai.cost_limit 5.00

# 2. Verificar configuración
ggconfig list | grep "ai\."
```

#### **Uso Diario**
```bash
# Caso 1: Cambios simples → IA
$ git add src/commands/ggfeat.py
$ ggfeat
🤖 Analizando cambios...
📝 Archivos: 1, Líneas: 15, Complejidad: 0.3
✅ Mensaje generado: "feat: add interactive branch selection to ggb command"

# Caso 2: Cambios complejos → Mensaje default
$ git add .
$ ggfeat
🤖 Analizando cambios...
📝 Archivos: 25, Líneas: 500, Complejidad: 0.9
⚠️ Cambios muy complejos, usando mensaje default
💡 Sugerencia: Usa 'ggfeat "mensaje manual"' para mensaje específico

# Caso 3: Ver consumo
$ ggai usage
📊 Consumo de IA - Período: 2024-12-19
├── Requests: 15
├── Tokens usados: 2,450
└── Costo estimado: $0.12/$5.00

# Caso 4: Reiniciar contador
$ ggai usage reset
✅ Contador de consumo reiniciado
📊 Nuevo período iniciado: 2024-12-19 15:00
```

### **5. Implementación del MVP Ajustado**

#### **Fase 1: Extender ConfigManager**
- [ ] Agregar configuraciones IA al esquema existente
- [ ] Implementar `_is_ai_configured()` en BaseCommand
- [ ] Lógica de activación: `if not message and self._is_ai_configured()`

#### **Fase 2: Análisis Inteligente**
- [ ] Análisis de área de staging
- [ ] Git diff analysis
- [ ] Criterios de complejidad
- [ ] Decisión IA vs. mensaje default

#### **Fase 3: Comando ggai**
- [ ] Comando principal `ggai`
- [ ] Subcomando `ggai usage`
- [ ] Subcomando `ggai usage reset`
- [ ] Archivo de tracking `.gggit/ai-usage.yaml`

#### **Fase 4: Integración**
- [ ] Integrar con comandos existentes
- [ ] Ajustar `ggbreak` (message opcional)
- [ ] Testing completo

### **6. Ventajas de la Propuesta Ajustada**

#### **1. Aprovecha Infraestructura Existente**
- **ConfigManager**: Ya implementado y probado
- **Comando `ggconfig`**: Ya funcional
- **Esquema IA**: Ya definido

#### **2. UX Consistente**
- **Configuración**: `ggconfig` para todo
- **Uso**: `ggai` para operaciones IA
- **Tracking**: `ggai usage` para monitoreo

#### **3. Implementación Simplificada**
- **Menos código**: Reutilizar ConfigManager
- **Menos testing**: Aprovechar tests existentes
- **Menos complejidad**: Un solo comando de configuración

#### **4. Flexibilidad**
- **Configuración por niveles**: repo, user, default
- **Tracking configurable**: Habilitar/deshabilitar
- **Límites ajustables**: Costo por período

## Preguntas para Discusión

1. **¿Te parece bien usar `ggconfig`** para toda la configuración?
2. **¿Los subcomandos de `ggai`** cubren tus necesidades?
3. **¿Qué configuraciones IA adicionales** necesitas?
4. **¿Cómo visualizas el archivo de tracking** de consumo?
5. **¿Qué nivel de feedback visual** prefieres?

## Referencias
- **Configuración existente**: `config/config-schema.yaml`
- **Comando ggconfig**: `src/commands/ggconfig.py`
- **ConfigManager**: `src/core/config.py`
- **MVP original**: 1.2.6.6 - mvp-ia-con-ux-mejorada.md
