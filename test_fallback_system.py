import asyncio
import sys
import os
from dotenv import load_dotenv

# Temporarily override the environment variable to simulate invalid API key
os.environ['GOOGLE_API_KEY'] = 'invalid_key_for_test'

load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.services.document_service import DocumentService
from backend.app.services.rag_service import RAGService

async def test_entire_rag_system():
    print('Testing complete RAG system with fallback...')
    
    # Test document service initialization
    doc_service = DocumentService()
    print('+ Document service initialized')
    
    # Check if collection has content
    collection_info = doc_service.qdrant_client.get_collection('book_document_chunks')
    print(f'+ Collection has {collection_info.points_count} points')
    
    # Test RAG service
    rag_service = RAGService()
    print('+ RAG service initialized')
    
    # Test search functionality with fallback embeddings
    try:
        results, citations = await rag_service.process_full_book_query('What is this book about?')
        print(f'+ Search completed successfully')
        print(f'  Results: {results}')
        print(f'  Citations: {citations}')
        print('+ RAG system is working with fallback mechanism!')
    except Exception as e:
        print(f'- RAG system test failed: {e}')
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_entire_rag_system())