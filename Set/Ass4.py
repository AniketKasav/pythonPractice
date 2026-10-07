#4. Calculate the Average of Set Elements
#Write a Python program to create a set of integers and calculate the average of all elements.

print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

count=0
sum=0

for i in s:
    sum+=i
    count+=1

print("The avrage is : ",sum//count)