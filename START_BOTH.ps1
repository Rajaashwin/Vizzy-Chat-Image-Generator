# Vizzy Chat - Start Backend + Frontend
# Usage: PowerShell -ExecutionPolicy Bypass -File START_BOTH.ps1

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Vizzy Chat - Starting Services" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BackendDir = Join-Path $RootDir "backend"
$FrontendDir = Join-Path $RootDir "frontend"
$VenvPython = Join-Path $BackendDir "venv\Scripts\python.exe"

# Check backend venv
if (-not (Test-Path $VenvPython)) {
    Write-Host "[ERROR] Virtual environment not found!" -ForegroundColor Red
    exit 1
}

# Start Backend
Write-Host "[1/2] Starting Backend (http://localhost:8000)..." -ForegroundColor Green
$BackendProc = Start-Process -FilePath $VenvPython -ArgumentList "main.py" `
    -WorkingDirectory $BackendDir -PassThru
Write-Host "      Backend PID: $($BackendProc.Id)" -ForegroundColor Green

Start-Sleep -Seconds 3

# Start Frontend
Write-Host "[2/2] Starting Frontend (http://localhost:5173)..." -ForegroundColor Green
$FrontendProc = Start-Process -FilePath "npm" -ArgumentList "run", "dev" `
    -WorkingDirectory $FrontendDir -PassThru
Write-Host "      Frontend PID: $($FrontendProc.Id)" -ForegroundColor Green

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Both services running!" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Yellow
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Yellow
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Yellow
Write-Host "`nPress Ctrl+C to stop`n" -ForegroundColor Cyan

# Keep script running - stop if either process exits
do {
    Start-Sleep -Seconds 1
} while (
    $BackendProc.ProcessName -eq "python" -or 
    $FrontendProc.ProcessName -eq "node"
)

Write-Host "`n[INFO] Services stopped" -ForegroundColor Yellow
