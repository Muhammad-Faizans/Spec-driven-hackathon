from chat_gemini import query_qdrant

def test_search_detailed():
    query = "Explain chapter 1 of the Physical AI and Humanoid Robotics curriculum"
    
    try:
        print("Querying Qdrant...")
        search_results = query_qdrant(query)
        print(f"Found {len(search_results)} results from Qdrant")
        
        for i, result in enumerate(search_results):
            print(f"\nResult {i+1}:")
            print(f"  ID: {result.id}")
            print(f"  Score: {result.score}")
            print(f"  Payload type: {type(result.payload)}")
            print(f"  Payload keys: {list(result.payload.keys()) if hasattr(result.payload, 'keys') else 'N/A'}")
            
            if hasattr(result.payload, 'get'):
                text_content = result.payload.get('text', '')
                source_content = result.payload.get('source_file', 'N/A')
            else:
                # If payload is not a dict-like object
                text_content = getattr(result.payload, 'text', '') if hasattr(result.payload, 'text') else str(result.payload)
                source_content = getattr(result.payload, 'source_file', 'N/A') if hasattr(result.payload, 'source_file') else 'N/A'
            
            print(f"  Text preview: {text_content[:200] if text_content else 'No text'}...")
            print(f"  Source: {source_content}")
        
    except Exception as e:
        print(f"Error in search: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_search_detailed()