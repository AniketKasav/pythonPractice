'''Q.5
Dictionary Update
Write a Python program to create a dictionary containing three key-value pairs. 
Ask the user for a key and a new value, then update the dictionary with the new value. 
Display the updated dictionary.'''


n=int(input("Enter the number of product  "))

d={}
for i in range(n):
    k=input("Enter product name :")
    val=int(input("Enter price :"))
    d[k]=val
    
k=input("Enter the product name you want to change the price : ")
val=int(input("Enter the new price :"))
d[k]=val
print("New dict : ",d)