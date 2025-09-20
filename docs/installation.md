# Guía de Instalación

Esta guía te ayudará a instalar ggGit en tu sistema, independientemente de la plataforma que uses.

## Requisitos del Sistema

ggGit está diseñado para funcionar en cualquier sistema que tenga Python 3.7 o superior. No requiere dependencias externas complejas, lo que hace que la instalación sea rápida y sencilla.

## Instalación Rápida

### Linux y macOS

La forma más sencilla de instalar ggGit es clonando el repositorio y ejecutando el script de instalación:

```bash
# Clonar el repositorio
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Ejecutar instalación
python install.py
```

El script de instalación se encarga de:
- Verificar que Python esté instalado correctamente
- Crear los enlaces simbólicos necesarios en tu PATH
- Configurar los permisos de ejecución
- Validar que la instalación funcione correctamente

### Windows

Para usuarios de Windows, utilizamos PowerShell:

```powershell
# Clonar el repositorio
git clone https://github.com/novafuria/ggGit.git
cd ggGit

# Ejecutar instalación
.\install.ps1
```

El script de PowerShell realiza las mismas tareas que la versión de Linux/macOS, adaptado para el entorno de Windows.

## Verificación de la Instalación

Una vez completada la instalación, puedes verificar que todo funciona correctamente:

```bash
# Verificar que los comandos están disponibles
ggv

# Probar un comando básico
ggs
```

Si ves la información de versión y el estado de git, la instalación fue exitosa.

## Instalación Manual (Avanzada)

Si prefieres una instalación más controlada o necesitas personalizar la ubicación de los comandos:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/novafuria/ggGit.git
cd ggGit
```

### 2. Crear Enlaces Simbólicos

```bash
# Crear directorio para comandos (si no existe)
mkdir -p ~/.local/bin

# Crear enlaces simbólicos para cada comando
ln -s $(pwd)/src/commands/ggfeat.py ~/.local/bin/ggfeat
ln -s $(pwd)/src/commands/ggfix.py ~/.local/bin/ggfix
# ... repetir para todos los comandos
```

### 3. Agregar al PATH

Asegúrate de que `~/.local/bin` esté en tu PATH. Agrega esta línea a tu archivo de configuración del shell:

```bash
# Para bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Para zsh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

## Solución de Problemas

### Comando no encontrado

Si recibes un error de "comando no encontrado", verifica que:

1. El directorio de instalación esté en tu PATH
2. Los archivos tengan permisos de ejecución
3. Python esté instalado correctamente

```bash
# Verificar PATH
echo $PATH

# Verificar permisos
ls -la ~/.local/bin/gg*

# Verificar Python
python --version
```

### Permisos insuficientes

Si tienes problemas de permisos, puedes ejecutar con sudo o cambiar los permisos:

```bash
# Con sudo (no recomendado para desarrollo)
sudo python install.py

# Cambiar permisos del directorio
chmod +x ~/.local/bin/gg*
```

### Python no encontrado

Si Python no está instalado o no está en tu PATH:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# macOS con Homebrew
brew install python3

# Windows
# Descargar desde python.org o usar Microsoft Store
```

## Desinstalación

Para desinstalar ggGit:

```bash
# Eliminar enlaces simbólicos
rm ~/.local/bin/gg*

# Eliminar directorio del proyecto
rm -rf /ruta/a/ggGit
```

## Actualización

Para actualizar ggGit a la última versión:

```bash
# Navegar al directorio del proyecto
cd /ruta/a/ggGit

# Actualizar desde el repositorio
git pull origin main

# Reinstalar (opcional, para asegurar enlaces actualizados)
python install.py
```

## Configuración Post-Instalación

Una vez instalado, te recomendamos configurar las características de IA para obtener la mejor experiencia:

```bash
# Habilitar IA
ggconfig set ai.enabled true

# Configurar para Ollama (recomendado)
ggconfig set ai.api_key_env GGGIT_AI_KEY
export GGGIT_AI_KEY=ollama
```

Para más detalles sobre la configuración de IA, consulta la [Guía de Configuración de IA](ai-setup.md).

## Soporte

Si encuentras problemas durante la instalación:

1. Revisa la sección de solución de problemas arriba
2. Consulta el [Troubleshooting](troubleshooting.md) para problemas comunes
3. Abre un issue en [GitHub](https://github.com/novafuria/ggGit/issues) si el problema persiste

La instalación de ggGit está diseñada para ser simple y sin complicaciones. En la mayoría de los casos, el script de instalación automática debería funcionar perfectamente.
