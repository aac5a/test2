#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.reddit
stories = db.stories

'''
def find():

    print "find, reporting for duty"

    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc

if __name__ == '__main__':
    find()
'''

db = connection.school
people = db.people

doc = {"name": "Andrew Erlichson", "company": "MongoDB",
              "interests": ['running', 'cycling', 'photography']}

try:
        people.insert_one(doc)   # first insert
        del(doc['_id'])
        people.insert_one(doc)   # second insert
        del (doc['_id'])

except Exception as e:
        print "Unexpected error:", type(e), e
