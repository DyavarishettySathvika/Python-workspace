# Program to find the largest number in a list
numbers = [10,20,12,30,15,25]

largest = numbers[0]   # assume first is largest

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)