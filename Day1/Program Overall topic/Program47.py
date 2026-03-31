n = int(input("Enter number of terms: "))

a = 2
b = 8

print("Fibonacci series:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c