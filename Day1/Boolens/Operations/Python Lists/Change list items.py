#Python-Change List Items
#Change Item Value(To change the value of a specific item, refer to the index number)
mylist=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
mylist[4]='Sunday'
print(mylist)
mylist[-3]='Sunday'

#Change a Range of Item Values(To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values)
thislist=["Tera Bin","Meem Se Mohabbat","Sher","Meri Zindagi hai tu"]
thislist[1:3]=["Kabhi main kabhi tum","Iqtidar"]
print(thislist)
thislist[1:-3]=["Kabhi main kabhi tum","Iqtidar"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items(To insert a new list item, without replacing any of the existing values, we can use the insert() method.The insert() method inserts an item at the specified index)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
mylist=["Pink","Black","Green","Blue"]
mylist.insert(1,"Purple")
print(mylist)
mylist.insert(2,"Gray")
print(mylist)