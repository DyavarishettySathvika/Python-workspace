#Copy list
#Use the Copy() method(You can use the built-in List method copy() to copy a list.)
list1=['Shift','Control','Insert','Delete','Capslock']
mylist=list1.copy()
print(mylist)
#Using numerical numbers
list2=[645,873,937,526]
mylist=list2.copy()
print(mylist)

#Use the list() method(Another way to make a copy is to use the built-in method list())
thislist=['Addition','Substraction','Multiplication','Division']
mylist=list(thislist)
print(thislist)
thislist=[97,24,42,6577]
mylist=list(thislist)
print(thislist)

#Using the Slice Operator(You can also make a copy of a list by using the : (slice) operator.)
list=['Travel','Songs','Vibe','Moblie']
mylist=list[:]
print(list)
list=[836,8623,63,24]
mylist=list[:]
print(list)