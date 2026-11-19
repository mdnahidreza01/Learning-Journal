
# Grading System:

print("===== Students Grading System =====")

running = True
while running:
    marks = int(input("Enter the Students Marks ('999' to Exit): "))

    if marks == 999:
        break

    elif marks >= 80 and marks <= 100:
        print("A+")
    elif marks >= 70 and marks < 79:
        print("A")
    elif marks >= 60 and marks <= 69:
        print("A-")
    elif marks >= 50 and marks <= 59:
        print("B")
    if marks >= 40 and marks <= 49:
        print("C")
    elif marks >= 33 and marks <= 39:
        print("D")
    elif marks >= 0 and marks < 33:
        print("F")
    else:
        print("Invalid Input! Try again")
