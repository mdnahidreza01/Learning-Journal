# Palindrome Checker:


print("\n>>> ===== Palindrome Checker ===== <<<\n")

running = True
while running:
    text = input("Enter a word ('x' to exit): ")
    if text.lower() == 'x':
        break
    else:
        if text.lower() == text[::-1].lower():
            print("The Word is a Palindrome\n")
        else:
            print("The Word is not a Palindrome\n")
