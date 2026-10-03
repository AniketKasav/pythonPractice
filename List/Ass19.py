'''Q19. Given an integer array, replace all the negative numbers in the array with 0 and print the updated array.
Explanation
Traverse the array from the first element to the last.
Check each element:
If the element is negative, replace it with 0.
If the element is zero or positive, keep it as it is.
After completing the traversal, print the modified array.
Input :- Array = [5, -3, 7, -1, 0, -6, 4]
Output :- Updated Array = [5, 0, 7, 0, 0, 0, 4]'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

for i in range(len(ls)):
    if ls[i]<0:
        ls[i]=0
        
print("List after removing negative numbers :",ls)        
