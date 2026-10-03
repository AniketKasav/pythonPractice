'''Q17. Write a Java program to count the number of even and odd elements present in a given integer array.
Explanation
An even number is a number that is completely divisible by 2.
An odd number is a number that is not divisible by 2.
Traverse the array using a loop.
Input :- Array = { 10, 15, 20, 25, 30 }
Output :- Even count = 3
    Odd count = 2'''
    
print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

eCount=0
oCount=0

for i in range(len(ls)):
    if ls[i]%2==0:
        eCount+=1
    else :
        oCount+=1
        
print("Even number count : ",eCount)
print("Odd number count : ",oCount)