#Membership operators are used to test if a sequence is presented in an object
#They are 2 operators 1.in and 2.not in
#in(Returns True if a sequence with the specified value is present in the object)
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
fruits = ["apple", "banana", "cherry"]
print("mango" in fruits)

#not in(Returns True if a sequence with the specified value is not present in the object)
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
fruits = ["apple", "banana", "cherry"]
print("apple" not in fruits)

#Membership in Strings The membership operators also work with strings:
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)
