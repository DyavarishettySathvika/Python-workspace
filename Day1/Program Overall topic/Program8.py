print("=== JOIN / COMBINE LISTS ===")

# Example lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 1) Using + operator (simple and easy)
joined1 = list1 + list2
print("Using + operator:", joined1)

# 2) Using extend() (changes the original list1)
listA = [1, 2, 3]
listA.extend(list2)
print("Using extend():", listA)

# 3) Using unpacking (*)
joined2 = [*list1, *list2]
print("Using unpacking *:", joined2)

# 4) Using a for loop (manual add)
joined3 = []
for item in list1:
    joined3.append(item)
for item in list2:
    joined3.append(item)
print("Using for loop:", joined3)

# 5) Using list comprehension
joined4 = [item for item in list1] + [item for item in list2]
print("Using list comprehension:", joined4)
print("\n=== COPY / CLONE LISTS ===")

original = [10, 20, 30, 40, 50]

# 1) Using copy() method
copy1 = original.copy()
print("Using copy():", copy1)

# 2) Using slicing [:]
copy2 = original[:]
print("Using slicing:", copy2)

# 3) Using list() constructor
copy3 = list(original)
print("Using list():", copy3)

# 4) Using list comprehension
copy4 = [item for item in original]
print("Using list comprehension:", copy4)

# 5) (For nested lists) Using deepcopy
import copy
nested = [[1, 6], [3, 5]]
deep_copy = copy.deepcopy(nested)
print("Using deepcopy for nested:", deep_copy)