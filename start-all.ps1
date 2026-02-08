# Vizzy Chat - Start Backend + Frontend in Parallel
# Usage: PowerShell ./start-all.ps1

param(
    [int]$BackendPort = 8000,
    [int]$FrontendPort = 5173,
    [string]$Mode = "dev"
)

Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  Vizzy Chat - Starting All Services" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BackendDir = Join-Path $RootDir "backend"
$FrontendDir = Join-Path $RootDir "frontend"
$VenvPython = Join-Path $BackendDir "venv\Scripts\python.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[ERROR] Virtual environment not found at $VenvPython" -ForegroundColor Red
    Write-Host "Run: python -m venv backend/venv" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path (Join-Path $FrontendDir "node_modules"))) {
    Write-Host "[WARN] Installing frontend dependencies..." -ForegroundColor Yellow
    Push-Location $FrontendDir
    npm install
    Pop-Location
}

Write-Host "[*] Starting Backend (port $BackendPort)..." -ForegroundColor Green
$BackendProcess = Start-Process `
    -FilePath $VenvPython `
    -ArgumentList "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", $BackendPort, "--reload" `
    -WorkingDirectory $BackendDir `
    -NoNewWindow `
    -PassThru

Write-Host "[OK] Backend started (PID: $($BackendProcess.Id))" -ForegroundColor Green
Start-Sleep -Seconds 2

Write-Host "[*] Starting Frontend (port $FrontendPort)..." -ForegroundColor Green
$FrontendProcess = Start-Process `
    -FilePath "npm" `
    -ArgumentList "run", "dev" `
    -WorkingDirectory $FrontendDir `
    -NoNewWindow `
    -PassThru

Write-Host "[OK] Frontend started (PID: $($FrontendProcess.Id))" -ForegroundColor Green

Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  Vizzy Chat is Running!" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend:  http://localhost:$BackendPort" -ForegroundColor Yellow
Write-Host "Frontend: http://localhost:$FrontendPort" -ForegroundColor Yellow
Write-Host ""
Write-Host "[TIP] Close windows to stop services" -ForegroundColor DarkGray
Write-Host ""

$BackendAlive = $true
$FrontendAlive = $true

try {
    while ($BackendAlive -or $FrontendAlive) {
        $BackendAlive = Get-Process -Id $BackendProcess.Id -ErrorAction SilentlyContinue
        $FrontendAlive = Get-Process -Id $FrontendProcess.Id -ErrorAction SilentlyContinue

        if (-not $BackendAlive) {
            Write-Host "[WARN] Backend process stopped" -ForegroundColor Red
        }
        if (-not $FrontendAlive) {
            Write-Host "[WARN] Frontend process stopped" -ForegroundColor Red
        }

        Start-Sleep -Seconds 1
    }
}
finally {
    Write-Host ""
    Write-Host "[*] Stopping services..." -ForegroundColor Yellow
    
    if ($BackendProcess -and (Get-Process -Id $BackendProcess.Id -ErrorAction SilentlyContinue)) {
        Stop-Process -Id $BackendProcess.Id -Force -ErrorAction SilentlyContinue
        Write-Host "[OK] Backend stopped" -ForegroundColor Green
    }
    
    if ($FrontendProcess -and (Get-Process -Id $FrontendProcess.Id -ErrorAction SilentlyContinue)) {
        Stop-Process -Id $FrontendProcess.Id -Force -ErrorAction SilentlyContinue
        Write-Host "[OK] Frontend stopped" -ForegroundColor Green
    }
    
    Write-Host ""
    Write-Host "Vizzy Chat shut down." -ForegroundColor Cyan
}
