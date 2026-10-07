'''Q.7
Display the dictionary.
Country and Capital
Write a Python program to take the names of three countries and their capitals from the user and store them in a dictionary. 
Display all country-capital pairs. '''

n=int(input("Enter the number of countries  "))

d={}
for i in range(n):
    k=input("Enter name country:")
    val=input("Enter capital :")
    d[k]=val

print("country\tcapital")
for key,val in d.items():
    print(key,"\t",val)
    