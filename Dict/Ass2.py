'''Q.2
Employee Salary Record
Write a Python program to take an employee ID and salary as input and store them in a dictionary. 
Display the employee ID and salary.'''

n=int(input("Enter the number employees  "))

d={}
for i in range(n):
    k=input("Enter employee id :")
    val=input("Enter salary :")
    d[k]=val
    
    
print(d)