"""Secure configuration validation for the AI Assistant Backend."""

import os
from dotenv import load_dotenv
import pathlib


def validate_config():
    """Validate that all required environment variables are set."""

    # Load environment variables from .env file
    current_dir = pathlib.Path(__file__).parent.resolve()
    env_path = current_dir / ".env"
    load_dotenv(dotenv_path=env_path)

    required_vars = [
        "GEMINI_API_KEY",
        "COHERE_API_KEY",
        "QDRANT_URL",
        "QDRANT_API_KEY"
    ]

    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

    print("All required environment variables are present")