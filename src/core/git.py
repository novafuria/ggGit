"""
Git interface module for ggGit.

This module provides a unified interface for Git operations
with error handling and consistent feedback.

The GitInterface class abstracts Git operations using subprocess calls
to maintain compatibility with the original Git behavior and error messages.
It provides a clean API for common Git operations while preserving
the native Git experience for users.

All methods return consistent types and handle errors gracefully,
providing meaningful feedback for debugging and user interaction.
"""

import subprocess
import os
import shutil
from typing import List, Optional, Dict, Any, Tuple
from pathlib import Path


class GitInterfaceError(Exception):
    """Excepción base para errores de GitInterface"""
    pass


class GitNotAvailableError(GitInterfaceError):
    """Git no está disponible en el sistema"""
    pass


class NotGitRepositoryError(GitInterfaceError):
    """No es un repositorio Git válido"""
    pass


class GitCommandError(GitInterfaceError):
    """Error al ejecutar comando Git"""
    pass


class GitInterface:
    """
    Unified interface for Git operations with error handling.
    
    This class provides a clean abstraction over Git operations using
    subprocess calls. It maintains compatibility with original Git
    behavior while providing consistent error handling and return types.
    
    All Git operations are executed in the current working directory
    and return structured data for easy consumption by command classes.
    
    Attributes:
        None: This class is stateless and doesn't maintain state
        
    Example:
        git = GitInterface()
        
        # Check if we're in a git repository
        if not git.is_git_repository():
            print("Not a git repository")
            return
        
        # Stage all changes
        if git.stage_all_changes():
            # Commit with message
            git.commit("feat: add new feature")
        
        # Get repository status
        status = git.get_repository_status()
        print(f"Current branch: {status['current_branch']}")
    """
    
    def __init__(self):
        """
        Initialize Git interface.
        
        This method sets up the Git interface. No state is maintained
        as all operations are stateless and work with the current
        working directory.
        
        Raises:
            GitNotAvailableError: If Git is not available in the system
        """
        # Verify Git is available
        if not shutil.which('git'):
            raise GitNotAvailableError(
                "Git no está disponible en el sistema. "
                "Por favor instala Git y asegúrate de que esté en el PATH."
            )
    
    def is_git_repository(self) -> bool:
        """
        Check if current directory is a Git repository.
        
        Verifies that the current directory is within a Git repository
        by checking for the .git directory or file.
        
        Returns:
            bool: True if current directory is a Git repository, False otherwise
        """
        try:
            # Check if .git directory or file exists
            git_path = Path('.git')
            if not git_path.exists():
                return False
            
            # Verify it's a valid Git repository by running git status
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, OSError):
            return False
    
    def stage_all_changes(self) -> bool:
        """
        Stage all changes in the repository.
        
        Equivalent to running 'git add .' - stages all modified and
        untracked files in the current directory and subdirectories.
        
        Returns:
            bool: True if staging was successful, False otherwise
            
        Raises:
            NotGitRepositoryError: If not in a Git repository
            GitCommandError: If git add command fails
        """
        if not self.is_git_repository():
            raise NotGitRepositoryError(
                "No es un repositorio Git válido. "
                "Ejecuta este comando desde un directorio con un repositorio Git inicializado."
            )
        
        try:
            result = subprocess.run(
                ['git', 'add', '.'],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                raise GitCommandError(
                    f"Error al ejecutar 'git add .': {result.stderr.strip()}"
                )
            
            return True
            
        except subprocess.TimeoutExpired:
            raise GitCommandError(
                "Timeout al ejecutar 'git add .'. "
                "El repositorio puede tener muchos archivos o estar en un estado inconsistente."
            )
        except subprocess.CalledProcessError as e:
            raise GitCommandError(
                f"Error al ejecutar 'git add .' (código {e.returncode}): {e.stderr.strip()}"
            )
    
    def stage_files(self, files: List[str]) -> bool:
        """
        Stage specific files.
        
        Stages only the specified files, equivalent to running
        'git add <file1> <file2> ...'.
        
        Args:
            files (List[str]): List of file paths to stage
            
        Returns:
            bool: True if all files were staged successfully, False otherwise
            
        Raises:
            NotGitRepositoryError: If not in a Git repository
            FileNotFoundError: If any file doesn't exist
            GitCommandError: If git add command fails
            
        Example:
            git.stage_files(['src/main.py', 'tests/test_main.py'])
        """
        if not self.is_git_repository():
            raise NotGitRepositoryError(
                "No es un repositorio Git válido. "
                "Ejecuta este comando desde un directorio con un repositorio Git inicializado."
            )
        
        if not files:
            raise ValueError("La lista de archivos no puede estar vacía")
        
        # Validate that all files exist
        for file_path in files:
            if not Path(file_path).exists():
                raise FileNotFoundError(f"El archivo '{file_path}' no existe")
        
        try:
            result = subprocess.run(
                ['git', 'add'] + files,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                raise GitCommandError(
                    f"Error al ejecutar 'git add': {result.stderr.strip()}"
                )
            
            return True
            
        except subprocess.TimeoutExpired:
            raise GitCommandError(
                "Timeout al ejecutar 'git add'. "
                "Los archivos pueden ser muy grandes o el repositorio estar en un estado inconsistente."
            )
        except subprocess.CalledProcessError as e:
            raise GitCommandError(
                f"Error al ejecutar 'git add' (código {e.returncode}): {e.stderr.strip()}"
            )
    
    def commit(self, message: str) -> bool:
        """
        Commit changes with the given message.
        
        Creates a new commit with the staged changes and the provided
        message. Equivalent to running 'git commit -m "<message>"'.
        
        Args:
            message (str): Commit message
            
        Returns:
            bool: True if commit was successful, False otherwise
            
        Raises:
            NotGitRepositoryError: If not in a Git repository
            ValueError: If message is empty or invalid
            GitCommandError: If git commit command fails
            
        Example:
            git.commit("feat: add user authentication")
        """
        if not self.is_git_repository():
            raise NotGitRepositoryError(
                "No es un repositorio Git válido. "
                "Ejecuta este comando desde un directorio con un repositorio Git inicializado."
            )
        
        if not message or not message.strip():
            raise ValueError("El mensaje de commit no puede estar vacío")
        
        # Check if there are staged changes
        staged_files = self.get_staged_files()
        if not staged_files:
            raise GitCommandError(
                "No hay cambios staged para hacer commit. "
                "Usa 'git add' para stagear archivos antes de hacer commit."
            )
        
        try:
            result = subprocess.run(
                ['git', 'commit', '-m', message.strip()],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                raise GitCommandError(
                    f"Error al ejecutar 'git commit': {result.stderr.strip()}"
                )
            
            return True
            
        except subprocess.TimeoutExpired:
            raise GitCommandError(
                "Timeout al ejecutar 'git commit'. "
                "El repositorio puede estar en un estado inconsistente."
            )
        except subprocess.CalledProcessError as e:
            raise GitCommandError(
                f"Error al ejecutar 'git commit' (código {e.returncode}): {e.stderr.strip()}"
            )
    
    def get_current_branch(self) -> Optional[str]:
        """
        Get current branch name.
        
        Returns the name of the currently checked out branch.
        Equivalent to running 'git branch --show-current'.
        
        Returns:
            Optional[str]: Current branch name, or None if not in a repository
                          or in detached HEAD state
        """
        if not self.is_git_repository():
            return None
        
        try:
            result = subprocess.run(
                ['git', 'branch', '--show-current'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return None
            
            branch_name = result.stdout.strip()
            return branch_name if branch_name else None
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, OSError):
            return None
    
    def get_staged_files(self) -> List[str]:
        """
        Get list of staged files.
        
        Returns a list of files that are currently staged for commit.
        Equivalent to running 'git diff --cached --name-only'.
        
        Returns:
            List[str]: List of staged file paths
        """
        if not self.is_git_repository():
            return []
        
        try:
            result = subprocess.run(
                ['git', 'diff', '--cached', '--name-only'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return []
            
            # Parse output and return list of files
            files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            return files
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, OSError):
            return []
    
    def get_unstaged_files(self) -> List[str]:
        """
        Get list of unstaged files.
        
        Returns a list of files that have been modified but not staged.
        Equivalent to running 'git diff --name-only'.
        
        Returns:
            List[str]: List of unstaged file paths
        """
        if not self.is_git_repository():
            return []
        
        try:
            # Get modified files
            diff_result = subprocess.run(
                ['git', 'diff', '--name-only'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            # Get untracked files
            untracked_result = subprocess.run(
                ['git', 'ls-files', '--others', '--exclude-standard'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            files = []
            
            # Add modified files
            if diff_result.returncode == 0:
                files.extend([line.strip() for line in diff_result.stdout.splitlines() if line.strip()])
            
            # Add untracked files
            if untracked_result.returncode == 0:
                files.extend([line.strip() for line in untracked_result.stdout.splitlines() if line.strip()])
            
            return files
            
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, OSError):
            return []
    
    def get_repository_status(self) -> Dict[str, Any]:
        """
        Get complete repository status.
        
        Returns a comprehensive status of the repository including
        current branch, staged files, unstaged files, and untracked files.
        Equivalent to parsing 'git status --porcelain'.
        
        Returns:
            Dict[str, Any]: Repository status with keys:
                - current_branch: Current branch name
                - staged_files: List of staged files
                - unstaged_files: List of unstaged files
                - untracked_files: List of untracked files
                - is_clean: Boolean indicating if working tree is clean
                
        Example:
            status = git.get_repository_status()
            print(f"Branch: {status['current_branch']}")
            print(f"Staged: {len(status['staged_files'])} files")
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement git status --porcelain parsing
        # 1. Verify we're in a git repository
        # 2. Execute 'git status --porcelain' command
        # 3. Parse output to extract file statuses
        # 4. Return structured status dictionary
        return {}
    
    def get_commit_history(self, limit: int = 10) -> List[Dict[str, str]]:
        """
        Get recent commit history.
        
        Returns a list of recent commits with their metadata.
        Equivalent to running 'git log --oneline -n <limit>'.
        
        Args:
            limit (int): Maximum number of commits to return
            
        Returns:
            List[Dict[str, str]]: List of commit dictionaries with keys:
                - hash: Short commit hash
                - message: Commit message
                - author: Author name
                - date: Commit date
                
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement git log functionality
        # 1. Verify we're in a git repository
        # 2. Execute 'git log --oneline -n <limit>' command
        # 3. Parse output to extract commit information
        # 4. Return list of commit dictionaries
        return []
    
    def create_branch(self, branch_name: str, start_point: Optional[str] = None) -> bool:
        """
        Create a new branch.
        
        Creates a new branch from the specified start point or current HEAD.
        Equivalent to running 'git branch <branch_name> [<start_point>]'.
        
        Args:
            branch_name (str): Name of the new branch
            start_point (Optional[str]): Starting point for the branch
            
        Returns:
            bool: True if branch was created successfully, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            ValueError: If branch name is invalid
            subprocess.CalledProcessError: If git branch command fails
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement git branch creation
        # 1. Verify we're in a git repository
        # 2. Validate branch name
        # 3. Execute 'git branch <name> [<start>]' command
        # 4. Handle errors and return result
        return True
    
    def switch_branch(self, branch_name: str) -> bool:
        """
        Switch to a different branch.
        
        Switches to the specified branch. Equivalent to running
        'git checkout <branch_name>' or 'git switch <branch_name>'.
        
        Args:
            branch_name (str): Name of the branch to switch to
            
        Returns:
            bool: True if switch was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            ValueError: If branch doesn't exist
            subprocess.CalledProcessError: If git checkout/switch command fails
            
        Note:
            This method will be implemented in STORY-1.2.3 - comandos base
        """
        # TODO: Implement git branch switching
        # 1. Verify we're in a git repository
        # 2. Check if branch exists
        # 3. Execute 'git switch <branch>' command
        # 4. Handle errors and return result
        return True
