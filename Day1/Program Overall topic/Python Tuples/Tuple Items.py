# Create a tuple items with 3 items
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(my_tuple[0])   
print(my_tuple[1])   
print(my_tuple[2])   
# simple tuple
tup = (10, 20, 30)
print(tup)
#Mixed Tuple          
mixed = (1, "hello", True, 3.14)
print(mixed)        
numbers = (1, 2, 3, 4, 5)
#Indexing and Slicing
print(numbers[0])   
print(numbers[2:4]) 
#Concatenation (Joining Tuples)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
joined = t1 + t2
print(joined)     
#Loop through a Tuple
items = ("apple", "banana", "cherry")
for x in items:
    print(x)