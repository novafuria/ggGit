# 1.2.7.2.1 - Decisiones: Análisis de Complejidad

## Resumen de Decisiones

**Fecha**: 2024-12-19
**Historia**: STORY-1.2.7.2 - Análisis de Complejidad
**Objetivo**: Documentar decisiones tomadas durante la implementación del análisis de complejidad

## Análisis de Estado Actual

### **✅ Elementos Ya Implementados**
1. **GitInterface**: Ya implementado con métodos `get_staged_files()` y `get_unstaged_files()`
2. **ColorManager**: Ya disponible para feedback visual
3. **ConfigManager**: Ya implementado con configuraciones IA para criterios de decisión
4. **BaseCommand**: Ya implementado con método `_is_ai_configured()`

### **⚠️ Inconsistencias Detectadas**
1. **Métodos de diff faltantes**: GitInterface no tiene métodos para obtener contenido de diff o contar líneas
2. **Clase ComplexityAnalyzer**: No existe
3. **Métodos para análisis de archivos**: No hay métodos para obtener tamaño de archivos o análisis de contenido

## Decisiones Tomadas

### **1. Extender GitInterface con Métodos de Análisis**

**Decisión**: Agregar métodos específicos para análisis de complejidad en GitInterface.

**Justificación**: 
- Mantiene la responsabilidad de Git en GitInterface
- Proporciona métodos reutilizables para análisis
- Sigue el patrón de métodos específicos ya implementado

**Métodos a Agregar**:
```python
def get_diff_content(self, files: Optional[List[str]] = None, staged: bool = False) -> str:
    """Get diff content as string for analysis."""

def get_diff_line_count(self, files: Optional[List[str]] = None, staged: bool = False) -> int:
    """Get number of lines in diff for complexity analysis."""

def get_file_size(self, file_path: str) -> int:
    """Get file size in bytes for complexity analysis."""

def get_files_to_analyze(self) -> List[str]:
    """Get files to analyze (staged if available, otherwise unstaged)."""
```

### **2. Crear Clase ComplexityAnalyzer**

**Decisión**: Crear clase independiente para análisis de complejidad.

**Justificación**:
- Separa responsabilidades (GitInterface para Git, ComplexityAnalyzer para análisis)
- Permite testing independiente
- Facilita mantenimiento y extensión

**Implementación Propuesta**:
```python
class ComplexityAnalyzer:
    def __init__(self, git_interface: GitInterface, config_manager: ConfigManager):
        self.git = git_interface
        self.config = config_manager
    
    def should_use_ai(self) -> Tuple[bool, Dict[str, Any]]:
        """Decide if AI should be used based on complexity analysis."""
    
    def get_fallback_message(self, analysis: Dict[str, Any]) -> str:
        """Get educational fallback message for complex changes."""
```

### **3. Criterios de Decisión Configurables**

**Decisión**: Usar configuraciones IA para criterios de decisión.

**Justificación**:
- Permite personalización por proyecto
- Sigue el patrón de configuración existente
- Facilita ajustes sin modificar código

**Configuraciones a Usar**:
- `ai.analysis.max_files`: Máximo número de archivos
- `ai.analysis.max_diff_lines`: Máximo número de líneas de diff
- `ai.analysis.max_file_size`: Máximo tamaño de archivo en bytes

### **4. Fallback Educativo Específico**

**Decisión**: Implementar mensajes educativos específicos para enseñar buenas prácticas.

**Justificación**:
- Mejora la experiencia de usuario
- Enseña buenas prácticas de Git
- Proporciona sugerencias accionables

**Mensajes Propuestos**:
```python
FALLBACK_MESSAGE = """
⚠️ No es aconsejable commitear tanto contenido
💡 Sugerencia: Selecciona grupos de archivos más pequeños
   Usa 'git add <archivo>' para archivos específicos
   O 'ggfeat "mensaje manual"' para commit completo
"""
```

## Estructura de Implementación

### **Archivos a Crear**
1. **`src/core/ai/complexity_analyzer.py`**: Clase ComplexityAnalyzer
2. **`tests/test_complexity_analyzer.py`**: Tests unitarios

### **Archivos a Modificar**
1. **`src/core/git.py`**: Agregar métodos de análisis de diff

### **Estructura de Clase ComplexityAnalyzer**
```python
class ComplexityAnalyzer:
    def __init__(self, git_interface: GitInterface, config_manager: ConfigManager):
        self.git = git_interface
        self.config = config_manager
    
    def analyze_complexity(self) -> Dict[str, Any]:
        """Analyze complexity of current changes."""
    
    def should_use_ai(self) -> Tuple[bool, Dict[str, Any]]:
        """Decide if AI should be used based on complexity analysis."""
    
    def get_fallback_message(self, analysis: Dict[str, Any]) -> str:
        """Get educational fallback message for complex changes."""
    
    def _get_files_to_analyze(self) -> List[str]:
        """Get files to analyze (staged if available, otherwise unstaged)."""
    
    def _get_complexity_metrics(self, files: List[str]) -> Dict[str, Any]:
        """Get complexity metrics for given files."""
```

## Criterios de Decisión

### **Lógica de Decisión**
```python
def should_use_ai(self) -> Tuple[bool, Dict[str, Any]]:
    """Decide if AI should be used based on complexity analysis."""
    analysis = self.analyze_complexity()
    
    # Get configuration limits
    max_files = self.config.get_config('ai.analysis.max_files', 10)
    max_diff_lines = self.config.get_config('ai.analysis.max_diff_lines', 200)
    max_file_size = self.config.get_config('ai.analysis.max_file_size', 5000)
    
    # Check if any limit is exceeded
    if (analysis['file_count'] > max_files or 
        analysis['diff_lines'] > max_diff_lines or 
        analysis['max_file_size'] > max_file_size):
        return False, analysis
    
    return True, analysis
```

### **Métricas de Complejidad**
- **file_count**: Número de archivos modificados
- **diff_lines**: Número total de líneas de diff
- **max_file_size**: Tamaño del archivo más grande modificado
- **files**: Lista de archivos modificados

## Integración con Sistema Existente

### **Uso en Comandos**
```python
# En cualquier comando que herede de BaseCommand
analyzer = ComplexityAnalyzer(self.git, self.config)
should_use_ai, analysis = analyzer.should_use_ai()

if should_use_ai:
    # Usar IA para generar mensaje
    pass
else:
    # Mostrar fallback educativo
    fallback_message = analyzer.get_fallback_message(analysis)
    click.echo(ColorManager.warning(fallback_message))
```

### **Configuración**
```yaml
ai:
  analysis:
    max_files: 10
    max_diff_lines: 200
    max_file_size: 5000
```

## Próximos Pasos

1. **Extender GitInterface** con métodos de análisis de diff
2. **Crear ComplexityAnalyzer** con lógica de decisión
3. **Implementar fallback educativo** con mensajes específicos
4. **Crear tests unitarios** para validar funcionalidad
5. **Integrar con comandos existentes** para uso real

## Referencias
- **Historia**: STORY-1.2.7.2 - Análisis de Complejidad
- **GitInterface**: `src/core/git.py`
- **ConfigManager**: `src/core/config.py`
- **Configuraciones IA**: `config/config-schema.yaml`
