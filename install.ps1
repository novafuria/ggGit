# ggGit Installation Script for Windows PowerShell
# This script installs ggGit on your Windows system

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
    Write-Host "  1. Check if Git is installed" -ForegroundColor White
    Write-Host "  2. Add ggGit commands to your PATH" -ForegroundColor White
    Write-Host "  3. Configure your PowerShell environment" -ForegroundColor White
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

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$CommandsPath = Join-Path $ScriptDir "commands"

Write-Info "ggGit commands directory: $CommandsPath"

# Check if commands directory exists
if (-not (Test-Path $CommandsPath)) {
    Write-Error "Commands directory not found: $CommandsPath"
    exit 1
}

# Add to PATH environment variable
Write-Info "Adding ggGit to your PATH..."

$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($currentPath -notlike "*$CommandsPath*") {
    $newPath = "$currentPath;$CommandsPath"
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Success "Added to PATH environment variable"
} else {
    Write-Info "ggGit is already in your PATH"
}

# Instructions
Write-Host ""
Write-Success "Installation completed!"
Write-Host ""
Write-Info "To start using ggGit, please:"
Write-Host "  1. Restart your PowerShell, or"
Write-Host "  2. Refresh your environment variables"
Write-Host ""
Write-Info "Test the installation with:"
Write-Host "  ggv --help"
Write-Host ""
Write-Info "Available commands:"
Write-Host "  gga, ggs, ggl, ggdif, ggfeat, ggfix, ggbreak, ggmain, ggmaster, ggmerge, ggpl, ggpp, ggreset, ggunstage, ggv, ggconfig"
Write-Host ""
Write-Info "For help with any command, use:"
Write-Host "  <command> --help"
Write-Host ""
Write-Info "Note: If you get execution policy errors, run:"
Write-Host "  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
