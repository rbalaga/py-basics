me = { "name": 'ram', 'age': 27 }

print(me)

values = me.values()
print(values)

print("name" in me)

friends = [
    {"name": "ram", "age": 27},
    {"name": "vignesh", "age": 21},
    {"name": "sundeep", "age": 23},
    {"name": "rajesh", "age": 24},
]

print(friends)

print(friends[0])


for friend in friends:
    print(f"{friend['name']}")