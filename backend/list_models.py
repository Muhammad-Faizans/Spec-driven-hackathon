from google import genai
import os
from config import GEMINI_API_KEY

def list_available_models():
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    
    try:
        print("Available models:")
        for model in genai.list_models():
            print(f"- {model.name}")
            # Check if this model supports generateContent
            if 'generateContent' in model.supported_generation_methods:
                print(f"  ✓ Supports generateContent")
            else:
                print(f"  ✗ Does not support generateContent")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_available_models()