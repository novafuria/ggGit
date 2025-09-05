"""
AI message generator for ggGit.

This module provides functionality to generate commit messages using AI services.
Currently implements a mock version for MVP development.
"""

import os
from typing import List, Dict, Any, Optional
from datetime import datetime


class AiMessageGenerator:
    """
    Generates commit messages using AI services.
    
    This class provides functionality to generate commit messages using
    various AI providers (OpenAI, Claude, etc.). Currently implements
    a mock version for MVP development and testing.
    
    Attributes:
        config (ConfigManager): Configuration management instance
        usage_tracker (AiUsageTracker): Usage tracking instance
        
    Example:
        generator = AiMessageGenerator(config_manager, usage_tracker)
        
        # Generate message
        message = generator.generate_message(files, diff_content)
        print(f"Generated: {message}")
        
        # Test connection
        if generator.test_connection():
            print("AI connection successful")
    """
    
    def __init__(self, config_manager, usage_tracker):
        """
        Initialize AI message generator.
        
        Args:
            config_manager (ConfigManager): Configuration management instance
            usage_tracker (AiUsageTracker): Usage tracking instance
        """
        self.config = config_manager
        self.usage_tracker = usage_tracker
    
    def generate_message(self, files: List[str], diff_content: str) -> str:
        """
        Generate commit message using AI (mock implementation).
        
        This method generates a commit message based on the files and diff content.
        Currently implements a mock version that creates simple messages.
        
        Args:
            files (List[str]): List of files that were modified
            diff_content (str): Git diff content for analysis
            
        Returns:
            str: Generated commit message
            
        Note:
            This is a mock implementation for MVP. In the future, this will
            integrate with real AI services like OpenAI, Claude, etc.
        """
        # Mock implementation for MVP
        if not files:
            return "chore: no changes detected"
        
        # Analyze file types and changes
        file_types = self._analyze_file_types(files)
        change_type = self._analyze_change_type(diff_content)
        
        # Generate message based on analysis
        if change_type == "feature":
            prefix = "feat"
        elif change_type == "fix":
            prefix = "fix"
        elif change_type == "docs":
            prefix = "docs"
        elif change_type == "test":
            prefix = "test"
        elif change_type == "refactor":
            prefix = "refactor"
        else:
            prefix = "chore"
        
        # Create descriptive message
        if len(files) == 1:
            file_name = os.path.basename(files[0])
            message = f"{prefix}: update {file_name}"
        else:
            message = f"{prefix}: update {len(files)} files"
        
        # Add scope if applicable
        if file_types:
            scope = self._get_scope_from_file_types(file_types)
            if scope:
                message = f"{prefix}({scope}): update {len(files)} files"
        
        # Track usage (mock values)
        self._track_usage(len(files), len(diff_content.splitlines()))
        
        return message
    
    def test_connection(self) -> bool:
        """
        Test AI connection and configuration (mock implementation).
        
        This method tests the connection to AI services and verifies
        that the configuration is correct.
        
        Returns:
            bool: True if connection successful, False otherwise
            
        Note:
            This is a mock implementation for MVP. In the future, this will
            test real connections to AI services.
        """
        # Mock implementation for MVP
        try:
            # Check if AI is configured
            if not self.config.get_config('ai.enabled', False):
                return False
            
            # Check if provider is set
            provider = self.config.get_config('ai.provider')
            if not provider:
                return False
            
            # Check if API key is available
            api_key_env = self.config.get_config('ai.api_key_env', 'OPENAI_API_KEY')
            if not os.getenv(api_key_env):
                return False
            
            # Mock successful connection
            return True
            
        except Exception:
            return False
    
    def _analyze_file_types(self, files: List[str]) -> List[str]:
        """
        Analyze file types from file list.
        
        Args:
            files (List[str]): List of file paths
            
        Returns:
            List[str]: List of file types found
        """
        file_types = set()
        
        for file_path in files:
            if file_path.endswith('.py'):
                file_types.add('python')
            elif file_path.endswith('.js') or file_path.endswith('.ts'):
                file_types.add('javascript')
            elif file_path.endswith('.md'):
                file_types.add('documentation')
            elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
                file_types.add('config')
            elif file_path.endswith('.json'):
                file_types.add('config')
            elif 'test' in file_path.lower():
                file_types.add('test')
            elif 'spec' in file_path.lower():
                file_types.add('test')
        
        return list(file_types)
    
    def _analyze_change_type(self, diff_content: str) -> str:
        """
        Analyze change type from diff content.
        
        Args:
            diff_content (str): Git diff content
            
        Returns:
            str: Type of change (feature, fix, docs, test, refactor, chore)
        """
        if not diff_content:
            return "chore"
        
        # Simple heuristics for change type
        diff_lower = diff_content.lower()
        
        if any(keyword in diff_lower for keyword in ['add', 'new', 'create', 'implement']):
            return "feature"
        elif any(keyword in diff_lower for keyword in ['fix', 'bug', 'error', 'issue']):
            return "fix"
        elif any(keyword in diff_lower for keyword in ['doc', 'readme', 'comment']):
            return "docs"
        elif any(keyword in diff_lower for keyword in ['test', 'spec', 'mock']):
            return "test"
        elif any(keyword in diff_lower for keyword in ['refactor', 'clean', 'optimize']):
            return "refactor"
        else:
            return "chore"
    
    def _get_scope_from_file_types(self, file_types: List[str]) -> Optional[str]:
        """
        Get scope from file types.
        
        Args:
            file_types (List[str]): List of file types
            
        Returns:
            Optional[str]: Scope string or None
        """
        if 'python' in file_types:
            return 'python'
        elif 'javascript' in file_types:
            return 'js'
        elif 'documentation' in file_types:
            return 'docs'
        elif 'config' in file_types:
            return 'config'
        elif 'test' in file_types:
            return 'test'
        else:
            return None
    
    def _track_usage(self, file_count: int, diff_lines: int) -> None:
        """
        Track AI usage for the generated message.
        
        Args:
            file_count (int): Number of files analyzed
            diff_lines (int): Number of diff lines analyzed
        """
        if not self.usage_tracker.is_tracking_enabled():
            return
        
        # Mock token calculation (rough estimate)
        tokens = max(50, file_count * 10 + diff_lines * 2)
        
        # Mock cost calculation (rough estimate)
        cost = tokens * 0.0001  # $0.0001 per token
        
        # Track usage
        self.usage_tracker.increment_usage("ggai", tokens, cost)
    
    def get_provider_info(self) -> Dict[str, Any]:
        """
        Get information about the configured AI provider.
        
        Returns:
            Dict[str, Any]: Provider information including name, model, and status
        """
        provider = self.config.get_config('ai.provider', 'openai')
        model = self.config.get_config('ai.model', 'gpt-3.5-turbo')
        base_url = self.config.get_config('ai.base_url')
        
        return {
            'provider': provider,
            'model': model,
            'base_url': base_url,
            'status': 'configured' if self.test_connection() else 'not_configured'
        }
