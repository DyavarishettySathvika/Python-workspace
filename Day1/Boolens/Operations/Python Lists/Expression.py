#->Expression
Tress=['Mango','Neem','Grapes','Banyan','PineApple']
newlist=[x.upper() for x in Tress]
print(newlist)
newlist = [x.lower() for x in Tress]
print(newlist)

#We can add a string to list and print the same string iterable.
Nonveg=['Chicken','Mutton','Fish','Prawns','Crab']
newlist=('My Favourite' for x in Nonveg)
print(newlist)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
Nonveg=['Chicken','Mutton','Soups','Prawns','Crab']
newlist=[x if x!='Soups' else 'Fish' for x in Nonveg]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x== "banana" else "orange" for x in fruits]
print(newlist)
