#!/usr/bin/env python3
"""
ggGit Installation Script
Installs ggGit with Python-based commands and creates shell aliases.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[32m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_success(message):
    """Print success message in green."""
    print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")


def print_error(message):
    """Print error message in red."""
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")


def print_info(message):
    """Print info message in blue."""
    print(f"{Colors.BLUE}ℹ {message}{Colors.RESET}")


def print_warning(message):
    """Print warning message in yellow."""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")


def check_git():
    """Check if Git is installed."""
    try:
        result = subprocess.run(['git', '--version'], 
                              capture_output=True, text=True, check=True)
        print_success(f"Git is installed: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Git is not installed. Please install Git first.")
        return False


def check_python():
    """Check if Python 3.12+ is available."""
    if sys.version_info < (3, 12):
        print_error(f"Python 3.12+ required, found {sys.version}")
        return False
    
    print_success(f"Python {sys.version.split()[0]} is available")
    return True


def get_shell_config():
    """Get the appropriate shell configuration file."""
    shell = os.environ.get('SHELL', '')
    
    if 'zsh' in shell:
        return Path.home() / '.zshrc'
    elif 'bash' in shell:
        return Path.home() / '.bashrc'
    else:
        print_warning(f"Unknown shell: {shell}")
        return None


def create_aliases():
    """Create shell aliases for ggGit commands."""
    script_dir = Path(__file__).parent.absolute()
    python_path = sys.executable
    
    # Commands to create aliases for
    commands = [
        'gga', 'ggs', 'ggl', 'ggdif', 'ggunstage', 'ggreset',
        'ggmain', 'ggdevelop', 'ggb', 'ggmerge', 'ggpl', 'ggpp',
        'ggfeat', 'ggfix', 'ggdocs', 'ggstyle', 'ggchore', 
        'ggbuild', 'ggci', 'ggperf', 'ggtest', 'ggbreak',
        'ggai', 'ggconfig', 'ggv'
    ]
    
    # Create alias definitions
    aliases = []
    aliases.append("")
    aliases.append("# ggGit aliases")
    aliases.append(f"export GGGIT_ROOT='{script_dir}'")
    aliases.append(f"export PYTHONPATH=\"$GGGIT_ROOT/src:$PYTHONPATH\"")
    
    for cmd in commands:
        aliases.append(f"alias {cmd}='{python_path} $GGGIT_ROOT/src/commands/{cmd}.py'")
    
    return aliases


def install_aliases():
    """Install aliases in shell configuration."""
    shell_config = get_shell_config()
    
    if not shell_config:
        print_warning("Could not determine shell configuration file.")
        print_info("Please manually add the following aliases to your shell config:")
        print("\n".join(create_aliases()))
        return False
    
    print_info(f"Installing aliases in {shell_config}")
    
    # Check if aliases already exist
    if shell_config.exists():
        with open(shell_config, 'r') as f:
            content = f.read()
            if 'ggGit aliases' in content:
                print_info("ggGit aliases already installed")
                return True
    
    # Add aliases to shell config
    aliases = create_aliases()
    
    with open(shell_config, 'a') as f:
        f.write('\n'.join(aliases) + '\n')
    
    print_success(f"Added aliases to {shell_config}")
    return True


def create_conda_environment():
    """Create conda environment if environment.yml exists."""
    env_file = Path('environment.yml')
    
    if not env_file.exists():
        print_info("No environment.yml found, skipping conda environment creation")
        return True
    
    print_info("Creating conda environment...")
    
    try:
        # Check if conda is available
        subprocess.run(['conda', '--version'], check=True, capture_output=True)
        
        # Create environment
        result = subprocess.run([
            'conda', 'env', 'create', '-f', 'environment.yml'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print_success("Conda environment created successfully")
            print_info("Activate with: conda activate gggit")
            return True
        else:
            print_warning(f"Conda environment creation failed: {result.stderr}")
            return False
            
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_warning("Conda not available, skipping environment creation")
        return False


def install_dependencies():
    """Install Python dependencies."""
    print_info("Installing Python dependencies...")
    
    try:
        # Install basic dependencies
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', 
            'click>=8.0.0', 'pyyaml>=6.0.0', 'jsonschema>=4.0.0', 'colorama'
        ], check=True)
        
        print_success("Dependencies installed successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False


def test_installation():
    """Test the installation."""
    print_info("Testing installation...")
    
    try:
        # Set up environment for test
        script_dir = Path(__file__).parent.absolute()
        env = os.environ.copy()
        env['PYTHONPATH'] = f"{script_dir}/src:{env.get('PYTHONPATH', '')}"
        
        # Test a simple command
        result = subprocess.run([
            sys.executable, 'src/commands/ggv.py', '--help'
        ], capture_output=True, text=True, cwd=script_dir, env=env)
        
        if result.returncode == 0:
            print_success("Installation test passed")
            return True
        else:
            print_error(f"Installation test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print_error(f"Installation test failed: {e}")
        return False


def main():
    """Main installation function."""
    print(f"{Colors.BOLD}ggGit Installation Script{Colors.RESET}")
    print("=" * 40)
    
    # Check prerequisites
    if not check_git():
        sys.exit(1)
    
    if not check_python():
        sys.exit(1)
    
    # Create conda environment (optional)
    create_conda_environment()
    
    # Install dependencies
    if not install_dependencies():
        print_warning("Some dependencies failed to install, but continuing...")
    
    # Install aliases
    if not install_aliases():
        print_warning("Alias installation failed, but continuing...")
    
    # Test installation
    test_installation()
    
    # Success message
    print("\n" + "=" * 40)
    print_success("Installation completed!")
    print()
    print_info("To start using ggGit:")
    print("  1. Restart your terminal, or")
    print("  2. Run: source ~/.bashrc (or ~/.zshrc)")
    print()
    print_info("Test the installation with:")
    print("  ggv --help")
    print()
    print_info("Available commands:")
    commands = [
        'gga', 'ggs', 'ggl', 'ggdif', 'ggunstage', 'ggreset',
        'ggmain', 'ggdevelop', 'ggb', 'ggmerge', 'ggpl', 'ggpp',
        'ggfeat', 'ggfix', 'ggdocs', 'ggstyle', 'ggchore', 
        'ggbuild', 'ggci', 'ggperf', 'ggtest', 'ggbreak',
        'ggai', 'ggconfig', 'ggv'
    ]
    print(f"  {', '.join(commands)}")
    print()
    print_info("For help with any command, use:")
    print("  <command> --help")


if __name__ == '__main__':
    main()
