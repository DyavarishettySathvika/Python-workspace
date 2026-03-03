#->Modules
#Date and Time
import datetime
dt=datetime.datetime.now()
print(dt)

import random
r=random.randint(1,20)
print(r)

from time import sleep
for i in range (1,11):
    print(i)
    sleep(1)#As sleep time increases the output takes time

from time import sleep
for i in range (1,11):
    print(i)
    sleep(5)#As sleep time increases the output takes time
