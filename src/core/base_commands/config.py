"""
Configuration command base class for ggGit.

This module provides functionality for configuration management commands.
"""

from typing import Dict, Any, Optional
from .base import BaseCommand


class ConfigCommand(BaseCommand):
    """Base class for configuration commands."""
    
    def __init__(self):
        """Initialize configuration command."""
        super().__init__()
    
    def execute(self, action: str, key: Optional[str] = None, value: Optional[str] = None, level: str = 'user') -> int:
        """
        Execute configuration command.
        
        Args:
            action (str): Action to perform ('get', 'set', 'list', 'reset')
            key (Optional[str]): Configuration key for get/set/reset actions
            value (Optional[str]): Configuration value for set action
            level (str): Configuration level ('repo', 'module', 'user', 'default')
            
        Returns:
            int: Exit code (0 for success, 1 for failure)
        """
        try:
            if action == 'get':
                return self._execute_get(key)
            elif action == 'set':
                return self._execute_set(key, value, level)
            elif action == 'list':
                return self._execute_list(level)
            elif action == 'reset':
                return self._execute_reset(key, level)
            else:
                self.logger.log_error(ValueError(f"Unknown action: {action}"), "execute")
                return 1
        except Exception as e:
            self.logger.log_error(e, "execute")
            return 1
    
    def get_config_value(self, key: str) -> Any:
        """Get configuration value."""
        return self.config.get_config(key)
    
    def set_config_value(self, key: str, value: Any, level: str = 'user') -> None:
        """Set configuration value."""
        self.config.set_config(key, value, level)
    
    def list_config(self) -> Dict[str, Any]:
        """List all configuration values."""
        return self.config.load_hierarchical_config()
    
    def _execute_get(self, key: Optional[str]) -> int:
        """Execute get action."""
        if not key:
            self.logger.log_error(ValueError("Key is required for get action"), "_execute_get")
            return 1
        
        try:
            value = self.config.get_config(key)
            if value is not None:
                print(value)
                return 0
            else:
                print("")
                return 0
        except Exception as e:
            self.logger.log_error(e, "_execute_get")
            return 1
    
    def _execute_set(self, key: Optional[str], value: Optional[str], level: str) -> int:
        """Execute set action."""
        if not key:
            self.logger.log_error(ValueError("Key is required for set action"), "_execute_set")
            return 1
        
        if value is None:
            self.logger.log_error(ValueError("Value is required for set action"), "_execute_set")
            return 1
        
        try:
            # Convert value to appropriate type
            converted_value = self._convert_value(value)
            
            # Set the configuration
            self.config.set_config(key, converted_value, level)
            
            print(f"Set {key} = {converted_value} at {level} level")
            return 0
        except Exception as e:
            self.logger.log_error(e, "_execute_set")
            return 1
    
    def _execute_list(self, level: Optional[str]) -> int:
        """Execute list action."""
        try:
            if level:
                # List configuration for specific level
                config_data = self._get_config_for_level(level)
                if config_data:
                    self._print_config(config_data, level)
                else:
                    print(f"No configuration found for {level} level")
            else:
                # List all configuration
                config_data = self.config.load_hierarchical_config()
                self._print_config(config_data, "all levels")
            
            return 0
        except Exception as e:
            self.logger.log_error(e, "_execute_list")
            return 1
    
    def _execute_reset(self, key: Optional[str], level: str) -> int:
        """Execute reset action."""
        try:
            if key:
                # Reset specific key
                self._reset_config_key(key, level)
                print(f"Reset {key} at {level} level")
            else:
                # Reset entire level
                self._reset_config_level(level)
                print(f"Reset entire {level} level")
            
            return 0
        except Exception as e:
            self.logger.log_error(e, "_execute_reset")
            return 1
    
    def _convert_value(self, value: str) -> Any:
        """Convert string value to appropriate type."""
        # Try to convert to boolean
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        
        # Try to convert to number
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            pass
        
        # Return as string
        return value
    
    def _get_config_for_level(self, level: str) -> Dict[str, Any]:
        """Get configuration for specific level."""
        if level == 'repo':
            return self.config._load_config_file(self.config.config_paths[0]) or {}
        elif level == 'user':
            return self.config._load_config_file(self.config.config_paths[2]) or {}
        elif level == 'default':
            return self.config._load_config_file(self.config.config_paths[3]) or {}
        else:
            return {}
    
    def _print_config(self, config: Dict[str, Any], level: str) -> None:
        """Print configuration in readable format."""
        print(f"Configuration ({level}):")
        print("-" * 40)
        
        if not config:
            print("No configuration found")
            return
        
        self._print_config_recursive(config, "")
    
    def _print_config_recursive(self, config: Dict[str, Any], prefix: str) -> None:
        """Print configuration recursively."""
        for key, value in config.items():
            if isinstance(value, dict):
                print(f"{prefix}{key}:")
                self._print_config_recursive(value, prefix + "  ")
            else:
                print(f"{prefix}{key}: {value}")
    
    def _reset_config_key(self, key: str, level: str) -> None:
        """Reset specific configuration key."""
        self.config.reset_config(level, key)
    
    def _reset_config_level(self, level: str) -> None:
        """Reset entire configuration level."""
        self.config.reset_config(level)
