from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ykwql.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List -- ")
print(db.list_collection_names())
