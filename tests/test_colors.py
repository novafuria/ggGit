"""
Tests for ColorManager module.
"""

import pytest
from unittest.mock import patch
from src.core.utils.colors import ColorManager


class TestColorManager:
    """Test cases for ColorManager class."""
    
    def test_success_message(self):
        """Test success message formatting."""
        message = "Test success"
        result = ColorManager.success(message)
        assert "✅" in result
        assert message in result
    
    def test_error_message(self):
        """Test error message formatting."""
        message = "Test error"
        result = ColorManager.error(message)
        assert "❌" in result
        assert message in result
    
    def test_warning_message(self):
        """Test warning message formatting."""
        message = "Test warning"
        result = ColorManager.warning(message)
        assert "⚠️" in result
        assert message in result
    
    def test_info_message(self):
        """Test info message formatting."""
        message = "Test info"
        result = ColorManager.info(message)
        assert "ℹ️" in result
        assert message in result
    
    def test_operation_message(self):
        """Test operation message formatting."""
        message = "Test operation"
        result = ColorManager.operation(message)
        assert "🔄" in result
        assert message in result
    
    def test_highlight_message(self):
        """Test highlight message formatting."""
        message = "Test highlight"
        result = ColorManager.highlight(message)
        assert message in result
    
    def test_dim_message(self):
        """Test dim message formatting."""
        message = "Test dim"
        result = ColorManager.dim(message)
        assert message in result
    
    @patch('click.style')
    def test_success_uses_click_style(self, mock_style):
        """Test that success method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.success(message)
        
        mock_style.assert_called_once_with(f"✅ {message}", fg="green")
    
    @patch('click.style')
    def test_error_uses_click_style(self, mock_style):
        """Test that error method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.error(message)
        
        mock_style.assert_called_once_with(f"❌ {message}", fg="red")
    
    @patch('click.style')
    def test_warning_uses_click_style(self, mock_style):
        """Test that warning method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.warning(message)
        
        mock_style.assert_called_once_with(f"⚠️ {message}", fg="yellow")
    
    @patch('click.style')
    def test_info_uses_click_style(self, mock_style):
        """Test that info method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.info(message)
        
        mock_style.assert_called_once_with(f"ℹ️ {message}", fg="blue")
    
    @patch('click.style')
    def test_operation_uses_click_style(self, mock_style):
        """Test that operation method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.operation(message)
        
        mock_style.assert_called_once_with(f"🔄 {message}", fg="cyan")
    
    @patch('click.style')
    def test_highlight_uses_click_style(self, mock_style):
        """Test that highlight method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.highlight(message)
        
        mock_style.assert_called_once_with(message, bold=True)
    
    @patch('click.style')
    def test_dim_uses_click_style(self, mock_style):
        """Test that dim method uses click.style with correct parameters."""
        mock_style.return_value = "styled message"
        message = "Test message"
        
        ColorManager.dim(message)
        
        mock_style.assert_called_once_with(message, dim=True)
