"""
Test the Gemini response and see which models are used
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google import genai
from config import GEMINI_API_KEY, MAX_TOKENS_RESPONSE, TEMPERATURE
from chat_gemini import query_qdrant

def test_updated_format_response():
    query = "Explain chapter 1"
    
    print("Getting search results...")
    search_results = query_qdrant(query)
    print(f"Got {len(search_results)} search results")
    
    # Prepare context from search results (copying the logic from format_response)
    context_parts = []

    # Check if search_results exist and have content
    if search_results:
        for result in search_results:
            # Handle different possible structures of result objects
            if hasattr(result, 'payload'):
                text = result.payload.get('text', '') if result.payload else ''
                source = result.payload.get('source_file', 'Unknown source') if result.payload else 'Unknown source'
            else:
                # If result is a dict or other format
                text = result.get('text', '') if isinstance(result, dict) else ''
                source = result.get('source_file', 'Unknown source') if isinstance(result, dict) else 'Unknown source'

            score = getattr(result, 'score', 0) if hasattr(result, 'score') else result.get('score', 0) if isinstance(result, dict) else 0

            context_parts.append(f"Source: {source}\nRelevance Score: {score}\nContent: {text}\n---")

    combined_context = "\n".join(context_parts)
    print(f"Combined context length: {len(combined_context)}")
    print(f"First 500 chars of context: {combined_context[:500]}...")

    # Create the same prompt that format_response creates
    prompt = f"""
    You are an AI assistant for the Physical AI & Humanoid Robotics Curriculum.
    Answer the user's query based ONLY on the provided context from the curriculum.
    It's critical that you only provide information that is directly contained in the context below.
    Do not provide general AI knowledge that is not in the context.
    If the context doesn't contain relevant information, respond with: "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base."

    Context:
    {combined_context}

    User Query:
    {query}

    Response:
    """

    print("\nTesting with newer model names...")
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    
    # Try the NEW models in the same order as updated format_response
    available_models = ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-1.5-pro', 'gemini-1.5-flash']
    
    for model_name in available_models:
        try:
            print(f"Trying model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=MAX_TOKENS_RESPONSE,
                    temperature=TEMPERATURE
                )
            )
            
            print(f"Model {model_name} succeeded!")
            print(f"Response: {response.text}")
            
            # Check if the response contains the "no relevant info" message
            if "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base." in response.text:
                print("⚠️  The model returned the 'no relevant info' message")
            else:
                print("✅ The model returned a normal response")
            
            return response.text
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue
    
    print("All models failed!")
    return "All models failed"


if __name__ == "__main__":
    test_updated_format_response()