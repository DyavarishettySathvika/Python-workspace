#Syntax of List Comprehension
#newlist = [expression for item in iterable if condition == True] This is the syntax for list comprehension 
#Condition (The condition is like a filter that only accepts the items that evaluate to True)
list=['Books','Bags','Laptop','Phone','Macbook']
newlist=[x for x in list if x!='Laptop']
print(newlist)
list=['Rishika','Srujana','Keerthana','Sathvika','Vaishnavi']
newlist=[x for x in list if x=='Vaishnavi']
print(newlist)

#->without if condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
name=['Spandhan','Vardhan','Sowmya','Harshh','Sneha']
newlist=[x for x in name]
print(newlist)


