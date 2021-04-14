from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ykwql.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

def printstudent(doc):
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")


docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    printstudent(doc)
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Jones"}})
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc = db.students.find_one({"student_id": "1007"})
printstudent(doc)    