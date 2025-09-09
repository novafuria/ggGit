# 1.2.6.8 - MVP Final IA

## Resumen de la Propuesta Final

**Fecha**: 2024-12-19
**Idea Padre**: 1.2.6 - el comando ggai
**Objetivo**: Definir MVP final de IA con feedback visual ajustado

## Propuesta Final del MVP

### **1. Feedback Visual Ajustado**

#### **Caso 1: Cambios Simples → IA**
```bash
$ ggfeat
🤖 Analizando cambios...
📝 Archivos: 1, Líneas: 15
✅ Mensaje generado: "feat: add interactive branch selection"
```

#### **Caso 2: Cambios Complejos → Fallback Inteligente**
```bash
$ ggfeat
🤖 Analizando cambios...
📝 Archivos: 25, Líneas: 500
⚠️ No es aconsejable commitear tanto contenido
💡 Sugerencia: Selecciona grupos de archivos más pequeños
   Usa 'git add <archivo>' para archivos específicos
   O 'ggfeat "mensaje manual"' para commit completo
```

#### **Caso 3: Ver Consumo**
```bash
$ ggai usage
📊 Consumo de IA - Período: 2024-12-19
├── Requests: 15
├── Tokens usados: 2,450
└── Costo estimado: $0.12/$5.00
```

### **2. Criterios de Decisión Ajustados**

#### **Análisis de Complejidad**
```yaml
ai:
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000  # bytes
    # Removido: complexity_threshold (no útil para usuario)
```

#### **Lógica de Decisión**
```python
def should_use_ai(files_count: int, diff_lines: int, file_size: int) -> bool:
    """Decide si usar IA o fallback inteligente."""
    if files_count > 10 or diff_lines > 200 or file_size > 5000:
        return False  # Usar fallback inteligente
    return True  # Usar IA
```

### **3. Fallback Inteligente**

#### **Mensaje de Fallback**
```bash
⚠️ No es aconsejable commitear tanto contenido
💡 Sugerencia: Selecciona grupos de archivos más pequeños
   Usa 'git add <archivo>' para archivos específicos
   O 'ggfeat "mensaje manual"' para commit completo
```

#### **Ventajas del Fallback**
- **Educativo**: Enseña buenas prácticas de Git
- **Práctico**: Sugiere comandos específicos
- **Flexible**: Permite commit manual si es necesario

### **4. Configuración Final**

#### **Esquema de Configuración Extendido**
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
    # Removido: complexity_threshold
```

### **5. Implementación del MVP Final**

#### **Fase 1: Extender ConfigManager**
- [ ] Agregar configuraciones IA al esquema existente
- [ ] Implementar `_is_ai_configured()` en BaseCommand
- [ ] Lógica de activación: `if not message and self._is_ai_configured()`

#### **Fase 2: Análisis Inteligente**
- [ ] Análisis de área de staging
- [ ] Git diff analysis
- [ ] Criterios de decisión (archivos, líneas, tamaño)
- [ ] Fallback inteligente con sugerencias

#### **Fase 3: Comando ggai**
- [ ] Comando principal `ggai`
- [ ] Subcomando `ggai usage`
- [ ] Subcomando `ggai usage reset`
- [ ] Archivo de tracking `.gggit/ai-usage.yaml`

#### **Fase 4: Integración**
- [ ] Integrar con comandos existentes
- [ ] Ajustar `ggbreak` (message opcional)
- [ ] Testing completo

### **6. Flujo de Uso Final**

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
📝 Archivos: 1, Líneas: 15
✅ Mensaje generado: "feat: add interactive branch selection"

# Caso 2: Cambios complejos → Fallback inteligente
$ git add .
$ ggfeat
🤖 Analizando cambios...
📝 Archivos: 25, Líneas: 500
⚠️ No es aconsejable commitear tanto contenido
💡 Sugerencia: Selecciona grupos de archivos más pequeños
   Usa 'git add <archivo>' para archivos específicos
   O 'ggfeat "mensaje manual"' para commit completo

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

### **7. Ventajas de la Propuesta Final**

#### **1. Feedback Visual Óptimo**
- **Información útil**: Archivos y líneas (no complejidad)
- **Colores apropiados**: Verde, amarillo, azul
- **Emojis claros**: 🤖, 📝, ✅, ⚠️, 💡, 📊

#### **2. Fallback Inteligente**
- **Educativo**: Enseña buenas prácticas
- **Práctico**: Sugiere comandos específicos
- **Flexible**: Permite commit manual

#### **3. Implementación Simplificada**
- **Sin complejidad**: No spinner por ahora
- **Sin métricas inútiles**: No complejidad para usuario
- **Enfoque claro**: IA para cambios simples, fallback para complejos

#### **4. Extensibilidad**
- **Spinner futuro**: Documentado en 3.2
- **Métricas avanzadas**: Para futuras versiones
- **Configuración flexible**: Por niveles

## Preguntas para Discusión

1. **¿Te parece bien el fallback inteligente** propuesto?
2. **¿Los criterios de decisión** son apropiados?
3. **¿El feedback visual** es el adecuado?
4. **¿Quieres proceder con la implementación** del MVP?

## Referencias
- **Spinner futuro**: 3.2 - spinner-progreso-ia.md
- **Configuración existente**: 1.2.6.7 - propuesta-ajustada-configuracion-existente.md
- **MVP original**: 1.2.6.6 - mvp-ia-con-ux-mejorada.md
