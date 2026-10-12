'''Input:
Input filename:
student.txt
Output:
File deleted successfully
OR
File not found or deletion failed '''

import os
f=input("Enter file path")

if os.path.exists(f) and os.path.isfile(f):
    try:
        os.remove(f)
        print("File deleted sucessfully")
    except OSError:
        print("File not found or deletion failed")
        
else:
    print("File not found or deletion failed")


