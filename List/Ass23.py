'''Q23. Write a Java program to find the Majority Element of an array.
A majority element in an array of size n is an element that appears more than n/2 times. There can be at most one majority element in the array.
Example :- The given array is: 4 8 4 6 7 4 4 8
       There are no Majority Elements in the given array
Explanation
1.Traverse the array using two loops.
2.For each element, count how many times it appears.
3.If the count of any element is greater than n/2, that element is the majority element.
4.If no such element is found after checking all elements, print that there is no majority element.'''

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

ans=0
count=0
for i in range(len(ls)):
    if(ls.count(ls[i])>count):
        ans=ls[i]
        count=ls.count(ls[i])
        
print("Majority element : ",ans)