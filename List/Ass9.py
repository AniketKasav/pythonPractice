'''Q9. Write a java program to copy one array to another array.
Input : Array1 = {5, 10, 15, 20}
Output : Array2 = {5, 10, 15, 20}
Explanation:
Copy each element of Array1 into Array2 using index-by-index assignment.'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

ls1=ls.copy()

print("Copied list ",ls1)