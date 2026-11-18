# Calculates the BMI of a person.
print("=====BMI Calculator=====")

running = True
while running:
    weight = float(input("Enter your weight (kg) ('0' to exit): "))
    if weight == 0:
        break
    height = float(input("Enter your height (meters): "))

    bmi = weight / (height ** 2)

    print("Your BMI is:", round(bmi, 2))
