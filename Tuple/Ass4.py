'''4. Tuple Length and Sum
Given:
numbers = (12, 25, 8, 40, 15)
Find:
- The length of the tuple
- The sum of all elements
- The maximum element
- The minimum element '''

print("Enter the integer in tuple with space separated values : ")
t=tuple(map(int,input().split()))

sum=0
len=0
mx=t[0]
mn=t[0]
for i in t:
    len+=1
    sum+=i
    if i<mn:
        mn=i
    if i>mx:
        mx=i
    
print("he length of the tuple : ",len)
print("The sum of all elements : ",sum)
print("The maximum element : ",mx)
print("The minimum element : ",mn)