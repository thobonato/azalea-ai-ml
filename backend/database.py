from pymongo import MongoClient
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('MONGODB_URI'))
db = client['azalea_db']
conversations = db['conversations']
energy_consumption = db['energy_consumption']

def save_conversation(conversation_id, query, response, model):
    conversations.update_one(
        {'_id': conversation_id},
        {'$push': {'messages': {'query': query, 'response': response, 'model': model}}},
        upsert=True
    )

def get_conversation(conversation_id):
    return conversations.find_one({'_id': conversation_id})

def save_energy_data(model, energy_data):
    energy_consumption.update_one(
        {'model': model},
        {'$inc': {
            'total_cost': energy_data['cost'],
            'total_water': energy_data['water'],
            'total_bag': energy_data['bag'],
            'total_feet': energy_data['feet'],
            'count': 1
        }},
        upsert=True
    )

def get_energy_data():
    return list(energy_consumption.find({}))

if __name__ == "__main__":
    save_conversation(mock_conversation_id, mock_query, mock_response, mock_model)
    save_energy_data(mock_model, mock_energy_data)

    # Fetch and display saved data
    conversation = get_conversation(mock_conversation_id)
    energy_data = get_energy_data()

    print(conversation)
    print(energy_data)
