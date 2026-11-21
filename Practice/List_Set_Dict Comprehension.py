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


#
