# [EXPERIMENTO] - Implementar validador de consistencia de comandos en CI

## 🎯 Objetivo

Desarrollar y validar un script automatizado en Python (`scripts/validate_docs_sync.py`) que compruebe la sincronización 1:1 entre los comandos físicos en `src/commands/*.py` y la documentación de referencia en `docs/commands.md`, integrándolo como un paso obligatorio del pipeline de CI/CD para impedir la deriva de documentación.

## 🌎 Contexto

Bajo la metodología Vibedoc, un cambio en el software sin su correspondiente reflejo documental rompe el producto. Este experimento busca demostrar empíricamente la hipótesis [[13a1 - Hipótesis: Validación de consistencia en pipeline de CI]] como un mecanismo robusto para erradicar el "Patrón de Jon" en el ciclo de desarrollo colaborativo humano-agente.

## 💡 Diseño Experimental

1. **Desarrollo del Script**: Crear `scripts/validate_docs_sync.py` que:
   - Liste todos los archivos `src/commands/gg*.py` excluyendo utilitarios generales o de configuración (si aplica).
   - Analice sintácticamente `docs/commands.md` (o el archivo de referencia correspondiente) buscando encabezados, tablas o menciones de formato estándar para cada uno de los comandos listados.
   - Retorne un código de salida `0` si todos los comandos están documentados, o `1` detallando qué comandos carecen de documentación.
2. **Fase de Simulación**: Correr el script localmente introduciendo un comando dummy sin documentación (`src/commands/ggdummytest.py`) y comprobar que el script falla de manera predecible.
3. **Integración en CI**: Agregar el paso en `.github/workflows/ci.yml` dentro del job `quality-gates`.

## 📦 Artefactos Esperados

- 📦 **Script Validador**: `scripts/validate_docs_sync.py` con pruebas unitarias asociadas.
- 📦 **Workflow de CI Modificado**: Modificación en `.github/workflows/ci.yml` para ejecutar el script validador.

## 🔍 Criterios de Éxito

### Detección Precisa de Omisiones:
- Dado que existe un comando no documentado en la carpeta `src/commands/`
- Cuando se ejecute el script `validate_docs_sync.py`
- Entonces el script debe fallar obligatoriamente, detallando el archivo huérfano de documentación y retornando un código de salida `1`.

### Falso Positivo Inexistente:
- Dado que todos los comandos reales de la suite están debidamente explicados en `docs/commands.md`
- When se ejecute el script `validate_docs_sync.py`
- Entonces el script debe pasar exitosamente con código de salida `0`.

🔗 Referencias

- [[13a1 - Hipótesis: Validación de consistencia en pipeline de CI]]
