'''Basic Exception Handling
Q1. Division of Two Numbers
Write a Python program to divide two numbers. Handle the exception that occurs when the denominator is zero.'''

print("Program of two number division")

try:
    a=int(input("Enter first number : "))
    b=int(input("Enter a second number : "))
    result=a/b
    print("Result is : ",result)
    
except ZeroDivisionError as e:
    print(e,"Not allowed ")