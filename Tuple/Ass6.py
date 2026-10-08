'''6. Separate Even and Odd Numbers
Given:
numbers = (11, 24, 35, 42, 53, 60, 71, 88)
Create two tuples:
- One containing all even numbers
- One containing all odd numbers
Expected:
Even: (24, 42, 60, 88)
Odd: (11, 35, 53, 71)'''

print("Enter the integer in tuple with space separated values : ")
t=tuple(map(int,input().split()))

e=[]
o=[]

for i in t:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
        
te=tuple(e)
to=tuple(o)

print("Even elements : ",te)
print("Odd elements : ",to)