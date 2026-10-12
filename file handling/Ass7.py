'''Question 7: Write a python program to check whether file exists or not.
Asked In Practice Assignment
Input:
Input filename:
student.txt

Output:
File exists
OR
File does not exist  '''


from pathlib import Path

f=Path("C:\\Users\\anike\\Desktop\\python\\file handling\\files\\Ass1.txt")

if f.exists():   # f.is_file() to check the file and f.is_dir() to check whether it is directory...
    print("File Exist !!")
else :
    print("File not exist !!")
    
