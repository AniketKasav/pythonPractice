'''Q.4
Product Price List
Write a Python program to take the names and prices of three products and store them in a dictionary. 
Display all product names and their prices.'''

n=int(input("Enter the number of product  "))

d={}
for i in range(n):
    k=input("Enter product name :")
    val=int(input("Enter price :"))
    d[k]=val
    
for key,val in d.items():
    print(key,"-->",val)