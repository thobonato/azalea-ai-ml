from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGODB_URI'))
db = client['azalea_db']
conversations = db['conversations']

def save_conversation(conversation_id, query, response, model):
    conversations.update_one(
        {'_id': conversation_id},
        {'$push': {'messages': {'query': query, 'response': response, 'model': model}}},
        upsert=True
    )

def get_conversation(conversation_id):
    return conversations.find_one({'_id': conversation_id})