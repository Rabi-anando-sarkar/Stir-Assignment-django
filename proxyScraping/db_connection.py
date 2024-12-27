import pymongo
from django.conf import settings

url = settings.MONGODB_URI

client = pymongo.MongoClient(url)

db = client['twitter-trends']