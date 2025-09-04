"""
Tests for ConfigManager validation functionality.

This module contains comprehensive tests for the validation features
of the ConfigManager class, covering JSON Schema validation.
"""

import pytest
import tempfile
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock
import jsonschema

from src.core.config import ConfigManager


class TestConfigValidation:
    """Test configuration validation functionality."""
    
    def test_validate_config_valid(self):
        """Test validation with valid configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create valid config
                valid_config = {
                    'version': '1.0',
                    'ui': {
                        'colors': {
                            'success': 'green',
                            'error': 'red'
                        },
                        'verbose': False
                    }
                }
                
                config = ConfigManager()
                result = config.validate_config(valid_config, 'config')
                assert result is True
    
    def test_validate_config_invalid_version(self):
        """Test validation with invalid version format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create invalid config with wrong version format
                invalid_config = {
                    'version': 'invalid_version',  # Should match pattern ^[0-9]+\\.[0-9]+$
                    'ui': {
                        'colors': {
                            'success': 'green'
                        }
                    }
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_config, 'config')
                
                assert 'version' in str(exc_info.value)
                assert 'pattern' in str(exc_info.value)
    
    def test_validate_config_invalid_type(self):
        """Test validation with invalid type."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create invalid config with wrong type
                invalid_config = {
                    'version': '1.0',
                    'ui': {
                        'colors': {
                            'success': 123  # Should be string, not number
                        }
                    }
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_config, 'config')
                
                assert 'success' in str(exc_info.value)
                assert 'string' in str(exc_info.value)
    
    def test_validate_config_missing_required(self):
        """Test validation with missing required field."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create config missing required 'version' field
                invalid_config = {
                    'ui': {
                        'colors': {
                            'success': 'green'
                        }
                    }
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_config, 'config')
                
                assert 'version' in str(exc_info.value)
                assert 'required' in str(exc_info.value)
    
    def test_validate_config_invalid_enum(self):
        """Test validation with invalid enum value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create config with invalid enum value
                invalid_config = {
                    'version': '1.0',
                    'ai': {
                        'provider': 'invalid_provider'  # Should be one of the enum values
                    }
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_config, 'config')
                
                assert 'provider' in str(exc_info.value)
                assert 'enum' in str(exc_info.value)
    
    def test_validate_config_commit_schema(self):
        """Test validation with commit schema."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create valid commit config
                valid_commit = {
                    'type': 'feat',
                    'scope': 'auth',
                    'description': 'Add user authentication'
                }
                
                config = ConfigManager()
                result = config.validate_config(valid_commit, 'commit')
                assert result is True
    
    def test_validate_config_commit_invalid_type(self):
        """Test validation with invalid commit type."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create commit config with invalid type
                invalid_commit = {
                    'type': 'invalid_type',  # Should be one of the enum values
                    'description': 'Test commit'
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_commit, 'commit')
                
                assert 'type' in str(exc_info.value)
                assert 'enum' in str(exc_info.value)
    
    def test_validate_config_commit_missing_required(self):
        """Test validation with missing required commit fields."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create commit config missing required fields
                invalid_commit = {
                    'type': 'feat'
                    # Missing required 'description' field
                }
                
                config = ConfigManager()
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_commit, 'commit')
                
                assert 'description' in str(exc_info.value)
                assert 'required' in str(exc_info.value)
    
    def test_validate_config_invalid_schema_type(self):
        """Test validation with invalid schema type."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                result = config.validate_config({'test': 'value'}, 'invalid_schema')
                assert result is False
    
    def test_validate_config_schema_file_not_found(self):
        """Test validation when schema file doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Mock the schema path to point to non-existent file
                with patch.object(ConfigManager, '_load_schema', return_value=None):
                    config = ConfigManager()
                    
                    result = config.validate_config({'test': 'value'}, 'config')
                    assert result is False


class TestValidationIntegration:
    """Test validation integration with ConfigManager."""
    
    def test_set_config_with_validation(self):
        """Test that set_config works and validation happens on reload."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create default config first
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
                
                # Test setting valid configuration
                config.set_config('ui.colors.success', 'bright_green', 'user')
                
                # The validation happens in load_hierarchical_config() which is called
                # after set_config, so the config should be valid
                assert config.get_config('ui.colors.success') == 'bright_green'
    
    def test_load_hierarchical_config_with_validation(self):
        """Test that load_hierarchical_config validates configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                # Create valid default config
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
                
                # Should load successfully with valid config
                assert result['version'] == '1.0'
                assert result['ui']['colors']['success'] == 'green'
    
    def test_validation_error_messages(self):
        """Test that validation provides descriptive error messages."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                # Test with multiple validation errors
                invalid_config = {
                    'version': 'invalid',  # Wrong pattern
                    'ui': {
                        'colors': {
                            'success': 123  # Wrong type
                        }
                    }
                }
                
                with pytest.raises(jsonschema.ValidationError) as exc_info:
                    config.validate_config(invalid_config, 'config')
                
                # Should contain information about the validation error
                error_message = str(exc_info.value)
                assert 'version' in error_message or 'success' in error_message


class TestSchemaLoading:
    """Test schema loading functionality."""
    
    def test_load_schema_config(self):
        """Test loading config schema."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                schema = config._load_schema('config')
                assert schema is not None
                assert 'type' in schema
                assert 'properties' in schema
    
    def test_load_schema_commit(self):
        """Test loading commit schema."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                schema = config._load_schema('commit')
                assert schema is not None
                assert 'type' in schema
                assert 'properties' in schema
    
    def test_load_schema_invalid_type(self):
        """Test loading invalid schema type."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('pathlib.Path.home', return_value=Path(tmpdir)):
                config = ConfigManager()
                
                schema = config._load_schema('invalid_type')
                assert schema is None
