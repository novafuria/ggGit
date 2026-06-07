# [EXPERIMENTO] - Deprecación y remoción segura de AiUsageTracker

## 🎯 Objetivo

Eliminar por completo el módulo `AiUsageTracker` y limpiar sus dependencias en el núcleo de `ggGit`, garantizando que la suite de tests unitarios y de integración siga pasando exitosamente (100% verde) tras la remoción del código redundante.

## 🌎 Contexto

La eliminación de características redundantes es clave para combatir la complejidad accidental. Este experimento demuestra empíricamente la viabilidad de la hipótesis [[13e1 - Hipótesis: Simplificación del núcleo mediante remoción de tracking de uso de IA]] definiendo un plan de eliminación seguro.

## 💡 Diseño Experimental

1. **Identificación de Dependencias**:
   - Usar un análisis estático (`grep -r "AiUsageTracker\|UsageTracker\|usage_tracker" src/`) para identificar todas las líneas de código donde se instancia o invoca el tracker de uso.
2. **Remoción del Código del Núcleo**:
   - Borrar el archivo `src/core/ai/usage_tracker.py`.
   - Modificar `src/core/base_commands/base.py` para eliminar la instanciación de `usage_tracker = AiUsageTracker(self.config)` y remover los pasos de guardado de cuota de tokens.
   - Modificar la firma y el cuerpo de `AiMessageGenerator` en `src/core/ai/message_generator.py` para que ya no reciba el tracker en su constructor.
3. **Limpieza de Tests**:
   - Eliminar el archivo de pruebas `tests/test_ai_usage_tracker.py`.
   - Eliminar los mocks de `usage_tracker` en `tests/test_base_command.py` u otros archivos de pruebas.
4. **Métrica de éxito**: Ejecutar `pytest` en la suite de pruebas y comprobar que todos los tests pasan en verde con cero tracebacks de importación rota o referencias huérfanas.

## 📦 Artefactos Esperados

- 📦 **Código del Núcleo Limpio**: Archivos `base.py`, `message_generator.py` modificados y simplificados.
- 📦 **Módulo Eliminado**: Eliminación física del archivo `usage_tracker.py` y de su test unitario `test_ai_usage_tracker.py`.

## 🔍 Criterios de Éxito

### Eliminación Completa:
- Dado que el módulo `usage_tracker.py` ha sido eliminado
- Cuando se ejecute la suite de pruebas mediante `pytest`
- Entonces la suite debe pasar al 100% con éxito, confirmando que ninguna otra clase depende críticamente del tracker.

### Generación de IA Intacta:
- Dado que el tracker de uso ya no existe en el sistema
- Cuando se invoque la generación automática con IA de un comando de commit (ej. `ggfeat`)
- Encontrándose el servicio de Ollama disponible, el comando debe generar el mensaje y realizar el commit con normalidad sin intentar escribir registros de uso de tokens en el disco.

🔗 Referencias

- [[13e1 - Hipótesis: Simplificación del núcleo mediante remoción de tracking de uso de IA]]
