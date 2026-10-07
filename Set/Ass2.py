#2.Find the Maximum Element
#Write a Python program to create a set of integers and find the largest element in the set.
print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

ele=s.pop()
for i in s:
    if ele<i:
        ele=i
print("Largest element is ",ele)       