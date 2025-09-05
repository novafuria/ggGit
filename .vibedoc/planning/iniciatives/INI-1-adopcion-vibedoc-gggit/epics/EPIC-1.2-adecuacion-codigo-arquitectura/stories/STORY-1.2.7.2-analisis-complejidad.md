# [HISTORIA] - Análisis de Complejidad

## 🎯 Objetivo

Implementar análisis de complejidad para decidir automáticamente entre generación de mensaje con IA y fallback educativo, basándose en el número de archivos modificados, líneas de diff y tamaño de archivos.

## 🌎 Contexto

Esta historia implementa la lógica de decisión inteligente definida en los zettels 1.2.6.6, 1.2.6.7 y 1.2.6.8. Sin el análisis de complejidad, no es posible decidir cuándo usar IA y cuándo mostrar un fallback educativo.

La historia se basa en la decisión de usar criterios simples (archivos, líneas, tamaño) sin métricas de complejidad que no sean útiles para el usuario, como se definió en el zettel 1.2.6.8.

## 💡 Propuesta de Resolución

Se propone crear una clase `ComplexityAnalyzer` que analice los cambios en el área de staging o working directory, aplicando criterios configurables para decidir si usar IA o fallback educativo. El análisis se integrará con GitInterface existente para obtener información de diff y archivos modificados.

La implementación incluirá fallback educativo con sugerencias específicas para enseñar buenas prácticas de Git, como se definió en el zettel 1.2.6.8.

## 📦 Artefactos

- 📦 **Clase ComplexityAnalyzer**: Implementación del análisis de complejidad en `src/core/ai/complexity_analyzer.py`
- 📦 **Integración con GitInterface**: Métodos para análisis de diff y archivos modificados
- 📦 **Fallback educativo**: Mensajes educativos con sugerencias específicas
- 📦 **Tests unitarios**: Tests para análisis de complejidad y criterios de decisión

## 🔍 Criterios de Aceptación

### **Análisis de Cambios**
- **Dado** que hay archivos en staging
- **Cuando** se analiza complejidad
- **Entonces** se analizan solo archivos staged

- **Dado** que no hay archivos en staging
- **Cuando** se analiza complejidad
- **Entonces** se analizan archivos listos para stage

### **Criterios de Decisión**
- **Dado** que los cambios tienen ≤ 10 archivos, ≤ 200 líneas de diff, ≤ 5000 bytes por archivo
- **Cuando** se analiza complejidad
- **Entonces** se decide usar IA

- **Dado** que los cambios exceden los límites de complejidad
- **Cuando** se analiza complejidad
- **Entonces** se decide usar fallback educativo

### **Fallback Inteligente**
- **Dado** que los cambios son complejos
- **Cuando** se muestra fallback
- **Entonces** se muestran sugerencias educativas específicas:
  - "No es aconsejable commitear tanto contenido"
  - "Selecciona grupos de archivos más pequeños"
  - "Usa 'git add <archivo>' para archivos específicos"
  - "O 'ggfeat \"mensaje manual\"' para commit completo"

## 🔗 Dependencias y Recursos

### Dependencias
- Configuración IA básica (STORY-1.2.7.1) debe estar implementada
- GitInterface existente debe estar funcional
- ColorManager para feedback visual debe estar disponible

### Recursos
- Acceso a GitInterface existente en `src/core/git.py`
- Acceso a ColorManager en `src/core/utils/colors.py`
- Acceso a configuraciones IA para criterios de decisión
