from operations import addition as add
from operations import subtraction as sub
from operations import multiplication as mul
from operations import division as div

from operations import power
from converter import celcius_to_fahrenheit, bmi_calculator


print("\n=====CALCULATOR=====\n")

running = True
while running:
    print("===============================================")
    print("1. Calculatuion")
    print("2. Convertion")
    print("3. Exit")
    print("===============================================")

    try:
        choice = input("Choose an Option (1-3): ")
        if choice == '1':
            print("===============================================")
            print("CALCULATION OPTIONS:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("===============================================")

            operation = input("Choose and Option(1-4): ")
            number1 = float(input("\nEnter the First Number: "))
            number2 = float(input("Enter the Second Number: "))

            if operation == '1':
                print(f"\nAddition: {add(number1, number2):.2f}\n")
            elif operation == '2':
                print(f"Subtraction: {sub(number1, number2):.2f}")
            elif operation == '3':
                print(f"Multiplication: {mul(number1, number2):.2f}")
            elif operation == '4':
                print(f"Division: {div(number1, number2):.2f}\n")
            elif operation == '5':
                print(f"Power: {power(number1, number2)}")
            else:
                print("Invalid Input! Please Choose between (1-4)")

        elif choice == '2':

            print("CONVERSION OPTIONS:")
            print("===============================================")
            print("1. Celcius to Fahrenheit: ")
            print("2. BMI Calculator")
            print("===============================================")
            choice = input("Enter an Option (1-2): ")
            if choice == '1':
                temperature = float(input("Enter Temperature in Celcius: "))
                print(
                    f"{temperature} Degree Celcius is {celcius_to_fahrenheit(temperature)} in Fahrenheit Scale")
            elif choice == '2':
                weight = float(input("Enter your Weight: "))
                height = float(input("Enter your Height: "))
                print(f"Your BMI is: {bmi_calculator(weight, height):.2f}")
            else:
                print("Invalid Input! Please Choose from (1-2)")

        elif choice == '3':
            break

    except ValueError:
        print("Invalid Input! Enter Choice (1-3)")
