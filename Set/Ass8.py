#8.Find the Difference Between Maximum and Minimum
#Write a Python program to create a set of integers and calculate the difference between the maximum and
#minimum elements.


print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

minNum=maxNum=s.pop()

for i in s:
    if i<minNum:
        minNum=i
    if i>maxNum:
        maxNum=i
        
print("Diff in min and max : ",(maxNum-minNum))
  
