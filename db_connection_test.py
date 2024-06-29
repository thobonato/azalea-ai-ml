from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Make sure this comes before trying to get environment variables
load_dotenv()

def test_mongodb():
    uri = os.getenv('MONGODB_URI')
    print("URI: ", uri)  # This will print the MongoDB URI to verify it's loaded correctly

    client = MongoClient(uri)
    db = client['azalea_db']  # replace 'myDatabaseName' with your actual database name
    collection = db['test_collection']

    # Try inserting a document
    insert_result = collection.insert_one({'name': 'test', 'value': 123})
    print('Document inserted with id:', insert_result.inserted_id)

    # Try retrieving a document
    document = collection.find_one({'name': 'test'})
    print('Document retrieved:', document)

    client.close()

if __name__ == '__main__':
    test_mongodb()
