"""
AI message generator for ggGit.

This module provides functionality to generate commit messages using AI services.
Currently implements a mock version for MVP development.
"""

import os
import re
import requests
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
    
    def generate_message(self, files: List[str], diff_content: str, commit_type: str = None) -> str:
        """
        Generate commit message using real AI.
        
        This method generates a commit message using real AI services
        based on the files and diff content.
        
        Args:
            files (List[str]): List of files that were modified
            diff_content (str): Git diff content for analysis
            commit_type (str): Type of commit (feat, fix, etc.) for context
            
        Returns:
            str: Generated commit message
        """
        if not files:
            return "chore: no changes detected"
        
        try:
            # Build context-aware prompt
            prompt = self._build_context_prompt(files, diff_content, commit_type)
            
            # Call real AI API
            response = self._call_ollama_api(prompt)
            
            # Process and clean response
            message = self._process_ai_response(response)
            
            # Track real usage
            self._track_real_usage(prompt, response)
            
            return message
            
        except Exception as e:
            # No fallback to mock - show clear error
            raise Exception(f"Error generando mensaje IA: {e}")
    
    def test_connection(self) -> bool:
        """
        Test AI connection and configuration.
        
        This method tests the connection to AI services and verifies
        that the configuration is correct.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            # Check if AI is configured
            if not self.config.get_config('ai.enabled', False):
                return False
            
            # Check if provider is set
            provider = self.config.get_config('ai.provider')
            if not provider:
                return False
            
            # Test with a simple prompt
            test_prompt = "Generate a simple commit message for: test file"
            response = self._call_ollama_api(test_prompt)
            
            # If we get a response, connection is working
            return bool(response and response.strip())
            
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
    
    def _call_ollama_api(self, prompt: str) -> str:
        """
        Call Ollama API to generate commit message.
        
        Args:
            prompt (str): Prompt to send to the AI model
            
        Returns:
            str: AI-generated response
            
        Raises:
            Exception: If API call fails
        """
        base_url = self.config.get_config('ai.base_url', 'http://localhost:11434')
        model = self.config.get_config('ai.model', 'gemma3:4b')
        
        url = f"{base_url}/api/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "max_tokens": 200
            }
        }
        
        try:
            response = requests.post(url, json=data, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "").strip()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error de conexión con Ollama: {e}")
        except Exception as e:
            raise Exception(f"Error procesando respuesta de IA: {e}")
    
    def _build_context_prompt(self, files: List[str], diff_content: str, commit_type: str = None) -> str:
        """
        Build context-aware prompt for better AI generation.
        
        Args:
            files (List[str]): List of files modified
            diff_content (str): Git diff content
            commit_type (str): Type of commit for context
            
        Returns:
            str: Formatted prompt for AI
        """
        # Get commit type context
        type_context = self._get_commit_type_context(commit_type)
        
        # Build file context
        file_context = ', '.join(files)
        
        # Build additional context
        additional_context = self._get_additional_context(files, diff_content)
        
        prompt = f"""Generate a concise commit message for the following changes:

{type_context}

Files modified: {file_context}

Changes:
{diff_content}

{additional_context}

Requirements:
- Use conventional commit format: {commit_type}: <description>
- Keep description under 50 characters
- Be specific about what was changed
- Use imperative mood (e.g., "add", "fix", "update")
- Do not use markdown formatting or code blocks
- Generate only the commit message, no explanations"""

        return prompt
    
    def _get_commit_type_context(self, commit_type: str) -> str:
        """
        Get context information for the commit type.
        
        Args:
            commit_type (str): Type of commit (feat, fix, etc.)
            
        Returns:
            str: Context information for the commit type
        """
        if not commit_type:
            return "Type: General changes"
        
        context_map = {
            'feat': 'Type: New feature or functionality',
            'fix': 'Type: Bug fix or issue resolution',
            'docs': 'Type: Documentation changes',
            'style': 'Type: Code style or formatting changes',
            'refactor': 'Type: Code refactoring without changing functionality',
            'test': 'Type: Test additions or modifications',
            'chore': 'Type: Maintenance or build process changes',
            'perf': 'Type: Performance improvements',
            'ci': 'Type: CI/CD pipeline changes',
            'build': 'Type: Build system changes',
            'break': 'Type: Breaking changes'
        }
        
        return context_map.get(commit_type, f"Type: {commit_type}")
    
    def _get_additional_context(self, files: List[str], diff_content: str) -> str:
        """
        Get additional context when needed.
        
        Args:
            files (List[str]): List of files modified
            diff_content (str): Git diff content
            
        Returns:
            str: Additional context information
        """
        context_parts = []
        
        # If many files, mention it
        if len(files) > 5:
            context_parts.append("Note: Multiple files modified - focus on the main change")
        
        # If configuration files, mention it
        config_files = [f for f in files if any(ext in f for ext in ['.yml', '.yaml', '.json', '.toml'])]
        if config_files:
            context_parts.append(f"Note: Configuration files modified: {', '.join(config_files)}")
        
        # If test files, mention it
        test_files = [f for f in files if 'test' in f.lower() or 'spec' in f.lower()]
        if test_files:
            context_parts.append(f"Note: Test files included: {', '.join(test_files)}")
        
        # If documentation files, mention it
        doc_files = [f for f in files if f.endswith('.md') or 'readme' in f.lower()]
        if doc_files:
            context_parts.append(f"Note: Documentation files modified: {', '.join(doc_files)}")
        
        return '\n'.join(context_parts) if context_parts else ""
    
    def _process_ai_response(self, response: str) -> str:
        """
        Process AI response and clean prefixes.
        
        Args:
            response (str): Raw AI response
            
        Returns:
            str: Cleaned commit message
        """
        # Clean response
        message = response.strip()
        
        # Remove markdown formatting
        message = re.sub(r'```.*?```', '', message, flags=re.DOTALL)
        message = re.sub(r'`([^`]+)`', r'\1', message)
        message = re.sub(r'\*\*([^*]+)\*\*', r'\1', message)
        message = re.sub(r'\*([^*]+)\*', r'\1', message)
        
        # Remove any conventional commit prefix if present
        prefix_pattern = r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|break)(\([^)]+\))?:\s*'
        message = re.sub(prefix_pattern, '', message, flags=re.IGNORECASE)
        
        # Clean up extra whitespace
        message = re.sub(r'\s+', ' ', message).strip()
        
        # Ensure it's not empty
        if not message:
            return "update files"
        
        return message
    
    def _track_real_usage(self, prompt: str, response: str) -> None:
        """
        Track real AI usage for cost monitoring.
        
        Args:
            prompt (str): Prompt sent to AI
            response (str): Response received from AI
        """
        if not self.usage_tracker.is_tracking_enabled():
            return
        
        # Estimate tokens (rough calculation)
        prompt_tokens = len(prompt.split()) * 1.3  # Rough estimate
        response_tokens = len(response.split()) * 1.3
        
        total_tokens = int(prompt_tokens + response_tokens)
        
        # Estimate cost (Ollama local is free, but track for consistency)
        cost = 0.0  # Local Ollama is free
        
        # Track usage
        self.usage_tracker.increment_usage("ggai", total_tokens, cost)
