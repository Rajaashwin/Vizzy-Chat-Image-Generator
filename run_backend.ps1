#!/usr/bin/env pwsh
# Run backend using the correct venv Python

$BackendDir = Join-Path $PSScriptRoot "backend"
$PythonExe = Join-Path $BackendDir "venv\Scripts\python.exe"

Set-Location $BackendDir
& $PythonExe main.py @args
