"""
Configuration management module for ggGit.

This module provides hierarchical configuration management
with priority: repository > module > user > default.

The ConfigManager follows a hierarchical configuration pattern where:
1. Repository config (.gggit/repo-config.yaml) - highest priority
2. Module configs (.gggit/modules/*.yaml) - module-specific settings
3. User config (~/.gggit/user-config.yaml) - user preferences
4. Default config (~/.gggit/default-config.yaml) - fallback defaults

Configuration files are validated against JSON schemas defined in config/
directory to ensure consistency and prevent configuration errors.
"""

import os
import yaml
import jsonschema
from typing import Dict, Any, Optional, List, Union
from pathlib import Path


class ConfigManager:
    """
    Manages configuration with hierarchical priority and validation.
    
    This class provides a centralized configuration management system
    that follows a hierarchical priority model. It supports YAML-based
    configuration files with JSON schema validation.
    
    Configuration Priority (highest to lowest):
    1. Repository-specific config (.gggit/repo-config.yaml)
    2. Module-specific configs (.gggit/modules/*.yaml)
    3. User config (~/.gggit/user-config.yaml)
    4. Default config (~/.gggit/default-config.yaml)
    
    Attributes:
        config (Dict[str, Any]): Merged configuration from all sources
        config_paths (List[str]): List of configuration file paths in priority order
        
    Example:
        config = ConfigManager()
        
        # Get a configuration value with fallback
        commit_format = config.get_config('commit.format', 'conventional')
        
        # Set a user-level configuration
        config.set_config('commit.auto_stage', True, level='user')
        
        # Load all configurations
        all_config = config.load_hierarchical_config()
    """
    
    def __init__(self):
        """
        Initialize configuration manager.
        
        Sets up the configuration manager with default paths and loads
        the hierarchical configuration. The configuration is loaded
        automatically during initialization.
        """
        self.config = {}
        self.config_paths = self._get_config_paths()
        # Load configuration during initialization
        self.config = self.load_hierarchical_config()
    
    def _get_config_paths(self) -> List[str]:
        """
        Get configuration file paths in priority order.
        
        Returns:
            List[str]: Configuration file paths ordered from highest
                      to lowest priority
        """
        home = Path.home()
        return [
            ".gggit/repo-config.yaml",  # Repository config (highest priority)
            f"{home}/.gggit/modules/",   # Module configs
            f"{home}/.gggit/user-config.yaml",  # User config
            f"{home}/.gggit/default-config.yaml"  # Default config (lowest priority)
        ]
    
    def load_hierarchical_config(self) -> Dict[str, Any]:
        """
        Load configuration following hierarchical priority.
        
        This method loads configuration from all sources and merges them
        according to the priority order. Higher priority configurations
        override lower priority ones.
        
        Returns:
            Dict[str, Any]: Merged configuration dictionary
            
        Raises:
            FileNotFoundError: If required default configuration is missing
            yaml.YAMLError: If configuration files contain invalid YAML
            jsonschema.ValidationError: If configuration doesn't match schema
        """
        merged_config = {}
        
        # Load configurations in priority order (lowest to highest)
        # 1. Default configuration (lowest priority)
        default_config = self._load_config_file(self.config_paths[3])  # default-config.yaml
        if default_config:
            merged_config = self._deep_merge(merged_config, default_config)
        
        # 2. User configuration
        user_config = self._load_config_file(self.config_paths[2])  # user-config.yaml
        if user_config:
            merged_config = self._deep_merge(merged_config, user_config)
        
        # 3. Module configurations
        module_configs = self._load_module_configs()
        for module_config in module_configs:
            merged_config = self._deep_merge(merged_config, module_config)
        
        # 4. Repository configuration (highest priority)
        repo_config = self._load_config_file(self.config_paths[0])  # repo-config.yaml
        if repo_config:
            merged_config = self._deep_merge(merged_config, repo_config)
        
        # Validate final configuration
        if merged_config:
            self.validate_config(merged_config)
        
        self.config = merged_config
        return merged_config
    
    def get_config(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by key using dot notation.
        
        Supports nested configuration access using dot notation.
        For example: 'commit.format' accesses config['commit']['format']
        
        Args:
            key (str): Configuration key in dot notation (e.g., 'commit.format')
            default (Any, optional): Default value if key not found
            
        Returns:
            Any: Configuration value or default if not found
            
        Example:
            config.get_config('commit.format', 'conventional')
            config.get_config('git.auto_stage', False)
            config.get_config('ui.colors.enabled', True)
        """
        # Load configuration if not already loaded
        if not self.config:
            self.load_hierarchical_config()
        
        # Split key by dots for nested access
        keys = key.split('.')
        current = self.config
        
        try:
            for k in keys:
                current = current[k]
            return current
        except (KeyError, TypeError):
            return default
    
    def set_config(self, key: str, value: Any, level: str = 'user') -> None:
        """
        Set configuration value at specified level.
        
        Args:
            key (str): Configuration key in dot notation
            value (Any): Value to set
            level (str): Configuration level ('repo', 'module', 'user', 'default')
            
        Raises:
            ValueError: If level is not valid
            PermissionError: If unable to write to configuration file
            jsonschema.ValidationError: If value doesn't match schema
            
        Example:
            config.set_config('commit.format', 'conventional', level='user')
            config.set_config('git.auto_stage', True, level='repo')
        """
        # Validate level parameter
        valid_levels = ['repo', 'module', 'user', 'default']
        if level not in valid_levels:
            raise ValueError(f"Invalid level '{level}'. Must be one of {valid_levels}")
        
        # Get configuration file path for the level
        config_path = self._get_config_path_for_level(level)
        
        # Load existing configuration for the level
        existing_config = self._load_config_file(config_path) or {}
        
        # Set nested value using dot notation
        self._set_nested_value(existing_config, key, value)
        
        # Validate against schema
        self.validate_config(existing_config)
        
        # Save to appropriate configuration file
        self._save_config_file(config_path, existing_config)
        
        # Reload hierarchical configuration
        self.load_hierarchical_config()
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate configuration against JSON schema.
        
        Validates the configuration dictionary against the appropriate
        JSON schema to ensure all required fields are present and
        values are of correct types.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary to validate
            
        Returns:
            bool: True if configuration is valid, False otherwise
            
        Raises:
            jsonschema.ValidationError: If configuration doesn't match schema
            FileNotFoundError: If schema file is not found
            
        Note:
            This method will be implemented in STORY-1.2.4 - comando de configuracion
        """
        # TODO: Implement configuration validation
        # 1. Load appropriate JSON schema
        # 2. Validate configuration against schema
        # 3. Return validation result
        return True
    
    def get_config_level(self, key: str) -> Optional[str]:
        """
        Get the configuration level where a key is defined.
        
        Args:
            key (str): Configuration key to check
            
        Returns:
            Optional[str]: Level where key is defined ('repo', 'module', 'user', 'default')
                          or None if key doesn't exist
            
        Note:
            This method will be implemented in STORY-1.2.4 - comando de configuracion
        """
        # TODO: Implement configuration level detection
        # 1. Check each configuration level in priority order
        # 2. Return the first level where key exists
        return None
    
    def list_config_keys(self, level: Optional[str] = None) -> List[str]:
        """
        List all configuration keys at specified level or all levels.
        
        Args:
            level (Optional[str]): Specific level to list keys for
            
        Returns:
            List[str]: List of configuration keys in dot notation
            
        Note:
            This method will be implemented in STORY-1.2.4 - comando de configuracion
        """
        # TODO: Implement configuration key listing
        # 1. If level specified, list keys for that level only
        # 2. If no level, list all keys from all levels
        # 3. Return flattened list of dot-notation keys
        return []
    
    def reset_config(self, level: str, key: Optional[str] = None) -> None:
        """
        Reset configuration at specified level.
        
        Args:
            level (str): Configuration level to reset
            key (Optional[str]): Specific key to reset, or None to reset entire level
            
        Raises:
            ValueError: If level is not valid
            FileNotFoundError: If configuration file doesn't exist
            
        Note:
            This method will be implemented in STORY-1.2.4 - comando de configuracion
        """
        # TODO: Implement configuration reset
        # 1. Validate level parameter
        # 2. Load configuration file for the level
        # 3. Remove specific key or reset entire configuration
        # 4. Save updated configuration
        pass
    
    def _load_config_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """
        Load configuration from a YAML file.
        
        Args:
            file_path (str): Path to the configuration file
            
        Returns:
            Optional[Dict[str, Any]]: Configuration dictionary or None if file doesn't exist
        """
        try:
            path = Path(file_path)
            if not path.exists():
                return None
            
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except (yaml.YAMLError, IOError):
            return None
    
    def _load_module_configs(self) -> List[Dict[str, Any]]:
        """
        Load all module configuration files.
        
        Returns:
            List[Dict[str, Any]]: List of module configurations
        """
        module_configs = []
        modules_dir = Path(self.config_paths[1])  # modules directory
        
        if modules_dir.exists() and modules_dir.is_dir():
            for yaml_file in modules_dir.glob("*.yaml"):
                config = self._load_config_file(str(yaml_file))
                if config:
                    module_configs.append(config)
        
        return module_configs
    
    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two dictionaries.
        
        Args:
            base (Dict[str, Any]): Base dictionary
            override (Dict[str, Any]): Override dictionary
            
        Returns:
            Dict[str, Any]: Merged dictionary
        """
        result = base.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result
    
    def _get_config_path_for_level(self, level: str) -> str:
        """
        Get configuration file path for a specific level.
        
        Args:
            level (str): Configuration level
            
        Returns:
            str: Path to configuration file
        """
        if level == 'repo':
            return self.config_paths[0]  # .gggit/repo-config.yaml
        elif level == 'user':
            return self.config_paths[2]  # ~/.gggit/user-config.yaml
        elif level == 'default':
            return self.config_paths[3]  # ~/.gggit/default-config.yaml
        else:
            raise ValueError(f"Invalid level: {level}")
    
    def _set_nested_value(self, config: Dict[str, Any], key: str, value: Any) -> None:
        """
        Set a nested value in configuration using dot notation.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary
            key (str): Dot notation key
            value (Any): Value to set
        """
        keys = key.split('.')
        current = config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def _save_config_file(self, file_path: str, config: Dict[str, Any]) -> None:
        """
        Save configuration to a YAML file.
        
        Args:
            file_path (str): Path to the configuration file
            config (Dict[str, Any]): Configuration dictionary
        """
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)
