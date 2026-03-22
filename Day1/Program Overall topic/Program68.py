import string

password = input("Enter password: ")
strength = 0

if any(c.islower() for c in password):
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c in string.punctuation for c in password):
    strength += 1

print("Strength level:", strength, "/4")