s1={'map','direction','right'}
s2={'left','start','stop'}
s3=s1.intersection(s2)
print(s3)

s1={'striaght','cross','back'}
s2={'front','up','down'}
s3=s1&s2
print(s3)

s1={'yellow','red','pink'}
s2={'white','black','blue'}
s1.intersection_update(s1)
print(s1)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)
