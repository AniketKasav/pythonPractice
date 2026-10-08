'''8. Swap Elements Using Tuple Unpacking
Given:
a = 10b = 20
Swap the values of a and b without using a third variable, using tuple unpacking.
Expected:
a = 20
b = 10   '''

a=10
b=20
print("before swap  a : ",a," b : ",b)
a,b=b,a

print("after swap  a : ",a," b : ",b)