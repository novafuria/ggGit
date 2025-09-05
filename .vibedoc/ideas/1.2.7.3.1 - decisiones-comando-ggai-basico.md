# 1.2.7.3.1 - Decisiones: Comando ggai Básico

## Resumen de Decisiones

**Fecha**: 2024-12-19
**Historia**: STORY-1.2.7.3 - Comando ggai Básico
**Objetivo**: Documentar decisiones tomadas durante la implementación del comando ggai básico

## Análisis de Estado Actual

### **✅ Elementos Ya Implementados**
1. **BaseCommand**: Ya implementado con método `_is_ai_configured()`
2. **ComplexityAnalyzer**: Ya implementado para análisis de complejidad
3. **ConfigManager**: Ya implementado con configuraciones IA
4. **Patrón de comandos**: Comandos siguen patrón BaseCommand + Click
5. **Configuraciones IA**: Ya definidas en `config-schema.yaml`

### **⚠️ Inconsistencias Detectadas**
1. **Comando ggai**: No existe
2. **Sistema de tracking**: No hay implementación de `.gggit/ai-usage.yaml`
3. **Subcomandos**: No hay patrón establecido para subcomandos (solo `ggconfig` usa argumentos)
4. **Generación de mensajes IA**: No hay implementación real de IA

## Decisiones Tomadas

### **1. Patrón de Subcomandos con Click**

**Decisión**: Usar Click Groups para implementar subcomandos en `ggai`.

**Justificación**: 
- Click Groups proporcionan subcomandos nativos
- Mantiene consistencia con el patrón Click existente
- Facilita la implementación de `ggai usage`, `ggai usage reset`, `ggai test`

**Implementación Propuesta**:
```python
@click.group()
def ggai():
    """ggai - AI-powered commit message generation and management."""
    pass

@ggai.command()
def usage():
    """Show AI usage statistics and costs."""
    pass

@ggai.command()
def test():
    """Test AI connection and configuration."""
    pass

@ggai.group()
def usage():
    """Usage management commands."""
    pass

@usage.command()
def reset():
    """Reset usage tracking counters."""
    pass
```

### **2. Sistema de Tracking de Consumo**

**Decisión**: Implementar sistema de tracking en archivo `.gggit/ai-usage.yaml`.

**Justificación**:
- Sigue el patrón de archivos de datos en `.gggit/`
- YAML es legible y fácil de procesar
- Permite tracking detallado de consumo por día

**Estructura del Archivo**:
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
  cost_limit: 5.00
  tracking_enabled: true
