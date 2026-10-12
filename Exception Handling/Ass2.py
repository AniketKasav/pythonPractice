'''Q2. Integer Input
Write a Python program to accept an integer from the user. Handle the exception if the user enters a non-numeric value.'''


try:
    a=int(input("Enter a integer value : "))
    print("Then number is : ",a)
except ValueError as e:
    print("Enter only integer value")