#Write a java program to find the sum of all natural numbers between 1 to n.

n=int(input("Enter a number :"));
sum=0;

for i in range(1,n+1):
    sum+=i
    
print("Total sum 1 to n : ",sum)