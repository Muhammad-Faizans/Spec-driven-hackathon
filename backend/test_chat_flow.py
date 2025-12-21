"""Test script to simulate the full chat flow"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the functions from chat_gemini
from chat_gemini import query_qdrant, format_response

def test_full_chat_flow():
    print("Testing full chat flow...")
    
    # Test query
    query = "What is ROS 2?"
    print(f"Query: {query}")
    
    # Step 1: Test query_qdrant function
    print("\n1. Testing query_qdrant function...")
    try:
        search_results = query_qdrant(query)
        print(f"[SUCCESS] query_qdrant returned {len(search_results)} results")

        if len(search_results) > 0:
            print("Sample result payload:")
            first_result = search_results[0]
            print(f"  Score: {first_result.score}")
            print(f"  Source: {first_result.payload.get('source_file', 'Unknown')}")
            print(f"  Text snippet: {first_result.payload.get('text', '')[:100]}...")
        else:
            print("  No results returned")

    except Exception as e:
        print(f"[ERROR] query_qdrant failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Step 2: Test format_response function
    print("\n2. Testing format_response function...")
    try:
        response = format_response(query, search_results)
        print(f"[SUCCESS] format_response completed")
        print(f"Response length: {len(response)} characters")
        print(f"Response preview: {response[:200]}...")

        # Check if response contains book content
        if len(search_results) > 0 and "I don't have enough information" not in response and "I'm sorry" not in response:
            print("[SUCCESS] Response appears to use book context successfully!")
        else:
            print("[INFO] Response may not be using book context")

    except Exception as e:
        print(f"[ERROR] format_response failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_full_chat_flow()