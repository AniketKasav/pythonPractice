'''Question 2: Write a Java program to read data from student.txt and display it.
Asked In Practice Assignment
Input:
File exists with content:
Rahul 78

Output:
Student Data:
Rahul 78          '''

with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","r") as file:
    data=file.read()
    print(data)