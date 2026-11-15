# Age Calculator:
from datetime import date

is_running = True

while is_running:
    try:
        birth_year = int(input("Enter birth year ('0' to Exit): "))
        current_year = date.today().year

        if birth_year == 0:
            break
        elif birth_year > current_year:
            print("Invalid Input! Enter the corrrect year")

        age = current_year - birth_year

        print("Your age is:", age)
    except (ValueError):
        print("Invalid Input! Enter a valid integer Number that represents a correct Year")
