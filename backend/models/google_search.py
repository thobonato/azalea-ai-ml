# backend/models/google_search.py
import requests
from googleapiclient.discovery import build
import os

def google_search(query):
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CSE_ID')
    
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    
    if 'items' in result:
        return result['items'][0]['snippet']
    return "No results found."