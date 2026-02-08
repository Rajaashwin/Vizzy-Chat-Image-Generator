"""
Vercel serverless entry point for FastAPI Vizzy Chat backend.
Vercel automatically routes API requests to this handler.
"""
import sys
import os

# Add backend folder to path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app

# Vercel expects a WSGI or ASGI app named 'app'  
# FastAPI is ASGI-compatible, so this works directly
