#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
#->They are 2 identity operators 1.is and 2.is not
#is(Returns True if both variables are the same object)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
#->Using numbers
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   
print(a is c)   

#is not(Returns True if both variables are not the same object)
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)
#Using integers
x = 10
y = 10
z = 20
print(x is not y) 
print(x is not z)  

#Difference Between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)