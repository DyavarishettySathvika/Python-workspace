text = input("Enter a word: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")