from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.mongodb_url)
db = client[settings.database_name]
