# Multiplication Quiz:
import random

print("==============================")
print("     MULTIPLICATION QUIZ")
print("==============================")

total_questions = 10
score = 0

for question in range(1, total_questions + 1):

    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    correct_answer = num1 * num2

    print(f"\nQuestion {question}/{total_questions}")

    try:
        answer = int(input(f"{num1} × {num2} = "))

        if answer == correct_answer:
            print("Correct! Great job!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {correct_answer}")

    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n==============================")
print("         QUIZ RESULT")
print("==============================")

print(f"Total Questions : {total_questions}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {total_questions - score}")
print(f"Final Score     : {score}/{total_questions}")
print(f"Percentage      : {(score / total_questions) * 100:.1f}%")

if score == total_questions:
    print("Excellent! Perfect Score!")
elif score >= 7:
    print("Very Good! Keep it up!")
elif score >= 5:
    print("Good effort! Keep practicing!")
else:
    print("Keep practicing. You can do better!")
