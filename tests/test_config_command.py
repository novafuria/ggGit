"""
Tests for ConfigCommand class.

This module contains comprehensive tests for the ConfigCommand class,
covering all methods and functionality as specified in the architecture.
"""

import pytest
import tempfile
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.core.base_commands.config import ConfigCommand


class TestConfigCommandInitialization:
    """Test ConfigCommand initialization."""
    
    def test_init_creates_instance(self):
        """Test that ConfigCommand initializes correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                assert config_cmd is not None
                assert hasattr(config_cmd, 'config')
                assert hasattr(config_cmd, 'logger')


class TestExecuteMethod:
    """Test execute method."""
    
    def test_execute_get_action(self):
        """Test execute with get action."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test get action
                result = config_cmd.execute('get', 'ui.colors.success')
                assert result == 0
    
    def test_execute_set_action(self):
        """Test execute with set action."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test set action
                result = config_cmd.execute('set', 'ui.colors.success', 'bright_green', 'user')
                assert result == 0
    
    def test_execute_list_action(self):
        """Test execute with list action."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test list action
                result = config_cmd.execute('list')
                assert result == 0
    
    def test_execute_reset_action(self):
        """Test execute with reset action."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test reset action (will fail because not implemented)
                result = config_cmd.execute('reset', level='user')
                assert result == 1  # Should fail because reset is not implemented
    
    def test_execute_invalid_action(self):
        """Test execute with invalid action."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test invalid action
                result = config_cmd.execute('invalid_action')
                assert result == 1


class TestExecuteGet:
    """Test _execute_get method."""
    
    def test_execute_get_with_key(self):
        """Test _execute_get with valid key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test get with valid key
                result = config_cmd._execute_get('ui.colors.success')
                assert result == 0
    
    def test_execute_get_without_key(self):
        """Test _execute_get without key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test get without key
                result = config_cmd._execute_get(None)
                assert result == 1
    
    def test_execute_get_nonexistent_key(self):
        """Test _execute_get with nonexistent key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test get with nonexistent key
                result = config_cmd._execute_get('nonexistent.key')
                assert result == 0  # Should return 0 but print empty string


class TestExecuteSet:
    """Test _execute_set method."""
    
    def test_execute_set_with_key_and_value(self):
        """Test _execute_set with key and value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test set with key and value
                result = config_cmd._execute_set('ui.colors.success', 'bright_green', 'user')
                assert result == 0
    
    def test_execute_set_without_key(self):
        """Test _execute_set without key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test set without key
                result = config_cmd._execute_set(None, 'value', 'user')
                assert result == 1
    
    def test_execute_set_without_value(self):
        """Test _execute_set without value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test set without value
                result = config_cmd._execute_set('key', None, 'user')
                assert result == 1


class TestExecuteList:
    """Test _execute_list method."""
    
    def test_execute_list_all_levels(self):
        """Test _execute_list for all levels."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config
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
                
                config_cmd = ConfigCommand()
                
                # Test list all levels
                result = config_cmd._execute_list(None)
                assert result == 0
    
    def test_execute_list_specific_level(self):
        """Test _execute_list for specific level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create user config
                user_config = {
                    'ui': {
                        'colors': {
                            'success': 'bright_green'
                        }
                    }
                }
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                user_path.parent.mkdir(parents=True, exist_ok=True)
                with open(user_path, 'w') as f:
                    yaml.dump(user_config, f)
                
                config_cmd = ConfigCommand()
                
                # Test list specific level
                result = config_cmd._execute_list('user')
                assert result == 0


class TestValueConversion:
    """Test value conversion functionality."""
    
    def test_convert_value_boolean(self):
        """Test converting boolean values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test boolean conversion
                assert config_cmd._convert_value('true') is True
                assert config_cmd._convert_value('false') is False
                assert config_cmd._convert_value('TRUE') is True
                assert config_cmd._convert_value('FALSE') is False
    
    def test_convert_value_number(self):
        """Test converting number values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test number conversion
                assert config_cmd._convert_value('123') == 123
                assert config_cmd._convert_value('45.67') == 45.67
                assert config_cmd._convert_value('0') == 0
    
    def test_convert_value_string(self):
        """Test converting string values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config_cmd = ConfigCommand()
                
                # Test string conversion
                assert config_cmd._convert_value('hello') == 'hello'
                assert config_cmd._convert_value('bright_green') == 'bright_green'
                assert config_cmd._convert_value('') == ''


class TestConfigCommandIntegration:
    """Test ConfigCommand integration."""
    
    def test_full_workflow(self):
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
                
                config_cmd = ConfigCommand()
                
                # Test get initial value
                result = config_cmd.execute('get', 'ui.colors.success')
                assert result == 0
                
                # Test set new value
                result = config_cmd.execute('set', 'ui.colors.success', 'bright_green', 'user')
                assert result == 0
                
                # Test get updated value
                result = config_cmd.execute('get', 'ui.colors.success')
                assert result == 0
                
                # Test list configuration
                result = config_cmd.execute('list')
                assert result == 0
