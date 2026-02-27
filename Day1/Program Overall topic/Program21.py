name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Welcome", name)
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
else:
    print("You are an adult")
print("Now let's do a simple math!")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum is", sum)
print("Goodbye!")