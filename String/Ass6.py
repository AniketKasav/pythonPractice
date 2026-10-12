#6. Check whether a string starts with a given substring.

text=input("Enter a string : ")
substring=input("Enter a substring : ")

if text.startswith(substring):
    print("Given string start with substring")
else:
    print("Given string is not start with substring")