#4. Count the number of vowels in a string.

s=input("Enter a string : ").lower()
count=0
for ch in s:
    if ch=='a' or ch=='i' or ch=='o' or ch=='u' or ch=='e' :
        count+=1
        
print("The number of vowels are : ",count)