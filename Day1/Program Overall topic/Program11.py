# 3. Collect 5 items and show list
items = []                             # Empty list
print("Enter 5 shopping items:")

for i in range(5):                     # Loop 5 times
    item = input(f"Item {i+1}: ")
    items.append(item)                 # Add to list

print("\nYour shopping list:")
for index, thing in enumerate(items):  # Print each
    print(f"{index+1}. {thing}")

print("Happy shopping!")
