from pymongo.mongo_client import MongoClient
from os import getenv

uri = getenv("MONGODB_URI")

client = MongoClient(uri)
print(f"Connected to {uri}")

metrics = client.users.metrics