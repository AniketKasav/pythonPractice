'''Question 8: Write a python program to display file size.
Asked In Practice Assignment
Input:
Input filename:
student.txt

Output:
File size = 120 bytes  '''

import os

f=input("Enter file path : ")

if os.path.isfile(f):
    size=os.path.getsize(f)
    print("File size : ",size,"bytes")
else:
    print("File not found")