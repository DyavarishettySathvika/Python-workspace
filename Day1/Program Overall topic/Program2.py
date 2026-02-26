# Add two numbers entered by the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)
# Loop through and print numbers
for i in range(1, 8):
    print(i)
    num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")