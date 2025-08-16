#!/bin/bash

# ggGit Health Check Script
# This script checks the health of your ggGit installation

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

print_header() {
    echo -e "\e[1;36m$1\e[0m"
    echo "=================================="
}

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMMANDS_DIR="$SCRIPT_DIR/commands"

echo ""
print_header "ggGit Health Check"
echo ""

# Check 1: Git installation
print_info "1. Checking Git installation..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    print_success "Git is installed: $GIT_VERSION"
else
    print_error "Git is not installed"
    echo "   Please install Git from https://git-scm.com/"
    exit 1
fi

# Check 2: Commands directory exists
print_info "2. Checking commands directory..."
if [ -d "$COMMANDS_DIR" ]; then
    print_success "Commands directory exists: $COMMANDS_DIR"
else
    print_error "Commands directory not found: $COMMANDS_DIR"
    exit 1
fi

# Check 3: Script permissions
print_info "3. Checking script permissions..."
ALL_EXECUTABLE=true
for script in "$COMMANDS_DIR"/*; do
    if [ -f "$script" ] && [ ! -x "$script" ]; then
        print_error "Script not executable: $(basename "$script")"
        ALL_EXECUTABLE=false
    fi
done

if [ "$ALL_EXECUTABLE" = true ]; then
    print_success "All scripts are executable"
else
    print_warning "Some scripts are not executable"
    echo "   Run: chmod +x $COMMANDS_DIR/*"
fi

# Check 4: Script syntax
print_info "4. Checking script syntax..."
SYNTAX_ERRORS=false
for script in "$COMMANDS_DIR"/*.sh "$COMMANDS_DIR"/gg*; do
    if [ -f "$script" ]; then
        if ! bash -n "$script" 2>/dev/null; then
            print_error "Syntax error in: $(basename "$script")"
            SYNTAX_ERRORS=true
        fi
    fi
done

if [ "$SYNTAX_ERRORS" = false ]; then
    print_success "All scripts have valid syntax"
else
    print_warning "Some scripts have syntax errors"
fi

# Check 5: PATH configuration
print_info "5. Checking PATH configuration..."
if [[ ":$PATH:" == *":$COMMANDS_DIR:"* ]]; then
    print_success "ggGit is in PATH"
else
    print_warning "ggGit is not in PATH"
    echo "   Add this line to your shell configuration:"
    echo "   export PATH=\$PATH:$COMMANDS_DIR"
fi

# Check 6: Test basic commands
print_info "6. Testing basic commands..."
TEST_COMMANDS=("ggv" "ggs" "ggl" "gga")
for cmd in "${TEST_COMMANDS[@]}"; do
    if [ -x "$COMMANDS_DIR/$cmd" ]; then
        if "$COMMANDS_DIR/$cmd" --help >/dev/null 2>&1; then
            print_success "$cmd works correctly"
        else
            print_warning "$cmd has issues"
        fi
    else
        print_error "$cmd is not executable"
    fi
done

# Check 7: Git repository status
print_info "7. Checking Git repository status..."
if [ -d ".git" ]; then
    print_success "This is a Git repository"
    
    # Check if there are uncommitted changes
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "There are uncommitted changes"
        echo "   Run 'git status' to see details"
    else
        print_success "Working directory is clean"
    fi
    
    # Check remote configuration
    if git remote -v | grep -q "origin"; then
        print_success "Remote origin is configured"
    else
        print_warning "No remote origin configured"
    fi
else
    print_warning "This is not a Git repository"
fi

# Check 8: System compatibility
print_info "8. Checking system compatibility..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    print_success "Linux system detected"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    print_success "macOS system detected"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    print_success "Windows (Git Bash) detected"
else
    print_warning "Unknown system type: $OSTYPE"
fi

# Summary
echo ""
print_header "Health Check Summary"
echo ""

if [ "$ALL_EXECUTABLE" = true ] && [ "$SYNTAX_ERRORS" = false ]; then
    print_success "ggGit is healthy and ready to use!"
    echo ""
    print_info "Next steps:"
    echo "  1. Restart your terminal or run: source ~/.bashrc"
    echo "  2. Test with: ggv --help"
    echo "  3. Use ggconfig to verify installation"
else
    print_warning "ggGit has some issues that need attention"
    echo ""
    print_info "Recommended actions:"
    echo "  1. Fix script permissions: chmod +x $COMMANDS_DIR/*"
    echo "  2. Check script syntax for errors"
    echo "  3. Add to PATH if not configured"
    echo "  4. Run this health check again"
fi

echo ""
print_info "For more information, run:"
echo "  $COMMANDS_DIR/ggconfig"
