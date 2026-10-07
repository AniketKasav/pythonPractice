'''10.Find Common Even Numbers

Write a Python program to create two sets and display the common elements that are even numbers.
Sample Input:
Set 1 = {2, 3, 4, 5, 12, 35}
Set 2 = {1,2,5,4,6,12}
Sample Output:
2
4
12  '''

print("Enter the integer in set in single line with space separated values for set1")
s1=set(map(int,input().split()))
print("Enter the integer in set in single line with space separated values for set2")
s2=set(map(int,input().split()))

print("display the common elements that are even numbers ")

for i in (s1 | s2):
    if i%2==0:
        print(i,end=" ")