'''Q15. Write a java program to find common elements between two arrays.
Input :
 Array1 = {1, 2, 3, 4, 5}
 Array2 = {3, 4, 5, 6, 7}
Output : Common elements = {3, 4, 5}
Explanation :
Compare each element of Array1 with all elements of Array2, if match found → it is a common element.'''

print("Enter the element of first list in single line with space separated values : ")
ls1=list(map(int,input().split()))

print("Enter the element of second list in single line with space separated values : ")
ls2=list(map(int,input().split()))

print("Common elements :")

s=set()

for i in range(len(ls1)):
    for j in range(len(ls2)):
        if ls1[i]==ls2[j]:
            s.add(ls1[i])
            
for i in s:
    print(i,end=" ")
    



        