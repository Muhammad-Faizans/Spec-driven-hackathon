"""Test script to verify Qdrant connection and data retrieval"""

from chat_gemini import query_qdrant, format_response
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

def test_qdrant_connection():
    print("Testing Qdrant connection...")
    
    try:
        # Test basic connection
        qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
        
        # Check collection info
        collection_info = qdrant_client.get_collection(collection_name=COLLECTION_NAME)
        point_count = collection_info.points_count if hasattr(collection_info, 'points_count') else collection_info.get('points_count', 0) if isinstance(collection_info, dict) else 0
        print(f"✓ Collection '{COLLECTION_NAME}' exists with {point_count} vectors")
        
        # Test a search query
        print("\nTesting search query...")
        search_results = query_qdrant("Physical AI")
        
        print(f"✓ Search returned {len(search_results)} results")
        
        if search_results:
            first_result = search_results[0]
            print(f"✓ First result source: {first_result.payload.get('source_file', 'Unknown') if hasattr(first_result, 'payload') else 'N/A'}")
            print(f"✓ First result text preview: {first_result.payload.get('text', '')[:100] if hasattr(first_result, 'payload') else 'N/A'}...")
        
        # Test response formatting
        print("\nTesting response formatting...")
        formatted_response = format_response("What is Physical AI?", search_results)
        print(f"✓ Formatted response length: {len(formatted_response)} characters")
        print(f"✓ Response preview: {formatted_response[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_qdrant_connection()
    if success:
        print("\n✓ All tests passed! Qdrant connection is working properly.")
    else:
        print("\n✗ Tests failed! Check the errors above.")