thistuple=('Apple','Banana','Grapes','Cherry')
y=list(thistuple)
y.append('Orange')
thistuple=tuple(y)

thistuple=('Bat','Ball','Bag','Cat')
y=('Books',)
thistuple +=y
print(thistuple)

tup = (1, 2, 3)
tup = tup + (4,)
print(tup) 

tup = (10, 20, 30)
tup = tup + (40, 50)
print(tup)   