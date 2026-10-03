#Write a java program to find the sum of all even numbers between 1 to n.

n=int(input("Enter a number : "))

sum=0
for i in range(2,n+1,2):
    sum+=i
    
print("total sum of even number : ",sum)