import asyncio
import os
from dotenv import load_dotenv

# Import the function to test
from main import get_docs

async def test_get_docs():
    """Test the get_docs function with different libraries and queries."""
    # Make sure we have the API key
    load_dotenv()
    if not os.getenv("SERPER_API_KEY"):
        print("Error: SERPER_API_KEY environment variable is not set.")
        return

    # Test cases
    test_cases = [
        {"library": "langchain", "query": "Chroma DB"},
        {"library": "openai", "query": "function calling"},
        {"library": "llama-index", "query": "document retrieval"}
    ]
    
    for case in test_cases:
        library = case["library"]
        query = case["query"]
        
        print(f"\nTesting get_docs with library={library}, query='{query}'")
        try:
            result = await get_docs(query=query, library=library)
            # Print part of the result to avoid overwhelming output
            print(f"Result: {result[:300]}...")
            print(f"Result length: {len(result)} characters")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_get_docs()) 