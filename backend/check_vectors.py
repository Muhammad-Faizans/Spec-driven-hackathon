from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

def check_collection():
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    result = client.count(collection_name=COLLECTION_NAME)
    print(f'Collection {COLLECTION_NAME} has {result.count} vectors')

if __name__ == "__main__":
    check_collection()