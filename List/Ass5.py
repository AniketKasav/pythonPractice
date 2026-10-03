'''Q5. Write a Java program to count even & odd values from an array.
Input:
 Array Size = 7
 Array Elements = 12 17 24 39 40 55 70
Output:
 Count of Even Values = 4
 Count of Odd Values = 3
Explanation:
Initialize counters: evenCount = 0, oddCount = 0.
For each element in the array:
If divisible by 2 → increase evenCount.
Otherwise → increase oddCount.
Final counts are displayed.'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

eCount=0
oCount=0

for i in range(len(ls)):
    if ls[i]%2==0:
        eCount+=1
    else :
        oCount+=1
        
print("Even number count : ",eCount)
print("Odd number count : ",oCount)