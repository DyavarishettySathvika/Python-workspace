#Remove Items(Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items)
thistuple=('A','B','C','D','E','F')
y=list(thistuple)
y.remove('D')
thistuple=tuple(y)
print(thistuple)

thistuple=('St','Martins','Kompally','Hyderabad','UGC')
y=list(thistuple)
y.remove('UGC')
thistuple=tuple(y)
print(thistuple)

thistuple=('Goat','Fish','Chicken','Mutton')
y=list(thistuple)
y.remove('Fish')
thistuple=tuple(y)
print(thistuple)


