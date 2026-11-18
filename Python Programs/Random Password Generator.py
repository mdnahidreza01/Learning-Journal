import random
import string

print("\n=====RANDOM PASSWORD GENERATOR=====")
running = True
while running:
    length = int(
        input("\nEnter the character length for the password ('0' to Exit): "))
    if length == 0:
        break
    characters = string.ascii_letters + string.digits

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your Random Generated Password is:", password)
