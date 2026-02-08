#Loop through a list(You can loop through the list items by using a for loop)
list=['Sathvika','Bunny','Lucky','Teju']
for x in list:
    print(x)
#Use the range() and len() functions to create a suitable iterable
list=['Dell','HP','Lenova','Macbook']
for x in range (len(list)):
    print(list[x])
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
count = 1
while count <= 5:
    print(count)
    count += 1  # increase count each time

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
list= ['Python','Java','C','C++']
[print(x) for x in list]