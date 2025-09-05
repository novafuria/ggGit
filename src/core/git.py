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
    
    def diff(self, files: Optional[List[str]] = None, staged: bool = False) -> bool:
        """
        Show git diff with colors.
        
        Shows the differences between working tree and index, or between
        index and HEAD. Equivalent to running 'git diff [--staged] [<files>]'.
        
        Args:
            files (Optional[List[str]]): Specific files to show diff for
            staged (bool): If True, show staged changes (--staged)
            
        Returns:
            bool: True if diff was shown successfully, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git diff command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'diff']
            if staged:
                cmd.append('--staged')
            if files:
                cmd.extend(files)
            
            result = subprocess.run(cmd, capture_output=False, text=True)
            return result.returncode == 0
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git diff failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in diff: {e}")
    
    def get_diff_content(self, files: Optional[List[str]] = None, staged: bool = False) -> str:
        """
        Get diff content as string for analysis.
        
        Gets the diff content between working tree and index, or between
        index and HEAD. Equivalent to running 'git diff [--staged] [<files>]'.
        
        Args:
            files (Optional[List[str]]): Specific files to get diff for
            staged (bool): If True, get staged changes (--staged)
            
        Returns:
            str: Diff content as string, empty string if no changes
            
        Raises:
            NotGitRepositoryError: If not in a Git repository
            GitCommandError: If git diff command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'diff']
            if staged:
                cmd.append('--staged')
            if files:
                cmd.extend(files)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git diff failed: {result.stderr}")
            
            return result.stdout
            
        except subprocess.TimeoutExpired:
            raise GitCommandError("Git diff timed out")
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git diff failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_diff_content: {e}")
    
    def get_diff_line_count(self, files: Optional[List[str]] = None, staged: bool = False) -> int:
        """
        Get number of lines in diff for complexity analysis.
        
        Counts the number of lines in the diff output, excluding context lines
        and focusing on actual changes (additions and deletions).
        
        Args:
            files (Optional[List[str]]): Specific files to count diff lines for
            staged (bool): If True, count staged changes (--staged)
            
        Returns:
            int: Number of lines in diff, 0 if no changes
            
        Raises:
            NotGitRepositoryError: If not in a Git repository
            GitCommandError: If git diff command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'diff', '--numstat']
            if staged:
                cmd.append('--staged')
            if files:
                cmd.extend(files)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git diff --numstat failed: {result.stderr}")
            
            # Parse numstat output to count lines
            total_lines = 0
            for line in result.stdout.splitlines():
                if line.strip():
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        try:
                            added = int(parts[0]) if parts[0] != '-' else 0
                            deleted = int(parts[1]) if parts[1] != '-' else 0
                            total_lines += added + deleted
                        except ValueError:
                            continue
            
            return total_lines
            
        except subprocess.TimeoutExpired:
            raise GitCommandError("Git diff --numstat timed out")
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git diff --numstat failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_diff_line_count: {e}")
    
    def get_file_size(self, file_path: str) -> int:
        """
        Get file size in bytes for complexity analysis.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            int: File size in bytes, 0 if file doesn't exist
            
        Raises:
            OSError: If file cannot be accessed
        """
        try:
            if not os.path.exists(file_path):
                return 0
            
            return os.path.getsize(file_path)
            
        except OSError as e:
            raise OSError(f"Cannot get size for file {file_path}: {e}")
    
    def get_files_to_analyze(self) -> List[str]:
        """
        Get files to analyze (staged if available, otherwise unstaged).
        
        Returns staged files if any are staged, otherwise returns unstaged files.
        This follows the UX pattern where staged files take priority.
        
        Returns:
            List[str]: List of files to analyze
        """
        # First check for staged files
        staged_files = self.get_staged_files()
        if staged_files:
            return staged_files
        
        # If no staged files, return unstaged files
        return self.get_unstaged_files()
    
    def unstage_files(self, files: Optional[List[str]] = None) -> bool:
        """
        Unstage files from index.
        
        Removes files from the staging area. Equivalent to running
        'git reset HEAD [<files>]' or 'git restore --staged [<files>]'.
        
        Args:
            files (Optional[List[str]]): Specific files to unstage, None for all
            
        Returns:
            bool: True if files were unstaged successfully, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git reset command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'reset', 'HEAD']
            if files:
                cmd.extend(files)
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git unstage failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in unstage_files: {e}")
    
    def reset_hard(self) -> bool:
        """
        Reset --hard HEAD.
        
        Resets the working tree and index to match HEAD.
        Equivalent to running 'git reset --hard HEAD'.
        
        Returns:
            bool: True if reset was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git reset command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'reset', '--hard', 'HEAD']
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git reset --hard failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in reset_hard: {e}")
    
    def pull(self, remote: Optional[str] = None, branch: Optional[str] = None) -> bool:
        """
        Pull from remote repository.
        
        Fetches and merges changes from the remote repository.
        Equivalent to running 'git pull [<remote>] [<branch>]'.
        
        Args:
            remote (Optional[str]): Remote name to pull from
            branch (Optional[str]): Branch name to pull
            
        Returns:
            bool: True if pull was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git pull command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'pull']
            if remote:
                cmd.append(remote)
            if branch:
                cmd.append(branch)
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git pull failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in pull: {e}")
    
    def push(self, remote: Optional[str] = None, branch: Optional[str] = None) -> bool:
        """
        Push to remote repository.
        
        Pushes changes to the remote repository.
        Equivalent to running 'git push [<remote>] [<branch>]'.
        
        Args:
            remote (Optional[str]): Remote name to push to
            branch (Optional[str]): Branch name to push
            
        Returns:
            bool: True if push was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git push command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'push']
            if remote:
                cmd.append(remote)
            if branch:
                cmd.append(branch)
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git push failed: {e}")
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in push: {e}")
    
    def get_version(self) -> str:
        """
        Get Git version.
        
        Returns the version of Git installed on the system.
        Equivalent to running 'git --version'.
        
        Returns:
            str: Git version string
            
        Raises:
            GitNotAvailableError: If Git is not available
            subprocess.CalledProcessError: If git --version command fails
        """
        try:
            result = subprocess.run(['git', '--version'], capture_output=True, text=True)
            if result.returncode != 0:
                raise GitNotAvailableError("Git is not available")
            return result.stdout.strip()
            
        except FileNotFoundError:
            raise GitNotAvailableError("Git is not installed")
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git version command failed: {e}")
        except GitNotAvailableError:
            # Re-raise GitNotAvailableError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_version: {e}")
    
    def get_branches(self) -> List[str]:
        """
        Get list of local branches.
        
        Returns a list of local branch names.
        Equivalent to running 'git branch --format="%(refname:short)"'.
        
        Returns:
            List[str]: List of local branch names
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git branch command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'branch', '--format=%(refname:short)']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git branch command failed: {result.stderr}")
            
            branches = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
            return branches
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git branch failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_branches: {e}")
    
    def get_remote_branches(self) -> List[str]:
        """
        Get list of remote branches.
        
        Returns a list of remote branch names.
        Equivalent to running 'git branch -r --format="%(refname:short)"'.
        
        Returns:
            List[str]: List of remote branch names
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git branch command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'branch', '-r', '--format=%(refname:short)']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git branch -r command failed: {result.stderr}")
            
            branches = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
            # Filter out HEAD reference
            branches = [branch for branch in branches if not branch.endswith('/HEAD')]
            return branches
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git branch -r failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_remote_branches: {e}")
    
    def get_all_branches(self) -> Dict[str, List[str]]:
        """
        Get all branches (local and remote).
        
        Returns a dictionary with local and remote branches.
        
        Returns:
            Dict[str, List[str]]: Dictionary with 'local' and 'remote' keys
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git branch commands fail
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            local_branches = self.get_branches()
            remote_branches = self.get_remote_branches()
            
            return {
                "local": local_branches,
                "remote": remote_branches
            }
            
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_all_branches: {e}")
    
    def merge_branch(self, branch_name: str) -> bool:
        """
        Merge branch into current branch.
        
        Merges the specified branch into the current branch.
        Equivalent to running 'git merge <branch_name>'.
        
        Args:
            branch_name (str): Name of the branch to merge
            
        Returns:
            bool: True if merge was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git merge command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'merge', branch_name]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git merge failed: {result.stderr}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git merge failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in merge_branch: {e}")
    
    def merge_abort(self) -> bool:
        """
        Abort current merge.
        
        Aborts the current merge operation.
        Equivalent to running 'git merge --abort'.
        
        Returns:
            bool: True if abort was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git merge --abort command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'merge', '--abort']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git merge --abort failed: {result.stderr}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git merge --abort failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in merge_abort: {e}")
    
    def merge_continue(self) -> bool:
        """
        Continue current merge.
        
        Continues the current merge operation.
        Equivalent to running 'git merge --continue'.
        
        Returns:
            bool: True if continue was successful, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git merge --continue command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            cmd = ['git', 'merge', '--continue']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git merge --continue failed: {result.stderr}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git merge --continue failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in merge_continue: {e}")
    
    def get_mergeable_branches(self) -> List[str]:
        """
        Get list of branches that can be merged.
        
        Returns a list of local branches that can be merged into the current branch.
        Excludes the current branch and remote branches.
        
        Returns:
            List[str]: List of branch names that can be merged
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            # Get current branch
            current_branch = self.get_current_branch()
            if not current_branch:
                return []
            
            # Get all local branches
            local_branches = self.get_branches()
            
            # Filter out current branch and remote branches
            mergeable_branches = []
            for branch in local_branches:
                if branch != current_branch and not branch.startswith('origin/'):
                    mergeable_branches.append(branch)
            
            return mergeable_branches
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git command failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_mergeable_branches: {e}")
    
    def get_branch_info(self, branch_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a branch.
        
        Args:
            branch_name (str): Name of the branch
            
        Returns:
            Dict[str, Any]: Dictionary with branch information
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            # Get branch information
            cmd = ['git', 'show-branch', '--sha1-name', branch_name]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise GitCommandError(f"Git show-branch failed: {result.stderr}")
            
            # Get last commit info
            cmd = ['git', 'log', '--oneline', '-1', branch_name]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            last_commit = result.stdout.strip() if result.returncode == 0 else "Unknown"
            
            # Get branch status
            cmd = ['git', 'branch', '-v']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            branch_status = "Unknown"
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if branch_name in line:
                        branch_status = line.strip()
                        break
            
            return {
                "name": branch_name,
                "last_commit": last_commit,
                "status": branch_status,
                "exists": True
            }
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git command failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in get_branch_info: {e}")
    
    def is_branch_mergeable(self, branch_name: str) -> bool:
        """
        Check if branch can be merged.
        
        Args:
            branch_name (str): Name of the branch to check
            
        Returns:
            bool: True if branch can be merged, False otherwise
            
        Raises:
            RuntimeError: If not in a Git repository
            subprocess.CalledProcessError: If git command fails
        """
        try:
            if not self.is_git_repository():
                raise NotGitRepositoryError("Not a git repository")
            
            # Check if branch exists
            branches = self.get_branches()
            if branch_name not in branches:
                return False
            
            # Check if it's the current branch
            current_branch = self.get_current_branch()
            if branch_name == current_branch:
                return False
            
            # Check if branch is remote
            if branch_name.startswith('origin/'):
                return False
            
            return True
            
        except subprocess.CalledProcessError as e:
            raise GitCommandError(f"Git command failed: {e}")
        except NotGitRepositoryError:
            # Re-raise NotGitRepositoryError without wrapping
            raise
        except GitCommandError:
            # Re-raise GitCommandError without wrapping
            raise
        except Exception as e:
            raise GitInterfaceError(f"Unexpected error in is_branch_mergeable: {e}")
