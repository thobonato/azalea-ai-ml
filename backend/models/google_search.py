# backend/models/google_search.py
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def google_search(query):
    api_key = os.getenv("GOOGLE_CSE_ID")
    cse_id = os.getenv("GOOGLE_API_KEY")

    if not api_key or not cse_id:
        raise ValueError("API key and Custom Search Engine ID must be set in environment variables.")
    
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    
    if 'items' in result:
        return result['items'][0]['snippet']
    return "No results found."

if __name__ == "__main__":
    # This is a test query to ensure the function works when the script is run directly
    print(google_search("What is the terminal command to remove directory?"))
