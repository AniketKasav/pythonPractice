'''Q14.  Write a java program to remove duplicated values from arrays.
Input : Array = {10, 20, 20, 30, 40, 40, 50}
Output : Unique elements = {10, 20, 30, 40, 50}
Explanation:
Traverse the array, check if element already exists before adding to result, thus avoiding duplicates.'''


print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))
ls.sort()
l=0

for r in range(0,len(ls)):
    if(ls[l]!=ls[r]):
        l+=1
        ls[l]=ls[r]
        
ls=ls[0:l+1]

print(ls)