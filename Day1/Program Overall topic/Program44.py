n = int(input("Enter number of terms: "))

a = 9
b = 3

print("Fibonacci series:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c