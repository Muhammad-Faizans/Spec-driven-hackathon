import sys
import traceback
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

print("Testing Qdrant connection using get_collections...")

try:
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    print('Qdrant client created successfully')
    
    # Try to search in the collection to see if it exists, even with compatibility issues
    collections = qdrant_client.get_collections()
    print(f'Available collections: {[c.name for c in collections.collections]}')
    
    # Check if our collection exists
    collection_exists = any(c.name == COLLECTION_NAME for c in collections.collections)
    print(f'Collection {COLLECTION_NAME} exists: {collection_exists}')
    
except Exception as e:
    print(f'Error: {e}')
    print("Full traceback:")
    traceback.print_exc()