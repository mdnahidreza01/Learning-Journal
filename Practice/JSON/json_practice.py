# #''' Javascript Object Notation '''

import json

people_string = '''
{
    "people": [
        {
            "name": "Abir Hasan",
            "phone": "+880128820",
            "emails" : ["abirhasan@gmail.com", "abir2394@gmail.com"],
            "has_license": true
        },
        {
            "name": "Hasibur Rahman",
            "phone": "+880439820",
            "emails" : ["hasiburrahman@gmail.com", "hasibur@gmail.com"],
            "has_license": false

        }
    ]
}
'''

# json string to python object[dict]
data = json.loads(people_string)
# print(type(data['people']))
# print(data)


# deletes the phone from every person in the people List:
for person in data['people']:
    del (person['phone'])

# python object to json string
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


with open('faculties.json', 'r') as file:
    data = json.load(file)

for faculty in data['faculties']:
    del faculty['Subject_Code']


with open('new_faculties.json', 'w') as file:
    json.dump(data, file, indent=2)
    print(f"Faculty['Subject_Code'] Deleted successfully")
