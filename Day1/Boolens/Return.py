#->Functions can Return a Boolean******
def myFunction() :
  return True
print(myFunction())
#Here we performed a function and used my if we use my or not used my the output will same

#If its True
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#If its False
def myFunction() :
  return False
if myFunction():
  print("YES!")
else:
  print("NO!")


#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
x = []
print(isinstance(x, int))

#->Using Int and Float
x = 200
print(isinstance(x, int))   
print(isinstance(x, float)) 

#->Using String
name = "Alice"
print(isinstance(name, str))    
print(isinstance(name, (int, str)))  

#Check a List
numbers = [1, 2, 3]
print(isinstance(numbers, list))  
print(isinstance(numbers, dict))  

#Multiple types
value = 3.14
print(isinstance(value, (int, float)))  





