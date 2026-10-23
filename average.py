def calculate_average(students):
    """Calculate the average marks of students."""
    if not students:
        return 0.0

    total = 0

    for name, marks in students:
        if not isinstance(marks, (int, float)):
            raise ValueError(f"Marks for {name} must be numeric.")

        if not 0 <= marks <= 100:
            raise ValueError(f"Marks for {name} must be between 0 and 100.")

        total += marks

    return total / len(students)


# Sample students
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

average = calculate_average(students)
print(f"Student average: {average:.2f}")