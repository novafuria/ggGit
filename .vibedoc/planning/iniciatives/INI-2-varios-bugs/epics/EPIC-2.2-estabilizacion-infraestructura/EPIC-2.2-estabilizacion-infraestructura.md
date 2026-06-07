# [EPICA] - Estabilización de Infraestructura y Dependencias de CI/CD

## 🎯 Objetivo de la Épica

Estabilizar las dependencias y la infraestructura de automatización (CI/CD) de ggGit resolviendo las Pull Requests obsoletas de Dependabot, unificando las actualizaciones de las GitHub Actions a sus versiones estables más recientes, y garantizando la confiabilidad del pipeline en múltiples entornos de desarrollo de forma consistente con las últimas mejoras de calidad.

## 🌎 Contexto y Justificación

Actualmente, existen 4 Pull Requests abiertas por Dependabot desde finales de 2025 para actualizar diferentes GitHub Actions (`actions/checkout`, `actions/cache`, `actions/upload-artifact`, y `actions/download-artifact`). Todas estas PRs están fallando en CI porque fueron creadas antes de la gran estabilización del pipeline que el equipo realizó el 2 de junio de 2026. Al estar basadas en commits obsoletos de 2025, no cuentan con las correcciones de Conda, PYTHONPATH, MyPy y Pytest que estabilizaron la suite de pruebas. 

Para eliminar esta deuda técnica de infraestructura de manera limpia y sin introducir complejidad accidental, se requiere consolidar estas actualizaciones en una sola rama de desarrollo basada en el `main` actual, validando que el pipeline pase completamente.

## 💡 Visión de la Solución

Se propone resolver todas las PRs de Dependabot aplicando un cambio consolidado manual directo sobre el código de producción actual, subiendo las versiones de las Actions en todos los flujos de trabajo de `.github/workflows/`. Esto cerrará automáticamente las PRs obsoletas de Dependabot y asegurará que usemos herramientas seguras y rápidas sin el coste de esperar encolamientos del bot externo.

## 🚀 Alcance de la Épica

### Debe Tener
- **Bumpear Actions**: Actualizar `actions/checkout` a `@v6`, `actions/cache` a `@v5`, `actions/upload-artifact` a `@v6`, y `actions/download-artifact` a `@v7` en todos los archivos de `.github/workflows/`.
- **Validación de Pipeline**: Asegurar que todos los workflows pasen en verde con el pipeline de CI/CD de GitHub.
- **Integración Limpia**: Cerrar automáticamente las 4 PRs antiguas de Dependabot.

### Podría Tener
- **Documentación**: Crear un zettel específico sobre mantenimiento de dependencias de infraestructura.

### Fuera de Alcance
- **Actualizaciones de código de dependencias Python**: No se tocará `requirements-dev.txt` ni `environment.yml` en esta épica.

## ⚠️ Riesgos y Supuestos

### Riesgos Identificados
- ❗ **Incompatibilidad de APIs de GitHub Actions**: Que alguna versión mayor de las Actions introduzca cambios de esquema en sus parámetros (por ejemplo, el parámetro `path` o `name`). Mitigado revisando la compatibilidad de `actions/checkout@v6` y `upload-artifact@v6`.

### Supuestos Clave
- ❓ Asumimos que los cambios propuestos por Dependabot son seguros y recomendados.
- ❓ Asumimos que GitHub cerrará automáticamente las PRs al detectar que la versión solicitada ya está instalada en `main`.

## 🔗 Dependencias y Recursos Clave

### Dependencias
- Ninguna. El código en `main` está limpio y listo para recibir los cambios.

### Recursos Clave Necesarios
- Acceso a GitHub CLI para crear la issue, rama, y pull request.

## Referencias a Zettels
- [[13 - bugs y deuda tecnica de software]]
- [[11a - estabilizacion-entorno-ci-cd]]

## 📋 Historias de la Épica

### 🔄 Historias En Proceso
1. **STORY-2.2.1**: [Actualización Unificada de Dependencias de CI/CD](stories/STORY-2.2.1-actualizacion-dependencias-ci.md)
