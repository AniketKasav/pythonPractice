'''Q20. Write a Java program to print all elements from an integer array that are greater than a given number.
Explanation
An integer array is given.
A number N is also given.
Traverse the array using a loop.
Compare each element with N.
If the element is greater than N, print it.
Input :- Array: 10 25 5 40 18
 Given Number: 20
Output :- Elements greater than 20 :
    25 40    '''
    
    
print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

n=int(input("Enter the number : "))
print(f"Elements greater than {n} :")
for i in range(len(ls)):
    if ls[i]>=n:
        print(ls[i],end=" ")
    