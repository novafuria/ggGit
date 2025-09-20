#!/bin/bash
# Script para actualizar referencias sistemáticamente
# STORY-2.1.4: Actualización de Referencias

echo "🔄 Iniciando actualización sistemática de referencias..."

# Función para actualizar referencias
update_ref() {
    local old_ref="$1"
    local new_ref="$2"
    local description="$3"
    
    echo "📝 Actualizando: $description"
    find . -name "*.md" -type f ! -name "mapa_actualizacion_referencias.md" ! -name "actualizar_referencias.sh" \
        -exec sed -i "s|$old_ref|$new_ref|g" {} \;
}

# Referencias de archivos con rutas relativas específicas
update_ref "\[1\.2\.3\.2 - ajustes alcance commitcommand\.md\](\./1\.2\.3\.2%20-%20ajustes%20alcance%20commitcommand\.md)" "[3a3 - ajustes alcance commitcommand.md](./3a3%20-%20ajustes%20alcance%20commitcommand.md)" "1.2.3.2 ajustes alcance commitcommand"

update_ref "\[1\.2\.3\.3 - analisis alcance loggingmanager\.md\](\./1\.2\.3\.3%20-%20analisis%20alcance%20loggingmanager\.md)" "[3a5 - analisis alcance loggingmanager.md](./3a5%20-%20analisis%20alcance%20loggingmanager.md)" "1.2.3.3 analisis alcance loggingmanager"

update_ref "\[1\.2\.3\.3 - reflexion implementacion loggingmanager\.md\](\./1\.2\.3\.3%20-%20reflexion%20implementacion%20loggingmanager\.md)" "[3a6 - reflexion implementacion loggingmanager.md](./3a6%20-%20reflexion%20implementacion%20loggingmanager.md)" "1.2.3.3 reflexion loggingmanager"

# Referencias simples sin rutas
update_ref "\[1\.2\.1 - estructura de directorios python\]" "[2a - estructura directorios python]" "1.2.1 estructura directorios"

update_ref "\[1\.2\.1\.1 - decisiones estructura directorios python\]" "[2a1 - decisiones estructura directorios]" "1.2.1.1 decisiones estructura"

update_ref "\[1\.2\.2 - implementacion de abstracciones\]" "[2b - implementacion abstracciones]" "1.2.2 implementacion abstracciones"

update_ref "\[1\.2\.3 - comandos base\]" "[3a - comandos base]" "1.2.3 comandos base"

update_ref "\[1\.2\.4 - comando de configuracion\]" "[4a1 - comando de configuracion]" "1.2.4 comando configuracion"

update_ref "\[1\.2\.4 - analisis serie historias configuracion\]" "[4a - analisis serie historias configuracion]" "1.2.4 analisis serie historias"

update_ref "\[1\.2\.5 - comandos especificos\]" "[3b - comandos especificos]" "1.2.5 comandos especificos"

update_ref "\[1\.2\.6 - el comando ggai\]" "[9a - comando ggai]" "1.2.6 comando ggai"

update_ref "\[1\.2\.7 - soporte para conda e instalacion de dependencias\]" "[6a - soporte conda instalacion dependencias]" "1.2.7 soporte conda"

# Referencias con rutas completas desde planning
update_ref "\[1\.2\.1 - estructura directorios\]\(\.\.\/\.\.\/ideas\/1\.2\.1 - estructura de directorios python\.md\)" "[2a - estructura directorios](../../ideas/2a%20-%20estructura%20directorios%20python.md)" "planning: 1.2.1 estructura directorios"

update_ref "\[1\.2\.1\.1 - decisiones estructura\]\(\.\.\/\.\.\/ideas\/1\.2\.1\.1 - decisiones estructura directorios python\.md\)" "[2a1 - decisiones estructura](../../ideas/2a1%20-%20decisiones%20estructura%20directorios.md)" "planning: 1.2.1.1 decisiones"

# Referencias restantes sin archivos específicos
update_ref "\[1\.3 - reflexion-final-iniciativa-adopcion-vibedoc\]" "[1b - reflexion-final-iniciativa-adopcion-vibedoc]" "1.3 reflexion final"

update_ref "\[3\.1 - ia-avanzada-futuro\]" "[9c - ia-avanzada-futuro]" "3.1 IA avanzada futuro"

update_ref "\[3\.2 - spinner-progreso-ia\]" "[9c1 - spinner-progreso-ia]" "3.2 spinner progreso IA"

echo "✅ Actualización sistemática completada"
echo "🔍 Verificando referencias restantes..."

remaining=$(find . -name "*.md" -type f ! -name "mapa_actualizacion_referencias.md" ! -name "actualizar_referencias.sh" -exec grep -l "\[1\." {} \; | wc -l)
echo "📊 Archivos con referencias restantes: $remaining"

if [ $remaining -gt 0 ]; then
    echo "📋 Archivos que aún necesitan revisión manual:"
    find . -name "*.md" -type f ! -name "mapa_actualizacion_referencias.md" ! -name "actualizar_referencias.sh" -exec grep -l "\[1\." {} \;
fi
