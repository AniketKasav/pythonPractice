'''10. Student Marks Using Nested Tuples ⭐
Given:
students = (    ("Aniket", 85, 90, 78),    ("Rahul", 72, 88, 80),    ("Priya", 92, 95, 89),    ("Amit", 65, 70, 75))
Each tuple contains:
(name, subject1, subject2, subject3)

Write a program to:
1. Print each student's name.
2. Calculate their total marks.
3. Calculate their average marks.
4. Find the student with the highest total marks.
Expected highest student:
Priya
Total: 276
Average: 92.0    '''


students = (
    ("Aniket", 85, 90, 78),
    ("Rahul", 72, 88, 80),
    ("Priya", 92, 95, 89),
    ("Amit", 65, 70, 75)
)

Highest_student=None
Highest_total=0

for student in students:
    name=student[0]
    
    total=student[1]+student[2]+student[3]
    average=total/3
    
    print("name : ",name)
    print("total : ",total)
    print("average : ",average)
    print()
    
    if total>Highest_total:
        Highest_student=name
        Highest_total=total
        
print("Highest Student : ",Highest_student)
print("Total : ",Highest_total)
print("Average : ",Highest_total/3)