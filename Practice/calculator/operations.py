def addition(num1: float, num2: float):
    return num1 + num2


def subtraction(num1: float, num2: float):
    return num1 - num2


def multiplication(num1: float, num2: float):
    return num1 * num2


def division(num1: float, num2: float):
    if num2 == 0:
        print("Number cannot be divided by Zero!")
    return num1 / num2


def power(base: int, exponent: int):
    return base ** exponent
