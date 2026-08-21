import json
Student=[
    {
    "name":"Dipak",
    "age":24,
    "Address":"Odisha"
    },
    {
    "name":"Papun",
    "age":22,
    "Address":"Odisha"
    },
    {
    "name":"Abhinash",
    "age":12,
    "Address":"Odisha"
    },
    {
    "name":"Pankaj",
    "age":47,
    "Address":"Odisha"
    }
    ]
with open("Student.json","w")as f:
    json.dump(Student,f)
    