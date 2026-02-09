#!/usr/bin/env node

/**
 * Vizzy Chat - Start Both Backend & Frontend
 * Usage: node start.js
 * 
 * Starts both services simultaneously and keeps them running.
 */

const { spawn } = require('child_process');
const path = require('path');
const os = require('os');

const isWindows = os.platform() === 'win32';
const rootDir = __dirname;
const backendDir = path.join(rootDir, 'backend');
const frontendDir = path.join(rootDir, 'frontend');

console.log('\n========================================');
console.log('  🚀 Vizzy Chat - Starting Services');
console.log('========================================\n');

// Start Backend
console.log('[1/2] Starting Backend (http://localhost:8000)...');
const pythonExe = isWindows 
  ? path.join(backendDir, 'venv\\Scripts\\python.exe')
  : path.join(backendDir, 'venv/bin/python');

const backendProcess = spawn(pythonExe, ['main.py'], {
  cwd: backendDir,
  stdio: 'inherit',
  shell: isWindows,
});

backendProcess.on('error', (err) => {
  console.error(`[ERROR] Failed to start backend: ${err.message}`);
  console.error('Make sure venv is set up: cd backend && python -m venv venv && pip install -r requirements.txt');
  process.exit(1);
});

console.log(`      Backend PID: ${backendProcess.pid}`);

// Wait a moment, then start Frontend
setTimeout(() => {
  console.log('[2/2] Starting Frontend (http://localhost:5173)...');
  
  const frontendProcess = spawn('npm', ['run', 'dev'], {
    cwd: frontendDir,
    stdio: 'inherit',
    shell: isWindows,
  });

  frontendProcess.on('error', (err) => {
    console.error(`[ERROR] Failed to start frontend: ${err.message}`);
    console.error('Make sure npm is installed and dependencies are set up: cd frontend && npm install');
    backendProcess.kill();
    process.exit(1);
  });

  console.log(`      Frontend PID: ${frontendProcess.pid}`);

  console.log('\n========================================');
  console.log('  ✅ Both services running!');
  console.log('========================================\n');
  console.log('Backend:  http://localhost:8000');
  console.log('Frontend: http://localhost:5173/vizzy-chat/');
  console.log('API Docs: http://localhost:8000/docs');
  console.log('\nPress Ctrl+C to stop\n');

  // Handle graceful shutdown
  process.on('SIGINT', () => {
    console.log('\n\n[INFO] Shutting down services...');
    backendProcess.kill();
    frontendProcess.kill();
    setTimeout(() => process.exit(0), 1000);
  });
}, 2000);

// Handle backend shutdown
backendProcess.on('exit', (code) => {
  if (code !== null && code !== 0) {
    console.error(`\n[ERROR] Backend exited with code ${code}`);
  }
});
