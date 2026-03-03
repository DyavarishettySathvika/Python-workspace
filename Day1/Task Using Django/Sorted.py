nums1=[3,4,5,2,1]
nums2=[1,2,3,4,5]
def is_sorted(lst):
    if lst==sorted(lst):
        return True
    else:
        return False
print(is_sorted(nums1))
print(is_sorted(nums2))

#->Squareroot
import math #import math module
s=math.sqrt(100)
print(s)

#->Factorial,sqrt
from math import sqrt,factorial
f=factorial(5)
print(f)


from math import factorial as fact
f=fact(6)
print(f)

from math import * #imports everything
f=floor(7.9)
c=ceil(9.2)
print(f)
print(c)
