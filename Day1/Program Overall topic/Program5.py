# Program to find the largest number in a list
numbers = [12, 65, 10, 23, 33]

largest = numbers[0]   # assume first is largest

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)