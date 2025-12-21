from chat_gemini import embed_query
import os
from google import genai
from config import (
    GEMINI_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY,
    COLLECTION_NAME, SEARCH_TOP_K, MAX_TOKENS_RESPONSE, TEMPERATURE
)

def format_response_debug(query, search_results):
    """Debug version of format_response to see what's happening."""
    # Prepare context from search results
    context_parts = []

    print(f"Input query: {query}")
    print(f"Number of search results: {len(search_results)}")
    
    # Check if search_results exist and have content
    if search_results:
        for i, result in enumerate(search_results):
            print(f"\nProcessing result {i+1}:")
            print(f"  Result type: {type(result)}")
            print(f"  Has payload attr: {hasattr(result, 'payload')}")
            print(f"  Has text attr: {hasattr(result, 'text')}")
            print(f"  Has score attr: {hasattr(result, 'score')}")
            
            # Handle different possible structures of result objects
            if hasattr(result, 'payload'):
                print(f"  Payload type: {type(result.payload)}")
                if hasattr(result.payload, 'get'):
                    print(f"  Payload is dict-like with keys: {list(result.payload.keys())}")
                    text = result.payload.get('text', '') if result.payload else ''
                    source = result.payload.get('source_file', 'Unknown source') if result.payload else 'Unknown source'
                else:
                    print(f"  Payload is not dict-like")
                    text = getattr(result.payload, 'text', '') if hasattr(result.payload, 'text') else str(result.payload)
                    source = getattr(result.payload, 'source_file', 'Unknown source') if hasattr(result.payload, 'source_file') else 'Unknown source'
            else:
                # If result is a dict or other format
                if isinstance(result, dict):
                    text = result.get('text', '')
                    source = result.get('source_file', 'Unknown source')
                else:
                    # If result is neither object with payload nor dict
                    text = str(result)
                    source = 'Unknown source'

            score = getattr(result, 'score', 0) if hasattr(result, 'score') else (
                result.get('score', 0) if isinstance(result, dict) else 0)
            
            print(f"  Extracted text (length {len(text)}): {text[:100]}...")
            print(f"  Extracted source: {source}")
            print(f"  Extracted score: {score}")

            context_parts.append(f"Source: {source}\nRelevance Score: {score}\nContent: {text}\n---")

    combined_context = "\n".join(context_parts)
    print(f"\nCombined context length: {len(combined_context)}")
    print(f"Combined context first 200 chars: {combined_context[:200]}...")

    # If no context was found from RAG, fail hard
    if not combined_context.strip():
        print("ERROR: No context was found from RAG")
        return "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base."

    # Create a prompt for Gemini that includes the context
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

    # Use the Gemini model to generate a response
    # Using models that are typically available, with fallbacks
    model_name = None
    available_models = ['gemini-1.0-pro', 'gemini-1.5-flash', 'gemini-pro']
    
    print(f"\nUsing prompt (first 500 chars): {prompt[:500]}...")

    for name in available_models:
        try:
            print(f"Trying model: {name}")
            model = genai.GenerativeModel(name)
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=MAX_TOKENS_RESPONSE,
                    temperature=TEMPERATURE
                )
            )
            model_name = name
            print(f"Model {name} worked successfully!")
            break  # Use the first working model
        except Exception as e:
            print(f"Model {name} failed: {e}")
            continue  # Try the next model

    # If no model worked, provide a hard failure response
    if model_name is None:
        print("ERROR: No model worked")
        return "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base."

    # Check if the response indicates lack of information
    response_text = response.text if hasattr(response, 'text') else str(response)
    print(f"Model response: {response_text[:200]}...")
    
    if "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base." in response_text:
        # If the AI correctly identified that it lacks info, return that message
        print("Gemini returned 'no relevant info' message")
        return response_text

    # Otherwise, return the full response
    print("Returning Gemini's response")
    return response_text

def test_format_response():
    query = "Explain chapter 1 of the Physical AI and Humanoid Robotics curriculum"
    
    # Simulate search results structure
    class MockResult:
        def __init__(self, id_val, score_val, payload):
            self.id = id_val
            self.score = score_val
            self.payload = payload
    
    mock_results = [
        MockResult(3, 0.7712737, {
            'source_file': 'C:\\Users\\LENOVO\\my-qwen-project\\backend\\..\\my-docusaurus-site\\docs\\intro.md',
            'text': 'Physical AI & Humanoid Robotics Curriculum Welcome to the comprehensive curriculum on Physical AI & Humanoid Robotics! This program is designed to take you from foundational concepts to advanced implementations in creating intelligent physical agents.',
            'chunk_id': 3
        }),
        MockResult(5, 0.7549956, {
            'source_file': 'C:\\Users\\LENOVO\\my-qwen-project\\backend\\..\\my-docusaurus-site\\docs\\physical-ai-humanoid-robotics\\physical-ai-humanoid-robotics.md',
            'text': 'Physical AI & Humanoid Robotics Complete Curriculum Overview Welcome to the comprehensive Physical AI & Humanoid Robotics curriculum. This program provides an in-depth exploration of the cutting-edge...',
            'chunk_id': 5
        })
    ]
    
    print("Testing format_response with mock results...")
    response = format_response_debug(query, mock_results)
    print(f"\nFinal response:\n{response}")


if __name__ == "__main__":
    # Configure Google Generative AI
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    test_format_response()