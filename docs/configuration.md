# Guía de Configuración

ggGit utiliza un sistema de configuración jerárquico que permite personalizar el comportamiento según tus necesidades, desde configuraciones globales hasta configuraciones específicas de proyecto.

## Sistema de Configuración Jerárquico

La configuración de ggGit sigue un orden de precedencia que permite diferentes niveles de personalización:

1. **Configuración de proyecto** (`.gggit/config.yaml`) - Tiene la mayor prioridad
2. **Configuración de usuario** (`~/.gggit/config.yaml`) - Configuración personal
3. **Configuración global** (valores por defecto) - Configuración base del sistema

Esta jerarquía permite que cada proyecto tenga su propia configuración mientras mantiene configuraciones personales como respaldo.

## Comando ggconfig

El comando `ggconfig` es tu herramienta principal para gestionar la configuración:

### Ver Configuración Actual

```bash
# Ver toda la configuración
ggconfig

# Ver configuración específica
ggconfig get ai.enabled

# Ver configuración con formato JSON
ggconfig --format json
```

### Establecer Configuraciones

```bash
# Establecer valor simple
ggconfig set ai.enabled true

# Establecer valor anidado
ggconfig set ai.provider ollama

# Establecer en nivel específico
ggconfig set --level project ai.enabled false
```

### Gestionar Configuraciones

```bash
# Listar todas las configuraciones
ggconfig list

# Eliminar configuración
ggconfig unset ai.enabled

# Restablecer a valores por defecto
ggconfig reset

# Restablecer configuración específica
ggconfig reset ai.enabled
```

## Configuración de IA

La integración con IA es una de las características más potentes de ggGit. Puedes configurar diferentes proveedores según tus necesidades.

### Configuración Básica de IA

```bash
# Habilitar IA
ggconfig set ai.enabled true

# Configurar proveedor (ollama, openai, anthropic, azure)
ggconfig set ai.provider ollama

# Configurar variable de entorno para API key
ggconfig set ai.api_key_env GGGIT_AI_KEY
```

### Configuración de Ollama (Recomendado)

Ollama es la opción recomendada para uso local, privado y sin costos:

```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelo recomendado
ollama pull gemma3:4b

# Configurar ggGit para Ollama
ggconfig set ai.provider ollama
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama

# Probar conexión
ggai test
```

### Configuración de OpenAI

Para usar OpenAI en la nube:

```bash
# Configurar proveedor
ggconfig set ai.provider openai

# Configurar API key
ggconfig set ai.api_key_env OPENAI_API_KEY
export OPENAI_API_KEY=tu_api_key_aqui

# Configurar modelo (opcional)
ggconfig set ai.model gpt-3.5-turbo
```

### Configuración de Anthropic

Para usar Claude de Anthropic:

```bash
# Configurar proveedor
ggconfig set ai.provider anthropic

# Configurar API key
ggconfig set ai.api_key_env ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=tu_api_key_aqui

# Configurar modelo (opcional)
ggconfig set ai.model claude-3-sonnet-20240229
```

### Configuración de Azure OpenAI

Para entornos empresariales con Azure:

```bash
# Configurar proveedor
ggconfig set ai.provider azure

# Configurar endpoint
ggconfig set ai.endpoint https://tu-recurso.openai.azure.com/

# Configurar API key
ggconfig set ai.api_key_env AZURE_OPENAI_API_KEY
export AZURE_OPENAI_API_KEY=tu_api_key_aqui

# Configurar versión de API
ggconfig set ai.api_version 2024-02-15-preview
```

## Configuración de Comandos

Puedes personalizar el comportamiento de los comandos individuales:

### Configuración de Conventional Commits

```bash
# Configurar prefijo por defecto para commits
ggconfig set commits.prefix "[PROJ-123]"

# Configurar longitud máxima de mensaje
ggconfig set commits.max_length 72

# Configurar formato de mensaje
ggconfig set commits.format "conventional"
```

### Configuración de Git

```bash
# Configurar editor por defecto
ggconfig set git.editor "code --wait"

# Configurar merge tool
ggconfig set git.merge_tool "vscode"

# Configurar configuración de usuario
ggconfig set git.user.name "Tu Nombre"
ggconfig set git.user.email "tu@email.com"
```

### Configuración de Ramas

```bash
# Configurar rama principal
ggconfig set branches.main "main"

# Configurar rama de desarrollo
ggconfig set branches.develop "develop"

# Configurar prefijo para ramas de feature
ggconfig set branches.feature_prefix "feature/"
```

## Configuración por Proyecto

