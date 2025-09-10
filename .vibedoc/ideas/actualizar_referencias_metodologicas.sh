#!/bin/bash
# actualizar_referencias_metodologicas.sh - Actualizar referencias 13.x → 1h.x

echo "🔄 Actualizando referencias metodológicas 13.x → 1h.x..."

# Actualizar títulos principales en los archivos
sed -i 's/# 13a - Reflexión/# 1h1 - Reflexión/g' "1h1 - reflexion story-2.1.1-preparacion-zettels-entrada.md"
sed -i 's/# 13b - Reflexión/# 1h2 - Reflexión/g' "1h2 - reflexion story-2.1.2-revision-validacion-script.md"
sed -i 's/# 13c - Reflexión/# 1h3 - Reflexión/g' "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"
sed -i 's/# 13d - Reflexión/# 1h4 - Reflexión/g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"

# Actualizar enlaces entre reflexiones
sed -i 's|\[13a - reflexion story-2.1.1\](13a - reflexion story-2.1.1-preparacion-zettels-entrada.md)|\[1h1 - reflexion story-2.1.1\](1h1 - reflexion story-2.1.1-preparacion-zettels-entrada.md)|g' "1h2 - reflexion story-2.1.2-revision-validacion-script.md"

sed -i 's|\[13b - reflexion story-2.1.2\](13b - reflexion story-2.1.2-revision-validacion-script.md)|\[1h2 - reflexion story-2.1.2\](1h2 - reflexion story-2.1.2-revision-validacion-script.md)|g' "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"

sed -i 's|\[13c - reflexion story-2.1.3\](13c%20-%20reflexion%20story-2.1.3-ejecucion-migracion.md)|\[1h3 - reflexion story-2.1.3\](1h3 - reflexion story-2.1.3-ejecucion-migracion.md)|g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"

# Actualizar referencias textuales a numeración
sed -i 's/- \*\*13a\*\*/- **1h1**/g' "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"
sed -i 's/- \*\*13b\*\*/- **1h2**/g' "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"
sed -i 's/- \*\*13c\*\*/- **1h3**/g' "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"

sed -i 's/- \*\*13a\*\*/- **1h1**/g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"
sed -i 's/- \*\*13b\*\*/- **1h2**/g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"
sed -i 's/- \*\*13c\*\*/- **1h3**/g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"
sed -i 's/- \*\*13d\*\*/- **1h4**/g' "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"

# Actualizar referencias en otros archivos
sed -i 's/reflexión 13a/reflexión 1h1/g' "1h2 - reflexion story-2.1.2-revision-validacion-script.md"

# Actualizar referencia en reporte de validación
sed -i 's/1 zettel de reflexión (13a)/1 zettel de reflexión (1h1)/g' "reporte_validacion_script.md"

echo "✅ Referencias metodológicas actualizadas"
echo "🔍 Verificando actualizaciones..."
echo ""
echo "📋 Referencias encontradas después de actualización:"
grep -r "1h[1-4]" . --include="*.md" | wc -l
echo ""
echo "⚠️  Referencias antiguas restantes (deberían ser 0):"
grep -r "13[a-d]" . --include="*.md" | grep -v migrate | wc -l
