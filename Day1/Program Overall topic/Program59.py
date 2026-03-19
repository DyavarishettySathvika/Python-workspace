# Check if a word is palindrome
text = input("Enter a word: ")

rev = text[::-1]

if text == rev:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")