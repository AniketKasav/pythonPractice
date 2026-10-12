#5. Count the number of consonants in a string.

s=input("Enter a string : ")
s=s.lower()
count=0
for ch in s:
    if ch not in "aioue":
        count+=1
        
print("The number of consonants are : ",count)