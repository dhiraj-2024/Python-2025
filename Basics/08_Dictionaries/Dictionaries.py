# creating a dictionary
person = {
    "name": "abc",
    "city": "xyz",
    "age": 21,
    "mobile_no": 823749387
}

# print dictionary
print(person)

# length of dictionary
print(len(person))

# print keys, values, and items
print("keys:", person.keys())
print("values:", person.values())
print("items:", person.items())

# access value using get()
print(person.get("city"))

# change values inside dictionary
person["name"] = "ram"
print(person)

# update multiple items
person.update({"age": 44, "city": "nagpur"})
print(person)

# add new key-value pair
person["is_married"] = True
print(person)

# remove item using pop()
print(person.pop("city"))

# popitem() removes last inserted item
print(person.popitem())

# clear() removes all items (commented to keep data)
# person.clear()
print(person)

# -------------------------------------
# looping through a dictionary
# -------------------------------------

cars = {
    1: "bmw",
    2: "audi",
    3: "lambo",
    4: "toyota",
    5: "ferrari"
}

# print whole dictionary
print(cars)

# print only keys
for key in cars:
    print(key)

# print only values
for value in cars.values():
    print(value)

# print both key and value
for key, value in cars.items():
    print(key, ":", value)

# -------------------------------------
# copy a dictionary
# -------------------------------------

fruits = {
    1: "banana",
    2: "orange",
    3: "pineapple",
    4: "apple"
}

print(fruits)

# copy using copy()
vegiAndFruits = fruits.copy()
print(vegiAndFruits)

# copy using dict()
newdic = dict(fruits)
print(newdic)
