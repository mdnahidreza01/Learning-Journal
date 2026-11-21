# LIST COPREHENSION:
# ===================================================================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print element(n), for each element(n) in numbers:
my_list = []
for n in numbers:
    my_list.append(n)
print(my_list)

# Shorten/Comprehension:
my_list = [n for n in numbers]
print(my_list)


# print square of element(n), for each element(n) in numbers:
my_list = [n*n for n in numbers]
print(my_list)


# print n for each 'n' in numbers if 'n' is even:
list = [n for n in numbers if n % 2 == 0]
print(list)


# (letter, number) pair for each letter in 'abcd' and each number '0123'
List = [(letter, number) for letter in 'abcd' for number in range(4)]
print(List)


# DICT COPREHENSION:
# ===================================================================================
names = ['John', 'Jack', 'Jones']
jobs = ['Engineer', 'Doctor', 'Scientist']

# print (name, job) for each name, job in zip(names, jobs) lists
dict = {name: job for name, job in zip(names, jobs)}
print(dict)


# print (name, job) for each name, job in zip(names, jobs) lists if I don't want Jones in dict:
Dict = {name: job for name, job in zip(names, jobs) if name != 'Jones'}
print(Dict)


# SET COPREHENSION:
# ===================================================================================

Numbers = [1, 2, 1, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10]
# print n for each 'n' in Numbers:
my_set = {n for n in Numbers}

# Generator Expressions:
my_gen = (n*n for n in numbers)
for i in my_gen:
    print(i)
