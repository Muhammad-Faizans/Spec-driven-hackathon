"""
Step-by-step debugging of the chat functionality
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chat_gemini import query_qdrant, format_response
from config import COLLECTION_NAME

def test_step_by_step():
    query = "Explain chapter 1"
    
    print("=== STEP 1: Querying Qdrant ===")
    try:
        search_results = query_qdrant(query)
        print(f"[SUCCESS] Found {len(search_results)} results from Qdrant")

        print("\n=== STEP 1b: Inspecting search results ===")
        for i, result in enumerate(search_results):
            print(f"Result {i+1}:")
            print(f"  - ID: {result.id}")
            print(f"  - Score: {result.score}")
            print(f"  - Text preview: {result.payload['text'][:100] if result.payload and 'text' in result.payload else 'N/A'}...")
            print(f"  - Payload keys: {list(result.payload.keys()) if result.payload else 'N/A'}")
            print()
    except Exception as e:
        print(f"[FAILED] Error in Qdrant query: {e}")
        import traceback
        traceback.print_exc()
        return

    print("\n=== STEP 2: Formatting response ===")
    try:
        formatted_response = format_response(query, search_results)
        print(f"[SUCCESS] Response formatted")
        print(f"Response content: {formatted_response}")
    except Exception as e:
        print(f"[FAILED] Error in response formatting: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    test_step_by_step()