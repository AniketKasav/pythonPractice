'''Q8. Write a java program to find missing elements in an array.
Input : Array = {1, 2, 4, 5, 7} (numbers from 1 to 7 should be present)
Output : Missing elements = {3, 6}
Explanation:
Check sequence numbers one by one. If a number from 1 to maximum (7) is not in the array, it is missing.
'''

print("Enter the element in single line with space separated values(1-10) : ")
print("Note : miss one or more number to find out !!"   )
ls=list(map(int,input().split()))

ls.sort()

print("Missing numbers :")
for i in range(1,11):
    flag=0
    for j in range(len(ls)):
        if(i==ls[j]):
            flag=1
            break
    if flag==0:
        print(i,end=" ")


    
            
    