import json
with open("Student.json","r") as f:
    data=json.load(f)
for i in data:
    print(i)