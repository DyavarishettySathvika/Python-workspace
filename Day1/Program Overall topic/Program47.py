n = int(input("Enter number of terms: "))

a = 58
b = 9

print("Fibonacci series:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c