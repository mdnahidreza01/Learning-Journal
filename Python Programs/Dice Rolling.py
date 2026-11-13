import random


# Unicode Characters used:
# ● ┌ ─ ┐ │ └ ┘
print("=====Dice Rolling=====")

dice_ASCII = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

dice = []
total = 0
number_of_dice = int(input("Enter the number of Dice to roll: "))

for die in range(number_of_dice):
    dice.append(random.randint(1, 6))

for die in range(number_of_dice):
    for line in dice_ASCII.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"Total: {total}")
