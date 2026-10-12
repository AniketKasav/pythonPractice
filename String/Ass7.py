#7. Check whether a string ends with a given substring.

text=input("Enter a string : ")
substring=input("Enter a substring : ")

if text.endswith(substring):
    print("Given string ends with substring")
else:
    print("Given string is not ends with substring")