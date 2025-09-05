# 1.2.6.6 - MVP IA con UX Mejorada

## Resumen de la Propuesta

**Fecha**: 2024-12-19
**Idea Padre**: 1.2.6 - el comando ggai
**Objetivo**: Definir MVP de IA con UX similar a VSCode/Cursor

## Propuesta del MVP Ajustada

### **1. UX Similar a VSCode/Cursor**
- **Análisis inteligente**: Git diff + análisis de archivos staged
- **Fallback inteligente**: Si hay muchos archivos o contenido amplio → mensaje default
- **Feedback visual**: Indicadores de progreso y análisis

### **2. Análisis de Cambios Inteligente**

#### **Flujo de Análisis**
1. **Verificar área de staging**:
   - Si hay archivos staged → analizar solo esos
   - Si área vacía → analizar archivos listos para stage

2. **Análisis de contenido**:
   - `git diff --cached` (si hay staged)
   - `git diff` (si no hay staged)
   - Análisis de tipos de archivos modificados

3. **Decisión de complejidad**:
   - **Simple**: Pocos archivos, cambios menores → IA
   - **Complejo**: Muchos archivos, cambios amplios → mensaje default

#### **Criterios de Decisión**
```yaml
ai:
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000  # bytes
    complexity_threshold: 0.7  # 0-1, donde 1 = muy complejo
```

### **3. Comando `ggai` con Subcomandos**

#### **Estructura Propuesta**
```bash
ggai                    # Generar mensaje IA (comando principal)
ggai status            # Ver estado de IA y configuración
ggai usage             # Ver consumo de tokens/costos
ggai reset             # Reiniciar contador de consumo
ggai config            # Configurar IA
ggai test              # Probar conexión IA
```

#### **Subcomando `ggai usage`**
```bash
$ ggai usage
📊 Consumo de IA - Período: 2024-12-19
├── Requests hoy: 15/100
├── Tokens usados: 2,450/10,000
├── Costo estimado: $0.12/$5.00
└── Última actualización: 14:30

💡 Comandos disponibles:
   ggai reset          # Reiniciar contador
   ggai config         # Ver configuración
```

#### **Subcomando `ggai reset`**
```bash
$ ggai reset
✅ Contador de consumo reiniciado
📊 Nuevo período iniciado: 2024-12-19 15:00
```

### **4. Archivo de Tracking de Consumo**

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
  max_requests_per_day: 100
  max_tokens_per_day: 10000
  max_cost_per_day: 5.00
```

### **5. Implementación del MVP**

#### **Fase 1: Base IA**
- [ ] Configuración básica (enabled, provider, api_key, model)
- [ ] Método `_is_ai_configured()` en BaseCommand
- [ ] Lógica de activación: `if not message and self._is_ai_configured()`

#### **Fase 2: Análisis Inteligente**
- [ ] Análisis de área de staging
- [ ] Git diff analysis
- [ ] Criterios de complejidad
- [ ] Decisión IA vs. mensaje default

#### **Fase 3: Comando ggai**
- [ ] Comando principal `ggai`
- [ ] Subcomando `ggai usage`
- [ ] Subcomando `ggai reset`
- [ ] Archivo de tracking `.gggit/ai-usage.yaml`

#### **Fase 4: Integración**
- [ ] Integrar con comandos existentes
- [ ] Ajustar `ggbreak` (message opcional)
- [ ] Testing completo

### **6. Configuración MVP Simplificada**

```yaml
# .gggit/config.yaml
ai:
  # Configuración básica
  enabled: true
  provider: "openai"
  api_key: "${OPENAI_API_KEY}"
  model: "gpt-4"
  
  # Análisis inteligente
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000
    complexity_threshold: 0.7
  
  # Control de costos
  limits:
    max_requests_per_day: 100
    max_tokens_per_day: 10000
    max_cost_per_day: 5.00
  
  # Tracking
  tracking:
    enabled: true
    file: ".gggit/ai-usage.yaml"
    reset_command: "ggai reset"
```

### **7. Ejemplo de Uso**

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
├── Requests hoy: 15/100
├── Tokens usados: 2,450/10,000
└── Costo estimado: $0.12/$5.00
```

## Ventajas de esta Propuesta

### **1. UX Familiar**
- Similar a VSCode/Cursor
- Feedback visual claro
- Fallbacks inteligentes

### **2. Control de Costos**
- Tracking detallado
- Límites configurables
- Comandos de gestión

### **3. Implementación Incremental**
- MVP funcional rápido
- Base sólida para expansión
- Compatible con arquitectura actual

### **4. Flexibilidad**
- Configuración simple
- Fallbacks robustos
- Extensible para futuras mejoras

## Preguntas para Discusión

1. **¿Te parece bien el flujo de análisis** propuesto?
2. **¿Qué criterios de complejidad** consideras más importantes?
3. **¿Los subcomandos de `ggai`** cubren tus necesidades?
4. **¿Cómo visualizas el archivo de tracking** de consumo?
5. **¿Qué nivel de feedback visual** prefieres?

## Referencias
- Idea original: 1.2.6.4 - decisiones-comando-sin-argumentos-ia.md
- Configuraciones: 1.2.6.5 - configuraciones-ia-detalladas.md
- Fase 3 futura: 3.1 - ia-avanzada-futuro.md
