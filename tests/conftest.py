"""
Global test configuration and fixtures for ggGit.

This module provides comprehensive test fixtures and utilities
for testing ggGit components. It includes mocks for external
dependencies, test data generators, and helper functions for
common testing patterns.

The fixtures are organized by functionality:
- Mock fixtures for external dependencies (click, subprocess, etc.)
- Test data fixtures for common objects
- Helper fixtures for testing patterns
- Integration test fixtures for end-to-end testing
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock, Mock, patch

import pytest

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import ggGit components for testing
from src.core.base_commands.base import BaseCommand
from src.core.config import ConfigManager
from src.core.git import GitInterface
from src.core.utils.colors import ColorManager
from src.core.utils.logging import LoggingManager
from src.core.validation import ArgumentValidator


@pytest.fixture(autouse=True)
def prevent_accidental_git_commits(monkeypatch):
    """
    Global protection to prevent accidental git operations on the host repository.

    This fixture ensures that if a mock fails or is missing in a test,
    any direct `subprocess.run` that attempts to modify git state
    (commit, checkout, branch) will be intercepted and raise an error,
    except if it's explicitly allowed in the isolated temp_git_repo fixture.
    """
    original_run = subprocess.run

    def guarded_run(*args, **kwargs):
        command_args = args[0] if args else kwargs.get("args", [])

        # If the command is a list and starts with 'git'
        if (
            isinstance(command_args, list)
            and len(command_args) > 0
            and command_args[0] == "git"
        ):

            # Allow read-only or harmless commands if they leak (though they should be mocked)
            dangerous_cmds = [
                "commit",
                "add",
                "checkout",
                "branch",
                "merge",
                "reset",
                "push",
                "pull",
                "revert",
            ]

            # Check if this command is trying to modify state
            if len(command_args) > 1 and command_args[1] in dangerous_cmds:

                # Check if it's running inside our isolated temp directory
                cwd = kwargs.get("cwd") or os.getcwd()
                if not cwd or "tmp" not in str(cwd):
                    # We are in the host repository and a mock failed!
                    # Prevent the execution to save the host git state
                    raise RuntimeError(
                        f"SECURITY: A test attempted to run real '{command_args}' on the host repo. "
                        f"Missing mock detected!"
                    )

        return original_run(*args, **kwargs)

    monkeypatch.setattr(subprocess, "run", guarded_run)


# ============================================================================
# Mock Fixtures for External Dependencies
# ============================================================================


@pytest.fixture
def mock_click_style():
    """Mock click.style for testing color methods."""
    with patch("click.style") as mock_style:
        mock_style.return_value = "styled_message"
        yield mock_style


@pytest.fixture
def mock_click_echo():
    """Mock click.echo for testing output methods."""
    with patch("click.echo") as mock_echo:
        yield mock_echo


@pytest.fixture
def mock_subprocess():
    """Mock subprocess for testing Git operations."""
    with patch("subprocess.run") as mock_run:
        # Default successful response
        mock_run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0, stdout=b"success", stderr=b""
        )
        yield mock_run


@pytest.fixture
def mock_pathlib_home():
    """Mock Path.home() for testing path operations."""
    with patch("pathlib.Path.home") as mock_home:
        mock_home.return_value = Path("/mock/home")
        yield mock_home


@pytest.fixture
def mock_logging():
    """Mock logging module for testing LoggingManager."""
    with patch("logging.getLogger") as mock_get_logger, patch(
        "logging.basicConfig"
    ) as mock_basic_config, patch("logging.FileHandler") as mock_file_handler, patch(
        "logging.StreamHandler"
    ) as mock_stream_handler:

        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger

        yield {
            "get_logger": mock_get_logger,
            "basic_config": mock_basic_config,
            "file_handler": mock_file_handler,
            "stream_handler": mock_stream_handler,
            "logger": mock_logger,
        }


# ============================================================================
# Test Data Fixtures
# ============================================================================


@pytest.fixture
def sample_config_data():
    """Sample configuration data for testing."""
    return {
        "commit": {"format": "conventional", "auto_stage": True, "max_length": 72},
        "git": {"auto_stage": True, "default_branch": "main"},
        "ui": {"colors": {"enabled": True, "theme": "default"}},
    }


@pytest.fixture
def sample_git_status():
    """Sample Git status data for testing."""
    return {
        "current_branch": "feature/new-feature",
        "staged_files": ["src/main.py", "tests/test_main.py"],
        "unstaged_files": ["README.md"],
        "untracked_files": ["new_file.txt"],
        "is_clean": False,
    }


@pytest.fixture
def sample_commit_history():
    """Sample commit history for testing."""
    return [
        {
            "hash": "abc1234",
            "message": "feat: add new feature",
            "author": "Test User",
            "date": "2024-01-15 10:30:00",
        },
        {
            "hash": "def5678",
            "message": "fix: resolve bug in validation",
            "author": "Test User",
            "date": "2024-01-14 15:45:00",
        },
    ]


@pytest.fixture
def sample_validation_data():
    """Sample validation data for testing."""
    return {
        "valid_commit_messages": [
            "feat: add new feature",
            "fix: resolve bug",
            "docs: update README",
            "feat(auth): add user authentication",
        ],
        "invalid_commit_messages": ["", "a" * 100, "invalid format"],  # Too long
        "valid_scopes": ["auth", "ui", "api", "test"],
        "invalid_scopes": ["Auth", "UI-COMPONENT", "api_", "test@"],
    }


# ============================================================================
# Component Fixtures
# ============================================================================


@pytest.fixture
def config_manager():
    """Create a ConfigManager instance for testing."""
    return ConfigManager()


@pytest.fixture
def git_interface():
    """Create a GitInterface instance for testing."""
    return GitInterface()


@pytest.fixture
def argument_validator():
    """Create an ArgumentValidator instance for testing."""
    return ArgumentValidator()


@pytest.fixture
def color_manager():
    """Create a ColorManager instance for testing."""
    return ColorManager()


@pytest.fixture
def logging_manager():
    """Create a LoggingManager instance for testing."""
    return LoggingManager()


@pytest.fixture
def concrete_command():
    """Create a concrete BaseCommand implementation for testing."""

    class ConcreteCommand(BaseCommand):
        def execute(self, *args, **kwargs) -> int:
            return 0

    return ConcreteCommand()


# ============================================================================
# Temporary Directory Fixtures
# ============================================================================


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def temp_git_repo(temp_dir):
    """Create a temporary Git repository for testing."""
    repo_path = temp_dir / "test_repo"
    repo_path.mkdir()

    # Initialize git repository
    subprocess.run(["git", "init"], cwd=repo_path, check=True)

    # Set up basic git config
    subprocess.run(
        ["git", "config", "user.name", "Test User"], cwd=repo_path, check=True
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"], cwd=repo_path, check=True
    )

    yield repo_path


# ============================================================================
# Helper Fixtures
# ============================================================================


@pytest.fixture
def mock_file_system(temp_dir):
    """Mock file system operations for testing."""
    with patch("pathlib.Path.exists") as mock_exists, patch(
        "pathlib.Path.mkdir"
    ) as mock_mkdir, patch("pathlib.Path.open") as mock_open:

        mock_exists.return_value = True
        mock_mkdir.return_value = None

        yield {"exists": mock_exists, "mkdir": mock_mkdir, "open": mock_open}


@pytest.fixture
def capture_output():
    """Capture stdout and stderr for testing."""
    import contextlib
    import io

    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(
        stderr_capture
    ):
        yield {"stdout": stdout_capture, "stderr": stderr_capture}


# ============================================================================
# Integration Test Fixtures
# ============================================================================


@pytest.fixture
def integration_test_env(temp_git_repo, sample_config_data):
    """Set up integration test environment."""
    # Create config files
    config_dir = temp_git_repo / ".gggit"
    config_dir.mkdir()

    # Create sample config file
    config_file = config_dir / "repo-config.yaml"
    config_file.write_text("commit:\n  format: conventional\n")

    return {
        "repo_path": temp_git_repo,
        "config_dir": config_dir,
        "config_file": config_file,
    }


# ============================================================================
# Test Utilities
# ============================================================================


class TestHelpers:
    """Helper class with utility methods for testing."""

    @staticmethod
    def create_mock_git_output(stdout: str = "", stderr: str = "", returncode: int = 0):
        """Create a mock subprocess.CompletedProcess for Git operations."""
        return subprocess.CompletedProcess(
            args=[],
            returncode=returncode,
            stdout=stdout.encode() if stdout else b"",
            stderr=stderr.encode() if stderr else b"",
        )

    @staticmethod
    def assert_command_info(command: BaseCommand, expected_keys: List[str]):
        """Assert that command has expected info keys."""
        info = command.get_command_info()
        for key in expected_keys:
            assert key in info, f"Expected key '{key}' not found in command info"

    @staticmethod
    def create_test_files(directory: Path, files: Dict[str, str]):
        """Create test files in a directory."""
        for file_path, content in files.items():
            file_obj = directory / file_path
            file_obj.parent.mkdir(parents=True, exist_ok=True)
            file_obj.write_text(content)


@pytest.fixture
def test_helpers():
    """Provide TestHelpers utility class."""
    return TestHelpers


@pytest.fixture(autouse=True)
def clean_logging_handlers():
    """Ensure all logging handlers are closed after each test to prevent I/O errors."""
    yield
    import logging

    # Close all handlers on the gggit root logger
    root_logger = logging.getLogger("gggit")
    for handler in list(root_logger.handlers):
        handler.close()
        root_logger.removeHandler(handler)

    # Also clean up standard library root logger just in case
    for handler in list(logging.root.handlers):
        handler.close()
        logging.root.removeHandler(handler)


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests for individual components")
    config.addinivalue_line(
        "markers", "integration: Integration tests for component interaction"
    )
    config.addinivalue_line("markers", "slow: Slow tests that may take longer to run")
    config.addinivalue_line("markers", "git: Tests that require Git operations")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Add unit marker to tests in test_* files
        if item.name.startswith("test_") and "integration" not in item.name:
            item.add_marker(pytest.mark.unit)

        # Add git marker to tests that use git fixtures
        if "git" in item.name or "temp_git_repo" in str(item.funcargs):
            item.add_marker(pytest.mark.git)
