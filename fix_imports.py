#!/usr/bin/env python3
"""
Script to fix imports in all command files.
Changes 'from src.core' to 'from core' for proper execution.
"""

import os
import re
from pathlib import Path

def fix_imports_in_file(file_path):
    """Fix imports in a single file."""
    print(f"Fixing imports in {file_path}")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace 'from src.core' with 'from core'
    content = re.sub(r'from src\.core', 'from core', content)
    
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Fix imports in all command files."""
    commands_dir = Path('src/commands')
    
    if not commands_dir.exists():
        print("Commands directory not found")
        return
    
    # Get all Python files in commands directory
    python_files = list(commands_dir.glob('*.py'))
    
    for file_path in python_files:
        if file_path.name != '__init__.py':
            fix_imports_in_file(file_path)
    
    print(f"Fixed imports in {len(python_files)} files")

if __name__ == '__main__':
    main()
