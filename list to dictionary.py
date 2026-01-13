students = [
    (1, "Ravi", "A"),
    (2, "Kiran", "B"),
    (3, "Sneha", "A"),
    (4, "Vikram", "C"),
    (5, "Meera", "B")
]

students_dict = {roll: {"name": name, "grade": grade} for roll, name, grade in students}

print(students)
print(students_dict)
