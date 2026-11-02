# DataTypes (List, Tuple, Set, Dictionary)

# List = []
# Tuple = ()
# Set = {}
# Dictionary = {}

# LIST OPERATIONS:
fruits = ['apple', 'banana', 'grapes', 'pineapple', 'coconut', 'banana']
# print(dir(fruits))
# print(help(fruits))

print(len(fruits))
print(fruits[3])
print(fruits[0::2])
print('apple' in fruits)
fruits[0] = 'jackfruit'
print(fruits)
fruits.append("blueberry")
fruits.remove("grapes")
fruits.insert(3, "avocado")
fruits.sort()
fruits.reverse()
fruits.index("coconut")
fruits.pop(3)
fruits.copy()
fruits.pop()
fruits.extend("avocado")
print(f"The number of banana is {fruits.count("banana")}")


print(fruits)


# TUPLE OPERATIONS:
fruits = ('apple', 'banana', 'grapes', 'pineapple', 'coconut', 'banana')
# print(dir(fruits))
# print(help(fruits))

print(len(fruits))
print(fruits[3])
print(fruits[0::2])
print('avocado' in fruits)


fruits.index("coconut")
print(f"The number of banana is {fruits.count("banana")}")

for fruit in fruits:
    print(fruit)


# DICTIONARY OPERATIONS:
capitals = {
    "Bangladesh": "Dhaka",
    "USA": "Washington D.C",
    "China": "Beijing",
    "Russia": "Moscow"
}

if capitals.get("China"):
    print("The capial exists")
else:
    print("The capital doesn't exist")

capitals.update({"Japan": "Tokyo"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
keys = capitals.keys()
values = capitals.values()
print(keys)
print(values)


for key in capitals.keys():
    print(key)

print("\n")

for value in capitals.values():
    print(value)

items = capitals.items()

for key, value in capitals.items():
    print(f"{key} : {value}")
print("\n")
