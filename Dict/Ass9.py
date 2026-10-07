'''Q.9
Subject Marks
Write a Python program to take subject names and marks for three subjects and store them in a dictionary
Display all subjects and marks and calculate the average marks. '''

n=int(input("Enter the number of sunject  "))

d={}
for i in range(n):
    k=input("Enter name of subject:")
    val=int(input("Enter marks :"))
    d[k]=val
    
sum=0
count=0

for key,val in d.items():
    print(key,"-->",val)
    sum+=val
    count+=1
    
print("Avrage marks :",(sum//count))
