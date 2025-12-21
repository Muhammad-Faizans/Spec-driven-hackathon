#!/usr/bin/env python3
"""Script to list available Gemini models"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google import genai
from config import GEMINI_API_KEY

print(f"GEMINI_API_KEY is set: {bool(GEMINI_API_KEY)}")

if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY is not set!")
    exit(1)

os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

try:
    # List available models to see what's accessible
    print('Fetching available models...')
    models = genai.list_models()
    
    print('Available models:')
    for model in models:
        print(f'- {model.name}')
        # Check if it supports generateContent
        if hasattr(model, 'supported_generation_methods') and 'generateContent' in model.supported_generation_methods:
            print(f'  Supports generateContent: Yes')
        else:
            print(f'  Supports generateContent: No')
            
    print(f"\nTotal models found: {len(list(models))}")
    
except Exception as e:
    print(f"Error listing models: {e}")
    import traceback
    traceback.print_exc()