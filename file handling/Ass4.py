'''Question 4: Write a Java program to count total words in a file.
Asked In Practice Assignment
Input:
File content:
Java is easy language

Output:
Total words = 4  '''

with open("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt","r") as file:
    data=file.read()
    count=len(data.split())
    
print("Total words : ",count)


