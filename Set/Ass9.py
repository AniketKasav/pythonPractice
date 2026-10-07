#9.Find the Product of All Elements
#Write a Python program to create a set of integers and calculate the product of all elements.

print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

p=1

for i in s:
    p*=i
    
print("product of all elements : ",p)