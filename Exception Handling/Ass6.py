'''Q.6 Age Validation
Accept the user's age as input. Handle invalid input and display the age if it is a valid integer.'''

try:
    age=int(input("Enter your age : "))
    
    if age<0:
        raise ValueError("Age cannot be negative ")
        
    print("your age is : ",age)
    
except ValueError as e:
    print("Invalid input : ",e)