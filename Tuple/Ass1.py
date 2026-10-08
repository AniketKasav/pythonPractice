'''1. Create and Access a Tuple
Create a tuple containing 5 integers. Print:
- The first element
- The last element
- The third element '''

print("Enter the integer in tuple with space separated values : ")
t=tuple(map(int,input().split()))
print("First element is : ",t[0])
print("Last element is : ",t[-1])
print("third element is : ",t[2])