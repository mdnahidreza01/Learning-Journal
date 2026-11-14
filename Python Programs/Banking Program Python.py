# Banking Program Python:

def show_balance():
    print("----------------------")
    print(f"Your balance is: ${balance:.2f}")
    print("----------------------")


def withdraw():
    amount = float(input("Enter the amount to withdraw: "))

    if amount > balance:
        print("----------------------")
        print("Insufficient Funds!")
        print("----------------------")
        return 0
    elif amount < 0:
        print("----------------------")
        print("Amount must be greater than 0")
        print("----------------------")
        return 0
    else:
        return amount


def deposite():
    amount = float(input("Enter an amount to be Deposited: "))

    if amount < 0:
        print("----------------------")
        print("That's not a valid amount")
        print("----------------------")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("=======================")
    print("BANKING PROGRAM PYTHON")
    print("=======================")
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposite()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("This is not a valid Choice!")
print("=======================")
print("Thank you! Have a nice day!")
