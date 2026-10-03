'''Q13. Write a java program to display only non-zero values from an array.
Input : Array = {1, 0, 5, 0, 7, 0, 9}
Output : Non-zero elements = {1, 5, 7, 9}
Explanation :
Traverse the array and print only elements that are not equal to zero.'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

print("Non Zero elements are : ",end=" ")

for i in range(len(ls)):
    if ls[i]!=0:
        print(ls[i],end=" ")
        
  