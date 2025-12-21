import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the backend directory to Python path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.services.document_service import DocumentService

async def index_book_content():
    """Index all book content from the docs directory"""
    print("Starting book content indexing...")
    
    # Initialize document service
    doc_service = DocumentService()
    
    # Index all markdown files in the docs directory
    docs_path = os.path.join(os.path.dirname(__file__), 'docs')
    if os.path.exists(docs_path):
        print(f"Found docs directory at {docs_path}")
        doc_service.index_directory(docs_path)
        print(f"Indexed documents from {docs_path}")
    else:
        print(f"Docs directory not found at {docs_path}")
        print("Looking for docs in subdirectories...")
        # Look for docs in common locations
        possible_paths = [
            os.path.join(os.path.dirname(__file__), 'my-docusaurus-site', 'docs'),
            os.path.join(os.path.dirname(__file__), 'backend', 'docs'),
            os.path.join(os.path.dirname(__file__), 'frontend', 'docs')
        ]
        for path in possible_paths:
            if os.path.exists(path):
                print(f"Found docs at alternative path: {path}")
                doc_service.index_directory(path)
                print(f"Indexed documents from {path}")
                return
        print("No docs directory found in expected locations.")
    
    print("Indexing completed!")

if __name__ == "__main__":
    asyncio.run(index_book_content())