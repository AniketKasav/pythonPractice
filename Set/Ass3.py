#3. Find the Minimum Element
#Write a Python program to create a set of integers and find the smallest element in the set.

print("Enter the integer in set in single line with space separated values")
s=set(map(int,input().split()))

#m=min(s)
m=s.pop()
for i in s:
    if i<m:
        m=i
print(m)