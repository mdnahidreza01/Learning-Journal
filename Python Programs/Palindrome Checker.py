# Palindrome Checker:

print("\n>>> ===== Palindrome Checker ===== <<<\n")

text = input("Enter a word: ")

if text.lower() == text[::-1].lower():
    print("The Word is a Palindrome\n")
else:
    print("The Word is not a Palindrome\n")
