"""
Simple test to verify Google API key functionality
"""
from google import genai
import os
from config import GEMINI_API_KEY

def test_gemini_key():
    print("Testing Google API key...")

    if not GEMINI_API_KEY or "YOUR_API_KEY_HERE" in GEMINI_API_KEY or len(GEMINI_API_KEY) < 20:
        print("[FAILED] GEMINI_API_KEY is not properly configured")
        print(f"Current key: {GEMINI_API_KEY[:20]}..." if GEMINI_API_KEY else "Current key: None")
        return False

    try:
        os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
        print("[SUCCESS] API key accepted by client")

        # Try listing models to check if the key has proper permissions
        models = genai.list_models()
        available_text_models = [model for model in models if 'generateContent' in model.supported_generation_methods]

        if available_text_models:
            print(f"[SUCCESS] Found {len(available_text_models)} text generation models")
            for model in available_text_models[:3]:  # Show first 3
                print(f"  - {model.name}")

            # Try a simple generation with the first available model
            model = genai.GenerativeModel(available_text_models[0].name)
            response = model.generate_content("Hello, are you working?")

            if response and response.text:
                print("[SUCCESS] Text generation successful")
                print(f"Response: {response.text[:100]}...")
                return True
            else:
                print("[FAILED] Text generation returned empty response")
                return False
        else:
            print("[FAILED] No text generation models available with this API key")
            return False

    except Exception as e:
        print(f"[FAILED] Error with API key: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_gemini_key()
    if not success:
        print("\nTo fix this issue:")
        print("1. Get a valid Google Gemini API key from https://aistudio.google.com/")
        print("2. Add it to your .env file as GEMINI_API_KEY='your-actual-key'")
        print("3. Make sure your billing is set up in Google Cloud Console")
    else:
        print("\nAPI key is working correctly!")