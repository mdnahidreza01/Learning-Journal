# PASSWORD STRENGTH CHECKER

import string


print("=====Password Strength Checker=====")

password = input("Enter the password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1

levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]

print("Password strength:", levels[score])
