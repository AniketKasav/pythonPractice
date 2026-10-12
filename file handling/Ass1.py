'''Question 1: Write a python program to create a file student.txt and store student name and marks into it.
Asked In Practice Assignment
Input:
Enter student name: Rahul
Enter marks: 78

Output:
File created successfully.
Data written successfully. '''

with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","w") as file:
    name=input("Enter student name : ")
    marks=input("Enter student marks : ")
    
    file.write("Student name : "+name+"\n")
    file.write("Studnet marks : "+marks+"\n")
    
print("Data written successfully.")
    