'''Question 6: Write a Java program to append data into an existing file.
Asked In Practice Assignment
Input:
Existing file contains:
Rahul 78
New data to append:
Amit 85

Output:
Data appended successfully. '''

with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","a") as file:
    name=input("Enter a student name : ")
    marks=input("Enter stundet marks : ")
    file.write("Student name : "+name+"\n")
    file.write("Student marks : "+marks+"\n")
    
print("Data appended successfully.")
    