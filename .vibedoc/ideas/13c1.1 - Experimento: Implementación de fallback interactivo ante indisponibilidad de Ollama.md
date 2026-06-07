# [EXPERIMENTO] - Implementación de fallback interactivo ante indisponibilidad de Ollama

## 🎯 Objetivo

Modificar el bloque de excepciones del generador de mensajes de IA (`_generate_ai_message` en `src/core/base_commands/base.py`) para capturar fallos de conexión específicos de Ollama u otros proveedores de IA y, en lugar de abortar, implementar un flujo interactivo mediante `click.confirm` y `click.prompt` que permita ingresar el mensaje manualmente y completar el commit de forma transparente.

## 🌎 Contexto

Actualmente, cualquier error en la llamada a la API de IA aborta la ejecución con código `1` (como se detalla en [[13c1 - Hipótesis: Degradación graciosa con fallback manual interactivo]]). Este experimento nos permitirá validar de manera práctica una mejora crítica en la UX y resiliencia de la suite de comandos de commit.

## 💡 Diseño Experimental

1. **Simulación de Caída**:
   - Detener el servicio local de Ollama (si está corriendo) o configurar una URL de API inexistente en `ggconfig` (p. ej., `ggconfig set ai.base_url http://localhost:9999`).
2. **Refactorización en BaseCommand (`src/core/base_commands/base.py`)**:
   - Capturar de forma precisa excepciones comunes de comunicación (ej. `ConnectionRefusedError`, `requests.exceptions.RequestException`).
   - Emitir un mensaje de aviso informativo en amarillo: `⚠️ El servicio de IA no está disponible o está apagado.`
   - Iniciar un flujo interactivo:
     ```python
     if click.confirm("¿Deseas ingresar un mensaje de commit manual para continuar?", default=True):
         mensaje = click.prompt("Mensaje de commit")
         return self._execute_manual_commit(mensaje, scope, amend)
     else:
         click.echo(ColorManager.info("Operación cancelada por el usuario."))
         return 1
     ```
3. **Validación Manual**: Ejecutar `ggfeat` sin argumentos con Ollama simuladamente apagado y verificar que la terminal nos guíe al flujo interactivo y realice el commit de manera exitosa.

## 📦 Artefactos Esperados

- 📦 **Código de BaseCommand Actualizado**: Cambios integrados en `src/core/base_commands/base.py`.
- 📦 **Suite de Tests de Integración de Fallback**: Un nuevo archivo `tests/test_ai_fallback_resilience.py` que verifique que el comando realiza una llamada interactiva (usando el mock de Click CliRunner) cuando la llamada de IA falla.

## 🔍 Criterios de Éxito

### Degradación Exitosa:
- Dado que el servicio de Ollama no responde
- Cuando el usuario ejecuta `ggfeat` sin especificar un mensaje de commit en los argumentos
- Entonces el sistema no debe lanzar un traceback ni salir con error, sino presentar de forma clara la opción para ingresar el mensaje manualmente.

### Confirmación de Commit:
- Dado que el usuario acepta ingresar el mensaje manual en el prompt de emergencia
- Cuando introduce un mensaje válido como "implement metadata parser"
- Entonces el commit se debe crear de forma exitosa bajo la convención correspondiente (`feat: implement metadata parser`).

🔗 Referencias

- [[13c1 - Hipótesis: Degradación graciosa con fallback manual interactivo]]
