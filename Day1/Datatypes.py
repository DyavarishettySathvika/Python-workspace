#->String
print('Sathvika')
#Double quotes are single quotes are donented for string.
print("Sathvika")


#->Int
print(376)
#or
x=43
print(x)

#->Float
print(34.5)
x=87.9
print(x)

#->Complex
print(1j)
x = 1j
print(x)
#for complex numbers we need to give spacing

#->List and tuple
#we can put square brackets[] and () and {}
x=["Sathvika", "Sadanand", "Saritha", "Venkat"]
print(x)
x=("Sathvika", "Sadanand", "Saritha", "Venkat")
print(x)
x={"Sathvika", "Sadanand", "Saritha", "Venkat"}
print(x)

#->Range
x=range(10)
print(x)
#If we add (list(x)) it will print as 0 to 10
print(list(x))

#->dict Dictionary 
x = {"name" : "Bunny", "age" : 20}
print(x)
#with spacing and without spacing the dict will same.But we can't use different symbols (),[]
x = {"name":"Lucky","age":16}
print(x)

#->Set
x = {"Apple", "Banana", "Cherry"}
print(x)
#with spacing and without spacing the set will same.Any type of (),[],{} symbol is used in set datatype
y=('Sathvika','Bunny')
print(y)
z=['Dyavrishetty','Sathvika']
print(z)

#->frozonset
x = frozenset({"apple", "banana", "cherry"})
#combination of (){} this two symbols called frozenset
print(x)

#->bool
x=True
print(x)
y=False
print(y)

#->byte 
x = b"Hello"
print(x)
print(type(x)) 
#In byte we should give b infront of string

#->bytearray
x = bytearray(12)
print(x)
#For bytearray we need to give bytearray in input 
#display the data type of x:
print(type(x)) 

#->None
x = None
#display x:
print(x)
#display the data type of x:
print(type(x)) 




 


