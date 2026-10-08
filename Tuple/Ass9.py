'''9. Find Common Elements Between Two Tuples
Given:
tuple1 = (10, 20, 30, 40, 50)tuple2 = (30, 40, 50, 60, 70)
Create a new tuple containing the elements that are present in both tuples.
Expected:
(30, 40, 50)'''

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for num in tuple1:
    if num in tuple2:
        common += (num,)

print(common)