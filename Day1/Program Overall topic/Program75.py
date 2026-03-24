text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")