# Análisis: Dependencias y Ambientes para ggGit

## Resumen Ejecutivo

Análisis completo de opciones de gestión de dependencias y ambientes virtuales para ggGit, considerando el contexto de Novafuria y las mejores prácticas actuales.

## Estado Actual del Proyecto

### Dependencias Identificadas
- **Python 3.8+** (requerido según arquitectura)
- **Click** - Framework CLI
- **PyYAML** - Manejo de configuración (TODO pendiente)
- **pathlib, typing, subprocess** - Librerías estándar

### Problemas Actuales
- ❌ No hay gestión formal de dependencias
- ❌ Dependencias hardcodeadas en imports
- ❌ No hay archivos de configuración de dependencias
- ⚠️ Instalación manual de dependencias requerida

## Evaluación de Opciones

### 1. venv + pip
**Ventajas:**
- Incluido en Python estándar
- Ligero y rápido
- Ampliamente adoptado

**Desventajas:**
- Solo maneja paquetes Python
- Resolución de dependencias limitada
- No ideal para entornos científicos

### 2. uv
**Ventajas:**
- Extremadamente rápido (Rust)
- Mejor resolución que pip
- Compatible con requirements.txt

**Desventajas:**
- Relativamente nuevo (2024)
- Menor adopción en comunidad científica
- Curva de aprendizaje

### 3. conda/mamba ⭐ RECOMENDADO
**Ventajas:**
- **Popular en Novafuria** (factor clave)
- Resolución automática de dependencias complejas
- Maneja dependencias no-Python
- **mamba es 10-100x más rápido que conda**
- Compatible con environment.yml
- Muy estable y maduro

**Desventajas:**
- Entornos más pesados
- Curva de aprendizaje inicial

## Recomendación Estratégica

### Opción Seleccionada: conda/mamba

**Justificación:**
1. **Alineación organizacional**: Ya es la herramienta preferida en Novafuria
2. **Compatibilidad total**: mamba usa los mismos archivos environment.yml que conda
3. **Rendimiento superior**: mamba es significativamente más rápido
4. **Futuro del proyecto**: ggGit podría necesitar dependencias científicas
5. **Ecosistema maduro**: Amplio soporte y documentación

### Estrategia de Implementación

#### Fase 1: Configuración Básica
1. Crear `environment.yml` con Python 3.12
2. Definir dependencias mínimas (click, pyyaml)
3. Documentar proceso de instalación

#### Fase 2: Integración con Scripts
1. Actualizar scripts de instalación para detectar conda/mamba
2. Crear script de setup automático del ambiente
3. Documentar flujo de trabajo para desarrolladores

#### Fase 3: Optimización
1. Evaluar dependencias adicionales necesarias
2. Optimizar tamaño del ambiente
3. Crear scripts de desarrollo automatizados

## Archivos Propuestos

### environment.yml
```yaml
name: gggit
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - click>=8.0.0
  - pyyaml>=6.0
  - pip
  - pip:
    - colorama  # Para colores multiplataforma
```

### Comandos de Desarrollo
```bash
# Crear ambiente de desarrollo
conda env create -f environment.yml
# o con mamba (si está disponible):
# mamba env create -f environment.yml

# Activar ambiente
conda activate gggit
# o con mamba:
# mamba activate gggit

# Desactivar ambiente
conda deactivate

# Eliminar ambiente
conda env remove -n gggit
# o con mamba:
# mamba env remove -n gggit
```

## Próximos Pasos

1. **Aprobar estrategia** con el equipo
2. **Crear environment.yml** con dependencias básicas
3. **Actualizar documentación** de instalación
4. **Probar en diferentes entornos** (Windows, Linux, macOS)
5. **Integrar con CI/CD** si es necesario

## Consideraciones Adicionales

### Compatibilidad con Herramientas Existentes
- Los archivos environment.yml son compatibles con conda y mamba
- No requiere cambios en el código existente
- Mantiene compatibilidad con scripts de instalación actuales

### Impacto en el Flujo de Trabajo
- Desarrolladores necesitarán activar el ambiente antes de trabajar
- Scripts de instalación detectarán automáticamente conda/mamba
- Documentación clara para nuevos contribuidores

### Beneficios a Largo Plazo
- Facilita la adición de dependencias científicas futuras
- Mejora la reproducibilidad del ambiente de desarrollo
- Alinea ggGit con las prácticas de Novafuria
- Reduce problemas de "funciona en mi máquina"
