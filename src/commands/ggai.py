#!/usr/bin/env python3
"""
ggai - AI-powered commit message generation and management.

This command provides AI-powered commit message generation and usage tracking
for ggGit. It includes subcommands for usage statistics, testing connections,
and managing AI consumption.

Usage: ggai [command] [options]
"""

import sys
import click
from pathlib import Path
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.base_commands.base import BaseCommand
from core.ai import ComplexityAnalyzer, AiUsageTracker, AiMessageGenerator
from core.utils.colors import ColorManager


class GgaiCommand(BaseCommand):
    """Command for AI-powered commit message generation and management."""
    
    def __init__(self):
        """Initialize ggai command."""
        super().__init__()
        self.usage_tracker = AiUsageTracker(self.config)
        self.message_generator = AiMessageGenerator(self.config, self.usage_tracker)
        self.analyzer = ComplexityAnalyzer(self.git, self.config)
    
    def execute(self, *args, **kwargs):
        """Execute the ggai command (required by BaseCommand)."""
        return self.execute_main()
    
    def execute_main(self) -> int:
        """Execute main ggai command (generate message or show fallback)."""
        try:
            # Check if AI is configured
            if not self._is_ai_configured():
                click.echo(ColorManager.warning("IA no configurada. Usa 'ggconfig set ai.enabled true'"))
                return 1
            
            # Check if we're in a git repository
            if not self.git.is_git_repository():
                click.echo(ColorManager.error("No es un repositorio Git"))
                return 1
            
            # Analyze complexity
            should_use_ai, analysis = self.analyzer.should_use_ai()
            
            if should_use_ai:
                # Generate message with AI
                files = analysis['files']
                diff_content = self.git.get_diff_content(files, staged=analysis['has_staged'])
                
                try:
                    message = self.message_generator.generate_message(files, diff_content)
                    click.echo(ColorManager.success(f"🤖 Mensaje generado: {message}"))
                    
                    # Show analysis summary
                    summary = self.analyzer.get_analysis_summary(analysis)
                    click.echo(ColorManager.info(f"📝 {summary}"))
                    
                    return 0
                    
                except Exception as e:
                    click.echo(ColorManager.error(f"Error generando mensaje: {e}"))
                    return 1
            else:
                # Show fallback message
                fallback = self.analyzer.get_fallback_message(analysis)
                click.echo(ColorManager.warning(fallback))
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error ejecutando comando: {e}"))
            return 1
    
    def execute_usage(self) -> int:
        """Execute ggai usage command (show usage statistics)."""
        if not self.usage_tracker.is_tracking_enabled():
            click.echo(ColorManager.warning("Tracking de IA deshabilitado"))
            return 0
        
        try:
            stats = self.usage_tracker.get_usage_stats()
            
            # Show usage statistics
            start_date = stats['period']['start_date']
            requests = stats['totals']['requests']
            tokens = stats['totals']['tokens']
            cost = stats['totals']['cost']
            cost_limit = stats['limits']['cost_limit']
            
            click.echo(f"📊 Consumo de IA - Período: {start_date}")
            click.echo(f"├── Requests: {requests}")
            click.echo(f"├── Tokens usados: {tokens:,}")
            click.echo(f"└── Costo estimado: ${cost:.2f}/${cost_limit:.2f}")
            
            # Show remaining budget
            remaining = self.usage_tracker.get_remaining_budget()
            if remaining < cost_limit:
                click.echo(f"💡 Presupuesto restante: ${remaining:.2f}")
            
            # Show help
            click.echo("\n💡 Comandos disponibles:")
            click.echo("   ggai usage reset    # Reiniciar contador")
            click.echo("   ggconfig get ai.*   # Ver configuración")
            
            return 0
            
        except Exception as e:
            click.echo(ColorManager.error(f"Error obteniendo estadísticas: {e}"))
            return 1
    
    def execute_usage_reset(self) -> int:
        """Execute ggai usage reset command (reset usage counters)."""
        if not self.usage_tracker.is_tracking_enabled():
            click.echo(ColorManager.warning("Tracking de IA deshabilitado"))
            return 0
        
        try:
            self.usage_tracker.reset_usage()
            click.echo(ColorManager.success("✅ Contador de consumo reiniciado"))
            click.echo(f"📊 Nuevo período iniciado: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            return 0
            
        except Exception as e:
            click.echo(ColorManager.error(f"Error reiniciando contador: {e}"))
            return 1
    
    def execute_test(self) -> int:
        """Execute ggai test command (test AI connection)."""
        try:
            # Test connection
            if self.message_generator.test_connection():
                click.echo(ColorManager.success("✅ Conexión IA exitosa"))
                
                # Show provider info
                provider_info = self.message_generator.get_provider_info()
                click.echo(f"🔧 Proveedor: {provider_info['provider']}")
                click.echo(f"🤖 Modelo: {provider_info['model']}")
                
                if provider_info['base_url']:
                    click.echo(f"🌐 URL: {provider_info['base_url']}")
                
                return 0
            else:
                click.echo(ColorManager.error("❌ Error de conexión IA"))
                click.echo("💡 Verifica la configuración con 'ggconfig get ai.*'")
                return 1
                
        except Exception as e:
            click.echo(ColorManager.error(f"Error probando conexión: {e}"))
            return 1


@click.group()
def ggai():
    """ggai - AI-powered commit message generation and management."""
    pass


@ggai.command()
def main():
    """Generate commit message using AI or show fallback."""
    try:
        command = GgaiCommand()
        result = command.execute_main()
        sys.exit(result)
    except Exception as e:
        ColorManager.error(f"Error: {e}")
        sys.exit(1)


@ggai.command()
def usage():
    """Show AI usage statistics and costs."""
    try:
        command = GgaiCommand()
        result = command.execute_usage()
        sys.exit(result)
    except Exception as e:
        ColorManager.error(f"Error: {e}")
        sys.exit(1)


@ggai.command()
def test():
    """Test AI connection and configuration."""
    try:
        command = GgaiCommand()
        result = command.execute_test()
        sys.exit(result)
    except Exception as e:
        ColorManager.error(f"Error: {e}")
        sys.exit(1)


@ggai.group()
def usage_group():
    """Usage management commands."""
    pass


@usage_group.command()
def reset():
    """Reset usage tracking counters."""
    try:
        command = GgaiCommand()
        result = command.execute_usage_reset()
        sys.exit(result)
    except Exception as e:
        ColorManager.error(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    ggai()
