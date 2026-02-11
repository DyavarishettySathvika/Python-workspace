#Case Insensitive Sort(By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters)
list1=['Sathvika','Bunny','lucky','Vinnu']
list1.sort()#Here the Capital letters string will print first,and next small letters string will print
print(list1)
list2=['Vaish','vardhan','soumya','Bunny']
list2.sort()
print(list2)

#In some cases we use built-in functions use str.lower as a key function
list1=['Sathvika','Bunny','lucky','Vinnu']
list1.sort(key=str.lower)
print(list1)
list2=['Vaish','vardhan','soumya','Bunny']
list2.sort(key=str.lower)
print(list2)