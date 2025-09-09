# 1.2.6.5 - Configuraciones IA Detalladas

## Resumen de Configuraciones

**Fecha**: 2024-12-19
**Idea Padre**: 1.2.6 - el comando ggai
**Objetivo**: Definir configuraciones completas para funcionalidad IA

## Configuraciones Básicas (Ya Identificadas)

### **1. Habilitación/Deshabilitación**
```yaml
ai:
  enabled: true  # true/false
```

### **2. Proveedor de IA**
```yaml
ai:
  provider: "openai"  # openai, claude, anthropic, local, custom
```

### **3. Credenciales**
```yaml
ai:
  api_key: "${OPENAI_API_KEY}"  # Variable de entorno
  api_url: "https://api.openai.com/v1"  # URL personalizada
```

### **4. Modelo**
```yaml
ai:
  model: "gpt-4"  # gpt-4, gpt-3.5-turbo, claude-3, etc.
```

## Configuraciones Avanzadas Propuestas

### **1. Control de Costos y Uso**

#### **Límites de Uso**
```yaml
ai:
  limits:
    max_requests_per_day: 100
    max_tokens_per_request: 1000
    max_cost_per_day: 5.00  # USD
    enable_cost_tracking: true
```

#### **Rate Limiting**
```yaml
ai:
  rate_limiting:
    requests_per_minute: 10
    requests_per_hour: 100
    burst_limit: 5
```

#### **Caching**
```yaml
ai:
  caching:
    enabled: true
    ttl_seconds: 3600  # 1 hora
    max_cache_size: 1000
    cache_similar_requests: true
```

### **2. Personalización de Comportamiento**

#### **Generación de Mensajes**
```yaml
ai:
  message_generation:
    auto_generate: true  # Generar automáticamente sin mensaje
    include_scope: true  # Incluir scope en mensajes generados
    max_message_length: 100
    language: "es"  # es, en, auto
    style: "concise"  # concise, detailed, technical
```

#### **Validación de Contexto**
```yaml
ai:
  context_validation:
    enabled: true
    strict_mode: false  # true = bloquear commits incorrectos
    confidence_threshold: 0.8  # Umbral de confianza para sugerencias
    suggest_alternatives: true
    learn_from_project: true
```

#### **Comportamiento por Tipo de Commit**
```yaml
ai:
  commit_types:
    feat:
      auto_generate: true
      require_scope: false
      validation_strict: false
    fix:
      auto_generate: true
      require_scope: false
      validation_strict: true
    perf:
      auto_generate: false  # Requiere validación manual
      require_scope: true
      validation_strict: true
    docs:
      auto_generate: true
      require_scope: false
      validation_strict: false
```

### **3. Configuración de Prompts**

#### **Prompts Personalizados**
```yaml
ai:
  prompts:
    commit_message:
      system: "Eres un experto en Conventional Commits. Genera mensajes concisos y descriptivos."
      user_template: |
        Analiza los siguientes cambios y genera un mensaje de commit para tipo '{commit_type}':
        
        Archivos modificados: {files}
        Cambios principales: {changes}
        
        Genera un mensaje que siga Conventional Commits.
    
    context_validation:
      system: "Eres un experto en análisis de código. Valida si el tipo de commit coincide con los cambios reales."
      user_template: |
        Valida si el tipo de commit '{commit_type}' es apropiado para estos cambios:
        
        Mensaje: '{message}'
        Archivos: {files}
        Cambios: {changes}
        
        Responde con: VALID, INVALID, o SUGGEST con alternativa.
```

#### **Templates de Respuesta**
```yaml
ai:
  templates:
    success: "✅ Mensaje generado: {message}"
    error: "❌ Error: {error}"
    suggestion: "💡 Sugerencia: {suggestion}"
    validation_warning: "⚠️ El tipo de commit '{current}' podría no ser apropiado. Considera: {suggested}"
```

### **4. Configuración de Archivos y Análisis**

#### **Filtros de Archivos**
```yaml
ai:
  file_analysis:
    include_patterns:
      - "*.py"
      - "*.js"
      - "*.ts"
      - "*.java"
      - "*.go"
    exclude_patterns:
      - "*.log"
      - "*.tmp"
      - "node_modules/**"
      - ".git/**"
    max_file_size: 10000  # bytes
    analyze_binary_files: false
```

#### **Contexto del Proyecto**
```yaml
ai:
  project_context:
    include_readme: true
    include_package_json: true
    include_dockerfile: true
    max_context_files: 5
    context_window: 4000  # tokens
```

### **5. Configuración de Logging y Debugging**

#### **Logging**
```yaml
ai:
  logging:
    level: "INFO"  # DEBUG, INFO, WARNING, ERROR
    log_requests: true
    log_responses: false  # Por privacidad
    log_costs: true
    log_file: ".gggit/ai.log"
```

