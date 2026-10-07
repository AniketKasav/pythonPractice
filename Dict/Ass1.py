#Q.1
#Student Marks Dictionary
#Write a Python program to take a student name and marks as input and store them in a dictionary. 
#Display the student name and marks.

n=int(input("Enter the number students "))

d={}
for i in range(n):
    k=input("Enter student name :")
    val=input("Enter marks :")
    d[k]=val
    
    
print(d)
    