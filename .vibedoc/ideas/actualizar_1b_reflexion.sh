#!/bin/bash
# Script específico para actualizar referencias en 1b - reflexion-final-iniciativa-adopcion-vibedoc.md

echo "🔄 Actualizando referencias en 1b - reflexion-final-iniciativa-adopcion-vibedoc.md..."

FILE="./1b - reflexion-final-iniciativa-adopcion-vibedoc.md"

# Reflexiones
sed -i 's|\[1\.2\.3\.2 - reflexion comandos base\]|\[3a4 - reflexion implementacion commitcommand\]|g' "$FILE"
sed -i 's|\[1\.2\.4\.2 - reflexion comandos especificos\]|\[4a4 - reflexion implementacion validacion-esquemas\]|g' "$FILE"
sed -i 's|\[1\.2\.5\.2 - reflexion comandos especificos\]|\[3b9 - reflexion comandos-conventional-commits-especializados\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.1\.2 - reflexion configuracion ia basica\]|\[9b2 - reflexion-configuracion-ia-basica\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.2\.2 - reflexion analisis complejidad\]|\[9b4 - reflexion-analisis-complejidad\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.3\.2 - reflexion comando ggai basico\]|\[9b6 - reflexion-comando-ggai-basico\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.4\.2 - reflexion integracion comandos existentes\]|\[9b8 - reflexion-integracion-comandos-existentes\]|g' "$FILE"

# Decisiones
sed -i 's|\[1\.2\.3\.1 - decisiones comandos base\]|\[3a1 - patrones manejo errores gitinterface\]|g' "$FILE"
sed -i 's|\[1\.2\.4\.1 - decisiones comandos especificos\]|\[4a2 - reflexion implementacion configmanager-basico\]|g' "$FILE"
sed -i 's|\[1\.2\.5\.1 - decisiones comandos especificos\]|\[3b4 - decisiones story-1.2.5.1\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.1\.1 - decisiones configuracion ia basica\]|\[9b1 - decisiones-configuracion-ia-basica\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.2\.1 - decisiones analisis complejidad\]|\[9b3 - decisiones-analisis-complejidad\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.3\.1 - decisiones comando ggai basico\]|\[9b5 - decisiones-comando-ggai-basico\]|g' "$FILE"
sed -i 's|\[1\.2\.7\.4\.1 - decisiones integracion comandos existentes\]|\[9b7 - decisiones-integracion-comandos-existentes\]|g' "$FILE"

echo "✅ Referencias actualizadas en $FILE"
