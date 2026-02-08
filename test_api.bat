@echo off
REM Test Vizzy Chat API

echo ============================================================
echo Testing Vizzy Chat Backend API
echo ============================================================

REM Test 1: Health check
echo.
echo [1] Health Check
curl -X GET http://localhost:8000/
echo.

REM Test 2: Chat endpoint
echo.
echo [2] Chat Endpoint - Generating images...
REM This may take 30-60 seconds
curl -X POST http://localhost:8000/chat ^
  -H "Content-Type: application/json" ^
  -d "{\"session_id\":\"demo_session\",\"message\":\"Create a dreamy landscape\",\"num_images\":2}"
echo.

echo ============================================================
echo Test complete!
echo ============================================================
