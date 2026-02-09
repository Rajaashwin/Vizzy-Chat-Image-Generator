"""
Vercel serverless entry point for FastAPI Vizzy Chat backend.
Wraps FastAPI ASGI app for Vercel's Python runtime.
"""
import sys
import os

# Add backend folder to path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi import FastAPI
from main import app as fastapi_app

# For Vercel, export the FastAPI app directly
# Vercel will automatically detect it's an ASGI app
app = fastapi_app
