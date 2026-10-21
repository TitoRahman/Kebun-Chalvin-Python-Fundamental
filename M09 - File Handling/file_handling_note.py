
# ==========================================
# FILE HANDLING
# ==========================================

def create_file(filename):
    file = open(filename, "w")
    file.close()


def read_file(filename):
    # Check whether the file exists
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        create_file(filename)
        file = open(filename, "r")

    # Read all lines from the file
    lines = file.readlines()
    file.close()

    # Convert lines into a list without "\n"
    students = []

    for line in lines:
        student = line.strip()
        students.append(student)

    return students


def write_file(filename, students):
    file = open(filename, "w")

    for student in students:
        file.write(student + "\n")

    file.close()


# ==========================================
# LIST HANDLING
# ==========================================

def display_students(students):
    print("List of students:")

    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print(f"- {student}")


def add_student(students, student_name):
    students.append(student_name)
    print(f"Student {student_name} added")


def search_student(students, student_name):
    for i in range(len(students)):
        if students[i] == student_name:
            print(f"Found {student_name} at line {i + 1}")
            return

    print("Student not found")


def remove_student(students, student_name):
    if student_name in students:
        students.remove(student_name)
        print(f"Student {student_name} removed")
    else:
        print("Student not found")


# ==========================================
# MAIN PROGRAM
# ==========================================

FILENAME = "grade_x.txt"

# Step 1: Read file into a list
students = read_file(FILENAME)

# Step 2: Manipulate the list
add_student(students, "Budi")
add_student(students, "Jane")
add_student(students, "Javier")

display_students(students)
search_student(students, "Jane")

# Step 3: Save the updated list to file
write_file(FILENAME, students)
