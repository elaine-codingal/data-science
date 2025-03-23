import numpy as np

# Define the structured data type 
data_type = [('name', 'U30'), ('course', 'U50'), ('grade', 'f4')]

# List of student details
student_details = [
    ('Mike Spencer', 'Bsc IT', 3.7),
    ('Jane Hannes', 'Msc Computer Science', 3.4),
    ('Willy Peters', 'Bsc Software Engineering', 2.9),
    ('Rodger Kevins', 'Bsc Data Science', 3.0)
]

# Create a structured array
students = np.array(student_details, dtype=data_type)

# Print original array
print("Original array:")
print(students)

# Sort by grade
print("\nSorted by grade:")
print(np.sort(students, order='grade'))
