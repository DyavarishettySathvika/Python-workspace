x = "awesome"
#Outside function
def myfunc():
  print("Python is " + x)
myfunc()

#Outside Function
x = "Simple"
def myfunc():
  x = "Easy"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#The Global Keyword
#Outside Function
def myfunc():
  global x
  x = "Keyword"
myfunc() # It is a mandatory thing in global variables
print("Python is " + x)

#Outside Function
x = "Language"
def myfunc():
  global x
  x = "Interesting"
myfunc()
print("Python is " + x)


