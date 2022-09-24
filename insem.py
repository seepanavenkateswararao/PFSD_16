from pymongo import MongoClient

db=MongoClient("mongodb://127.0.0.1:27017")

client=db['KLU']

Student_data=client.Students

s1=[{"Name":"HARSHA","id":"123456789","year":"2","percentage":"90"},
    {"Name":"SHIVA","id":"124567893","year":"1","percentage":"85"},
    {"Name":"TEJA","id":"456789123","year":"3","percentage":"76"},
    {"Name":"RAM","id":"789632541","year":"4","percentage":"89"}]
Student_data.insert_many(s1)
