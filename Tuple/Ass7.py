'''7. Find the Second Largest Element
Given:
numbers = (10, 45, 23, 67, 89, 34, 89, 12)
Find the second-largest unique number.
Expected:
67    '''

print("Enter the integer in tuple with space separated values : ")
t=tuple(map(int,input().split()))

l=t[0]
sl=t[0]

for i in t:
    if i>sl:
        sl=i
    if sl>l:
        temp=l
        l=sl
        sl=temp


print("second-largest : ",sl)