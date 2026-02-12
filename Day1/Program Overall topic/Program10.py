# 2. Basic calculator
print("Simple Calculator")

a = float(input("Enter first number: "))   # First value
b = float(input("Enter second number: "))  # Second value

print("Sum:", a + b)                        # Add
print("Difference:", a - b)                 # Subtract

print("Product:", a * b)                    # Multiply
if b != 0:                                  # Safe division
    print("Division:", a / b)
else:
    print("Cannot divide by zero!")

print("Calculation done!")