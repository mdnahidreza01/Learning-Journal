# This Program takes input of all data types and prints the Output


# INPUT Section:

# 1. INTEGER:
integer = int(input("Enter a an integer number: "))

# 2. FLOATING:
floating = float(input("Enter a decimal (floating point) number: "))

# 3. BOOLEAN:
boolean = (input("Enter a a Boolean value: ")).lower

# 4. COMPLEX:
complex_number = complex(input("Enter a Complex number (e.g. 2 + 3j): "))

# 5. STRING:
string = input("Enter a String: ")

# 6. LIST:
list = input("Enter list elements (comma separated): ").split(",")

# 7. TUPLE:
tuple = tuple(input("Enter tuple elements (comma separated): ").split(","))

# 8. SET:
set = set(input("Enter set elements (comma separated): "))

# 9. DICTIONARY:
print("Input the value of Key and Value for the dictionary.")
dictionary = {}

dictionary_key = input("Enter dictionary key: ")
dictionary_value = input("Enter dictionary value: ")

dictionary[dictionary_key] = dictionary_value


# OUTPUT SECTION:

print("========OUTPUT=========\n")

datatypes = {
    "Integer": integer,
    "Float": floating,
    "Boolean": boolean,
    "Complex": complex_number,
    "String": string,
    "List": list,
    "Tuple": tuple,
    "Set": set,
    "Dictionary": dictionary,
}

for name, value in datatypes.items():
    print(f"{name} : {value}")
    print(f"Data Type : {type(value).__name__}")
