import sys
import traceback
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

print("Testing Qdrant search...")

try:
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    print('Qdrant client created successfully')
    
    # Test search to see if we can query the collection
    # We'll use a simple search with a dummy vector
    import random
    dummy_query_vector = [random.random() for _ in range(1024)]  # Cohere embed-english-v3.0 has 1024 dimensions
    
    search_results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=dummy_query_vector,
        limit=1,
        with_payload=True
    )
    
    print(f'Search successful! Found {len(search_results)} results')
    
    if search_results:
        first_result = search_results[0]
        print(f'First result ID: {first_result.id}')
        print(f'First result payload keys: {list(first_result.payload.keys()) if first_result.payload else "None"}')
        print(f'First result score: {first_result.score}')
    
except Exception as e:
    print(f'Error during search: {e}')
    print("Full traceback:")
    traceback.print_exc()