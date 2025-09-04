"""
Global test configuration and fixtures.
"""

import pytest
import sys
import os
from pathlib import Path

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def mock_click_style():
    """Mock click.style for testing color methods."""
    with pytest.mock.patch('click.style') as mock_style:
        mock_style.return_value = "styled_message"
        yield mock_style


@pytest.fixture
def mock_click_echo():
    """Mock click.echo for testing output methods."""
    with pytest.mock.patch('click.echo') as mock_echo:
        yield mock_echo


@pytest.fixture
def temp_config():
    """Temporary configuration for testing."""
    return {
        "version": "1.0",
        "git": {
            "default_branch": "main"
        },
        "ui": {
            "colors": {
                "success": "green",
                "error": "red",
                "warning": "yellow",
                "info": "blue"
            }
        }
    }
