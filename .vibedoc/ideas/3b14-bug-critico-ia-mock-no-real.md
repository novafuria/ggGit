# 3b14 - Bug Crítico: IA es solo mock, no usa modelos reales

## Problema Identificado
El `AiMessageGenerator` es solo una implementación mock que hace análisis estático de archivos, NO está usando modelos de IA reales como Ollama, OpenAI, etc.

## Evidencia del Bug

### **Configuración Correcta del Usuario**
```yaml
ai:
  api_key_env: OPENAI_API_KEY
  base_url: http://localhost:11434  # Ollama local
  enabled: True
  model: gemma3:4b
  provider: openai
```

### **Código Actual (Mock)**
```python
def generate_message(self, files: List[str], diff_content: str) -> str:
    # Mock implementation for MVP
    if not files:
        return "chore: no changes detected"
    
    # Analyze file types and changes (ANÁLISIS ESTÁTICO)
    file_types = self._analyze_file_types(files)
    change_type = self._analyze_change_type(diff_content)
    
    # Generate message based on analysis (SIN IA REAL)
    if change_type == "feature":
        prefix = "feat"
    # ... más lógica estática
```

### **Comentarios en el Código**
- "Currently implements a mock version that creates simple messages"
- "This is a mock implementation for MVP"
- "In the future, this will integrate with real AI services"

## Impacto del Bug

### **Funcionalidad Prometida vs. Realidad**
- **Prometido**: IA real con Ollama, OpenAI, etc.
- **Realidad**: Solo análisis estático de archivos
- **Resultado**: Los usuarios no obtienen la funcionalidad de IA prometida

### **Configuración Inútil**
- Los usuarios configuran proveedores de IA que no se usan
- `base_url`, `model`, `provider` son ignorados
- Solo se usa análisis estático básico

### **Expectativas Incumplidas**
- Según `architecture.md`: "Sistema de IA Integrado"
- Según `product-design.md`: "genera mensajes de commit usando IA"
- Realidad: Solo heurísticas estáticas

## Análisis de la Documentación

### **Architecture.md - Sistema de IA** (líneas 913-1120)
- **AiMessageGenerator**: "Genera mensajes de commit usando proveedores de IA"
- **Proveedores soportados**: OpenAI, Anthropic, Azure, Local (Ollama)
- **Configuración**: `ai.provider`, `ai.model`, `ai.base_url`

### **Product-design.md - IA Automática** (líneas 108-109)
- "El sistema analiza cambios automáticamente y genera mensajes de commit usando IA"
- "Análisis de Complejidad: El sistema evalúa la complejidad de cambios para decidir entre generación automática con IA"

## Verificación de Ollama
- ✅ Ollama funcionando en `http://localhost:11434`
- ✅ Modelo `gemma3:4b` disponible
- ✅ API responde correctamente con mensajes de alta calidad
- ✅ Configuración de usuario correcta

## Prioridad
**CRÍTICA** - La funcionalidad principal de IA no funciona como se prometió en la documentación.

## Consecuencias
- Los usuarios no obtienen la funcionalidad de IA prometida
- La configuración de IA es inútil
- La documentación es engañosa
- El producto no cumple con sus especificaciones