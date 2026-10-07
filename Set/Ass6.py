#6.Find the Square of Each Element
#Write a Python program to create a set of integers and create a new set containing the square of each
#element.


print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

print("Square of each element :",end=" ")

for i in s:
    print(i*i,end=" ")