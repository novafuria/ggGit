"""
Tests for ConfigManager class.

This module contains comprehensive tests for the ConfigManager class,
covering all methods and functionality as specified in the architecture.
"""

import pytest
import tempfile
import os
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.core.config import ConfigManager


class TestConfigManagerInitialization:
    """Test ConfigManager initialization."""
    
    def test_init_creates_config_paths(self):
        """Test that initialization creates config paths."""
        config = ConfigManager()
        assert len(config.config_paths) == 4
        assert '.gggit/repo-config.yaml' in config.config_paths
        assert 'user-config.yaml' in config.config_paths[2]
        assert 'default-config.yaml' in config.config_paths[3]
    
    def test_init_loads_configuration(self):
        """Test that initialization loads configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                assert isinstance(config.config, dict)


class TestLoadHierarchicalConfig:
    """Test load_hierarchical_config method."""
    
    def test_load_hierarchical_config_empty(self):
        """Test loading configuration when no files exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                result = config.load_hierarchical_config()
                assert isinstance(result, dict)
    
    def test_load_hierarchical_config_with_default(self):
        """Test loading configuration with default file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config file
                default_config = {
                    'version': '1.0',
                    'ui': {
                        'colors': {
                            'success': 'green'
                        }
                    }
                }
                default_path = Path(tmpdir) / '.gggit' / 'default-config.yaml'
                default_path.parent.mkdir(parents=True, exist_ok=True)
                with open(default_path, 'w') as f:
                    yaml.dump(default_config, f)
                
                config = ConfigManager()
                result = config.load_hierarchical_config()
                assert result['version'] == '1.0'
                assert result['ui']['colors']['success'] == 'green'
    
    def test_load_hierarchical_config_priority_order(self):
        """Test that higher priority configs override lower priority ones."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
                default_config = {
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        }
                    }
                }
                default_path = Path(tmpdir) / '.gggit' / 'default-config.yaml'
                default_path.parent.mkdir(parents=True, exist_ok=True)
                with open(default_path, 'w') as f:
                    yaml.dump(default_config, f)
                
                # Create user config that overrides some values
                user_config = {
                    'ui': {
                        'colors': {
                            'success': 'bright_green'
                        }
                    }
                }
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                with open(user_path, 'w') as f:
                    yaml.dump(user_config, f)
                
                config = ConfigManager()
                result = config.load_hierarchical_config()
                
                # User config should override default
                assert result['ui']['colors']['success'] == 'bright_green'
                # But other values should remain from default
                assert result['ui']['colors']['error'] == 'red'


class TestGetConfig:
    """Test get_config method."""
    
    def test_get_config_existing_key(self):
        """Test getting existing configuration key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
                default_config = {
                    'ui': {
                        'colors': {
                            'success': 'green'
                        }
                    }
                }
                default_path = Path(tmpdir) / '.gggit' / 'default-config.yaml'
                default_path.parent.mkdir(parents=True, exist_ok=True)
                with open(default_path, 'w') as f:
                    yaml.dump(default_config, f)
                
                config = ConfigManager()
                value = config.get_config('ui.colors.success')
                assert value == 'green'
    
    def test_get_config_non_existing_key(self):
        """Test getting non-existing configuration key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                value = config.get_config('non.existing.key', 'default_value')
                assert value == 'default_value'
    
    def test_get_config_nested_access(self):
        """Test getting nested configuration values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
                default_config = {
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        },
                        'verbose': False
                    }
                }
                default_path = Path(tmpdir) / '.gggit' / 'default-config.yaml'
                default_path.parent.mkdir(parents=True, exist_ok=True)
                with open(default_path, 'w') as f:
                    yaml.dump(default_config, f)
                
                config = ConfigManager()
                
                # Test nested access
                assert config.get_config('ui.colors.success') == 'green'
                assert config.get_config('ui.colors.error') == 'red'
                assert config.get_config('ui.verbose') == False


class TestSetConfig:
    """Test set_config method."""
    
    def test_set_config_user_level(self):
        """Test setting configuration at user level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Set a configuration value
                config.set_config('ui.colors.success', 'bright_green', 'user')
                
                # Check that it was set
                value = config.get_config('ui.colors.success')
                assert value == 'bright_green'
                
                # Check that file was created
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                assert user_path.exists()
    
    def test_set_config_invalid_level(self):
        """Test setting configuration with invalid level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                with pytest.raises(ValueError, match="Invalid level"):
                    config.set_config('ui.colors.success', 'green', 'invalid_level')
    
    def test_set_config_nested_value(self):
        """Test setting nested configuration values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Set nested values
                config.set_config('ui.colors.success', 'bright_green', 'user')
                config.set_config('ui.colors.error', 'bright_red', 'user')
                config.set_config('ui.verbose', True, 'user')
                
                # Check that they were set
                assert config.get_config('ui.colors.success') == 'bright_green'
                assert config.get_config('ui.colors.error') == 'bright_red'
                assert config.get_config('ui.verbose') == True


class TestHelperMethods:
    """Test helper methods."""
    
    def test_deep_merge(self):
        """Test _deep_merge method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                base = {
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        }
                    }
                }
                
                override = {
                    'ui': {
                        'colors': {
                            'success': 'bright_green'
                        }
                    }
                }
                
                result = config._deep_merge(base, override)
                
                # Override should take precedence
                assert result['ui']['colors']['success'] == 'bright_green'
                # But other values should remain
                assert result['ui']['colors']['error'] == 'red'
    
    def test_set_nested_value(self):
        """Test _set_nested_value method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                test_config = {}
                config._set_nested_value(test_config, 'ui.colors.success', 'green')
                
                assert test_config['ui']['colors']['success'] == 'green'
    
    def test_get_config_path_for_level(self):
        """Test _get_config_path_for_level method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Test valid levels
                assert 'repo-config.yaml' in config._get_config_path_for_level('repo')
                assert 'user-config.yaml' in config._get_config_path_for_level('user')
                assert 'default-config.yaml' in config._get_config_path_for_level('default')
                
                # Test invalid level
                with pytest.raises(ValueError):
                    config._get_config_path_for_level('invalid')


class TestConfigIntegration:
    """Test ConfigManager integration."""
    
    def test_full_configuration_workflow(self):
        """Test complete configuration workflow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
                default_config = {
                    'version': '1.0',
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        }
                    }
                }
                default_path = Path(tmpdir) / '.gggit' / 'default-config.yaml'
                default_path.parent.mkdir(parents=True, exist_ok=True)
                with open(default_path, 'w') as f:
                    yaml.dump(default_config, f)
                
                # Initialize config manager
                config = ConfigManager()
                
                # Test getting default values
                assert config.get_config('ui.colors.success') == 'green'
                assert config.get_config('ui.colors.error') == 'red'
                
                # Test setting user values
                config.set_config('ui.colors.success', 'bright_green', 'user')
                config.set_config('ui.verbose', True, 'user')
                
                # Test that user values override defaults
                assert config.get_config('ui.colors.success') == 'bright_green'
                assert config.get_config('ui.verbose') == True
                assert config.get_config('ui.colors.error') == 'red'  # Still from default
                
                # Test that files were created
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                assert user_path.exists()
                
                # Verify user config file content
                with open(user_path, 'r') as f:
                    user_config = yaml.safe_load(f)
                assert user_config['ui']['colors']['success'] == 'bright_green'
                assert user_config['ui']['verbose'] == True
