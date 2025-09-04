"""
Tests for ConfigManager advanced functionality.

This module contains comprehensive tests for the advanced features
of the ConfigManager class, including level detection, key listing, and reset.
"""

import pytest
import tempfile
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.core.config import ConfigManager


class TestGetConfigLevel:
    """Test get_config_level method."""
    
    def test_get_config_level_user(self):
        """Test getting config level for user-defined key."""
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
                
                # Create user config that overrides
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
                
                # Test that user level takes precedence
                level = config.get_config_level('ui.colors.success')
                assert level == 'user'
    
    def test_get_config_level_default(self):
        """Test getting config level for default key."""
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
                
                config = ConfigManager()
                
                # Test that default level is returned
                level = config.get_config_level('ui.colors.success')
                assert level == 'default'
    
    def test_get_config_level_nonexistent(self):
        """Test getting config level for nonexistent key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Test that None is returned for nonexistent key
                level = config.get_config_level('nonexistent.key')
                assert level is None


class TestListConfigKeys:
    """Test list_config_keys method."""
    
    def test_list_config_keys_all_levels(self):
        """Test listing keys from all levels."""
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
                
                # Create user config
                user_config = {
                    'ai': {
                        'enabled': True
                    }
                }
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                with open(user_path, 'w') as f:
                    yaml.dump(user_config, f)
                
                config = ConfigManager()
                
                # Test listing all keys
                keys = config.list_config_keys()
                assert 'version' in keys
                assert 'ui.colors.success' in keys
                assert 'ai.enabled' in keys
                assert len(keys) > 0
    
    def test_list_config_keys_specific_level(self):
        """Test listing keys from specific level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create user config
                user_config = {
                    'ai': {
                        'enabled': True
                    },
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
                
                config = ConfigManager()
                
                # Test listing user level keys
                keys = config.list_config_keys('user')
                assert 'ai.enabled' in keys
                assert 'ui.colors.success' in keys
                assert 'version' not in keys  # Not in user level
    
    def test_list_config_keys_empty_level(self):
        """Test listing keys from empty level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Test listing keys from empty level
                keys = config.list_config_keys('user')
                assert keys == []


class TestResetConfig:
    """Test reset_config method."""
    
    def test_reset_config_specific_key(self):
        """Test resetting specific configuration key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create user config
                user_config = {
                    'ai': {
                        'enabled': True
                    },
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
                
                config = ConfigManager()
                
                # Test resetting specific key
                config.reset_config('user', 'ai.enabled')
                
                # Check that key was removed
                keys = config.list_config_keys('user')
                assert 'ai.enabled' not in keys
                assert 'ui.colors.success' in keys  # Should still be there
    
    def test_reset_config_entire_level(self):
        """Test resetting entire configuration level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create user config
                user_config = {
                    'ai': {
                        'enabled': True
                    },
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
                
                config = ConfigManager()
                
                # Test resetting entire level
                config.reset_config('user')
                
                # Check that all keys were removed
                keys = config.list_config_keys('user')
                assert keys == []
                
                # Check that file was deleted
                assert not user_path.exists()
    
    def test_reset_config_invalid_level(self):
        """Test resetting with invalid level."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Test resetting with invalid level
                with pytest.raises(ValueError, match="Invalid level"):
                    config.reset_config('invalid_level')


class TestHelperMethods:
    """Test helper methods for advanced functionality."""
    
    def test_key_exists_in_config(self):
        """Test _key_exists_in_config method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                test_config = {
                    'ui': {
                        'colors': {
                            'success': 'green'
                        }
                    }
                }
                
                # Test existing key
                assert config._key_exists_in_config(test_config, 'ui.colors.success') is True
                assert config._key_exists_in_config(test_config, 'ui.colors') is True
                
                # Test nonexistent key
                assert config._key_exists_in_config(test_config, 'ui.colors.error') is False
                assert config._key_exists_in_config(test_config, 'nonexistent.key') is False
    
    def test_extract_keys_from_config(self):
        """Test _extract_keys_from_config method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                test_config = {
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        },
                        'verbose': False
                    },
                    'ai': {
                        'enabled': True
                    }
                }
                
                keys = config._extract_keys_from_config(test_config)
                
                assert 'ui.colors.success' in keys
                assert 'ui.colors.error' in keys
                assert 'ui.verbose' in keys
                assert 'ai.enabled' in keys
                assert len(keys) == 4
    
    def test_remove_key_from_config(self):
        """Test _remove_key_from_config method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                test_config = {
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        },
                        'verbose': False
                    },
                    'ai': {
                        'enabled': True
                    }
                }
                
                # Remove specific key
                config._remove_key_from_config(test_config, 'ui.colors.success')
                
                # Check that key was removed
                assert 'success' not in test_config['ui']['colors']
                assert 'error' in test_config['ui']['colors']  # Should still be there
                assert 'verbose' in test_config['ui']  # Should still be there
                assert 'ai' in test_config  # Should still be there


class TestAdvancedIntegration:
    """Test advanced functionality integration."""
    
    def test_full_advanced_workflow(self):
        """Test complete advanced functionality workflow."""
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
                
                # Create user config
                user_config = {
                    'ui': {
                        'colors': {
                            'success': 'bright_green'
                        }
                    },
                    'ai': {
                        'enabled': True
                    }
                }
                user_path = Path(tmpdir) / '.gggit' / 'user-config.yaml'
                with open(user_path, 'w') as f:
                    yaml.dump(user_config, f)
                
                config = ConfigManager()
                
                # Test get_config_level
                assert config.get_config_level('ui.colors.success') == 'user'
                assert config.get_config_level('ui.colors.error') == 'default'
                assert config.get_config_level('version') == 'default'
                
                # Test list_config_keys
                all_keys = config.list_config_keys()
                assert 'ui.colors.success' in all_keys
                assert 'ui.colors.error' in all_keys
                assert 'ai.enabled' in all_keys
                
                user_keys = config.list_config_keys('user')
                assert 'ui.colors.success' in user_keys
                assert 'ai.enabled' in user_keys
                assert 'ui.colors.error' not in user_keys
                
                # Test reset specific key
                config.reset_config('user', 'ai.enabled')
                assert config.get_config_level('ai.enabled') is None
                assert 'ai.enabled' not in config.list_config_keys('user')
                
                # Test reset entire level
                config.reset_config('user')
                assert config.list_config_keys('user') == []
                assert config.get_config_level('ui.colors.success') == 'default'
