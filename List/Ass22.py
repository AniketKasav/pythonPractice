'''Q22. Write a Java program to check whether two integer arrays are equal.
 Two arrays are considered equal if:
Both arrays have the same length
Corresponding elements at each index are exactly the same
Do not use inbuilt methods like Arrays.equals().
Input :- Array1 = {10, 20, 30, 40}
            Array2 = {10, 20, 30, 40}
Output :- Arrays are equal. '''


print("Enter the element of first list in single line with space separated values : ")
ls1=list(map(int,input().split()))

print("Enter the element of second list in single line with space separated values : ")
ls2=list(map(int,input().split()))

if ls1==ls2:
    print("Lists are equal")
else:
    print("Lists are not equal")