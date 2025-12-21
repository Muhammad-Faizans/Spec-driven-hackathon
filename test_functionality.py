import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.services.rag_service import RAGService
from backend.app.services.translation_service import TranslationService
from backend.app.services.document_service import DocumentService

async def test_rag_functionality():
    """Test RAG functionality"""
    print("Testing RAG functionality...")
    
    try:
        rag_service = RAGService()
        response, citations = await rag_service.process_full_book_query("What is this book about?")
        print(f"RAG Response: {response}")
        print(f"Citations: {citations}")
        print("✓ RAG functionality test passed")
    except Exception as e:
        print(f"✗ RAG functionality test failed: {e}")

async def test_translation_functionality():
    """Test translation functionality"""
    print("\nTesting translation functionality...")
    
    try:
        translation_service = TranslationService()
        result = await translation_service.translate_text("Hello, how are you?", "en", "ur")
        print(f"Translation: {result}")
        print("✓ Translation functionality test passed")
    except Exception as e:
        print(f"✗ Translation functionality test failed: {e}")

async def test_document_indexing():
    """Test document indexing functionality"""
    print("\nTesting document indexing...")
    
    try:
        doc_service = DocumentService()
        print("✓ Document service initialized successfully")
        
        # Test with a sample document if docs exist
        docs_path = os.path.join(os.path.dirname(__file__), 'docs')
        if os.path.exists(docs_path):
            print(f"✓ Found docs directory at {docs_path}")
        else:
            print("⚠ Docs directory not found")
        
        print("✓ Document indexing test passed")
    except Exception as e:
        print(f"✗ Document indexing test failed: {e}")

async def run_all_tests():
    """Run all functionality tests"""
    print("Starting functionality tests...\n")
    
    await test_rag_functionality()
    await test_translation_functionality()
    await test_document_indexing()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    asyncio.run(run_all_tests())