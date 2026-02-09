#Iterable(The iterable can be any iterable object, like a list, tuple, set etc.)
#Same like List Comprehision syntax but we used range here.
newlist=[x for x in range(18)]
print(newlist)
#UpperCase using list Comprehension
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)
#Lowercase using list comprehension
words = ["apple", "banana", "cherry"]
lower_words = [w.lower() for w in words]
print(lower_words)

#with different condition
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x for x in range(10) if x > 8]
print(newlist)