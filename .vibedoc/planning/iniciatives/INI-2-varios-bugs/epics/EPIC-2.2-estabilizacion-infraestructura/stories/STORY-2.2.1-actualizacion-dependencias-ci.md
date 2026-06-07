# [HISTORIA] - Actualización Unificada de Dependencias de CI/CD

## 🎯 Objetivo

Actualizar de forma consolidada las versiones de las GitHub Actions utilizadas en todos los workflows de automatización a sus últimas versiones estables (Checkout v6, Cache v5, Upload-Artifact v6, Download-Artifact v7), validando el paso correcto de la CI y cerrando de manera automática las PRs de Dependabot obsoletas que están encoladas desde 2025.

## 🌎 Contexto

Actualmente, tenemos 4 PRs abiertas de Dependabot en GitHub que intentan actualizar las Actions pero fallan en CI. Esto ocurre porque estas ramas de Dependabot fueron creadas en 2025 y carecen de las correcciones de estabilización del entorno aplicadas el 2 de junio de 2026. Resolver esto de manera unificada previene la fricción y limpia la deuda técnica de infraestructura rápidamente.

## 💡 Propuesta de Resolución

Se propone editar manualmente los archivos YAML de `.github/workflows/` (`ci.yml`, `security-lint.yml`, `test-commands.yml`, `test.yml`, `cross-platform-test.yml`) para elevar las versiones de las Actions. El cambio se realizará en una rama específica creada con `gh issue develop`, y se validará mediante un Pull Request. Al integrarse a `main`, las PRs de Dependabot se marcarán automáticamente como superadas.

## 📦 Artefactos

- 📦 **Archivos de Workflow Actualizados**: `.github/workflows/ci.yml`, `.github/workflows/security-lint.yml`, `.github/workflows/test-commands.yml`, `.github/workflows/test.yml`, `.github/workflows/cross-platform-test.yml`.
- 📦 **Zettel de Decisión**: Documentación de la resolución en el Zettelkasten bajo el Sistema 13.

## 🔍 Criterios de Aceptación

### Consistencia en Workflows:
- Dado que actualizamos las dependencias de GitHub Actions
- Cuando se inspeccione cualquier archivo en `.github/workflows/`
- Entonces todas las menciones a `actions/checkout` deben usar `@v6`, `actions/cache` debe usar `@v5`, `actions/upload-artifact` debe usar `@v6`, y `actions/download-artifact` debe usar `@v7`.

### Éxito de la CI/CD:
- Dado que los workflows fueron actualizados
- Cuando se ejecute el pipeline de GitHub Actions en la Pull Request
- Entonces todos los jobs (tests, calidad, seguridad, notificaciones) deben pasar en verde sin errores de deprecación o sintaxis.

### Resolución de PRs obsoletas:
- Dado que los cambios unificados se integran a la rama `main`
- Cuando se revise la pestaña de Pull Requests de GitHub
- Entonces las PRs antiguas de Dependabot (#14, #15, #16, #17) deben cerrarse automáticamente por estar superadas por la nueva implementación.

🔗 Dependencias y Recursos

### Dependencias
- Ninguna.

### Recursos
- GitHub CLI (`gh`) configurado en la terminal.
