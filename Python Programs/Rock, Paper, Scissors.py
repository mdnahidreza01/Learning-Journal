import random


def play_round():
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = input("Choose rock, paper or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        return 0, 0

    print("Computer:", computer)

    if player == computer:
        print("Draw!")
        return 0, 0

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("You win this round!")
        return 1, 0

    else:
        print("Computer wins this round!")
        return 0, 1


player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    print("\n--- New Round ---")

    p, c = play_round()

    player_score += p
    computer_score += c

    print(f"Score: You {player_score} - {computer_score} Computer")

print("\n========== GAME RESULT ==========")

if player_score == 3:
    print("Congratulations! You won!")
else:
    print("Computer won!")