Cada proyecto puede tener su propia configuración creando un archivo `.gggit/config.yaml` en la raíz del proyecto:

```yaml
# .gggit/config.yaml
ai:
  enabled: true
  provider: ollama
  api_key_env: GGGIT_AI_KEY

commits:
  prefix: "[PROJ-123]"
  max_length: 100

branches:
  main: "main"
  develop: "develop"
  feature_prefix: "feature/"

git:
  editor: "code --wait"
  merge_tool: "vscode"
```

## Configuración de Usuario

Tu configuración personal se almacena en `~/.gggit/config.yaml`:

```yaml
# ~/.gggit/config.yaml
ai:
  enabled: true
  provider: ollama
  api_key_env: GGGIT_AI_KEY

commits:
  max_length: 72

git:
  user:
    name: "Tu Nombre"
    email: "tu@email.com"
```

## Variables de Entorno

ggGit respeta las siguientes variables de entorno:

### Variables de IA

- `GGGIT_AI_KEY` - API key para proveedores de IA
- `OPENAI_API_KEY` - API key específica de OpenAI
- `ANTHROPIC_API_KEY` - API key específica de Anthropic
- `AZURE_OPENAI_API_KEY` - API key específica de Azure OpenAI

### Variables de Git

- `GIT_AUTHOR_NAME` - Nombre del autor para commits
- `GIT_AUTHOR_EMAIL` - Email del autor para commits
- `GIT_EDITOR` - Editor por defecto para Git

### Variables de ggGit

- `GGGIT_CONFIG_FILE` - Ruta personalizada al archivo de configuración
- `GGGIT_LOG_LEVEL` - Nivel de logging (DEBUG, INFO, WARNING, ERROR)

## Configuración Avanzada

### Configuración de Logging

```bash
# Configurar nivel de logging
ggconfig set logging.level INFO

# Configurar archivo de log
ggconfig set logging.file ~/.gggit/gggit.log

# Configurar formato de log
ggconfig set logging.format "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### Configuración de Cache

```bash
# Habilitar cache de IA
ggconfig set cache.enabled true

# Configurar tiempo de vida del cache
ggconfig set cache.ttl 3600

# Configurar directorio de cache
ggconfig set cache.directory ~/.gggit/cache
```

### Configuración de Red

```bash
# Configurar timeout de conexión
ggconfig set network.timeout 30

# Configurar proxy
ggconfig set network.proxy "http://proxy:8080"

# Configurar verificación SSL
ggconfig set network.verify_ssl true
```

## Validación de Configuración

ggGit valida automáticamente la configuración al cargar:

```bash
# Validar configuración actual
ggconfig validate

# Validar archivo específico
ggconfig validate --file ~/.gggit/config.yaml

# Mostrar errores de validación
ggconfig validate --verbose
```

## Migración de Configuración

Si tienes configuraciones de versiones anteriores:

```bash
# Migrar configuración existente
ggconfig migrate

# Migrar desde archivo específico
ggconfig migrate --from ~/.gggit/config.old

# Hacer backup antes de migrar
ggconfig migrate --backup
```

## Resolución de Problemas

### Configuración No Se Aplica

```bash
# Verificar orden de precedencia
ggconfig --show-precedence

# Verificar archivos de configuración
ggconfig --show-files

# Limpiar cache de configuración
ggconfig clear-cache
```

### Errores de Validación

```bash
# Ver errores detallados
ggconfig validate --verbose

# Restablecer configuración problemática
ggconfig reset ai.provider

# Verificar esquema de configuración
ggconfig schema
```

### Problemas de IA

```bash
# Probar conexión de IA
ggai test

# Ver configuración de IA
ggai config

# Reiniciar servicio de IA
ggai restart
```

## Mejores Prácticas

### Organización de Configuración

- Usa configuración global para preferencias personales
- Usa configuración de proyecto para reglas específicas del equipo
- Mantén archivos de configuración en control de versiones cuando sea apropiado
- Documenta configuraciones especiales en el README del proyecto

### Seguridad

- Nunca incluyas API keys en archivos de configuración versionados
- Usa variables de entorno para información sensible
- Considera usar herramientas de gestión de secretos para entornos de producción

### Mantenimiento

- Revisa regularmente la configuración para eliminar opciones obsoletas
- Mantén backups de configuraciones importantes
- Actualiza configuraciones cuando actualices ggGit

La configuración de ggGit está diseñada para ser flexible y poderosa, permitiéndote adaptar el comportamiento a tus necesidades específicas sin complicar el uso básico.
