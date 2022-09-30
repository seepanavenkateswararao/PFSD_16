import json
employee=[{
    'patient id':12345,
    'name':"tripathy",
    'Age': 19,
    'Mobile':6303312125,
    'email':'sachidanandatripathy789@gmail.com',
    'Address':'Tuni'
    },
    {
    'patient id':4567,
    'name': 'venky',
    'Age': 19,
    'Mobile': 23456789,
    'email': 'seppanana789@gmail.com',
    'Address': 'visakhapatnam'}
]
json_string=json.dumps(employee,indent=4) #used to convert python object to json object
print(json_string)
with open('emp.json','w')as file:
    json.dump(employee,file,indent=4) # used to convrt serialisation

with open('emp.json','r') as f:
    r=json.load(f)
    data=list(r)
    for row in data:
        print(row)