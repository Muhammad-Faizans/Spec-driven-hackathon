#!/usr/bin/env python3
"""Simple debug script to test chat functionality step by step"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chat_gemini import query_qdrant, format_response
from config import GEMINI_API_KEY

print(f"GEMINI_API_KEY is set: {bool(GEMINI_API_KEY)}")

test_query = 'What is the introduction to robotic nervous systems?'
print(f'Testing query: {test_query}')

# Step 1: Test query_qdrant
print("\nStep 1: Testing query_qdrant function...")
search_results = query_qdrant(test_query)
print(f'Found {len(search_results)} search results')

if search_results:
    print('Sample result payload keys:', list(search_results[0].payload.keys()) if hasattr(search_results[0], 'payload') else 'No payload attribute')
    print('Sample result text preview:', str(search_results[0].payload.get('text', ''))[:200] if hasattr(search_results[0], 'payload') else 'No payload')

# Step 2: Test format_response
print("\nStep 2: Testing format_response function...")
try:
    response = format_response(test_query, search_results)
    print(f'Response: {response}')
except Exception as e:
    print(f'Error in format_response: {e}')
    import traceback
    traceback.print_exc()