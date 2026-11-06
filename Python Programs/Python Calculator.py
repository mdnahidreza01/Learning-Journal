
while True:
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Exit")

    choice = input("\nPlease Choose an Operation (1-8): ")

    if choice == '8':
        print("Calculator closed. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice! Try again.")
        continue

    try:
        number1 = float(input("Enter first Number: "))
        number2 = float(input("Enter second Number: "))

        if choice == '1':
            result = number1 + number2
            operator = '+'

        elif choice == '2':
            result = number1 - number2
            operator = '-'

        elif choice == '3':
            result = number1 * number2
            operator = '*'

        elif choice == '4':
            if number2 == 0:
                print("Error! Cannot divide by zero.")
                continue
            result = number1 / number2
            operator = '/'

        elif choice == '5':
            if number2 == 0:
                print("Error! Cannot use zero as divisor.")
                continue
            result = number1 % number2
            operator = '%'

        elif choice == '6':
            result = number1 ** number2
            operator = '**'

        elif choice == '7':
            if number2 == 0:
                print("Error! Cannot divide by zero.")
                continue
            result = number1 // number2
            operator = '//'

        print("\n---------- RESULT ----------")
        print(f"{number1:g} {operator} {number2:g} = {result:g}")
        print("----------------------------")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
