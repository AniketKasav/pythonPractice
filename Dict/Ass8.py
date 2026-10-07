'''Q.8
Simple Login System
Write a Python program to create a dictionary containing usernames and passwords. 
Ask the user to enter a username and password and check whether the login details are correct.'''

n=int(input("Enter the number of users : "))

d={}
for i in range(n):
    k=input("Enter the username :")
    val=input("Enter a password :")
    d[k]=val

k=input("Enter your username :")
p=input("Enter your password :")

if k in d and d[k]==p:
    print("Valid user")
else :
    print("Invalid user ")
