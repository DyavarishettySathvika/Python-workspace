#type()
#From Python's perspective, lists are defined as objects with the data type 'list':<class 'list'>
my_list = [1, 2, 3]
print(type(my_list))   
nums = [1, 2, 3]   
print(type(nums))                
words = ["a", "b", "c"]    
print(type(words))       
mixed = [1, "hello", 3.14, True]
print(type(mixed))  
nested = [[1, 2], [3, 4]] 
print(type(nested))        

#->The list constructor
#It is also possible to use the list() constructor when creating a new list.
a = list()            
print(a)              
b = list((1, 2, 3))   
print(b)             
c = list("Hello")     
print(c)             

print(list(range(5)))          
print(list({10, 20, 30}))     
print(list({'a':1, 'b':2}))     