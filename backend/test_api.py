import requests
import json

def test_chatbot():
    try:
        resp = requests.post('http://localhost:8000/chat', json={'query': 'Introduction to robotics'})
        print(f"Status Code: {resp.status_code}")
        print(f"Response: {resp.text}")
        
        # Try another query that we know works from our previous testing
        resp2 = requests.post('http://localhost:8000/chat', json={'query': 'Explain robot motion control'})
        print(f"\nSecond query Status Code: {resp2.status_code}")
        print(f"Second query Response: {resp2.text}")
    except Exception as e:
        print(f"Error making request: {e}")
        print("Make sure the backend server is running on http://localhost:8000")

if __name__ == "__main__":
    test_chatbot()