# Create database:
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.
# MongoDB will create the database if it does not exist, and make a connection to it.
#  a database is not created until it gets content.

# to check if a database exists:
print(myclient.list_database_names())   #Return a list of your system's databases

# OR
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
  
# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
# MongoDB will create the collection if it does not exist.

# Creating a collection called "customers":

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]   #database
mycol = mydb["customers"]

# to check if collection exist:

print(mydb.list_collection_names())
# OR
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

# insert 

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

# return _id 

mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

# insert multiple doc

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# insert multiple doc with specified id

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# find - In MongoDB we use the find and findOne methods to find data in a collection.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)

# find all doc

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find():
  print(x)
  
# return only selected fields
# Return only the names and addresses, not the _ids:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
# You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):

# Querry
# filtering the result - When finding documents in a collection, you can filter the result by using a query object.
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

# Example
# Find documents where the address starts with the letter "S" or higher:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
# Example
# Sort the result alphabetically by name:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)
  
# Sort the result reverse alphabetically by name:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
  
# To delete one document, we use the delete_one() method.
# The first parameter of the delete_one() method is a query object defining which document to delete.
# If the query finds more than one document, only the first occurrence is deleted.

# Example
# Delete the document with the address "Mountain 21":

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

# Delete Many Documents
# To delete more than one document, use the delete_many() method.
# The first parameter of the delete_many() method is a query object defining which documents to delete.

# Example
# Delete all documents were the address starts with the letter S:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

# Delete All Documents in a Collection
# To delete all documents in a collection, pass an empty query object to the delete_many() method:

# Example
# Delete all documents in the "customers" collection:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Delete Collection
# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

# Example
# Delete the "customers" collection:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()
# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.

# update one doc

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
 
# update many
# Update all documents where the address starts with the letter "S":

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# Limit the Result
# To limit the result in MongoDB, we use the limit() method.
# The limit() method takes one parameter, a number defining how many documents to return.

# Consider you have a "customers" collection:
# Customers
# {'_id': 1, 'name': 'John', 'address': 'Highway37'}
# {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
# {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
# {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
# {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
# {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
# {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
# {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
# {'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
# {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
# {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
# {'_id': 12, 'name': 'William', 'address': 'Central st 954'}
# {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
# {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
# Example
# Limit the result to only return 5 documents:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
