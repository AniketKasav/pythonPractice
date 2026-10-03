#Write a java program to count the number of digits in a number.

n=int(input("Enter a number : "))
-
count=0
while(n>0):
    count+=1
    n//=10 
    
print("Total digit are : ",count)