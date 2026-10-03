'''Q10. Write a program in java to delete an element at desired position from an array.
	Test Data :
	Input the size of array : 5
	Input 5 elements in the array in ascending order :
	1   2    3    4    5
	Input the position where to delete : 3
	Expected Output : The new list is : 1 2 3 5 '''
    


print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

pos=int(input("Enter the position : "))
idx=pos-1

for i in range(pos,len(ls)-1):
    ls[i]=ls[i+1]
    
print("The new list is : ")

for i in range(0,len(ls)-1):
    print(ls[i],end=" ")
