# backend/models/google_search.py
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def google_search(query):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CSE_ID')
    
    print("API Key:", api_key)  # Debug print to verify the correct API key is loaded
    print("CSE ID:", cse_id)    # Debug print to verify the correct CSE ID is loaded

    if not api_key or not cse_id:
        raise ValueError("API key and Custom Search Engine ID must be set in environment variables.")
    
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    
    if 'items' in result:
        return result['items'][0]['snippet']
    return "No results found."

if __name__ == "__main__":
    # This is a test query to ensure the function works when the script is run directly
    print(google_search("OpenAI"))
