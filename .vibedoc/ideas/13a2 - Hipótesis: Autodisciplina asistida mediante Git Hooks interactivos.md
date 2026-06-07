# 13a2 - Hipótesis: Autodisciplina asistida mediante Git Hooks interactivos

## Enunciado de la Hipótesis

**Dado** que el pipeline de CI puede resultar lento o tardío al ejecutarse solo después del `push`,  
**Si** implementamos un Git Hook de tipo `pre-push` o `pre-commit` local e interactivo que escanee el área de staging y pregunte activamente al desarrollador si ha actualizado los zettels del Zettelkasten o la documentación principal de los comandos que está modificando,  
**Entonces** fomentaremos un hábito de autodisciplina asistida consciente que atajará el desfase documental en una etapa temprana (local), reduciendo las ejecuciones fallidas en CI/CD en un 90%.

## Justificación y Modelo Mental

Un desarrollador valora el feedback instantáneo. Si la CI tarda 3-5 minutos en decirle que olvidó documentar algo, se interrumpe el flujo mental. Al trasladar esta verificación al hook local (`pre-push`), se crea un búcle de retroalimentación ultrarrápido y consultivo. No es un bloqueo ciego, sino una herramienta de asistencia que fomenta la autorreflexión y la responsabilidad personal antes de que el código salga de la máquina de trabajo.

## Validación Experimental Propuesta

El experimento consistiría en diseñar un script de hook interactivo en Python dentro de `config/hooks/` que use prompts de terminal (estilo Click) y configurar su instalación automática durante el proceso de `python install.py`.

## Referencias

- [[6 - sistema de instalacion y distribucion]]
- [[13a - Prevención del patrón de Jon en documentación]]
