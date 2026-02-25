# Create a list of numbers
numbers = [10, 20, 90, 40, 30,60,70]

# Print the whole list
print("List:", numbers)

# Access elements using index
print("First element:", numbers[0])
print("Third element:", numbers[2])

# Add a new element to the list
numbers.append(60)
print("After adding an element:", numbers)

# Remove an element from the list
numbers.remove(30)
print("After removing an element:", numbers)

# Loop through the list and print each item
for item in numbers:
    print("Number:", item)