'''Q11. Write a java program to give an array, find the second largest element.
Input : Array = {12, 35, 1, 10, 34, 1}
Output : Second largest = 34
Explanation:
First largest is 35, second largest is the next maximum (34). We maintain two variables (largest, secondLargest).'''\

print("Enter the element in single line with space separated values : ")
ls=list(map(int,input().split()))

ls.sort(reverse=True)
print("Second highest number is : ",ls[1])


