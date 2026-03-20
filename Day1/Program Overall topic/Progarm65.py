marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
avg = total / n

print("Total Marks:", total)
print("Average:", avg)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")