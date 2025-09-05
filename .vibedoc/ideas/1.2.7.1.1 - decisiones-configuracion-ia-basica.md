# 1.2.7.1.1 - Decisiones: Configuración IA Básica

## Resumen de Decisiones

**Fecha**: 2024-12-19
**Historia**: STORY-1.2.7.1 - Configuración IA Básica
**Objetivo**: Documentar decisiones tomadas durante la implementación de configuración IA básica

## Análisis de Estado Actual

### **✅ Elementos Ya Implementados**
1. **Esquema de configuración IA**: Ya existe sección `ai` en `config-schema.yaml` con configuraciones básicas
2. **ConfigManager**: Ya implementado con métodos `get_config()` y `set_config()`
3. **Comando ggconfig**: Ya funcional con acciones `get`, `set`, `list`, `reset`
4. **BaseCommand**: Ya implementado con acceso a `self.config`

### **⚠️ Inconsistencias Detectadas**
1. **Configuraciones faltantes**: El esquema actual no incluye las configuraciones requeridas por la historia
2. **Método `_is_ai_configured()`**: No existe en BaseCommand

## Decisiones Tomadas

### **1. Extender Esquema de Configuración Existente**

**Decisión**: Agregar configuraciones faltantes al esquema existente en lugar de crear uno nuevo.

**Justificación**: 
- Mantiene consistencia con el sistema de configuración actual
- Aprovecha la validación JSON Schema ya implementada
- Sigue el patrón de configuración jerárquica existente

**Configuraciones a Agregar**:
```yaml
ai:
  # Configuraciones existentes (ya implementadas)
  enabled: boolean
  provider: enum ["openai", "anthropic", "azure", "local"]
  api_key_env: string
  model: string
  base_url: string (opcional)
  
  # Nuevas configuraciones requeridas
  cost_limit: number (default: 5.00)
  tracking_enabled: boolean (default: true)
  usage_file: string (default: ".gggit/ai-usage.yaml")
  analysis:
    max_files: integer (default: 10)
    max_diff_lines: integer (default: 200)
    max_file_size: integer (default: 5000)
```

### **2. Implementar Método `_is_ai_configured()` en BaseCommand**

**Decisión**: Agregar método `_is_ai_configured()` en BaseCommand para verificar disponibilidad de IA.

**Justificación**:
- Centraliza la lógica de verificación de IA
- Permite reutilización en todos los comandos
- Sigue el patrón de métodos de utilidad en BaseCommand

**Implementación Propuesta**:
```python
def _is_ai_configured(self) -> bool:
    """Check if AI is configured and available."""
    # Verificar configuración básica
    if not self.config.get_config('ai.enabled', False):
        return False
    
    # Verificar proveedor
    provider = self.config.get_config('ai.provider')
    if not provider:
        return False
    
    # Verificar API key
    api_key_env = self.config.get_config('ai.api_key_env')
    if not api_key_env or not os.getenv(api_key_env):
        return False
    
    return True
```

### **3. Mantener Compatibilidad con Sistema Existente**

**Decisión**: No modificar la estructura existente del ConfigManager o ggconfig.

**Justificación**:
- Evita breaking changes
- Mantiene la funcionalidad existente intacta
- Sigue el principio de extensión sobre modificación

## Configuración por Defecto

### **Valores por Defecto para Configuraciones IA**
```yaml
ai:
  enabled: false
  provider: "openai"
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-3.5-turbo"
  base_url: null
  cost_limit: 5.00
  tracking_enabled: true
  usage_file: ".gggit/ai-usage.yaml"
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000
```

## Validaciones Requeridas

### **Validaciones JSON Schema**
- `ai.enabled`: boolean
- `ai.provider`: enum ["openai", "anthropic", "azure", "local"]
- `ai.api_key_env`: string, no vacío
- `ai.model`: string, no vacío
- `ai.base_url`: string, URL válida o null
- `ai.cost_limit`: number, > 0
- `ai.tracking_enabled`: boolean
- `ai.usage_file`: string, ruta válida
- `ai.analysis.max_files`: integer, > 0
- `ai.analysis.max_diff_lines`: integer, > 0
- `ai.analysis.max_file_size`: integer, > 0

## Impacto en Arquitectura

### **Archivos a Modificar**
1. **`config/config-schema.yaml`**: Agregar configuraciones IA faltantes
2. **`src/core/base_commands/base.py`**: Agregar método `_is_ai_configured()`

### **Archivos a Crear**
1. **Tests unitarios**: Para ConfigManager con configuraciones IA
2. **Tests unitarios**: Para método `_is_ai_configured()`

## Próximos Pasos

1. **Extender esquema de configuración** con configuraciones IA faltantes
2. **Implementar método `_is_ai_configured()`** en BaseCommand
3. **Crear tests unitarios** para validar funcionalidad
4. **Documentar configuraciones IA** en documentación existente

## Referencias
- **Historia**: STORY-1.2.7.1 - Configuración IA Básica
- **Esquema existente**: `config/config-schema.yaml`
- **ConfigManager**: `src/core/config.py`
- **BaseCommand**: `src/core/base_commands/base.py`
