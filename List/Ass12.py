'''Q12. Write a program in java to insert an element at desired position from an array.
	Test Data :
	Input the size of array : 6
	Input 5 elements in the array in ascending order :
	1   2    3    4    5
	Input the position where to insert : 2
	Value :      200
	Expected Output : The new list is : 1 2 200 3 4 5'''
    
print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

pos=int(input("Enter the position : "))
pos=pos-1
data=int(input("Enter the data :"))
ls.append(0)
for i in range(len(ls)-2,pos-1,-1):
    ls[i+1]=ls[i]
    
ls[pos]=data

print("List after insersion :")
for i in range(len(ls)):
    print(ls[i],end=" ")