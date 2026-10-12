'''Question 3: Write a Java program to count total characters in a file.
Asked In Practice Assignment
Input:
File content:
Java Programming

Output:
Total characters = 17 '''


with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","r") as file:
    data=file.read()
    count=len(data)
    
print("Total characters : ",count)