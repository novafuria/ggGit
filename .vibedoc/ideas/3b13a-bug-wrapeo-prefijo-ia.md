# 3b13a - Bug: Wrapeo de prefijo en mensajes de IA

## Problema Identificado
Los mensajes generados por IA tienen doble prefijo: `"feat: feat: mensaje"` en lugar de `"feat: mensaje"`.

## Causa Raíz
El flujo actual tiene duplicación de prefijos:

1. **`AiMessageGenerator.generate_message()`** genera: `"feat: update file.py"`
2. **`CommitCommand.format_commit_message()`** agrega: `"feat: feat: update file.py"`

## Flujo Actual (Incorrecto)
```
ggfeat (sin mensaje)
├── _generate_ai_message()
│   ├── AiMessageGenerator.generate_message() → "feat: update file.py"
│   └── _execute_manual_commit("feat: update file.py")
│       └── CommitCommand("feat").execute("feat: update file.py")
│           └── format_commit_message() → "feat: feat: update file.py"
```

## Solución Propuesta

### Opción 1: Modificar AiMessageGenerator (Recomendada)
**Archivo**: `src/core/ai/message_generator.py`

**Cambio**:
```python
# Antes (línea 67)
message = f"{prefix}: update {file_name}"

# Después
message = f"update {file_name}"  # Sin prefijo
```

**Ventajas**:
- ✅ `CommitCommand` maneja el prefijo correctamente
- ✅ Consistente con mensajes manuales
- ✅ No duplica lógica de prefijos

### Opción 2: Modificar BaseCommand._generate_ai_message()
**Archivo**: `src/core/base_commands/base.py`

**Cambio**:
```python
# Antes (línea 220)
message = generator.generate_message(files, diff_content)

# Después
message = generator.generate_message(files, diff_content)
# Remover prefijo si existe
if ':' in message:
    message = message.split(':', 1)[1].strip()
```

**Desventajas**:
- ❌ Lógica compleja de parsing
- ❌ Duplica manejo de prefijos
- ❌ Menos robusto

## Implementación Recomendada

### 1. Modificar AiMessageGenerator
```python
def generate_message(self, files: List[str], diff_content: str) -> str:
    # ... análisis de archivos ...
    
    # Generar mensaje SIN prefijo
    if len(files) == 1:
        file_name = os.path.basename(files[0])
        message = f"update {file_name}"
    else:
        message = f"update {len(files)} files"
    
    # Agregar scope si aplica
    if file_types:
        scope = self._get_scope_from_file_types(file_types)
        if scope:
            message = f"({scope}) {message}"
    
    return message
```

### 2. Verificar Comportamiento
- **ggfeat**: `"feat: update file.py"` ✅
- **ggfix**: `"fix: update file.py"` ✅
- **ggbreak**: `"break: update file.py"` ✅
- **Con scope**: `"feat(api): update file.py"` ✅

## Impacto de la Solución
- ✅ Resuelve el bug de wrapeo
- ✅ Mantiene consistencia con mensajes manuales
- ✅ No afecta funcionalidad existente
- ✅ Simplifica la lógica de generación de mensajes
