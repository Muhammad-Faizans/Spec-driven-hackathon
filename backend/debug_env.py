#!/usr/bin/env python3
"""
Debug script to check environment variables and configuration validation
"""

import os
import sys
import dotenv

# Load environment variables
dotenv.load_dotenv()

print("Environment Variables Check:")
print("=" * 40)
print(f"GEMINI_API_KEY: {'SET' if os.getenv('GEMINI_API_KEY') else 'NOT SET'}")
print(f"COHERE_API_KEY: {'SET' if os.getenv('COHERE_API_KEY') else 'NOT SET'}")
print(f"QDRANT_URL: {'SET' if os.getenv('QDRANT_URL') else 'NOT SET'}")
print(f"QDRANT_API_KEY: {'SET' if os.getenv('QDRANT_API_KEY') else 'NOT SET'}")

print("\nActual Values:")
print(f"GEMINI_API_KEY: {os.getenv('GEMINI_API_KEY')[:10] if os.getenv('GEMINI_API_KEY') else 'None'}")
print(f"COHERE_API_KEY: {os.getenv('COHERE_API_KEY')[:10] if os.getenv('COHERE_API_KEY') else 'None'}")
print(f"QDRANT_URL: {os.getenv('QDRANT_URL')}")
print(f"QDRANT_API_KEY: {os.getenv('QDRANT_API_KEY')[:10] if os.getenv('QDRANT_API_KEY') else 'None'}")

print("\nPython Path:")
print(sys.path)

# Try importing and validating config
print("\nTrying to import config...")
try:
    from config import *
    print("Successfully imported config")
    print(f"GEMINI_API_KEY from config: {GEMINI_API_KEY[:10] if GEMINI_API_KEY else 'None'}")
    print(f"COHERE_API_KEY from config: {COHERE_API_KEY[:10] if COHERE_API_KEY else 'None'}")
    print(f"QDRANT_URL from config: {QDRANT_URL}")
    print(f"QDRANT_API_KEY from config: {QDRANT_API_KEY[:10] if QDRANT_API_KEY else 'None'}")
except Exception as e:
    print(f"Error importing config: {e}")

print("\nTrying to run validation...")
try:
    from secure_config import validate_config
    validate_config()
    print("Configuration validation passed!")
except Exception as e:
    print(f"Configuration validation failed: {e}")