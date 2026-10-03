'''Q6. Write a java program to search an element in an array , its element found or not.
Input:
 Array = {10, 20, 30, 40, 50}
 Element to search = 30
Output : Element 30 found at index 2
Explanation :
We traverse the array and compare each element with the search key. 
If it matches, print "found" with index; otherwise print "not found".'''


print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

target=int(input("Enter the target to find in list : "))

flag=0
for i in range(len(ls)):
    if ls[i]==target:
        print(f"Element {target} found at index {i}")
        flag=1
        break
        
if flag==0:
    print("Element not found")