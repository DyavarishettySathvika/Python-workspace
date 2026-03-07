num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial not possible")
else:
    i = 1
    while i <= num:
        fact = fact * i
        i = i + 1

print("Factorial of", num, "is", fact)
print("Program finished")
print("Thank you")