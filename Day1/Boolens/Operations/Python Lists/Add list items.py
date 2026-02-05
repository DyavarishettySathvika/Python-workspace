#Add List Items
#Append Items(To add an item to the end of the list, use the append() method)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.append("Pine apple")
print(thislist)

#Extend List(To append elements from another list to the current list, use the extend() method.)
thislist = ["apple", "banana", "cherry"]
fruits = ["mango", "pineapple", "papaya"]
thislist.extend(fruits)
print(thislist)
a = [1, 2]
b = [3, 4]
a.extend(b)   # adds items of b into a
print(a)

#Add Any Iterable(The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 

