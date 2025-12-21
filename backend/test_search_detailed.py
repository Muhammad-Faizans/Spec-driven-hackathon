from chat_gemini import query_qdrant

def test_search():
    try:
        results = query_qdrant('Explain chapter 1')
        print('Search successful!')
        print(f'Found {len(results)} results')
        for i, result in enumerate(results):
            print(f'Result {i+1}:')
            print(f'  ID: {result.id}')
            print(f'  Score: {result.score}')
            print(f'  Text preview: {result.payload["text"][:100]}...')
            print()
    except Exception as e:
        print(f'Error during search: {e}')
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_search()