'''Q7. Write a java program to display the reverse array.
Input : Array = {1, 2, 3, 4, 5}
Output : Reverse array = {5, 4, 3, 2, 1}
Explanation :
The last element becomes the first, and the first becomes the last by traversing from the end to the start.'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

print("List before reverse : ",ls)
ls=ls[::-1]
print("List after reverse : ",ls)