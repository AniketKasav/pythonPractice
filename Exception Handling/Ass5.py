#Q5. Using finally
#Write a Python program to divide two numbers and display "Program Completed" using the finally block, whether an exception occurs or not.

print("Program to divide two number ")

try: 
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    result=a/b
    print("Result is : ",result)
    
except ZeroDivisionError as e:
    print("Divide by zero not possible")

finally:
    print("Program Completed")