print("Find the Largest Number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("The largest number is:", largest)
print("Program finished")