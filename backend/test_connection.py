import sys
import traceback
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

print("Testing Qdrant connection...")

try:
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    print('Qdrant client created successfully')
    
    collection_info = qdrant_client.get_collection(collection_name=COLLECTION_NAME)
    print(f'Collection exists with {collection_info.vectors_count} vectors')
    print(f'Collection info type: {type(collection_info)}')
    
except Exception as e:
    print(f'Error: {e}')
    print("Full traceback:")
    traceback.print_exc()