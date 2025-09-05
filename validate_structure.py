#!/usr/bin/env python3
"""
Script de validación para verificar la estructura de directorios Python de ggGit.

Este script valida que la estructura de directorios implementada
coincida con las decisiones tomadas en el zettel 1.2.1.1.
"""

import os
import sys
from pathlib import Path


def validate_directory_structure():
    """Valida la estructura de directorios Python."""
    print("🔍 Validando estructura de directorios Python de ggGit...")
    
    # Estructura esperada según las decisiones
    expected_structure = {
        "src/": "Directorio principal del código fuente",
        "src/__init__.py": "Archivo __init__.py del paquete principal",
        "src/core/": "Directorio de lógica central y abstracciones",
        "src/core/__init__.py": "Archivo __init__.py del módulo core",
        "src/core/cli.py": "Abstracción CLI base",
        "src/core/config.py": "ConfigManager",
        "src/core/git.py": "GitWrapper",
        "src/core/validation.py": "Validadores",
        "src/core/base_commands/": "Comandos base reutilizables",
        "src/core/base_commands/__init__.py": "Archivo __init__.py de base_commands",
        "src/core/base_commands/base.py": "BaseCommand",
        "src/core/base_commands/commit.py": "CommitCommand",
        "src/core/base_commands/config.py": "ConfigCommand",
        "src/core/utils/": "Utilidades",
        "src/core/utils/__init__.py": "Archivo __init__.py de utils",
        "src/core/utils/colors.py": "Sistema de colores",
        "src/core/utils/logging.py": "Sistema de logging",
        "src/commands/": "Comandos específicos ejecutables",
        "src/commands/ggfeat.py": "Comando ggfeat",
        "src/commands/ggfix.py": "Comando ggfix",
        "src/commands/ggbreak.py": "Comando ggbreak",
        "config/": "Directorio de configuración",
        "config/config-schema.yaml": "Esquema de configuración",
        "config/commit-schema.yaml": "Esquema de commits",
        "tests/": "Directorio de tests",
        "tests/__init__.py": "Archivo __init__.py de tests",
        "tests/test_core.py": "Tests del módulo core",
        "tests/test_commands.py": "Tests de comandos"
    }
    
    errors = []
    warnings = []
    
    for path, description in expected_structure.items():
        full_path = Path(path)
        
        if not full_path.exists():
            errors.append(f"❌ FALTA: {path} - {description}")
        else:
            if full_path.is_file():
                print(f"✅ ARCHIVO: {path}")
            else:
                print(f"✅ DIRECTORIO: {path}")
    
    # Verificar que los comandos Python son ejecutables
    python_commands = [
        "src/commands/ggfeat.py",
        "src/commands/ggfix.py", 
        "src/commands/ggbreak.py"
    ]
    
    for cmd in python_commands:
        if Path(cmd).exists():
            if os.access(cmd, os.X_OK):
                print(f"✅ EJECUTABLE: {cmd}")
            else:
                warnings.append(f"⚠️  NO EJECUTABLE: {cmd}")
    
    # Verificar importaciones básicas
    print("\n🔍 Verificando importaciones básicas...")
    try:
        import src.core.config
        print("✅ Importación: src.core.config")
    except ImportError as e:
        errors.append(f"❌ ERROR IMPORTACIÓN: src.core.config - {e}")
    
    try:
        import src.core.git
        print("✅ Importación: src.core.git")
    except ImportError as e:
        errors.append(f"❌ ERROR IMPORTACIÓN: src.core.git - {e}")
    
    try:
        import src.core.validation
        print("✅ Importación: src.core.validation")
    except ImportError as e:
        errors.append(f"❌ ERROR IMPORTACIÓN: src.core.validation - {e}")
    
    # Mostrar resultados
    print(f"\n📊 RESUMEN DE VALIDACIÓN:")
    print(f"✅ Elementos encontrados: {len(expected_structure) - len(errors)}")
    print(f"❌ Elementos faltantes: {len(errors)}")
    print(f"⚠️  Advertencias: {len(warnings)}")
    
    if errors:
        print(f"\n❌ ERRORES ENCONTRADOS:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print(f"\n⚠️  ADVERTENCIAS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors:
        print(f"\n🎉 ¡VALIDACIÓN EXITOSA! La estructura de directorios es correcta.")
        return True
    else:
        print(f"\n💥 VALIDACIÓN FALLIDA. Corrige los errores antes de continuar.")
        return False


if __name__ == "__main__":
    success = validate_directory_structure()
    sys.exit(0 if success else 1)
