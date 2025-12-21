from chat_gemini import query_qdrant, format_response

def test_full_chat():
    query = "Explain chapter 1 of the Physical AI and Humanoid Robotics curriculum"
    
    try:
        print("Step 1: Querying Qdrant...")
        search_results = query_qdrant(query)
        print(f"Found {len(search_results)} results from Qdrant")

        print("\nStep 2: Formatting response...")
        response = format_response(query, search_results)
        print("Response formatted successfully")
        
        print(f"\nFinal Response:\n{response}")
        
    except Exception as e:
        print(f"Error in chat process: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_full_chat()