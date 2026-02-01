# 1. String Slicing
text = "Hello, Sathvika!"
name1 = text[0:5]      # Gets characters from index 0 up to (but not including) 5
name2 = text[7:]       # Gets characters from index 7 to the end

print("Original:", text)
print("name1:", name1)   # "Hello"
print("name2:", name2)   # "World!"

# 2. Modify String (Strings are immutable -> so we create a new one)
# Example: Change "World" to "Universe"
new_text = text[:7] + "Universe!"
print("Modified:", new_text)

# 3. String Concatenation
first = "Good"
second = "Morning"
combined = first + " " + second   # Adding a space in between
print("Concatenated:", combined)

# 4. String Formatting
name = "Alice"
age = 25

# Method 1: f-string (Python 3.6+)
formatted1 = f"My name is {name} and I am {age} years old."

# Method 2: format()
formatted2 = "My name is {} and I am {} years old.".format(name, age)

print("Formatted (f-string):", formatted1)
print("Formatted (.format()):", formatted2)
