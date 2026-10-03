Q18. Write a Java program to check whether a given array is empty or not.
Explanation
Every array has a predefined property called length.
If array.length == 0, then the array is empty.
Otherwise, the array contains elements.
Input :- Array elements: { }
Output :- Array is empty

arr = []

if len(arr) == 0:
    print("Array is empty")
else:
    print("Array is not empty")