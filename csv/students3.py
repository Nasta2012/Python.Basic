students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


# a way to sorting out a dictionary by using a function and key
def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name, reverse=False):
    print(f"{student['name']} is in {student['house']}")

# ------------------------------------------------------------------
print("#")
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is in {student['house']}")
