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

async def test_complete_rag_system():
    print('Testing complete RAG system with fallback...')
    
    # Initialize document service
    doc_service = DocumentService()
    print('+ Document service initialized')
    
    # Index some documents to populate the collection
    docs_path = os.path.join(os.path.dirname(__file__), 'docs')
    import glob
    md_files = glob.glob(os.path.join(docs_path, '**/*.md'), recursive=True)
    
    if md_files:
        test_file = md_files[0]  # Use first file to test
        chapter_name = os.path.splitext(os.path.basename(test_file))[0].replace('_', ' ').replace('-', ' ').title()
        chunks_count = await doc_service.index_book_content(test_file, chapter_name)
        print(f'+ Indexed {chunks_count} chunks from {test_file}')
        
        # Check if collection has content
        collection_info = doc_service.qdrant_client.get_collection('book_document_chunks')
        print(f'+ Collection now has {collection_info.points_count} points')
    else:
        print('- No markdown files found to index')
        return
    
    # Initialize RAG service
    rag_service = RAGService()
    print('+ RAG service initialized')
    
    # Test search functionality with fallback embeddings
    try:
        results, citations = await rag_service.process_full_book_query('What is this book about?')
        print(f'+ Search completed successfully')
        print(f'  Results: {results}')
        print(f'  Citations: {citations}')
        
        if results != "Answer not found in book":
            print('+ SUCCESS: RAG system is working with fallback mechanism!')
        else:
            print('+ PARTIAL: RAG system is working but no relevant content found (which is expected with fallback embeddings)')
    except Exception as e:
        print(f'- RAG system test failed: {e}')
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_complete_rag_system())