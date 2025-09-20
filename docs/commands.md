# Referencia de Comandos

Esta guía cubre todos los 26 comandos disponibles en ggGit, organizados por categorías para facilitar su uso.

## Comandos de Conventional Commits

Los comandos de conventional commits siguen el estándar [Conventional Commits](https://www.conventionalcommits.org/) para generar mensajes de commit consistentes y semánticamente claros.

### ggfeat - Commits de Funcionalidad

Crea commits para nuevas funcionalidades o características.

```bash
# Uso básico (IA genera el mensaje)
ggfeat

# Con mensaje personalizado
ggfeat "Agregar autenticación de usuarios"

# Con scope específico
ggfeat "auth: implementar login con OAuth2"
```

**Ejemplo de mensaje generado:** `feat: agregar sistema de autenticación con JWT`

### ggfix - Commits de Corrección

Crea commits para corrección de bugs o errores.

```bash
# Uso básico
ggfix

# Con descripción específica
ggfix "Corregir validación de email en formulario de registro"

# Con referencia a issue
ggfix "Corregir error 404 en página de perfil (#123)"
```

**Ejemplo de mensaje generado:** `fix: corregir validación de email en formulario de registro`

### ggdocs - Commits de Documentación

Crea commits para cambios en documentación.

```bash
# Uso básico
ggdocs

# Con descripción específica
ggdocs "Actualizar guía de instalación para Windows"

# Con scope
ggdocs "api: agregar documentación de endpoints REST"
```

**Ejemplo de mensaje generado:** `docs: actualizar guía de instalación para Windows`

### ggstyle - Commits de Estilo

Crea commits para cambios de formato, estilos de código o linting.

```bash
# Uso básico
ggstyle

# Con descripción específica
ggstyle "Aplicar prettier a archivos JavaScript"

# Con scope
ggstyle "css: corregir indentación en archivos de estilos"
```

**Ejemplo de mensaje generado:** `style: aplicar prettier a archivos JavaScript`

### ggrefactor - Commits de Refactorización

Crea commits para refactorización de código sin cambiar funcionalidad.

```bash
# Uso básico
ggrefactor

# Con descripción específica
ggrefactor "Extraer lógica de validación a función separada"

# Con scope
ggrefactor "utils: simplificar función de formateo de fechas"
```

**Ejemplo de mensaje generado:** `refactor: extraer lógica de validación a función separada`

### ggtest - Commits de Pruebas

Crea commits para agregar o modificar pruebas.

```bash
# Uso básico
ggtest

# Con descripción específica
ggtest "Agregar pruebas unitarias para módulo de autenticación"

# Con scope
ggtest "auth: agregar pruebas de integración para login"
```

**Ejemplo de mensaje generado:** `test: agregar pruebas unitarias para módulo de autenticación`

### ggchore - Commits de Mantenimiento

Crea commits para tareas de mantenimiento, configuración o dependencias.

```bash
# Uso básico
ggchore

# Con descripción específica
ggchore "Actualizar dependencias de desarrollo"

# Con scope
ggchore "deps: actualizar React a versión 18"
```

**Ejemplo de mensaje generado:** `chore: actualizar dependencias de desarrollo`

### ggperf - Commits de Rendimiento

Crea commits para mejoras de rendimiento.

```bash
# Uso básico
ggperf

# Con descripción específica
ggperf "Optimizar consultas de base de datos"

# Con scope
ggperf "db: agregar índices para consultas frecuentes"
```

**Ejemplo de mensaje generado:** `perf: optimizar consultas de base de datos`

### ggci - Commits de CI/CD

Crea commits para cambios en integración continua o despliegue.

```bash
# Uso básico
ggci

# Con descripción específica
ggci "Configurar pipeline de despliegue automático"

# Con scope
ggci "github: agregar workflow para pruebas en múltiples versiones de Node"
```

**Ejemplo de mensaje generado:** `ci: configurar pipeline de despliegue automático`

### ggbuild - Commits de Sistema de Construcción

Crea commits para cambios en el sistema de build o compilación.

```bash
# Uso básico
ggbuild

# Con descripción específica
ggbuild "Configurar webpack para producción"

# Con scope
ggbuild "webpack: optimizar configuración para bundle más pequeño"
```

**Ejemplo de mensaje generado:** `build: configurar webpack para producción`

### ggbreak - Commits de Cambios Importantes

Crea commits para cambios que rompen la compatibilidad hacia atrás.

```bash
# Uso básico
ggbreak

# Con descripción específica
ggbreak "Cambiar API de autenticación"

# Con scope
ggbreak "api: remover soporte para autenticación básica"
```

**Ejemplo de mensaje generado:** `feat!: cambiar API de autenticación`

## Comandos de Operaciones Git

Estos comandos proporcionan acceso rápido a las operaciones más comunes de Git.

### gga - Git Add

Agrega archivos al área de staging.

```bash
# Agregar todos los archivos modificados
gga

# Agregar archivo específico
gga archivo.txt

# Agregar múltiples archivos
gga archivo1.txt archivo2.py
```

### ggs - Git Status

Muestra el estado actual del repositorio.

```bash
# Estado básico
ggs

# Estado con más detalles
ggs --porcelain
```

### ggl - Git Log

Muestra el historial de commits.

```bash
# Log básico
ggl

# Log con gráfico
ggl --graph

# Log de últimos 10 commits
ggl -10
```

### ggdif - Git Diff

Muestra las diferencias entre commits o archivos.

```bash
# Diff de archivos modificados
ggdif

# Diff de archivo específico
ggdif archivo.txt

# Diff entre commits
ggdif HEAD~1 HEAD
```

### ggunstage - Git Unstage

Quita archivos del área de staging.

```bash
# Quitar todos los archivos del staging
ggunstage

# Quitar archivo específico
ggunstage archivo.txt
```

### ggreset - Git Reset

Resetea el repositorio a un estado anterior.

```bash
# Reset suave (mantiene cambios en working directory)
ggreset

# Reset a commit específico
ggreset HEAD~2

# Reset duro (pierde todos los cambios)
ggreset --hard HEAD~1
```

## Comandos de Gestión de Ramas

Estos comandos facilitan la gestión de ramas en Git.

### ggmain - Cambiar a Rama Principal

Cambia a la rama principal (main o master).

```bash
# Cambiar a main
ggmain

# Cambiar a main y actualizar
ggmain --pull
```

### ggdevelop - Cambiar a Rama de Desarrollo

Cambia a la rama de desarrollo.

```bash
# Cambiar a develop
ggdevelop

# Cambiar a develop y actualizar
ggdevelop --pull
```

### ggb - Gestión de Ramas

Crea, cambia o lista ramas.

```bash
# Listar ramas
ggb

# Crear nueva rama
ggb nueva-rama

# Cambiar a rama existente
ggb rama-existente

# Crear y cambiar a nueva rama
ggb -b nueva-rama
```

### ggmerge - Fusionar Ramas

Fusiona ramas de forma segura.

```bash
# Fusionar rama actual a main
ggmerge

# Fusionar rama específica
ggmerge feature/nueva-funcionalidad

# Fusionar con mensaje personalizado
ggmerge --message "Fusionar feature de autenticación"
```

## Comandos de Operaciones Remotas

Estos comandos manejan la sincronización con repositorios remotos.

### ggpl - Git Pull

Descarga cambios del repositorio remoto.

```bash
# Pull básico
ggpl

# Pull de rama específica
ggpl origin main

# Pull con rebase
ggpl --rebase
```

### ggpp - Git Push

Sube cambios al repositorio remoto.

```bash
# Push básico
ggpp

# Push a rama específica
ggpp origin main

# Push forzado (usar con cuidado)
ggpp --force
```

## Comandos de IA y Configuración

Estos comandos manejan las características de IA y la configuración del sistema.

### ggai - Comandos de IA

Gestiona las características de IA de ggGit.

```bash
# Probar conexión de IA
ggai test

# Generar mensaje de commit
ggai generate

# Ver estado de IA
ggai status

# Configurar proveedor de IA
ggai setup
```

### ggconfig - Gestión de Configuración

Gestiona la configuración de ggGit.

```bash
# Ver configuración actual
ggconfig

# Establecer valor de configuración
ggconfig set ai.enabled true

# Obtener valor de configuración
ggconfig get ai.enabled

# Listar todas las configuraciones
ggconfig list

# Restablecer configuración
ggconfig reset
```

### ggv - Información de Versión

Muestra información de versión y sistema.

```bash
# Información básica
ggv

# Información detallada
ggv --verbose

# Información de sistema
ggv --system
```

## Opciones Comunes

Muchos comandos comparten opciones comunes:

### Opciones de Ayuda

```bash
# Mostrar ayuda para cualquier comando
ggfeat --help
ggfix --help
ggs --help
```

### Opciones de Verbosidad

```bash
# Modo silencioso
ggfeat --quiet

# Modo verbose
ggfeat --verbose
```

### Opciones de Configuración

```bash
# Usar configuración específica
ggfeat --config /ruta/a/config.yaml

# Ignorar configuración global
ggfeat --no-config
```

## Integración con IA

Todos los comandos de conventional commits pueden usar IA para generar mensajes automáticamente. Para habilitar esta funcionalidad:

```bash
# Habilitar IA
ggconfig set ai.enabled true

# Configurar proveedor (Ollama recomendado)
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama
```

Una vez configurada, simplemente ejecuta cualquier comando de commit sin argumentos y la IA generará un mensaje apropiado basado en los cambios detectados.

## Ejemplos de Flujo de Trabajo

### Flujo Básico de Desarrollo

```bash
# 1. Crear nueva rama
ggb feature/nueva-funcionalidad

# 2. Hacer cambios y agregar archivos
gga

# 3. Hacer commit con IA
ggfeat

# 4. Subir cambios
ggpp

# 5. Crear pull request (fuera de ggGit)
```

### Flujo de Corrección de Bugs

```bash
# 1. Cambiar a main y actualizar
ggmain
ggpl

# 2. Crear rama de hotfix
ggb hotfix/corregir-bug-critico

# 3. Hacer cambios y commit
gga
ggfix

# 4. Fusionar a main
ggmerge

# 5. Subir cambios
ggpp
```

Esta referencia cubre todos los comandos disponibles en ggGit. Para más ejemplos y casos de uso específicos, consulta la [Guía de Ejemplos](examples.md).
