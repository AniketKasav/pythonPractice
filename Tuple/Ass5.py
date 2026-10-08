'''5. Reverse a Tuple
Given:
numbers = (10, 20, 30, 40, 50)
Create a new tuple containing the elements in reverse order.
Expected:
(50, 40, 30, 20, 10)  '''

t = (10, 20, 30, 40, 50)
print("Tuple before reverse : ",t)
rev=t[::-1]
print("Reverse tuple : ",rev)