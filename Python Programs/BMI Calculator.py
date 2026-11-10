# Calculates the BMI of a person.

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))
