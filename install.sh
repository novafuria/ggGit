#!/bin/bash

# ggGit Installation Script
# This script installs ggGit on your system

set -e

print_success() {
    echo -e "\e[32m✓ $1\e[0m"
}

print_error() {
    echo -e "\e[31m✗ $1\e[0m"
}

print_info() {
    echo -e "\e[34mℹ $1\e[0m"
}

print_warning() {
    echo -e "\e[33m⚠ $1\e[0m"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

print_success "Git is installed"

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Make all scripts executable
print_info "Making scripts executable..."
chmod +x "$SCRIPT_DIR/commands"/*

print_success "Scripts are now executable"

# Detect shell
SHELL_CONFIG=""
if [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_CONFIG="$HOME/.zshrc"
    print_info "Detected zsh shell"
elif [[ "$SHELL" == *"bash"* ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
    print_info "Detected bash shell"
else
    print_warning "Unknown shell: $SHELL"
    print_info "Please manually add the following line to your shell configuration file:"
    echo "export PATH=\$PATH:$SCRIPT_DIR/commands"
    exit 0
fi

# Check if PATH is already configured
if grep -q "$SCRIPT_DIR/commands" "$SHELL_CONFIG" 2>/dev/null; then
    print_info "ggGit is already in your PATH"
else
    # Add to PATH
    print_info "Adding ggGit to your PATH in $SHELL_CONFIG"
    echo "" >> "$SHELL_CONFIG"
    echo "# ggGit commands" >> "$SHELL_CONFIG"
    echo "export PATH=\$PATH:$SCRIPT_DIR/commands" >> "$SHELL_CONFIG"
    
    print_success "Added to $SHELL_CONFIG"
fi

# Instructions
echo ""
print_success "Installation completed!"
echo ""
print_info "To start using ggGit, please:"
echo "  1. Restart your terminal, or"
echo "  2. Run: source $SHELL_CONFIG"
echo ""
print_info "Test the installation with:"
echo "  ggv --help"
echo ""
print_info "Available commands:"
echo "  gga, ggs, ggl, ggdif, ggfeat, ggfix, ggbreak, ggmain, ggmaster, ggmerge, ggpl, ggpp, ggreset, ggunstage, ggv"
echo ""
print_info "For help with any command, use:"
echo "  <command> --help"
