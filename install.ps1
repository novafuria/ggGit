# ggGit Installation Script for Windows PowerShell
# Installs ggGit with Python-based commands and creates PowerShell aliases.

param(
    [switch]$Help
)

if ($Help) {
    Write-Host "ggGit Installation Script for Windows" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\install.ps1" -ForegroundColor White
    Write-Host ""
    Write-Host "This script will:" -ForegroundColor Yellow
    Write-Host "  1. Check if Git and Python are installed" -ForegroundColor White
    Write-Host "  2. Install Python dependencies" -ForegroundColor White
    Write-Host "  3. Create PowerShell aliases for ggGit commands" -ForegroundColor White
    Write-Host "  4. Test the installation" -ForegroundColor White
    Write-Host ""
    exit 0
}

# Function to write colored output
function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Blue
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

# Check if Git is installed
Write-Info "Checking Git installation..."
try {
    $gitVersion = git --version
    if ($gitVersion) {
        Write-Success "Git is installed: $gitVersion"
    }
} catch {
    Write-Error "Git is not installed. Please install Git first from https://git-scm.com/"
    exit 1
}

# Check if Python is installed
Write-Info "Checking Python installation..."
try {
    $pythonVersion = python --version
    if ($pythonVersion) {
        Write-Success "Python is installed: $pythonVersion"
    } else {
        Write-Error "Python is not installed. Please install Python 3.12+ first."
        exit 1
    }
} catch {
    Write-Error "Python is not installed. Please install Python 3.12+ first."
    exit 1
}

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonPath = (Get-Command python).Source

Write-Info "ggGit root directory: $ScriptDir"
Write-Info "Python executable: $PythonPath"

# Install Python dependencies
Write-Info "Installing Python dependencies..."
try {
    & $PythonPath -m pip install click>=8.0.0 pyyaml>=6.0.0 jsonschema>=4.0.0 colorama
    Write-Success "Dependencies installed successfully"
} catch {
    Write-Error "Failed to install dependencies: $_"
    exit 1
}

# Create PowerShell profile if it doesn't exist
$ProfilePath = $PROFILE
if (-not (Test-Path $ProfilePath)) {
    Write-Info "Creating PowerShell profile..."
    New-Item -Path $ProfilePath -ItemType File -Force | Out-Null
    Write-Success "PowerShell profile created"
}

# Create aliases
Write-Info "Creating PowerShell aliases..."

$Aliases = @"
# ggGit aliases
`$env:GGGIT_ROOT = '$ScriptDir'
`$env:PYTHONPATH = "`$env:GGGIT_ROOT\src;`$env:PYTHONPATH"

# Basic Git Operations
function gga { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\gga.py" `$args }
function ggs { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggs.py" `$args }
function ggl { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggl.py" `$args }
function ggdif { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggdif.py" `$args }
function ggunstage { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggunstage.py" `$args }
function ggreset { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggreset.py" `$args }

# Branch Management
function ggmain { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggmain.py" `$args }
function ggdevelop { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggdevelop.py" `$args }
function ggb { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggb.py" `$args }
function ggmerge { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggmerge.py" `$args }

# Remote Operations
function ggpl { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggpl.py" `$args }
function ggpp { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggpp.py" `$args }

# Conventional Commits
function ggfeat { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggfeat.py" `$args }
function ggfix { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggfix.py" `$args }
function ggdocs { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggdocs.py" `$args }
function ggstyle { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggstyle.py" `$args }
function ggchore { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggchore.py" `$args }
function ggbuild { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggbuild.py" `$args }
function ggci { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggci.py" `$args }
function ggperf { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggperf.py" `$args }
function ggtest { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggtest.py" `$args }
function ggbreak { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggbreak.py" `$args }

# AI Commands
function ggai { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggai.py" `$args }

# Configuration
function ggconfig { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggconfig.py" `$args }

# Information
function ggv { & '$PythonPath' "`$env:GGGIT_ROOT\src\commands\ggv.py" `$args }
"@

# Check if aliases already exist
$ProfileContent = Get-Content $ProfilePath -Raw
if ($ProfileContent -like "*ggGit aliases*") {
    Write-Info "ggGit aliases already installed"
} else {
    # Add aliases to profile
    Add-Content -Path $ProfilePath -Value $Aliases
    Write-Success "Added aliases to PowerShell profile"
}

# Test installation
Write-Info "Testing installation..."
try {
    $env:GGGIT_ROOT = $ScriptDir
    $env:PYTHONPATH = "$env:GGGIT_ROOT\src;$env:PYTHONPATH"
    
    $testResult = & $PythonPath "$ScriptDir\src\commands\ggv.py" --help
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Installation test passed"
    } else {
        Write-Warning "Installation test failed, but aliases were created"
    }
} catch {
    Write-Warning "Installation test failed: $_"
}

# Success message
Write-Host ""
Write-Success "Installation completed!"
Write-Host ""
Write-Info "To start using ggGit:"
Write-Host "  1. Restart your PowerShell, or"
Write-Host "  2. Run: . `$PROFILE"
Write-Host ""
Write-Info "Test the installation with:"
Write-Host "  ggv --help"
Write-Host ""
Write-Info "Available commands:"
$commands = @(
    'gga', 'ggs', 'ggl', 'ggdif', 'ggunstage', 'ggreset',
    'ggmain', 'ggdevelop', 'ggb', 'ggmerge', 'ggpl', 'ggpp',
    'ggfeat', 'ggfix', 'ggdocs', 'ggstyle', 'ggchore', 
    'ggbuild', 'ggci', 'ggperf', 'ggtest', 'ggbreak',
    'ggai', 'ggconfig', 'ggv'
)
Write-Host "  $($commands -join ', ')"
Write-Host ""
Write-Info "For help with any command, use:"
Write-Host "  <command> --help"
Write-Host ""
Write-Info "Note: If you get execution policy errors, run:"
Write-Host "  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"