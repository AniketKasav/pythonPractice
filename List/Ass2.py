'''Q2. Write a Java program to calculate the sum of all elements in an array.
Input:
 Array Size = 5
 Array Elements = 2 4 6 8 10
Output:
 Sum of array elements = 30 '''
 

length=int(input("Enter the list length : "))

arr=[]

print("Enter the elements one by one : ")

i=0
while len(arr)<length:
    ls=list(map(int,input().split()))
    arr.extend(ls)


arr = arr[:length]
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print("Array elements ",arr)
print("Total sum : ",sum)

