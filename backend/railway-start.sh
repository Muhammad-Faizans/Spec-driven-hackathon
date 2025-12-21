#!/bin/sh
set -e

echo "Starting document ingestion process..."
cd /app  # Ensure we're in the right directory

# Check if docs directory exists
if [ ! -d "./docs" ]; then
    echo "WARNING: docs directory does not exist! This might be expected in production."
    ls -la  # List current directory for debugging
fi

# Only run ingestion if docs exist
if [ -d "./docs" ]; then
    echo "Found docs directory, proceeding with ingestion..."
    python backend/main.py ingest
    echo "Document ingestion process completed."
else
    echo "Skipping document ingestion as no docs directory found."
fi

echo "Starting API server..."
PORT=${PORT:-8000}  # Use PORT from environment, default to 8000 if not set
exec uvicorn backend.api:app --host 0.0.0.0 --port $PORT