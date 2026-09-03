import os
import pymongo
from bson import ObjectId
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
    return [_json_safe(project) for project in collection.find()]

def _json_safe(value):
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value

def post_project(project):
    db = client[db_name]
    collection = db['projects']
    result = collection.insert_one(project.copy())
    return {
        "id": str(result.inserted_id),
        **project
    }