import asyncio
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the backend directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

print("Starting Qdrant fix test...")

# Import after setting up paths
from backend.app.services.document_service import DocumentService
from backend.app.services.rag_service import RAGService

async def test_document_indexing():
    print('Environment variables:')
    print('  QDRANT_HOST:', os.getenv('QDRANT_HOST', 'NOT SET'))
    print('  GOOGLE_API_KEY:', 'SET' if os.getenv('GOOGLE_API_KEY') else 'NOT SET')

    print('\nTesting document indexing...')

    try:
        doc_service = DocumentService()
        print('+ Document service initialized successfully')

        # List files in docs directory
        docs_path = os.path.join(os.getcwd(), 'docs')
        if os.path.exists(docs_path):
            print('+ Found docs directory at:', docs_path)
            for root, dirs, files in os.walk(docs_path):
                for file in files:
                    if file.endswith(('.md', '.mdx')):
                        file_path = os.path.join(root, file)
                        print('  - Found markdown file:', file_path)
        else:
            print('* Docs directory not found')

        # Index all markdown files found
        import glob
        md_files = glob.glob(os.path.join(docs_path, '**/*.md'), recursive=True)

        if md_files:
            total_chunks = 0
            for file_path in md_files:
                print(f'Indexing: {file_path}')
                chapter_name = os.path.splitext(os.path.basename(file_path))[0].replace('_', ' ').replace('-', ' ').title()
                chunks_count = await doc_service.index_book_content(file_path, chapter_name)
                total_chunks += chunks_count
                print(f'  + Indexed {chunks_count} chunks from {file_path}')

            print(f'\n+ Total indexed: {total_chunks} chunks from {len(md_files)} files')
        else:
            print('No markdown files found to index')

        # Check collection status
        try:
            collection_info = doc_service.qdrant_client.get_collection('book_document_chunks')
            print(f'Collection info: {collection_info.points_count} points stored')
            print(f'Collection status: {collection_info.status}')
        except Exception as e:
            print(f'Could not get collection info: {e}')

        print('\n+ Document indexing test completed successfully')
        return True
    except Exception as e:
        print(f'- Document indexing test failed: {e}')
        import traceback
        traceback.print_exc()
        return False

    return True

async def test_rag_search():
    print('\nTesting RAG search functionality...')

    try:
        rag_service = RAGService()
        print('+ RAG service initialized successfully')

        # Test search with a simple query
        results, citations = await rag_service.process_full_book_query(
            "What is this book about?"
        )

        print(f'Search results: {results}')
        print(f'Citations: {citations}')

        print('+ RAG search test completed successfully')
        return True
    except Exception as e:
        print(f'- RAG search test failed: {e}')
        import traceback
        traceback.print_exc()
        return False

async def main():
    print("Running Qdrant fix verification...")

    indexing_success = await test_document_indexing()
    if indexing_success:
        rag_success = await test_rag_search()
        if rag_success:
            print("\n[SUCCESS] All tests passed! Qdrant fix is working correctly.")
        else:
            print("\n[WARNING] RAG test failed, but indexing worked.")
    else:
        print("\n[ERROR] Indexing test failed.")

if __name__ == "__main__":
    asyncio.run(main())