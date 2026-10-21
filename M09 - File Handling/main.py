# FILE HANDLING > HANDLE CRUD (CREATE, READ, UPDATE, DELETE) FILE
# FILE IS JUST ANOTHER STRING FROM DIFFERENT FILE
# FILE COULD OPEN EITHER A TEXT OR BINARY DATA (IMAGE, EXCEL), CSV, EXE (BINARY CODE)

# open(<location of the file>, <mode r,w>)
# TEXT FILE > BUNCH OF STRING, AND AT THE OF THE SENTENCE IT WILL HAVE A NEW LINE ("\n")

# FILENAME = "example.txt"
# f = open(FILENAME, "r")
# f.write("HELLO EDITED")
# line = f.readline() # READ THE NEXT LINE STORE IT AS A STRING
# print("using readline() : ",line)

# lines = f.readlines()
#
# print("using readlines() : ",lines)
# filtered_lines = "".join(lines).split("\n") # "".join > ["123", "000", "111"] > "123000111"

# 'HELLO EDITED\nSECOND LINE' > ['HELLO EDITED', 'SECOND LINE']

# print("delete any '\\n' : ", filtered_lines)
# search_name = input("Enter your search term: ")
#
# for i in range(len(filtered_lines)):
#     person_name = filtered_lines[i]
#
#     if person_name == search_name:
#         print(f"Found {search_name} at line {i+1}")
#         break
# f.close()


# IMPORT
# CONSTANT
# FUNCTION


def read_grade(filename):
    # CHECK WETHER THE FILE EXIST
    try :
        f = open(filename)
        f.close()
    except FileNotFoundError : # IF FILE DOESNT EXIST THEN CREATE FILE
        create_file(filename)

    # OPEN THE FILE USING READING MODE
    file = open(filename, "r")

    # FILTER THE FILE SO IT DOESNT HAVE ANY NEW LINE SYMBOL
    students = "".join(file.readlines()).split("\n")

    print("List of students :")
    if len(students) == 0 or students[0] == "" :
        print("No students found")
    else :
        for student in students:
            print(f"\t- {student}")

# CREATE A NEW FILE
def create_file(filename):
    file = open(filename, "w")
    file.close()

def add_student(filename, student_name):
    # CHECK WETHER THE FILE EXIST
    try :
        f = open(filename)
        f.close()
    except FileNotFoundError : # IF FILE DOESNT EXIST THEN CREATE FILE
        create_file(filename)

    file = open(filename, "r+")
    old_student = file.readlines()

    old_student.append(f"{student_name}\n")
    file.close()

    file = open(filename, "w")
    file.writelines(old_student)
    print(f"Student {student_name} added")
    file.close()

FILENAME = "grade_x.txt"
add_student(FILENAME, "Budi")
add_student(FILENAME, "Jane")
add_student(FILENAME, "Javier")

read_grade(FILENAME)