#### **Debugging**
```yaml
ai:
  debug:
    enabled: false
    show_prompts: false
    show_tokens_used: true
    show_confidence_scores: true
    dry_run: false  # No hacer llamadas reales a IA
```

### **6. Configuración de Seguridad y Privacidad**

#### **Privacidad**
```yaml
ai:
  privacy:
    send_file_contents: true
    send_git_diff: true
    anonymize_paths: false
    exclude_sensitive_files:
      - "*.key"
      - "*.pem"
      - "*.env"
      - "secrets/**"
```

#### **Seguridad**
```yaml
ai:
  security:
    validate_api_key: true
    encrypt_local_cache: true
    require_confirmation: false  # Confirmar antes de enviar a IA
    max_retries: 3
    timeout_seconds: 30
```

### **7. Configuración de Fallbacks**

#### **Fallback Strategies**
```yaml
ai:
  fallback:
    on_api_error: "error"  # error, local, skip
    on_rate_limit: "wait"  # wait, error, local
    on_invalid_response: "retry"  # retry, error, local
    local_fallback:
      enabled: true
      use_templates: true
      use_git_hooks: true
```

#### **Modo Offline**
```yaml
ai:
  offline:
    enabled: true
    use_cached_responses: true
    use_templates: true
    use_git_hooks: true
```

## Configuración Completa de Ejemplo

```yaml
# .gggit/config.yaml
ai:
  # Configuración básica
  enabled: true
  provider: "openai"
  api_key: "${OPENAI_API_KEY}"
  api_url: "https://api.openai.com/v1"
  model: "gpt-4"
  
  # Control de costos
  limits:
    max_requests_per_day: 100
    max_tokens_per_request: 1000
    max_cost_per_day: 5.00
    enable_cost_tracking: true
  
  # Rate limiting
  rate_limiting:
    requests_per_minute: 10
    requests_per_hour: 100
    burst_limit: 5
  
  # Caching
  caching:
    enabled: true
    ttl_seconds: 3600
    max_cache_size: 1000
    cache_similar_requests: true
  
  # Generación de mensajes
  message_generation:
    auto_generate: true
    include_scope: true
    max_message_length: 100
    language: "es"
    style: "concise"
  
  # Validación de contexto
  context_validation:
    enabled: true
    strict_mode: false
    confidence_threshold: 0.8
    suggest_alternatives: true
    learn_from_project: true
  
  # Comportamiento por tipo
  commit_types:
    feat:
      auto_generate: true
      require_scope: false
      validation_strict: false
    fix:
      auto_generate: true
      require_scope: false
      validation_strict: true
    perf:
      auto_generate: false
      require_scope: true
      validation_strict: true
  
  # Análisis de archivos
  file_analysis:
    include_patterns:
      - "*.py"
      - "*.js"
      - "*.ts"
    exclude_patterns:
      - "*.log"
      - "node_modules/**"
    max_file_size: 10000
    analyze_binary_files: false
  
  # Logging
  logging:
    level: "INFO"
    log_requests: true
    log_responses: false
    log_costs: true
    log_file: ".gggit/ai.log"
  
  # Privacidad
  privacy:
    send_file_contents: true
    send_git_diff: true
    anonymize_paths: false
    exclude_sensitive_files:
      - "*.key"
      - "*.env"
      - "secrets/**"
  
  # Fallback
  fallback:
    on_api_error: "error"
    on_rate_limit: "wait"
    on_invalid_response: "retry"
    local_fallback:
      enabled: true
      use_templates: true
```

## Consideraciones de Implementación

### **1. Configuración por Niveles**
- **Global**: Configuración por defecto
- **Proyecto**: `.gggit/config.yaml`
- **Usuario**: `~/.gggit/config.yaml`
- **Comando**: Parámetros de línea de comandos

### **2. Validación de Configuración**
- **Validar API keys**: Al inicializar
- **Validar límites**: Antes de hacer llamadas
- **Validar modelos**: Verificar disponibilidad
- **Validar permisos**: Archivos, red, etc.

### **3. Configuración Dinámica**
- **Hot reload**: Recargar configuración sin reiniciar
- **Override temporal**: Parámetros de línea de comandos
- **Configuración condicional**: Basada en contexto del proyecto

## Preguntas para Discusión

1. **¿Qué configuraciones consideras más críticas** para la primera implementación?
2. **¿Cómo manejar costos** en equipos grandes?
3. **¿Qué nivel de personalización** es necesario vs. complejidad?
4. **¿Cómo validar configuración** sin hacer llamadas costosas?
5. **¿Qué fallbacks** son más importantes?
6. **¿Cómo balancear privacidad** vs. funcionalidad?
