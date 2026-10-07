#1. Find the Sum of All Elements in a Set
#Write a Python program to create a set of integers and calculate the sum of all elements.

print("Enter the element in set in single line with space separated values")
s=set(map(int,input().split()))
print(s)
sum=0
for i in s:
    sum+=i
    
print("Total sum : ",sum)
    