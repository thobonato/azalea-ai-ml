from pymongo import MongoClient
import certifi
import os

# Load environment variables if using a .env file
from dotenv import load_dotenv
load_dotenv()

def test_mongodb():
    # Connect to MongoDB
    uri = os.getenv("MONGODB_URI")
    client = MongoClient(uri, tlsCAFile=certifi.where())
    
    # Select your database
    db = client['azalea_db']
    
    # Select your collection
    collection = db['user_data']
    
    # Insert a document
    insert_result = collection.insert_one({'name': 'test', 'value': 123})
    print(f'Document inserted with id {insert_result.inserted_id}')
    
    # Retrieve the document
    retrieved_document = collection.find_one({'name': 'test'})
    print(f'Document retrieved: {retrieved_document}')

    # Close the MongoDB connection
    client.close()

if __name__ == '__main__':
    test_mongodb()
