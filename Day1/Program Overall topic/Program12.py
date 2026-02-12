# 4. Check if number is even or odd
num = int(input("Enter a number: "))      # Get a number
if num % 2 == 0:                          # Check remainder
    print(f"{num} is even")
else:
    print(f"{num} is odd")

print("Done checking!")