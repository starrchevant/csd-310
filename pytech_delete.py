from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ykwql.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#db.collection_name.remove({"fieldname":"value"})

def printstudent(doc):
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

#instruction 3
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    printstudent(doc)
# instruction 4 
Doc = {
 "first_name": "Bugs","last_name": "Bunny","student_id":"1010" 
}
db.students.insert_one(Doc)
print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id 607d0935215566751f9f6106")
print("")
#instruction 5
print("-- DISPLAYING STUDENT TEST DOC --")
doc = db.students.find_one({"student_id": "1010"})
printstudent(doc)
#instruction 6
db.students.delete_one({"student_id": "1010"})
#instruction 7
#docs = db.students.find({})
#print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    printstudent(doc)
