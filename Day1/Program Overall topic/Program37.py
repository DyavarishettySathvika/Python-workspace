text = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count = count + 1

print("Number of vowels:", count)
print("String checked")
print("Program completed")
print("Done")