import random
import string

print("\n=====RANDOM PASSWORD GENERATOR=====")

length = int(input("\nEnter the character length for the password: "))
characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your Random Generated Password is:", password)
