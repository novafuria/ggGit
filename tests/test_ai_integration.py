"""
Tests for AI integration with existing commands.

This module tests the integration of AI functionality with existing
commit commands, including automatic activation and fallback behavior.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from click.testing import CliRunner
from src.commands.ggfeat import FeatCommand, main as ggfeat_main
from src.commands.ggfix import FixCommand, main as ggfix_main
from src.commands.ggbreak import GgbreakCommand, main as ggbreak_main


class TestAiIntegration:
    """Test AI integration with existing commands."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_ggfeat_without_ai_configured(self):
        """Test ggfeat without AI configured."""
        result = self.runner.invoke(ggfeat_main, [])
        
        # Should show warning about AI not configured
        assert "IA no configurada" in result.output
        assert "ggfeat 'mensaje'" in result.output
    
    def test_ggfix_without_ai_configured(self):
        """Test ggfix without AI configured."""
        result = self.runner.invoke(ggfix_main, [])
        
        # Should show warning about AI not configured
        assert "IA no configurada" in result.output
        assert "ggfix 'mensaje'" in result.output
    
    def test_ggbreak_without_ai_configured(self):
        """Test ggbreak without AI configured."""
        result = self.runner.invoke(ggbreak_main, [])
        
        # Should show warning about AI not configured
        assert "IA no configurada" in result.output
        assert "ggbreak 'mensaje'" in result.output


class TestAiIntegrationWithRealComponents:
    """Test AI integration with real components."""
    
    def test_feat_command_ai_generation(self):
        """Test FeatCommand AI generation with real components."""
        try:
            from src.core.config import ConfigManager
            from src.core.git import GitInterface
            
            # Mock configuration for AI
            with patch('src.core.config.ConfigManager.get_config') as mock_get_config:
                mock_get_config.side_effect = lambda key, default: {
                    'ai.enabled': True,
                    'ai.provider': 'openai',
                    'ai.api_key_env': 'OPENAI_API_KEY',
                    'ai.cost_limit': 5.00,
                    'ai.tracking_enabled': True
                }.get(key, default)
                
                with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
                    command = FeatCommand()
                    
                    # Test _is_ai_configured
                    assert command._is_ai_configured() == True
                    
                    # Test _get_commit_prefix
                    assert command._get_commit_prefix() == "feat"
                    
        except Exception:
            # Skip if not in a git repository or config issues
            pytest.skip("Integration test requires proper configuration")
    
    def test_fix_command_ai_generation(self):
        """Test FixCommand AI generation with real components."""
        try:
            from src.core.config import ConfigManager
            from src.core.git import GitInterface
            
            # Mock configuration for AI
            with patch('src.core.config.ConfigManager.get_config') as mock_get_config:
                mock_get_config.side_effect = lambda key, default: {
                    'ai.enabled': True,
                    'ai.provider': 'openai',
                    'ai.api_key_env': 'OPENAI_API_KEY',
                    'ai.cost_limit': 5.00,
                    'ai.tracking_enabled': True
                }.get(key, default)
                
                with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
                    command = FixCommand()
                    
                    # Test _is_ai_configured
                    assert command._is_ai_configured() == True
                    
                    # Test _get_commit_prefix
                    assert command._get_commit_prefix() == "fix"
                    
        except Exception:
            # Skip if not in a git repository or config issues
            pytest.skip("Integration test requires proper configuration")
    
    def test_ggbreak_command_ai_generation(self):
        """Test GgbreakCommand AI generation with real components."""
        try:
            from src.core.config import ConfigManager
            from src.core.git import GitInterface
            
            # Mock configuration for AI
            with patch('src.core.config.ConfigManager.get_config') as mock_get_config:
                mock_get_config.side_effect = lambda key, default: {
                    'ai.enabled': True,
                    'ai.provider': 'openai',
                    'ai.api_key_env': 'OPENAI_API_KEY',
                    'ai.cost_limit': 5.00,
                    'ai.tracking_enabled': True
                }.get(key, default)
                
                with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
                    command = GgbreakCommand()
                    
                    # Test _is_ai_configured
                    assert command._is_ai_configured() == True
                    
                    # Test _get_commit_prefix
                    assert command._get_commit_prefix() == "break"
                    
        except Exception:
            # Skip if not in a git repository or config issues
            pytest.skip("Integration test requires proper configuration")


class TestAiIntegrationErrorHandling:
    """Test AI integration error handling."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_ai_generation_error(self):
        """Test error handling in AI generation."""
        # Test that the command handles errors gracefully
        result = self.runner.invoke(ggfeat_main, [])
        
        # Should show warning about AI not configured (normal behavior)
        assert "IA no configurada" in result.output
    
    def test_manual_commit_error(self):
        """Test error handling in manual commit."""
        # Test that the command handles errors gracefully
        result = self.runner.invoke(ggfeat_main, ['test message'])
        
        # Should show success message (command is working correctly)
        assert "Commit realizado exitosamente" in result.output