```

### **3. Clase AiUsageTracker**

**Decisión**: Crear clase independiente para manejo de tracking de consumo.

**Justificación**:
- Separa responsabilidades (comando vs. tracking)
- Permite testing independiente
- Facilita reutilización en otros comandos

**Implementación Propuesta**:
```python
class AiUsageTracker:
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.usage_file = self.config.get_config('ai.usage_file', '.gggit/ai-usage.yaml')
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get current usage statistics."""
    
    def increment_usage(self, command: str, tokens: int, cost: float) -> None:
        """Increment usage counters."""
    
    def reset_usage(self) -> None:
        """Reset usage tracking counters."""
    
    def is_tracking_enabled(self) -> bool:
        """Check if tracking is enabled."""
```

### **4. Generación de Mensajes IA Mock**

**Decisión**: Implementar generación de mensajes IA con mock para MVP.

**Justificación**:
- Permite completar la funcionalidad sin dependencias externas
- Facilita testing y desarrollo
- Puede ser reemplazado por implementación real en el futuro

**Implementación Propuesta**:
```python
class AiMessageGenerator:
    def __init__(self, config_manager: ConfigManager, usage_tracker: AiUsageTracker):
        self.config = config_manager
        self.usage_tracker = usage_tracker
    
    def generate_message(self, files: List[str], diff_content: str) -> str:
        """Generate commit message using AI (mock implementation)."""
        # Mock implementation for MVP
        return f"feat: update {len(files)} files"
    
    def test_connection(self) -> bool:
        """Test AI connection (mock implementation)."""
        # Mock implementation for MVP
        return True
```

### **5. Integración con ComplexityAnalyzer**

**Decisión**: Usar ComplexityAnalyzer para decisión IA vs. fallback.

**Justificación**:
- Reutiliza funcionalidad ya implementada
- Mantiene consistencia en la decisión
- Sigue el patrón de separación de responsabilidades

**Flujo de Decisión**:
```python
def execute_ggai(self):
    """Execute main ggai command."""
    # Check if AI is configured
    if not self._is_ai_configured():
        click.echo(ColorManager.warning("IA no configurada. Usa 'ggconfig set ai.enabled true'"))
        return 1
    
    # Analyze complexity
    analyzer = ComplexityAnalyzer(self.git, self.config)
    should_use_ai, analysis = analyzer.should_use_ai()
    
    if should_use_ai:
        # Generate message with AI
        generator = AiMessageGenerator(self.config, self.usage_tracker)
        message = generator.generate_message(analysis['files'], diff_content)
        click.echo(ColorManager.success(f"Mensaje generado: {message}"))
    else:
        # Show fallback message
        fallback = analyzer.get_fallback_message(analysis)
        click.echo(ColorManager.warning(fallback))
    
    return 0
```

## Estructura de Implementación

### **Archivos a Crear**
1. **`src/commands/ggai.py`**: Comando principal con subcomandos
2. **`src/core/ai/usage_tracker.py`**: Clase AiUsageTracker
3. **`src/core/ai/message_generator.py`**: Clase AiMessageGenerator (mock)
4. **`tests/test_ggai_command.py`**: Tests para comando ggai
5. **`tests/test_ai_usage_tracker.py`**: Tests para AiUsageTracker

### **Archivos a Modificar**
1. **`src/core/ai/__init__.py`**: Agregar exports de nuevas clases

### **Estructura de Comando ggai**
```python
@click.group()
def ggai():
    """ggai - AI-powered commit message generation and management."""
    pass

@ggai.command()
def usage():
    """Show AI usage statistics and costs."""
    # Show usage stats from AiUsageTracker

@ggai.command()
def test():
    """Test AI connection and configuration."""
    # Test connection using AiMessageGenerator

@ggai.group()
def usage():
    """Usage management commands."""
    pass

@usage.command()
def reset():
    """Reset usage tracking counters."""
    # Reset counters using AiUsageTracker

# Main command (no subcommand)
@ggai.command()
def main():
    """Generate commit message using AI or show fallback."""
    # Main AI generation logic
```

## Criterios de Decisión

### **Lógica de Subcomandos**
```python
# ggai usage
def show_usage_stats():
    """Show usage statistics in formatted output."""
    stats = usage_tracker.get_usage_stats()
    click.echo(f"📊 Consumo de IA - Período: {stats['period']['start_date']}")
    click.echo(f"├── Requests: {stats['totals']['requests']}")
    click.echo(f"├── Tokens usados: {stats['totals']['tokens']:,}")
    click.echo(f"└── Costo estimado: ${stats['totals']['cost']:.2f}/${stats['limits']['cost_limit']:.2f}")

# ggai usage reset
def reset_usage_counters():
    """Reset usage tracking counters."""
    usage_tracker.reset_usage()
    click.echo(ColorManager.success("✅ Contador de consumo reiniciado"))
    click.echo(f"📊 Nuevo período iniciado: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ggai test
def test_ai_connection():
    """Test AI connection and configuration."""
    generator = AiMessageGenerator(config, usage_tracker)
    if generator.test_connection():
        click.echo(ColorManager.success("✅ Conexión IA exitosa"))
    else:
        click.echo(ColorManager.error("❌ Error de conexión IA"))
```

### **Manejo de Archivos de Tracking**
```python
def load_usage_file(self) -> Dict[str, Any]:
    """Load usage data from YAML file."""
    if not os.path.exists(self.usage_file):
        return self._create_default_usage_data()
    
    with open(self.usage_file, 'r') as f:
        return yaml.safe_load(f)

def save_usage_file(self, data: Dict[str, Any]) -> None:
    """Save usage data to YAML file."""
    os.makedirs(os.path.dirname(self.usage_file), exist_ok=True)
    with open(self.usage_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
```

## Integración con Sistema Existente

### **Uso en Comandos Existentes**
```python
# En cualquier comando que herede de BaseCommand
if not message and self._is_ai_configured():
    # Use ggai logic for AI generation
    analyzer = ComplexityAnalyzer(self.git, self.config)
    should_use_ai, analysis = analyzer.should_use_ai()
    
    if should_use_ai:
        generator = AiMessageGenerator(self.config, self.usage_tracker)
        message = generator.generate_message(analysis['files'], diff_content)
    else:
        fallback = analyzer.get_fallback_message(analysis)
        click.echo(ColorManager.warning(fallback))
        return 1
```

### **Configuración**
```yaml
ai:
  enabled: true
  provider: "openai"
  model: "gpt-3.5-turbo"
  cost_limit: 5.00
  tracking_enabled: true
  usage_file: ".gggit/ai-usage.yaml"
```

## Próximos Pasos

1. **Crear AiUsageTracker** para manejo de tracking de consumo
2. **Crear AiMessageGenerator** con implementación mock
3. **Implementar comando ggai** con subcomandos Click
4. **Crear tests unitarios** para validar funcionalidad
5. **Integrar con ComplexityAnalyzer** para decisión IA vs. fallback

## Referencias
- **Historia**: STORY-1.2.7.3 - Comando ggai Básico
- **ComplexityAnalyzer**: `src/core/ai/complexity_analyzer.py`
- **BaseCommand**: `src/core/base_commands/base.py`
- **ConfigManager**: `src/core/config.py`
- **Configuraciones IA**: `config/config-schema.yaml`
