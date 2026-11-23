from operations import addition as add
from operations import subtraction as sub
from operations import multiplication as mul
from operations import division as div


number1 = float(input("Enter the value for Number1: "))
number2 = float(input("Enter the value for Number2: "))


print(f"Addition: {add(number1, number2)}")
print(f"Subtraction: {sub(number1, number2)}")
print(f"Multiplication: {mul(number1, number2)}")
print(f"Division: {div(number1, number2)}")
