# Calculates the price final price/actual Price of a product after Discount:

price = float(input("Enter the Price of the Product: "))
discount = float(input("Enter the Discount for thr product(%): "))

final_price = price * (1 - discount / 100)

print(f"The final price is {round(final_price, 2)} after discount!")
