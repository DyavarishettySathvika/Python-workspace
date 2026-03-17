text = input("Enter a string: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print("Original:", text)
print("Reversed:", rev)
print("Done")