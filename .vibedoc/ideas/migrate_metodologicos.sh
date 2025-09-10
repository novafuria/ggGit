#!/bin/bash
# migrate_metodologicos.sh - Migración de zettels metodológicos
# Corrección conceptual: metodología Vibedoc → Sistema 1

echo "========================================="
echo "Migración zettels metodológicos 13.x → 1h.x"
echo "Corrección conceptual: metodología ≠ bugs"
echo "========================================="
echo ""

echo "🔄 Migrando zettel de entrada metodológico..."
mv "13 - varios bugs.md" "1h - mejoras estructura zettelkasten.md"

echo "🔄 Migrando reflexiones de historias..."
mv "13a - reflexion story-2.1.1-preparacion-zettels-entrada.md" "1h1 - reflexion story-2.1.1-preparacion-zettels-entrada.md"
mv "13b - reflexion story-2.1.2-revision-validacion-script.md" "1h2 - reflexion story-2.1.2-revision-validacion-script.md"
mv "13c - reflexion story-2.1.3-ejecucion-migracion.md" "1h3 - reflexion story-2.1.3-ejecucion-migracion.md"
mv "13d - reflexion story-2.1.4-actualizacion-referencias.md" "1h4 - reflexion story-2.1.4-actualizacion-referencias.md"

echo ""
echo "✅ Migración metodológica completada"
echo "📊 Archivos migrados: 5"
echo "🎯 Nueva ubicación: Sistema 1 (Vibedoc)"
echo ""
echo "🔍 Verificando nueva estructura..."
ls -la | grep "1h"
