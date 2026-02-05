#->Remove List Items
#Remove Specifies Item(The remove() method removes the specified item)
thislist=['Vinnu','Lucky','Teja','Bunny']
thislist.remove('Teja')
print(thislist)
#If there are more than one item with the specified value, the remove() method removes the first occurrence
list=['Vinayaka','Tejaswi','Venkat','Sathvika']
list.remove('Tejaswi')
print(list)

#Remove Specified Index(The pop() method removes the specified index)
thislist = ["Neem", "Mango", "Carrot"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#The del keyword also removes the specified index
list=['One','Two','Three','Four']
del list[0]
print(list)
#The del keyword can also delete the list completely.
thislist = ["Blue", "Black", "Pink"]
del list[1]
print(thislist)

#->Clear the list(The clear() method empties the list.The list still remains, but it has no content.)
thislist = ["Bussiness", "Teacher", "Lawyer"]
thislist.clear()
print(thislist)