
#Exception Handling
#raise Exception('this is a test error!')

try:
    print(10/0)
except ZeroDivisionError as error:
    print('an error occured:',error)

try:
    print(10/1)
except ZeroDivisionError as error:
    print('an error occured:',error)

try:
    print(40/0)
    print(10+'10')
except ZeroDivisionError as error:
    print('an error occured:',error)
except TypeError as error:
    print('an error occured:',error)

