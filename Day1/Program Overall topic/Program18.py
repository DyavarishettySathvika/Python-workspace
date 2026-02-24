# Example: Lists and Tuples in Python

# 1. Creating a list (mutable)
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Changing a list element
my_list[2] = 35
print("Modified List:", my_list)

# Adding an element to the list
my_list.append(60)
print("Extended List:", my_list)

print("-" * 40)

# 2. Creating a tuple (immutable)
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Trying to modify a tuple element would cause an error
# Uncommenting the next line will raise an exception
# my_tuple[1] = 10

# But we can access elements
print("First element of tuple:", my_tuple[0])

print("-" * 40)

# 3. Converting tuple to list
converted_list = list(my_tuple)
print("Tuple converted to List:", converted_list)

# Now we can change it
converted_list.append(6)
print("Modified Converted List:", converted_list)

print("-" * 40)

# 4. Looping through list and tuple
print("Loop through list:")
for item in my_list:
    print(item, end=" ")

print("\nLoop through tuple:")
for item in my_tuple:
    print(item, end=" ")
