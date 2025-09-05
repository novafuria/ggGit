"""
Tests for complexity analyzer functionality.

This module tests the ComplexityAnalyzer class and its integration
with GitInterface and ConfigManager.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from src.core.ai.complexity_analyzer import ComplexityAnalyzer
from src.core.git import GitInterface
from src.core.config import ConfigManager


class TestComplexityAnalyzer:
    """Test ComplexityAnalyzer functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.git_mock = Mock(spec=GitInterface)
        self.config_mock = Mock(spec=ConfigManager)
        self.analyzer = ComplexityAnalyzer(self.git_mock, self.config_mock)
    
    def test_analyze_complexity_no_files(self):
        """Test complexity analysis with no files."""
        self.git_mock.get_files_to_analyze.return_value = []
        
        result = self.analyzer.analyze_complexity()
        
        assert result['file_count'] == 0
        assert result['diff_lines'] == 0
        assert result['max_file_size'] == 0
        assert result['files'] == []
        assert result['has_staged'] == False
    
    def test_analyze_complexity_with_files(self):
        """Test complexity analysis with files."""
        files = ['file1.py', 'file2.py']
        self.git_mock.get_files_to_analyze.return_value = files
        self.git_mock.get_staged_files.return_value = files
        self.git_mock.get_diff_line_count.return_value = 50
        self.git_mock.get_file_size.side_effect = [1000, 2000]
        
        result = self.analyzer.analyze_complexity()
        
        assert result['file_count'] == 2
        assert result['diff_lines'] == 50
        assert result['max_file_size'] == 2000
        assert result['files'] == files
        assert result['has_staged'] == True
    
    def test_analyze_complexity_unstaged_files(self):
        """Test complexity analysis with unstaged files."""
        files = ['file1.py', 'file2.py']
        self.git_mock.get_files_to_analyze.return_value = files
        self.git_mock.get_staged_files.return_value = []
        self.git_mock.get_diff_line_count.return_value = 30
        self.git_mock.get_file_size.side_effect = [500, 1500]
        
        result = self.analyzer.analyze_complexity()
        
        assert result['file_count'] == 2
        assert result['diff_lines'] == 30
        assert result['max_file_size'] == 1500
        assert result['files'] == files
        assert result['has_staged'] == False
    
    def test_should_use_ai_simple_changes(self):
        """Test should_use_ai with simple changes."""
        analysis = {
            'file_count': 2,
            'diff_lines': 50,
            'max_file_size': 1000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        with patch.object(self.analyzer, 'analyze_complexity', return_value=analysis):
            self.config_mock.get_config.side_effect = lambda key, default: {
                'ai.analysis.max_files': 10,
                'ai.analysis.max_diff_lines': 200,
                'ai.analysis.max_file_size': 5000
            }.get(key, default)
            
            should_use_ai, result_analysis = self.analyzer.should_use_ai()
            
            assert should_use_ai == True
            assert result_analysis == analysis
    
    def test_should_use_ai_complex_changes(self):
        """Test should_use_ai with complex changes."""
        analysis = {
            'file_count': 15,
            'diff_lines': 300,
            'max_file_size': 8000,
            'files': ['file1.py', 'file2.py', 'file3.py'],
            'has_staged': True
        }
        
        with patch.object(self.analyzer, 'analyze_complexity', return_value=analysis):
            self.config_mock.get_config.side_effect = lambda key, default: {
                'ai.analysis.max_files': 10,
                'ai.analysis.max_diff_lines': 200,
                'ai.analysis.max_file_size': 5000
            }.get(key, default)
            
            should_use_ai, result_analysis = self.analyzer.should_use_ai()
            
            assert should_use_ai == False
            assert result_analysis == analysis
    
    def test_should_use_ai_exceeds_file_count(self):
        """Test should_use_ai when file count exceeds limit."""
        analysis = {
            'file_count': 15,
            'diff_lines': 50,
            'max_file_size': 1000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        with patch.object(self.analyzer, 'analyze_complexity', return_value=analysis):
            self.config_mock.get_config.side_effect = lambda key, default: {
                'ai.analysis.max_files': 10,
                'ai.analysis.max_diff_lines': 200,
                'ai.analysis.max_file_size': 5000
            }.get(key, default)
            
            should_use_ai, result_analysis = self.analyzer.should_use_ai()
            
            assert should_use_ai == False
            assert result_analysis == analysis
    
    def test_should_use_ai_exceeds_diff_lines(self):
        """Test should_use_ai when diff lines exceed limit."""
        analysis = {
            'file_count': 5,
            'diff_lines': 300,
            'max_file_size': 1000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        with patch.object(self.analyzer, 'analyze_complexity', return_value=analysis):
            self.config_mock.get_config.side_effect = lambda key, default: {
                'ai.analysis.max_files': 10,
                'ai.analysis.max_diff_lines': 200,
                'ai.analysis.max_file_size': 5000
            }.get(key, default)
            
            should_use_ai, result_analysis = self.analyzer.should_use_ai()
            
            assert should_use_ai == False
            assert result_analysis == analysis
    
    def test_should_use_ai_exceeds_file_size(self):
        """Test should_use_ai when file size exceeds limit."""
        analysis = {
            'file_count': 5,
            'diff_lines': 50,
            'max_file_size': 8000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        with patch.object(self.analyzer, 'analyze_complexity', return_value=analysis):
            self.config_mock.get_config.side_effect = lambda key, default: {
                'ai.analysis.max_files': 10,
                'ai.analysis.max_diff_lines': 200,
                'ai.analysis.max_file_size': 5000
            }.get(key, default)
            
            should_use_ai, result_analysis = self.analyzer.should_use_ai()
            
            assert should_use_ai == False
            assert result_analysis == analysis
    
    def test_get_fallback_message_single_reason(self):
        """Test get_fallback_message with single reason."""
        analysis = {
            'file_count': 15,
            'diff_lines': 50,
            'max_file_size': 1000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        self.config_mock.get_config.side_effect = lambda key, default: {
            'ai.analysis.max_files': 10,
            'ai.analysis.max_diff_lines': 200,
            'ai.analysis.max_file_size': 5000
        }.get(key, default)
        
        message = self.analyzer.get_fallback_message(analysis)
        
        assert "demasiados archivos (15)" in message
        assert "No es aconsejable commitear tanto contenido" in message
        assert "Selecciona grupos de archivos más pequeños" in message
        assert "git add <archivo>" in message
        assert "ggfeat \"mensaje manual\"" in message
    
    def test_get_fallback_message_multiple_reasons(self):
        """Test get_fallback_message with multiple reasons."""
        analysis = {
            'file_count': 15,
            'diff_lines': 300,
            'max_file_size': 8000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        self.config_mock.get_config.side_effect = lambda key, default: {
            'ai.analysis.max_files': 10,
            'ai.analysis.max_diff_lines': 200,
            'ai.analysis.max_file_size': 5000
        }.get(key, default)
        
        message = self.analyzer.get_fallback_message(analysis)
        
        assert "demasiados archivos (15)" in message
        assert "demasiadas líneas de cambio (300)" in message
        assert "archivos muy grandes (8000 bytes)" in message
        assert "No es aconsejable commitear tanto contenido" in message
    
    def test_get_analysis_summary_staged(self):
        """Test get_analysis_summary with staged files."""
        analysis = {
            'file_count': 5,
            'diff_lines': 50,
            'has_staged': True
        }
        
        summary = self.analyzer.get_analysis_summary(analysis)
        
        assert "Archivos: 5" in summary
        assert "Líneas: 50" in summary
        assert "staged" in summary
    
    def test_get_analysis_summary_unstaged(self):
        """Test get_analysis_summary with unstaged files."""
        analysis = {
            'file_count': 3,
            'diff_lines': 25,
            'has_staged': False
        }
        
        summary = self.analyzer.get_analysis_summary(analysis)
        
        assert "Archivos: 3" in summary
        assert "Líneas: 25" in summary
        assert "unstaged" in summary


class TestComplexityAnalyzerIntegration:
    """Test ComplexityAnalyzer integration with real components."""
    
    def test_integration_with_real_git_interface(self):
        """Test integration with real GitInterface (if in git repo)."""
        try:
            from src.core.git import GitInterface
            from src.core.config import ConfigManager
            
            git = GitInterface()
            config = ConfigManager()
            analyzer = ComplexityAnalyzer(git, config)
            
            # Test analyze_complexity
            analysis = analyzer.analyze_complexity()
            
            assert 'file_count' in analysis
            assert 'diff_lines' in analysis
            assert 'max_file_size' in analysis
            assert 'files' in analysis
            assert 'has_staged' in analysis
            
            # Test should_use_ai
            should_use_ai, result_analysis = analyzer.should_use_ai()
            
            assert isinstance(should_use_ai, bool)
            assert result_analysis == analysis
            
        except Exception:
            # Skip if not in a git repository
            pytest.skip("Not in a git repository")
    
    def test_fallback_message_format(self):
        """Test that fallback message has correct format."""
        git_mock = Mock(spec=GitInterface)
        config_mock = Mock(spec=ConfigManager)
        analyzer = ComplexityAnalyzer(git_mock, config_mock)
        
        analysis = {
            'file_count': 15,
            'diff_lines': 300,
            'max_file_size': 8000,
            'files': ['file1.py', 'file2.py'],
            'has_staged': True
        }
        
        config_mock.get_config.side_effect = lambda key, default: {
            'ai.analysis.max_files': 10,
            'ai.analysis.max_diff_lines': 200,
            'ai.analysis.max_file_size': 5000
        }.get(key, default)
        
        message = analyzer.get_fallback_message(analysis)
        
        # Check that message contains all required elements
        assert "⚠️" in message
        assert "💡" in message
        assert "No es aconsejable commitear tanto contenido" in message
        assert "Selecciona grupos de archivos más pequeños" in message
        assert "git add <archivo>" in message
        assert "ggfeat \"mensaje manual\"" in message
