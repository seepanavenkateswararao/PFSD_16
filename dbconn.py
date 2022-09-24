#import mongoclient
from pymongo import MongoClient

#create an istance
client=MongoClient("mongodb://127.0.0.1:27017")

#create databse
db=client['KLU-B16']

#Creat collection
stud_data=db.students

#creat documents
s1={"no":"123","name":"abc"}
s2=[{"no":"456","name":"def"},
    {"no":"789","name":"abc"},
    {"no":"111","name":"xyz"}]

# insert documents
stud_data.insert_one(s1)

# #insert many documents
# stud_data.insert_many(s2)
#
# #Retrive or fetch data single document
# a={"no":"123"}
# stud_data.find_one(a)
#
# #retrive multiple documents
# b={"name":"abc"}
# for x in stud_data.find(b):
#     print(x)
#
# #delete single doc
# c={"no":"456"}
# stud_data.delete_one(c)
#
# #delete many doc
# d={"name":"abc"}
# stud_data.delete_many(d)
#
# #updation doc
# e={"no":"111"}
# f={"$set":{"no":"222"}}
# stud_data.update_one(e,f)

#close connection
client.close()

