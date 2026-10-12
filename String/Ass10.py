#10. Find the index of a given character in a string.

s=input("Enter a string : ")
c=input("Enter a char : ")

index=s.find(c)

if index!=-1:
    print("Index : ",index)
else:
    print("Character not found 6")