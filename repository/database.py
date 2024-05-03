from pymongo import MongoClient
from .config import Config

def get_db():
    client = MongoClient(Config.uri)
    db = client[Config.mongo_init_db_name]
    return db

collection = get_db()['datetime_for_aggregation']
