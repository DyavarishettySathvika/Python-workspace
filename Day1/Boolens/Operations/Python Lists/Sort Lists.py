#Sort List Alphanumerically(List objects have a sort() method that will sort the list alphanumerically, ascending, by default)
#In this topic the strings are numerical numbers with sort in a order
list=['a','t','i','r','e','u','p','k','w']
list.sort()
print(list)
list=['Janu','Monkey','Apple','Square']
list.sort()
print(list)

#Numerical numbers
thislist=[23,54,12,67,75]
thislist.sort()
print(thislist)
thislist=[45.6,7.6,43.4,6.7,4.2,5.1]
thislist.sort()
print(thislist)

#Sort Descending(To sort descending, use the keyword argument reverse = True)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
thislist = ["Butterfly", "Parrot", "Peacock", "Duck", "Pegion"]
thislist.sort(reverse = True)
print(thislist)

#Using numerical numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
thislist = [10.0, 7.50, 5.65, 3.82, 4.23]
thislist.sort(reverse = True)
print(thislist)

#Asending  Order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = False)
print(thislist)
thislist = ["Butterfly", "Parrot", "Peacock", "Duck", "Pegion"]
thislist.sort(reverse = False)
print(thislist)

#Using numerical numbers(Asecending order)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = False)
print(thislist)
thislist = [10.0, 7.50, 5.65, 3.82, 4.23]
thislist.sort(reverse = False)
print(thislist)