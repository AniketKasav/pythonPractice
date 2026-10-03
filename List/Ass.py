'''Q3. Write a Java program to display even & odd values from an array.
Input:
 Array Size = 6
 Array Elements = 11 20 33 42 55 60
Output:
 Even Values = 20 42 60
 Odd Values = 11 33 55
Explanation:
Traverse the array element by element.
If an element is divisible by 2, it is even. Otherwise, it is odd.
Separate lists are displayed for even and odd values.'''


print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

odd=[]
even=[]

for i in range(len(ls)):
    if ls[i]%2==0:
        even.append(ls[i])
    else :
        odd.append(ls[i])
        
print("Even numbers ",even)
print("Odd numbers ",odd)
