'''Q21. Given an integer array and a specific element, write a Java program to 
find the index position of that element in the array. If the element is not found, print -1.
Explanation
Traverse the array from index 0 to length - 1
Compare each element with the target element
If a match is found, return its index
If the loop ends and no match is found, return -1
Input :- Array: {10, 20, 30, 40, 50}
Element to find: 30
Output :- Element found at index: 2'''


print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

ele=int(input("Enter the element to find : "))

flag=0
for i in range(len(ls)):
    if ls[i]==ele:
        print(f"element found at index {i}")
        flag=1
        break;
        
if flag==0:
    print("Element not found")