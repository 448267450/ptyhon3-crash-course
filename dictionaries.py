person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

# print(person, type(person))

# print(person['first_name'])
# print(person.get('last_name'))

person['phone'] = '312-789-1345'


# print(person.keys())

# print(person.items())
person2 = person.copy() 
person2['city'] = 'Boston'

# del(person['age'])
# person.pop('phone')

# person.clear()

# print(person)

print(len(person2))

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people, type(people))

print(people[1]['name'])