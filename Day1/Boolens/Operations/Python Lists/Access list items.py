#->Access list items
#List items are indexed and you can access them by referring to the index number
thislist=['Sathvika','Bunny','Lucky']
print(thislist[1])
mylist=['Sadanand','Saritha','Saikrishna','Krishnaveni']
print(thislist[0])
#The first item has index 0

#->Negative Indexing
#Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
thislist=['Sathvika','Bunny','Lucky']
print(thislist[-1])
print(thislist[0])

#->Range of Indexing
#You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items
mylist=['Maths','Science','Chemistry','Telugu','Hindi','Social']
print(mylist[3:6])
print(mylist[-2:-3])

#Examples
thislist=['Manasa','Choti','Spandhan','Vardhan','Soumya','Rishika','Srujana','Rinky']
print(mylist[:2])
print(mylist[4:])
print(mylist[3:6])
print(mylist[:-2])
print(mylist[-6:])
print(mylist[-1-2])
print(mylist[-2+3])#It does first -2(Srujana) operation after comes to +3(Vardhan)
print(mylist[3-5])

#->Check if item Exists(To determine if a specified item is present in a list use the in keyword)
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
   print("Yes, 'apple' is in the fruits list")#Space used becaus if condition exits
if 'mango' in thislist:
   print("Yes, 'Mango' is in the fruits list")
else:
    ("Mango does not in the list")


my_list = [10, 20, 30, 40]
if 30 in my_list:
    print("Item exists")
else:
    print("Item does not exist")