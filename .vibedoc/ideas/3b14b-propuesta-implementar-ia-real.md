# 3b14b - Propuesta: Implementar IA real con Ollama

## Objetivo
Reemplazar la implementación mock de `AiMessageGenerator` con una implementación real que use modelos de IA a través de Ollama.

## Análisis de la Configuración Actual

### **Ollama Disponible**
- ✅ URL: `http://localhost:11434`
- ✅ Modelo: `gemma3:4b`
- ✅ API funcionando correctamente
- ✅ Respuestas de alta calidad

### **Configuración del Usuario**
```yaml
ai:
  api_key_env: OPENAI_API_KEY
  base_url: http://localhost:11434
  enabled: True
  model: gemma3:4b
  provider: openai
```

## Propuesta de Implementación

### **1. Estructura de la Nueva Implementación**
```python
def generate_message(self, files: List[str], diff_content: str) -> str:
    """Generate commit message using real AI."""
    try:
        # 1. Build prompt with context
        prompt = self._build_commit_prompt(files, diff_content)
        
        # 2. Call real AI API
        response = self._call_ollama_api(prompt)
        
        # 3. Process and clean response
        message = self._process_ai_response(response)
        
        # 4. Track real usage
        self._track_real_usage(prompt, response)
        
        return message
        
    except Exception as e:
        # Fallback to mock implementation
        return self._fallback_to_mock(files, diff_content)
```

### **2. Implementación de API Call**
```python
def _call_ollama_api(self, prompt: str) -> str:
    """Call Ollama API to generate commit message."""
    import requests
    
    url = f"{self.config.get_config('ai.base_url')}/api/generate"
    data = {
        "model": self.config.get_config('ai.model'),
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "max_tokens": 200
        }
    }
    
    response = requests.post(url, json=data, timeout=30)
    response.raise_for_status()
    
    return response.json()["response"]
```

### **3. Construcción de Prompt Efectivo**
```python
def _build_commit_prompt(self, files: List[str], diff_content: str) -> str:
    """Build effective prompt for commit message generation."""
    
    # Get commit type from context (if available)
    commit_type = self._get_commit_type_from_context()
    
    prompt = f"""Generate a concise commit message for the following changes:

Files modified: {', '.join(files)}

Changes:
```
{diff_content}
```

Requirements:
- Use conventional commit format: {commit_type}: <description>
- Keep description under 50 characters
- Be specific about what was changed
- Use imperative mood (e.g., "add", "fix", "update")
- If multiple changes, focus on the main one

Generate only the commit message, no explanations:"""

    return prompt
```

### **4. Procesamiento de Respuesta**
```python
def _process_ai_response(self, response: str) -> str:
    """Process AI response to extract commit message."""
    
    # Clean response
    message = response.strip()
    
    # Remove any prefix if AI included it
    if ':' in message and not message.startswith(('feat:', 'fix:', 'docs:', 'style:', 'refactor:', 'test:', 'chore:', 'perf:', 'ci:', 'build:', 'break:')):
        # Extract description after colon
        message = message.split(':', 1)[1].strip()
    
    # Ensure it's not empty
    if not message:
        return "update files"
    
    return message
```

### **5. Tracking Real de Uso**
```python
def _track_real_usage(self, prompt: str, response: str) -> None:
    """Track real AI usage for cost monitoring."""
    
    if not self.usage_tracker.is_tracking_enabled():
        return
    
    # Estimate tokens (rough calculation)
    prompt_tokens = len(prompt.split()) * 1.3  # Rough estimate
    response_tokens = len(response.split()) * 1.3
    
    total_tokens = int(prompt_tokens + response_tokens)
    
    # Estimate cost (Ollama local is free, but track for consistency)
    cost = 0.0  # Local Ollama is free
    
    # Track usage
    self.usage_tracker.increment_usage("ggai", total_tokens, cost)
```

### **6. Manejo de Errores y Fallback**
```python
def _fallback_to_mock(self, files: List[str], diff_content: str) -> str:
    """Fallback to mock implementation if AI fails."""
    
    # Use existing mock logic as fallback
    if not files:
        return "chore: no changes detected"
    
    file_types = self._analyze_file_types(files)
    change_type = self._analyze_change_type(diff_content)
    
    if len(files) == 1:
        file_name = os.path.basename(files[0])
        message = f"update {file_name}"
    else:
        message = f"update {len(files)} files"
    
    if file_types:
        scope = self._get_scope_from_file_types(file_types)
        if scope:
            message = f"({scope}) {message}"
    
    return message
```

## Ventajas de la Implementación Propuesta

### **✅ IA Real**
- Usa modelos de IA reales (Ollama)
- Genera mensajes contextuales y descriptivos
- Entiende el contenido real de los cambios

### **✅ Configuración Utilizada**
- Respeta `ai.base_url` y `ai.model`
- Usa la configuración del usuario
- Tracking real de uso

### **✅ Robustez**
- Manejo de errores de API
- Fallback a implementación mock
- Timeout para evitar bloqueos

### **✅ Compatibilidad**
- Mantiene la misma interfaz
- No rompe funcionalidad existente
- Mejora gradual

## Consideraciones de Implementación

### **1. Dependencias**
- Agregar `requests` a requirements
- Manejar timeouts y errores de red
- Validar configuración antes de usar

### **2. Performance**
- Ollama local es rápido
- Timeout de 30 segundos
- Fallback inmediato si falla

### **3. Testing**
- Probar con diferentes tipos de cambios
- Verificar manejo de errores
- Comparar calidad con mock

## Conclusión
Esta implementación reemplazaría completamente la funcionalidad mock con IA real, cumpliendo con las especificaciones de la documentación y proporcionando la funcionalidad prometida a los usuarios.
