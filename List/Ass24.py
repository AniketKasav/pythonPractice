'''Q24. Write a program in java to rotate an array by N positions ?(pending)
Expected Output:
	The given array is: 0  3  6  9  12  14  18  20  22  25  27
	From 4th position the values of the array are: 12 14 18 20 22 25 27 
	Before 4th position the values of the array are: 0  3  6  9 
	After rotating from 4th position the array is: 12 14 18 20 22 25 27 0 3  6 9'''
    



def helpher(l,r,ls):
    while l<=r:
        temp=ls[l]
        ls[l]=ls[r]
        ls[r]=temp
        l+=1
        r-=1
        

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

k=int(input("Enter the position :"))

helpher(0,k-1,ls)
helpher(k,len(ls)-1,ls)
helpher(0,len(ls)-1,ls)

print(ls)


'''1 2 3 4 5 6 7
3 2 1 4 5 6 7
3 2 1 7 6 5 4
4 5 6 7 1 2 3'''