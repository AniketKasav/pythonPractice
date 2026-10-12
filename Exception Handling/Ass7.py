#Q.7 Password Length Check
#Accept a password from the user. If the password contains fewer than six characters, raise a ValueError and handle it using try-except.

try:
    p=input("Enter the password : ")
    if len(p)<6 :
        raise ValueError("Password length must be greater than eqauls to 6")
    print("your password is : ",p)
        
except ValueError as e :
    print(e)