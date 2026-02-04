#Bitwise Operators
#->Bitwise operators are used to compare (binary) numbers
#AND (&) Operation
print(7 & 3) #where 6 is a 110 and 3 is a 011
print(7&-9)
print(-0.8-8)
#TrueTrueTrue 1,1=1 (Here multiplication is used)
#TrueFalseFalse 1,0=0
#FalseTrueFalse  0,1=0
#FalseFalseFalse 0,0=0

#OR (|) Operation
print(9|6)
print(6|-3)
print(6|8)
#T,T=T 11=1(Addition operation by binary numbers)
#T,F=T 10=1
#F,T=T 01=1
#F,F=F 00=0

#XOR (^) Operation
print(6 ^ 3)
print(5^-3)
#FalseFalseFalse 00=0
#FalseTrueTrue 01=1
#TrueFalseTrue 10=1
#TrueTrueFalse 11=0

#NOT (~) Operation
#0->1       
#1->0
print(~3)   
print(~0)   
print(~10)
print(not 0)      
print(not 42)     
print(not "")     
print(not "Hi")   



