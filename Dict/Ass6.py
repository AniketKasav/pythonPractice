'''Q.6
Student Grade Dictionary
Write a Python program to take a student's name and percentage as input. Store the student's name and 
grade in a dictionary based on the following criteria:
75 and above → A
60 to 74     → B
40 to 59     → C
Below 40     → Fail '''

n=int(input("Enter the number of student  "))

d={}
for i in range(n):
    k=input("Enter student name :")
    marks=int(input("Enter marks :"))
    if marks>=75:
        d[k]="A"
    elif marks>=60:
        d[k]="B"
    elif marks>=40:
        d[k]="C"
    else:
        d[k]="Fail"
        
print(d)
    