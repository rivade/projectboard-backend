import os
import pymongo
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

def init():
    load_dotenv()

    uri = os.getenv('MONGODB_URI')

    global db_name
    db_name = os.getenv('MONGODB_DB_NAME')

    global client
    client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

def test_connection():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    print(client.list_database_names())

def get_projects():
    db = client[db_name]
    collection = db['projects']
    return list(collection.find({}, {'_id': 0}))