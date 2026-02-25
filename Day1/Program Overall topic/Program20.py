# Convert tuple to list
tuple_data = (100, 600, 500)
list_data = list(tuple_data)
list_data.append(400)
print("List from tuple:", list_data)

# Convert list back to tuple
new_tuple = tuple(list_data)
print("New tuple:", new_tuple)