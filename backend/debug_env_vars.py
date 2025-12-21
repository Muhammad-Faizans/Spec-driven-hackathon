import os
from dotenv import load_dotenv

# Load environment variables from .env file
print("Loading .env file...")
load_dotenv(dotenv_path='./.env')

print("Environment variables:")
print(f"GEMINI_API_KEY: {os.getenv('GEMINI_API_KEY')}")
print(f"COHERE_API_KEY: {os.getenv('COHERE_API_KEY')}")
print(f"QDRANT_URL: {os.getenv('QDRANT_URL')}")
print(f"QDRANT_API_KEY: {os.getenv('QDRANT_API_KEY')}")

# Check if file exists
import pathlib
env_file = pathlib.Path('./.env')
print(f".env file exists: {env_file.exists()}")

if env_file.exists():
    print("Contents of .env file:")
    print(env_file.read_text())