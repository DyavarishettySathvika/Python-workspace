#->Logical operators are used to combine conditional statements
#AND,OR,NOT
#->And Logical operator (Returns True if both statements are true)
x = 5
print(x > 3 and x < 10)
x=-86
print(x<-7 and x-54)
x = 5
print(x > 0 and x < 10)


#->OR Operator(Returns True if one of the statements is true)
x = 5
print(x > 3 or x < 4)
y=87
print(y>54 or x<=65)
#->Taking 2 values
x=76
y=67
print(x>y or x<y)
x = 5
print(x < 5 or x > 10)


#NOT Operator(Reverse the result, returns False if the result is true)
x = 5
print(not(x > 3 and x < 10))
x=4
y=6
print (not(x>y and x<y))
x = 5
print(not(x > 3 and x < 10))

