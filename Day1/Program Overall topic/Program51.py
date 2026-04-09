n = int(input("Enter terms: "))

a = 1
b = 3

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\nDone")
print("Fibonacci generated")