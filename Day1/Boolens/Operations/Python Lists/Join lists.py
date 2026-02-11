#Join two Lists(There are several ways to join, or concatenate, two or more lists in Python.One of the easiest ways are by using the + operator.)
list1=['w','r','s','v','p']
list2=[3,5,6,9,7,1,2]
list3=list1+list2
print(list3)
list1="Sathvika"
list2="Dyavarishetty"
list3=list1+list2
print(list3)

list1 = ['a','e','i','o','u']
list2 = [1,2,3,4,5]
for x in list2:
  list1.append(x)
print(list1)

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1=['ab','cd','ef','gh','ij']
list2=[1,2,3,4,5]
list1.extend(list2)
print(list1)
list1=[1244]
list2=[3294]
list1.extend(list2)
print(list1)
