from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ykwql.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("-- INSERT STATEMENTS --")
fred = {
 "first_name": "Fred","last_name": "Frogger","student_id":"1007" 
}
fred_student_id = db.students.insert_one(fred).inserted_id
print(f"Inserted student record {fred['first_name']} {fred['last_name']} into the students collection with document_id {fred_student_id}")
fred = {
 "first_name": "Fred","last_name": "Frog","student_id":"1008" 
}
fred_student_id = db.students.insert_one(fred).inserted_id
print(f"Inserted student record {fred['first_name']} {fred['last_name']} into the students collection with document_id {fred_student_id}")
fred = {
 "first_name": "Fred","last_name": "Froggy","student_id":"1009" 
}
fred_student_id = db.students.insert_one(fred).inserted_id
print(f"Inserted student record {fred['first_name']} {fred['last_name']} into the students collection with document_id {fred_student_id}")
