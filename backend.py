import os

import pymongo
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from fastapi import FastAPI

load_dotenv()

uri = os.getenv('MONGODB_URI')

client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
app = FastAPI()

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(client.list_database_names())