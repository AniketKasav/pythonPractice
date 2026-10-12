#Q4. Multiple Exceptions
#Write a Python program to accept two numbers and divide them. Handle both ValueError and ZeroDivisionError.

print("Program to perform tow number division ")

try: 
    a=int(input("Enter a first number : "))
    b=int(input("Enter a second number : "))
    result =a/b
    print("result is : ",result)
    
except ValueError as e:
    print("Enter only integer values ")
except ZeroDivisionError as e:
    print("Divide by zero not allowed ")