# Contributing to ggGit

¡Gracias por tu interés en contribuir a ggGit! Este documento te guiará a través del proceso de contribución.

## 🚀 Getting Started

### Prerequisites
- Git instalado en tu sistema
- Conocimientos básicos de Bash scripting
- Familiaridad con Conventional Commits

### Development Setup
1. **Fork y clona el repositorio**
```bash
git clone https://github.com/YOUR_USERNAME/ggGit.git
cd ggGit
```

2. **Instala ggGit en modo desarrollo**
```bash
export PATH=$PATH:$(pwd)/commands
```

3. **Verifica la instalación**
```bash
ggv --help
```

## 🛠️ Development Guidelines

### Script Structure
Todos los scripts siguen esta estructura estándar:

```bash
#!/bin/bash

source $(dirname $0)/_utils.sh

print_usage() {
    print_text "NAME"
    print_text "    command_name - Brief description"
    # ... más documentación
}

main() {
    # Lógica principal del comando
}

# Manejo de argumentos
if [ "$#" -eq 0 ]; then
    main
    exit 0
fi

while [ "$1" != "" ]; do
    case $1 in
        -h | --help )   print_usage
                        exit 0
                        ;;
        * )             main "$@"
                        exit 0
                        ;;
    esac
    shift
done
```

### Naming Conventions
- **Comandos**: Prefijo `gg` + nombre descriptivo (ej: `ggfeat`, `ggfix`)
- **Funciones**: `snake_case` (ej: `print_usage`, `main`)
- **Variables**: `UPPER_CASE` para constantes, `lowercase` para variables locales

### Error Handling
- Usa `exit 0` para éxito, `exit 1` para errores
- Implementa manejo de argumentos inválidos
- Proporciona mensajes de error útiles

### Testing
Antes de enviar un PR, asegúrate de:

1. **Verificar sintaxis**
```bash
bash -n commands/your_script
```

2. **Probar funcionalidad**
```bash
./commands/your_script --help
./commands/your_script [argumentos de prueba]
```

3. **Ejecutar health check**
```bash
./health-check.sh
```

## 📝 Adding New Commands

### 1. Crear el script
```bash
touch commands/ggnewcommand
chmod +x commands/ggnewcommand
```

### 2. Implementar funcionalidad
- Sigue la estructura estándar
- Incluye documentación completa
- Maneja errores apropiadamente

### 3. Actualizar documentación
- README.md con descripción del comando
- Ejemplos de uso
- Opciones disponibles

### 4. Probar exhaustivamente
- Diferentes argumentos
- Casos edge
- Mensajes de error

## 🔧 Conventional Commits

Si estás agregando un nuevo comando de commit, asegúrate de:

- Seguir la especificación de Conventional Commits
- Implementar opciones `-s` (scope) y `-a` (amend)
- Validar que el mensaje no esté vacío
- Auto-staging si el área de staging está vacía

## 📋 Pull Request Process

### 1. Crear una rama
```bash
git checkout -b feature/nueva-funcionalidad
```

### 2. Hacer cambios
- Implementa tu funcionalidad
- Actualiza documentación
- Agrega tests si es necesario

### 3. Commit con Conventional Commits
```bash
ggfeat -s commands Add new command for X functionality
```

### 4. Push y crear PR
```bash
git push origin feature/nueva-funcionalidad
```

### 5. Checklist del PR
- [ ] Código sigue las convenciones del proyecto
- [ ] Documentación actualizada
- [ ] Tests pasan
- [ ] Health check exitoso
- [ ] Descripción clara del cambio

## 🐛 Reporting Issues

### Bug Reports
Incluye:
- Descripción del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Información del sistema
- Output del comando `ggconfig`

### Feature Requests
Describe:
- Caso de uso
- Beneficios esperados
- Alternativas consideradas

## 📚 Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
- [Git Documentation](https://git-scm.com/doc)

## 🤝 Code of Conduct

Este proyecto sigue el [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). Por favor, léelo y síguelo en todas tus interacciones.

## 📞 Getting Help

- **Issues**: Para bugs y feature requests
- **Discussions**: Para preguntas y discusiones
- **Email**: [mauroa.alderete@novafuria.com](mailto:mauro.alderete@novafuria.com)

¡Gracias por contribuir a hacer ggGit mejor! 🎉
