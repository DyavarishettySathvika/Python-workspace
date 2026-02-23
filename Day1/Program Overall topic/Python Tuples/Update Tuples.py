#Update Tuples(Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.)
#Change Tuple Values()
x=('Sathvika','Bunny','Lucky','Vinay')
y=list(x)
y[1]='Dyavarishetty'
x=tuple(y)
print(x)

x=('Bag','Book','Pencil','Bottle')
y=list(x)
y[3]='Pen'
x=tuple(y)
print(x)