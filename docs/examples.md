# Ejemplos de Uso

Esta guía presenta ejemplos prácticos y flujos de trabajo reales para ayudarte a aprovechar al máximo ggGit en diferentes escenarios de desarrollo.

## Flujos de Trabajo Comunes

### Desarrollo de Nueva Funcionalidad

Este es el flujo más común cuando trabajas en una nueva característica:

```bash
# 1. Actualizar rama principal
ggmain
ggpl

# 2. Crear rama para la nueva funcionalidad
ggb feature/autenticacion-usuarios

# 3. Hacer cambios en el código
# ... editar archivos ...

# 4. Agregar archivos modificados
gga

# 5. Hacer commit con IA (genera mensaje automáticamente)
ggfeat

# 6. Continuar desarrollando
# ... más cambios ...

# 7. Agregar y hacer commit de progreso
gga
ggfeat

# 8. Cuando esté listo, subir cambios
ggpp

# 9. Crear Pull Request (fuera de ggGit)
# 10. Después de aprobación, fusionar
ggmerge
```

### Corrección de Bug Crítico

Para bugs que requieren corrección inmediata:

```bash
# 1. Cambiar a rama principal y actualizar
ggmain
ggpl

# 2. Crear rama de hotfix
ggb hotfix/corregir-error-login

# 3. Hacer corrección
# ... corregir el bug ...

# 4. Agregar archivos y hacer commit
gga
ggfix

# 5. Fusionar inmediatamente a main
ggmerge

# 6. Subir cambios
ggpp

# 7. Etiquetar versión si es necesario
git tag v1.2.1
ggpp --tags
```

### Refactorización de Código

Para mejoras de código sin cambiar funcionalidad:

```bash
# 1. Crear rama para refactorización
ggb refactor/optimizar-consultas-db

# 2. Hacer cambios de refactorización
# ... optimizar código ...

# 3. Agregar archivos modificados
gga

# 4. Hacer commit de refactorización
ggrefactor

# 5. Agregar pruebas si es necesario
# ... escribir tests ...

# 6. Commit de pruebas
gga
ggtest

# 7. Subir y crear PR
ggpp
```

## Escenarios Específicos

### Trabajo con Documentación

Cuando actualizas documentación del proyecto:

```bash
# 1. Crear rama para documentación
ggb docs/actualizar-readme

# 2. Actualizar archivos de documentación
# ... editar README.md, docs/, etc. ...

# 3. Agregar archivos de documentación
gga *.md docs/

# 4. Hacer commit de documentación
ggdocs

# 5. Si también actualizas código de ejemplo
gga src/examples/
ggdocs
```

### Mejoras de Rendimiento

Para optimizaciones de rendimiento:

```bash
# 1. Crear rama de performance
ggb perf/optimizar-carga-imagenes

# 2. Implementar optimizaciones
# ... optimizar código ...

# 3. Agregar archivos modificados
gga

# 4. Hacer commit de rendimiento
ggperf

# 5. Agregar benchmarks si es necesario
gga tests/benchmarks/
ggtest

# 6. Subir cambios
ggpp
```

### Cambios en CI/CD

Para actualizaciones de integración continua:

```bash
# 1. Crear rama para CI
ggb ci/agregar-tests-automatizados

# 2. Actualizar archivos de CI
# ... editar .github/workflows/, etc. ...

# 3. Agregar archivos de CI
gga .github/

# 4. Hacer commit de CI
ggci

# 5. También actualizar scripts de build si es necesario
gga scripts/
ggbuild
```

## Trabajo en Equipo

### Sincronización con Equipo

Para mantenerte sincronizado con el trabajo del equipo:

```bash
# 1. Verificar estado actual
ggs

# 2. Actualizar rama principal
ggmain
ggpl

# 3. Actualizar tu rama de trabajo
ggb tu-rama-actual
ggpl

# 4. Si hay conflictos, resolverlos
# ... resolver conflictos ...

# 5. Continuar con tu trabajo
gga
ggfeat
```

### Revisión de Código

Antes de crear un Pull Request:

```bash
# 1. Verificar que todo esté agregado
ggs

# 2. Ver diferencias con main
ggdif main

# 3. Hacer commit final si es necesario
gga
ggfeat

# 4. Subir rama
ggpp

# 5. Crear Pull Request (fuera de ggGit)
```

