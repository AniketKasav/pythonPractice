#5.Find the Sum of Even Numbers
#Write a Python program to create a set of integers and calculate the sum of only the even numbers.

print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

sum=0
for i in s:
    if i%2==0:
        sum+=i     
print("sum of even number : ",sum)
