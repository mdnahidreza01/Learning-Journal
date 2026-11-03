print("============== MENU ==============")

menu = {
    "chips": 1.50,
    "coke": 1.75,
    "noodles": 2.00,
    "juice": 1.5,
    "popcorn": 4,
    "nachos": 3.25,
    "cake": 2.75
}


cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("==================================")


while True:
    snacks = input("Please select an item (Q to Quit): ").lower()
    if snacks == 'q':
        break
    elif menu.get(snacks) is not None:
        cart.append(snacks)

print("============== YOUR ORDER ==============")

for snacks in cart:
    total += menu.get(snacks)
    print(snacks, end=" ")

print()
print(f"Total price is: ${total:.2f}")
