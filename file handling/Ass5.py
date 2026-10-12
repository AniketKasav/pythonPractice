'''Question 5: Write a Java program to count total lines in a file.
Asked In Practice Assignment
Input:
File content:
Java
Python
C++

Output:
Total lines = 3   '''

with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","r") as file:
    lines=file.readlines();
    count=len(lines)
    
print("Total lines are : ",count)