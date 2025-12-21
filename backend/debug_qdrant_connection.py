"""Debug script to test Qdrant connection and search functionality"""

from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME
import cohere
from config import COHERE_API_KEY

print(f"Target collection: {COLLECTION_NAME}")
print(f"QDRANT_URL: {QDRANT_URL}")

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)

# Test 1: Basic connection
print("\n=== Test 1: Basic Connection ===")
try:
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
    collections = qdrant_client.get_collections()
    print(f"[SUCCESS] Connected successfully")
    print(f"Available collections: {[c.name for c in collections.collections]}")
except Exception as e:
    print(f"[ERROR] Connection failed: {e}")
    import traceback
    traceback.print_exc()

# Test 2: Check specific collection
print(f"\n=== Test 2: Check Collection '{COLLECTION_NAME}' ===")
try:
    collection_info = qdrant_client.get_collection(COLLECTION_NAME)
    print(f"[SUCCESS] Collection '{COLLECTION_NAME}' exists")
    point_count = collection_info.points_count if hasattr(collection_info, 'points_count') else 0
    print(f"Point count: {point_count}")
except Exception as e:
    print(f"[ERROR] Collection '{COLLECTION_NAME}' access failed: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Try embedding
print(f"\n=== Test 3: Test Embedding ===")
try:
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",
        texts=["test query"],
    )
    embedding = response.embeddings[0]
    print(f"[SUCCESS] Embedding created successfully, length: {len(embedding)}")
    print(f"Sample values: {embedding[:5]}")
except Exception as e:
    print(f"[ERROR] Embedding failed: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Try search if previous tests passed
print(f"\n=== Test 4: Test Search ===")
try:
    # First create embedding
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",
        texts=["What is ROS 2?"],
    )
    query_embedding = response.embeddings[0]

    # Then search
    search_results = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=2,
        with_payload=True
    )

    print(f"[SUCCESS] Search completed successfully")
    print(f"Number of results: {len(search_results)}")
    for i, result in enumerate(search_results):
        print(f"Result {i}: Score={result.score}, Text snippet: {result.payload['text'][:100]}...")

except Exception as e:
    print(f"[ERROR] Search failed: {e}")
    import traceback
    traceback.print_exc()

print(f"\n=== Debug completed ===")