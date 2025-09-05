"""
AI usage tracking for ggGit.

This module provides functionality to track AI usage, costs, and consumption
for monitoring and limiting AI service usage.
"""

import os
import yaml
from datetime import datetime, date
from typing import Dict, Any, Optional
from pathlib import Path


class AiUsageTracker:
    """
    Tracks AI usage, costs, and consumption for monitoring and limiting.
    
    This class manages the tracking of AI usage through a YAML file,
    providing methods to increment usage, get statistics, and reset counters.
    It integrates with the configuration system to determine tracking settings
    and file locations.
    
    Attributes:
        config (ConfigManager): Configuration management instance
        usage_file (str): Path to the usage tracking file
        
    Example:
        tracker = AiUsageTracker(config_manager)
        
        # Check if tracking is enabled
        if tracker.is_tracking_enabled():
            # Increment usage
            tracker.increment_usage("ggfeat", 150, 0.05)
            
            # Get usage stats
            stats = tracker.get_usage_stats()
            print(f"Total requests: {stats['totals']['requests']}")
            
            # Reset usage
            tracker.reset_usage()
    """
    
    def __init__(self, config_manager):
        """
        Initialize AI usage tracker.
        
        Args:
            config_manager (ConfigManager): Configuration management instance
        """
        self.config = config_manager
        self.usage_file = self.config.get_config('ai.usage_file', '.gggit/ai-usage.yaml')
    
    def is_tracking_enabled(self) -> bool:
        """
        Check if usage tracking is enabled.
        
        Returns:
            bool: True if tracking is enabled, False otherwise
        """
        return self.config.get_config('ai.tracking_enabled', True)
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """
        Get current usage statistics.
        
        Returns:
            Dict[str, Any]: Usage statistics including totals, daily usage, and limits
        """
        if not self.is_tracking_enabled():
            return self._create_default_usage_data()
        
        return self._load_usage_file()
    
    def increment_usage(self, command: str, tokens: int, cost: float) -> None:
        """
        Increment usage counters for a command.
        
        Args:
            command (str): Command that used AI (e.g., "ggfeat", "ggfix")
            tokens (int): Number of tokens used
            cost (float): Cost in USD
        """
        if not self.is_tracking_enabled():
            return
        
        # Load current usage data
        usage_data = self._load_usage_file()
        
        # Get current date
        today = date.today().isoformat()
        
        # Initialize daily usage if not exists
        if today not in usage_data['daily_usage']:
            usage_data['daily_usage'][today] = {
                'requests': 0,
                'tokens': 0,
                'cost': 0.0,
                'commands': {}
            }
        
        # Increment daily counters
        daily = usage_data['daily_usage'][today]
        daily['requests'] += 1
        daily['tokens'] += tokens
        daily['cost'] += cost
        
        # Increment command counter
        if command not in daily['commands']:
            daily['commands'][command] = 0
        daily['commands'][command] += 1
        
        # Update totals
        usage_data['totals']['requests'] += 1
        usage_data['totals']['tokens'] += tokens
        usage_data['totals']['cost'] += cost
        
        # Save updated data
        self._save_usage_file(usage_data)
    
    def reset_usage(self) -> None:
        """
        Reset usage tracking counters.
        
        This method resets all usage counters and starts a new tracking period.
        """
        if not self.is_tracking_enabled():
            return
        
        # Create new usage data with current date
        usage_data = self._create_default_usage_data()
        
        # Save reset data
        self._save_usage_file(usage_data)
    
    def _load_usage_file(self) -> Dict[str, Any]:
        """
        Load usage data from YAML file.
        
        Returns:
            Dict[str, Any]: Usage data from file or default if file doesn't exist
        """
        if not os.path.exists(self.usage_file):
            return self._create_default_usage_data()
        
        try:
            with open(self.usage_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or self._create_default_usage_data()
        except (yaml.YAMLError, IOError):
            # If file is corrupted, return default data
            return self._create_default_usage_data()
    
    def _save_usage_file(self, data: Dict[str, Any]) -> None:
        """
        Save usage data to YAML file.
        
        Args:
            data (Dict[str, Any]): Usage data to save
        """
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.usage_file), exist_ok=True)
        
        try:
            with open(self.usage_file, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        except IOError as e:
            # Log error but don't raise to avoid breaking the command
            print(f"Warning: Could not save usage data: {e}")
    
    def _create_default_usage_data(self) -> Dict[str, Any]:
        """
        Create default usage data structure.
        
        Returns:
            Dict[str, Any]: Default usage data structure
        """
        today = date.today().isoformat()
        cost_limit = self.config.get_config('ai.cost_limit', 5.00)
        
        return {
            'period': {
                'start_date': today,
                'end_date': today
            },
            'daily_usage': {},
            'totals': {
                'requests': 0,
                'tokens': 0,
                'cost': 0.0
            },
            'limits': {
                'cost_limit': cost_limit,
                'tracking_enabled': True
            }
        }
    
    def get_cost_limit(self) -> float:
        """
        Get the current cost limit.
        
        Returns:
            float: Cost limit in USD
        """
        return self.config.get_config('ai.cost_limit', 5.00)
    
    def is_cost_limit_exceeded(self) -> bool:
        """
        Check if cost limit has been exceeded.
        
        Returns:
            bool: True if cost limit exceeded, False otherwise
        """
        if not self.is_tracking_enabled():
            return False
        
        stats = self.get_usage_stats()
        current_cost = stats['totals']['cost']
        cost_limit = stats['limits']['cost_limit']
        
        return current_cost >= cost_limit
    
    def get_remaining_budget(self) -> float:
        """
        Get remaining budget before hitting cost limit.
        
        Returns:
            float: Remaining budget in USD
        """
        if not self.is_tracking_enabled():
            return float('inf')
        
        stats = self.get_usage_stats()
        current_cost = stats['totals']['cost']
        cost_limit = stats['limits']['cost_limit']
        
        return max(0.0, cost_limit - current_cost)
