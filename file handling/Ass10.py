'''Question 10: Write a Java program to display file path.
Input:
Input filename:
student.txt
Output: '''
#File path: C:\Users\Java\student.txt

import os
filename=input("Enter file name : ")

filepath=os.path.abspath(filename)

print("File path : ",filepath)
