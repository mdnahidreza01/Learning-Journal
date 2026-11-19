
print("----- Celcius to Fahrenheit Scale -----\n")
running = True
while running:
    control = input("Enter 'x' to exit or 'Any Key' to continue: ").lower()
    if control == 'x':
        break
    else:
        celcius_scale = float(input("\nEnter Temperature in Celsius Scale: "))

        fahrenheit_scale = (celcius_scale * 9/5) + 32
        print("==============================================")
        print(
            f"{celcius_scale} degree Celcius is {fahrenheit_scale} degree in Fahrenheit Scale")
        print("==============================================")
