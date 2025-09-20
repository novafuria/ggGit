"""
Complexity analyzer for ggGit.

This module provides functionality to analyze the complexity of changes
and decide whether to use AI for commit message generation or show
educational fallback messages.
"""

from typing import List, Dict, Any, Tuple
from ..git import GitInterface
from ..config import ConfigManager
from ..utils.colors import ColorManager


class ComplexityAnalyzer:
    """
    Analyzes complexity of changes to decide between AI and fallback.
    
    This class analyzes the complexity of current changes based on
    configurable criteria and decides whether to use AI for commit
    message generation or show educational fallback messages.
    
    Attributes:
        git (GitInterface): Git operations interface
        config (ConfigManager): Configuration management instance
        
    Example:
        analyzer = ComplexityAnalyzer(git_interface, config_manager)
        should_use_ai, analysis = analyzer.should_use_ai()
        
        if should_use_ai:
            # Use AI for commit message generation
            pass
        else:
            # Show educational fallback
            fallback_message = analyzer.get_fallback_message(analysis)
            print(fallback_message)
    """
    
    def __init__(self, git_interface: GitInterface, config_manager: ConfigManager):
        """
        Initialize complexity analyzer.
        
        Args:
            git_interface (GitInterface): Git operations interface
            config_manager (ConfigManager): Configuration management instance
        """
        self.git = git_interface
        self.config = config_manager
    
    def analyze_complexity(self) -> Dict[str, Any]:
        """
        Analyze complexity of current changes.
        
        Analyzes the complexity of current changes by examining:
        - Number of files modified
        - Number of lines in diff
        - Size of largest file modified
        
        Returns:
            Dict[str, Any]: Analysis results with metrics:
                - file_count: Number of files modified
                - diff_lines: Number of lines in diff
                - max_file_size: Size of largest file in bytes
                - files: List of files modified
                - has_staged: Whether there are staged files
        """
        # Get files to analyze
        files = self.git.get_files_to_analyze()
        
        if not files:
            return {
                'file_count': 0,
                'diff_lines': 0,
                'max_file_size': 0,
                'files': [],
                'has_staged': False
            }
        
        # Check if there are staged files
        staged_files = self.git.get_staged_files()
        has_staged = len(staged_files) > 0
        
        # Get diff line count
        diff_lines = self.git.get_diff_line_count(files, staged=has_staged)
        
        # Get file sizes
        file_sizes = []
        for file_path in files:
            try:
                size = self.git.get_file_size(file_path)
                file_sizes.append(size)
            except OSError:
                # Skip files that can't be accessed
                continue
        
        max_file_size = max(file_sizes) if file_sizes else 0
        
        return {
            'file_count': len(files),
            'diff_lines': diff_lines,
            'max_file_size': max_file_size,
            'files': files,
            'has_staged': has_staged
        }
    
    def should_use_ai(self) -> Tuple[bool, Dict[str, Any]]:
        """
        Decide if AI should be used based on complexity analysis.
        
        Analyzes the complexity of current changes and decides whether
        to use AI for commit message generation or show educational
        fallback messages.
        
        Returns:
            Tuple[bool, Dict[str, Any]]: 
                - bool: True if AI should be used, False for fallback
                - Dict: Analysis results for further processing
        """
        analysis = self.analyze_complexity()
        
        # Always use AI - removed complexity limits for better user experience
        # Cost control is handled by ai.cost_limit in configuration
        return True, analysis
    
    def get_fallback_message(self, analysis: Dict[str, Any]) -> str:
        """
        Get educational fallback message for complex changes.
        
        Generates an educational message that teaches good Git practices
        when changes are too complex for AI analysis.
        
        Args:
            analysis (Dict[str, Any]): Analysis results from analyze_complexity()
            
        Returns:
            str: Educational fallback message
        """
        file_count = analysis['file_count']
        diff_lines = analysis['diff_lines']
        max_file_size = analysis['max_file_size']
        
        # Build specific feedback based on what exceeded limits
        reasons = []
        if file_count > self.config.get_config('ai.analysis.max_files', 10):
            reasons.append(f"demasiados archivos ({file_count})")
        if diff_lines > self.config.get_config('ai.analysis.max_diff_lines', 200):
            reasons.append(f"demasiadas líneas de cambio ({diff_lines})")
        if max_file_size > self.config.get_config('ai.analysis.max_file_size', 5000):
            reasons.append(f"archivos muy grandes ({max_file_size} bytes)")
        
        reason_text = ", ".join(reasons)
        
        return f"""⚠️ No es aconsejable commitear tanto contenido ({reason_text})
💡 Sugerencia: Selecciona grupos de archivos más pequeños
   Usa 'git add <archivo>' para archivos específicos
   O 'ggfeat "mensaje manual"' para commit completo"""
    
    def get_analysis_summary(self, analysis: Dict[str, Any]) -> str:
        """
        Get a summary of the analysis for display.
        
        Generates a user-friendly summary of the complexity analysis
        for display in the CLI.
        
        Args:
            analysis (Dict[str, Any]): Analysis results from analyze_complexity()
            
        Returns:
            str: Analysis summary for display
        """
        file_count = analysis['file_count']
        diff_lines = analysis['diff_lines']
        has_staged = analysis['has_staged']
        
        status = "staged" if has_staged else "unstaged"
        
        return f"📝 Archivos: {file_count}, Líneas: {diff_lines} ({status})"
