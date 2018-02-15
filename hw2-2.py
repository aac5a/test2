import pymongo
import sys

# establish a connection to the server, and use it to get a handle on the scores collection.
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database and the scores collection.
db = connection.students
grades = db.grades
x=0
try:
        for x in range(1,200):
            doc = grades.find({"student_id":x, "type":"homework"},{"student_id":1,"score":1})
            if doc[0]["score"] > doc[1]["score"]:
                id_to_remove = doc[1]["_id"]
                #print(id_to_remove)
                grades.delete_one({"_id": id_to_remove})
            else:
                grades.delete_one({"_id": doc[0]["_id"]})

        #print doc[1]["score"]

except Exception as e:
        print "Unexpected error:", type(e), e

#print doc