### Integración de Cambios

Después de que se apruebe tu PR:

```bash
# 1. Cambiar a main y actualizar
ggmain
ggpl

# 2. Eliminar rama local (opcional)
git branch -d feature/tu-rama

# 3. Limpiar ramas remotas obsoletas
git remote prune origin
```

## Configuración de IA Avanzada

### Configuración por Proyecto

Para proyectos que requieren configuración específica:

```bash
# 1. Crear configuración de proyecto
mkdir .gggit
cat > .gggit/config.yaml << EOF
ai:
  enabled: true
  provider: ollama
  model: gemma3:4b

commits:
  prefix: "[PROJ-123]"
  max_length: 100

branches:
  main: "main"
  develop: "develop"
EOF

# 2. Configurar variable de entorno
export GGGIT_AI_KEY=ollama

# 3. Probar configuración
ggai test
```

### Uso con Diferentes Modelos de IA

```bash
# Para proyectos que requieren análisis más profundo
ggconfig set ai.model gemma3:8b

# Para proyectos simples
ggconfig set ai.model gemma3:4b

# Para proyectos que requieren contexto específico
ggconfig set ai.context "Este es un proyecto de e-commerce"
```

## Casos de Uso Avanzados

### Automatización con Scripts

Crear scripts que usen ggGit:

```bash
#!/bin/bash
# deploy.sh - Script de despliegue

# Verificar que estamos en main
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "Error: Debe estar en la rama main para desplegar"
    exit 1
fi

# Actualizar código
ggpl

# Ejecutar tests
pytest

# Si los tests pasan, hacer commit de despliegue
gga
ggci "Desplegar versión $(date +%Y%m%d-%H%M%S)"

# Subir cambios
ggpp
```

### Integración con IDEs

Configurar tu IDE para usar ggGit:

```json
// VS Code settings.json
{
    "git.enableSmartCommit": false,
    "terminal.integrated.shell.linux": "/bin/bash",
    "git.postCommitCommand": "ggs"
}
```

### Hooks de Git Personalizados

Crear hooks que usen ggGit:

```bash
#!/bin/sh
# .git/hooks/pre-commit

# Verificar que ggGit esté instalado
if ! command -v ggfeat &> /dev/null; then
    echo "Error: ggGit no está instalado"
    exit 1
fi

# Verificar que no haya archivos de debug
if git diff --cached --name-only | grep -E "\.(log|tmp|debug)$"; then
    echo "Error: No se pueden hacer commit de archivos de debug"
    exit 1
fi
```

## Solución de Problemas Comunes

### IA No Responde

```bash
# Verificar configuración
ggai status

# Probar conexión
ggai test

# Reiniciar servicio de IA
ggai restart

# Usar modo manual si es necesario
ggfeat "Mensaje manual"
```

### Conflictos de Merge

```bash
# Ver estado actual
ggs

# Ver archivos en conflicto
ggdif

# Resolver conflictos manualmente
# ... editar archivos ...

# Agregar archivos resueltos
gga

# Continuar merge
git commit
```

### Comandos No Encontrados

```bash
# Verificar instalación
ggv

# Reinstalar si es necesario
python install.py

# Verificar PATH
echo $PATH

# Agregar al PATH si es necesario
export PATH="$HOME/.local/bin:$PATH"
```

## Mejores Prácticas

### Organización de Commits

- Haz commits pequeños y frecuentes
- Un commit por concepto o cambio lógico
- Usa mensajes descriptivos generados por IA
- Revisa siempre antes de hacer commit

### Gestión de Ramas

- Usa nombres descriptivos para ramas
- Mantén ramas actualizadas con main
- Elimina ramas después de fusionar
- Usa ramas de feature para desarrollo

### Configuración

- Configura IA para tu flujo de trabajo
- Usa configuración de proyecto para reglas del equipo
- Mantén configuración personal en ~/.gggit/
- Documenta configuraciones especiales

Estos ejemplos cubren la mayoría de casos de uso comunes con ggGit. Para escenarios específicos o preguntas, consulta la documentación adicional o crea un issue en el repositorio.
