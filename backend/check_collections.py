from qdrant_client import QdrantClient
import os
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

def check_collections():
    print('Collection name from config:', COLLECTION_NAME)

    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    
    try:
        collections = client.get_collections()
        print('Available collections:', [c.name for c in collections.collections])

        for coll in collections.collections:
            try:
                result = client.count(collection_name=coll.name)
                print(f'Collection {coll.name} has {result.count} vectors')
            except Exception as e:
                print(f'Error counting vectors in {coll.name}: {e}')
                
    except Exception as e:
        print(f'General error: {e}')
        
        # Try connecting without prefer_grpc
        try:
            client_alt = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
            collections = client_alt.get_collections()
            print('Alternative connection - Available collections:', [c.name for c in collections.collections])
            
            for coll in collections.collections:
                try:
                    result = client_alt.count(collection_name=coll.name)
                    print(f'Collection {coll.name} has {result.count} vectors')
                except Exception as e_alt:
                    print(f'Error counting vectors in {coll.name} (alt): {e_alt}')
        except Exception as alt_e:
            print(f'Alternative connection also failed: {alt_e}')

if __name__ == "__main__":
    check_collections()