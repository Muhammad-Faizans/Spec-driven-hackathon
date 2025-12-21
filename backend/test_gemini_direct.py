"""
Test the Gemini response content directly
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google import genai
from config import GEMINI_API_KEY, MAX_TOKENS_RESPONSE, TEMPERATURE

def test_gemini_directly():
    query = "Explain chapter 1"
    
    # Create context similar to what's passed to format_response
    context = """
Source: C:\\Users\\LENOVO\\my-qwen-project\\backend\\..\\my-docusaurus-site\\docs\\intro.md
Relevance Score: 0.28331342
Content: - Master the mathematical foundations of robot motion and control
- Gain expertise in robotic perception and environmental interaction
- Explore cutting-edge techniques in robot learning and adaptation
---

Source: C:\\Users\\LENOVO\\my-qwen-project\\backend\\..\\my-docusaurus-site\\docs\\physical-ai-humanoid-robotics\\module-1\\introduction.md
Relevance Score: 0.2763202
Content:  In the next chapter, we will tie together sensors and actuators with the brain of the nervous system analogy in robotics.
---

Source: C:\\Users\\LENOVO\\my-qwen-project\\backend\\..\\my-docusaurus-site\\docs\\physical-ai-humanoid-robotics\\module-2\\introduction.md
Relevance Score: 0.2195234
Content: Module 2: The Robotic Brain - AI and Machine Learning in Robotics
Welcome to Module 2 of Physical AI & Humanoid Robotics! Here, we explore the intelligence that powers a robot's actions - its "brain".
---
    """

    # Create the same prompt that format_response creates
    prompt = f"""
    You are an AI assistant for the Physical AI & Humanoid Robotics Curriculum.
    Answer the user's query based ONLY on the provided context from the curriculum.
    It's critical that you only provide information that is directly contained in the context below.
    Do not provide general AI knowledge that is not in the context.
    If the context doesn't contain relevant information, respond with: "No relevant information found in the Physical AI & Humanoid Robotics Curriculum. Cannot answer based on available knowledge base."

    Context:
    {context}

    User Query:
    {query}

    Response:
    """

    print("Testing Gemini directly with the prompt:")
    print(f"First 500 chars of prompt: {prompt[:500]}...")
    print("=" * 50)
    
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    
    # Try the models in the same order as format_response
    available_models = ['gemini-1.5-flash', 'gemini-1.0-pro', 'gemini-pro']
    
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
    test_gemini_directly()