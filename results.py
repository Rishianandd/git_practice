# Student Results Manager
# Pass mark is 50 out of 100.

PASS_MARK = 50


def get_valid_mark(name):
    """Get a valid mark between 0 and 100."""
    while True:
        mark = input(f"Enter marks for {name}: ")

        try:
            mark = float(mark)

            if 0 <= mark <= 100:
                return mark

            print("Invalid mark. Please enter a number between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numeric mark.")


def display_result(name, mark):
    """Display the student's marks and pass/fail result."""
    if mark >= PASS_MARK:
        result = "Pass"
    else:
        result = "Fail"

    print(f"{name}: {mark:g}/100 - {result}")


# Sample students
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 42
}

print("Student Results")
print("----------------")

for name, mark in students.items():
    display_result(name, mark)
