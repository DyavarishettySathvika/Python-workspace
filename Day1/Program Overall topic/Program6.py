# Program to count how many times 'apple' appears
fruits = ["apple", "banana", "apple", "orange", "apple"]

count = 0
for fruit in fruits:
    if fruit == "apple":
        count += 1

print("Apple appears", count, "times in the list")