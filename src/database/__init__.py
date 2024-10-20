from pymongo import MongoClient
from ..config import settings

cluster = MongoClient(settings.MONGO_URI)
db = cluster[settings.MONGO_NAME]