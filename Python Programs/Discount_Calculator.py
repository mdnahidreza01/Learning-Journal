# Calculates the price final price/actual Price of a product after Discount:

while True:
    print("=====DISCOUNT CALCULATOR=====")
    price = float(input("Enter the Price of the Product (0 to exit): "))

    if price == 0:
        break
    else:
        discount = float(input("Enter the Discount for the product (in %): "))
        final_price = price * (1 - discount / 100)
        print(f"The final price is {round(final_price, 2)} after discount!")
