#->String Format
#age = 20 #This will be error
#txt = "My name is Bunnnyy, I am " + age
#print(txt)
#This code produce and error  because int and string can't exist.To overcome that we are doing some operations

#->FString
age = 20
txt = f"My name is Sathvika, I am {age}"
print(txt)
#To specify a string as an f-string, simply put an f in front of the string, and add curly brackets {} as placeholders for variables and other operations.
bus = 43
txt=f'Which bus number,Its {bus}'
print(txt)

#->Placeholders and Modifiers
pincode = 503224
txt=f'What is the pincode of Armoor {pincode}'
print(txt)
price = 7858
txt = f"The price is {price:.2f} dollars"
print(txt)
#Here we added:. this two symbols. Because adding decimal points to the output.

#->Using Math
txt = f"The price is {20 * 59} dollars"
print(txt)
txt=f'the price is {224-123} dollars'
print(txt)
#Any operation can done here in {}