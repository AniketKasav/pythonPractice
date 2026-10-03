'''Q1. Write a Java program to input an array & display it.
Input:
 Array Size = 5
 Array Elements = 10 20 30 40 50
Output:
 10 20 30 40 50
Explanation:
First, we take the size of the array from the user.
Then, elements are entered one by one into the array.
Finally, using a loop, we display all elements in the same order they were entered.'''

#len=int(input("Enter the list length :"))

#arr=[];

print("Enter the list element one by one ")

'''for i in range(len):
    ele=int(input(f"Enter the {i+1} element : "))
    arr.append(ele);'''
    
arr=list(map(int,input().split()))
    
print("Display list : ",arr)