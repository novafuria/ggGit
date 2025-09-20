# 3b14d - Análisis: Diseño actual de IA en ggGit

## Arquitectura Actual de IA

### **Flujo de IA en Comandos de Commit**
```
Comando (ggfeat, ggfix, etc.)
├── _is_ai_configured() → Verificar configuración
├── _generate_ai_message()
│   ├── ComplexityAnalyzer.should_use_ai() → Decidir IA vs. fallback
│   ├── AiMessageGenerator.generate_message() → Generar mensaje (MOCK)
│   └── _execute_manual_commit() → Ejecutar commit
└── _execute_manual_commit() → Si no hay IA
```

### **Flujo de IA en Comando ggai**
```
ggai main
├── _is_ai_configured() → Verificar configuración
├── ComplexityAnalyzer.should_use_ai() → Decidir IA vs. fallback
├── Si should_use_ai:
│   ├── GitInterface.get_diff_content() → Obtener diff
│   ├── AiMessageGenerator.generate_message() → Generar mensaje (MOCK)
│   └── Mostrar mensaje generado
└── Si no should_use_ai:
    └── ComplexityAnalyzer.get_fallback_message() → Mensaje educativo
```

## Componentes de IA

### **1. ComplexityAnalyzer**
- **Propósito**: Analizar complejidad de cambios
- **Métodos**:
  - `analyze_complexity()` → Analiza archivos, líneas, tamaños
  - `should_use_ai()` → Decide IA vs. fallback (actualmente siempre True)
  - `get_fallback_message()` → Mensaje educativo para cambios complejos
  - `get_analysis_summary()` → Resumen para display

### **2. AiMessageGenerator (MOCK)**
- **Propósito**: Generar mensajes de commit usando IA
- **Métodos**:
  - `generate_message(files, diff_content)` → Genera mensaje (MOCK)
  - `test_connection()` → Prueba conexión (MOCK)
  - `get_provider_info()` → Info del proveedor (MOCK)

### **3. AiUsageTracker**
- **Propósito**: Tracking de uso y costos de IA
- **Métodos**:
  - `increment_usage()` → Incrementar contador
  - `get_usage_stats()` → Obtener estadísticas
  - `reset_usage()` → Reiniciar contadores

## Análisis del Diseño

### **✅ Fortalezas del Diseño**
1. **Separación de responsabilidades**: Cada componente tiene un propósito claro
2. **Análisis de complejidad**: Sistema inteligente para decidir IA vs. fallback
3. **Tracking de uso**: Monitoreo de costos y consumo
4. **Integración en comandos**: IA automática en comandos existentes
5. **Fallback educativo**: Mensajes que enseñan buenas prácticas

### **❌ Problemas Identificados**
1. **AiMessageGenerator es MOCK**: No usa IA real
2. **Análisis de complejidad deshabilitado**: `should_use_ai()` siempre retorna True
3. **Falta contexto específico**: No se pasa el tipo de commit (feat, fix, etc.) al modelo
4. **Prompt simple**: Solo archivos y diff, sin contexto adicional

## Preguntas de Diseño

### **1. ¿Cómo incorporar contexto específico?**
- **Problema**: Los comandos `ggfeat`, `ggfix`, etc. ya saben el tipo de commit
- **Solución propuesta**: Pasar el tipo de commit al prompt para mejor contexto

### **2. ¿Una o dos llamadas al modelo?**
- **Opción A**: Una llamada con contexto completo
- **Opción B**: Dos llamadas (análisis + generación)
- **Recomendación**: Una llamada con prompt inteligente

### **3. ¿Cómo manejar prefijos con scope?**
- **Problema**: Modelos pueden generar `feat(scope): message`
- **Solución**: Regex para detectar y limpiar prefijos existentes

### **4. ¿Fallback a mock o error directo?**
- **Problema**: Mock actual es engañoso
- **Recomendación**: Error directo con instrucciones claras

## Propuesta de Mejora

### **1. Implementar IA Real**
```python
def generate_message(self, files: List[str], diff_content: str, commit_type: str = None) -> str:
    """Generate commit message using real AI."""
    try:
        # Build context-aware prompt
        prompt = self._build_context_prompt(files, diff_content, commit_type)
        
        # Call real AI API
        response = self._call_ollama_api(prompt)
        
        # Process and clean response
        message = self._process_ai_response(response)
        
        return message
        
    except Exception as e:
        # No fallback to mock - show clear error
        raise Exception(f"Error generando mensaje IA: {e}")
```

### **2. Prompt Contextual Inteligente**
```python
def _build_context_prompt(self, files: List[str], diff_content: str, commit_type: str = None) -> str:
    """Build context-aware prompt for better AI generation."""
    
    # Get commit type context
    type_context = self._get_commit_type_context(commit_type)
    
    # Build file context
    file_context = self._build_file_context(files)
    
    # Build change context
    change_context = self._build_change_context(diff_content)
    
    prompt = f"""Generate a concise commit message for the following changes:

{type_context}

Files modified: {file_context}

Changes:
```
{diff_content}
```

Requirements:
- Use conventional commit format: {commit_type}: <description>
- Keep description under 50 characters
- Be specific about what was changed
- Use imperative mood (e.g., "add", "fix", "update")

Generate only the commit message, no explanations:"""

    return prompt
```

### **3. Manejo Robusto de Prefijos**
```python
def _process_ai_response(self, response: str) -> str:
    """Process AI response and clean prefixes."""
    import re
    
    # Clean response
    message = response.strip()
    
    # Remove any conventional commit prefix if present
    prefix_pattern = r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|break)(\([^)]+\))?:\s*'
    message = re.sub(prefix_pattern, '', message, flags=re.IGNORECASE)
    
    # Ensure it's not empty
    if not message:
        return "update files"
    
    return message
```

## Conclusión
El diseño actual es sólido pero necesita implementación real de IA. La clave está en:
1. **Implementar IA real** reemplazando el mock
2. **Contexto específico** para mejor generación
3. **Manejo robusto de prefijos** con regex
4. **Error directo** sin fallback engañoso
5. **Prompt inteligente** con contexto completo
