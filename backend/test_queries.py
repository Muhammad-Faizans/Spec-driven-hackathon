"""
Test with different queries to see what works
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chat_gemini import query_qdrant, format_response

def test_different_queries():
    queries = [
        "What is Physical AI?",
        "Introduction to robotics",
        "What are the learning objectives?",
        "Explain robot motion control"
    ]
    
    for query in queries:
        print(f"\n=== Testing query: '{query}' ===")
        try:
            search_results = query_qdrant(query)
            print(f"Found {len(search_results)} search results")
            
            if search_results:
                # Show first result as example
                first_result = search_results[0]
                print(f"First result preview: {first_result.payload['text'][:100]}...")
            
            response = format_response(query, search_results)
            print(f"Response: {response[:200]}...")
            
        except Exception as e:
            print(f"Error with query '{query}': {e}")

if __name__ == "__main__":
    test_different_queries()