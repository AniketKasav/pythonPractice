'''7.Add Corresponding Elements from Two Sets
Write a Python program to create two sets containing the same number of elements. Convert them into 
lists and calculate the sum of corresponding elements.
Sample Input:
Set 1 = {10, 20, 30}
Set 2 = {1, 2, 3}
Sample Output:
11
22
33    '''

print("Enter the integer in set in single line with space separated values for set1")
s1=set(map(int,input().split()))
print("Enter the integer in set in single line with space separated values for set2")
s2=set(map(int,input().split()))

l1=list(s1)
l2=list(s2)

for i in range(len(l1)):
    print(l1[i]+l2[i])