#Q.3
#Phone Book
#Write a Python program to take a person's name and phone number as input and store them in a dictionary.
#Ask the user for a name and display the corresponding phone number.

n=int(input("Enter the number person  "))

d={}
for i in range(n):
    k=input("Enter person name :")
    val=input("Enter phone number :")
    d[k]=val
   
t=input("Enter the name : ")
print("phone number is : ",d[t])