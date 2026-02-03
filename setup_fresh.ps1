# ========================================
# GraphRAG Complete Setup Script
# Run this to set up everything from scratch
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GraphRAG Fresh Installation" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Step 1: Create directory structure
Write-Host "Step 1: Creating directory structure..." -ForegroundColor Yellow
$basePath = "D:\GraphRAG_FINAL"
$projectPath = "$basePath\project"

New-Item -ItemType Directory -Path $basePath -Force | Out-Null
New-Item -ItemType Directory -Path $projectPath -Force | Out-Null
New-Item -ItemType Directory -Path "$projectPath\input" -Force | Out-Null
New-Item -ItemType Directory -Path "$projectPath\output" -Force | Out-Null
New-Item -ItemType Directory -Path "$projectPath\cache" -Force | Out-Null
New-Item -ItemType Directory -Path "$projectPath\logs" -Force | Out-Null
New-Item -ItemType Directory -Path "$projectPath\prompts" -Force | Out-Null

Write-Host "   ✓ Directory structure created" -ForegroundColor Green

# Step 2: Create virtual environment
Write-Host "`nStep 2: Creating virtual environment..." -ForegroundColor Yellow
cd $basePath

if (Test-Path "venv") {
    Write-Host "   ⚠️  venv already exists, skipping..." -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "   ✓ Virtual environment created" -ForegroundColor Green
}

# Step 3: Activate venv and install GraphRAG
Write-Host "`nStep 3: Installing GraphRAG..." -ForegroundColor Yellow
Write-Host "   Please run these commands manually:" -ForegroundColor White
Write-Host "   cd $basePath" -ForegroundColor Cyan
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "   pip install --upgrade pip" -ForegroundColor Cyan
Write-Host "   pip install graphrag" -ForegroundColor Cyan

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Download all the configuration files from this chat" -ForegroundColor White
Write-Host "2. Place them in the correct locations:" -ForegroundColor White
Write-Host "   - .env → $projectPath\.env" -ForegroundColor Gray
Write-Host "   - settings.yaml → $projectPath\settings.yaml" -ForegroundColor Gray
Write-Host "   - entity_extraction.txt → $projectPath\prompts\" -ForegroundColor Gray
Write-Host "   - summarize_descriptions.txt → $projectPath\prompts\" -ForegroundColor Gray
Write-Host "   - community_report.txt → $projectPath\prompts\" -ForegroundColor Gray
Write-Host "3. Copy your 5 .md files to: $projectPath\input\" -ForegroundColor White
Write-Host "4. Run: cd $projectPath" -ForegroundColor White
Write-Host "5. Run: graphrag index --root ." -ForegroundColor White
Write-Host "`n========================================`n" -ForegroundColor Cyan
