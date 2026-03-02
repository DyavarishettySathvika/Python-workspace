def greet():
    print('Hi, Welcome to my class!')
    print('After return')
result=greet()
print(result)

def greet(name):
    print(f'Hi {name}, welcome to my class!')
greet('Bunny')
greet('Lucky')

def sub(x,y):
    return x-y
result=sub(50,30)
print(result)

def sub(x,y):
    return x-y
result=sub(y=50,x=30)#Keyword args
print(result)

def sub(x=0,y=0):
    return x-y
result=sub()
print(result)

def sub(x=0,y=0):#default args
    return x-y
result=sub(50)
print(result)