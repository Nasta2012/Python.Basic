# make a list
students = []

with open("students.csv") as file:
    for lol in file:
        name, house = lol.rstrip().split(",")

        # make a dictionary, every line of list will have two variubales name and house
        student={}
        student["name"] = name
        student["house"] = house

        # adding it to the list
        students.append(student)

# now for priniting we use the variuables of the dic
for student in students:
    print(f"{student['name']} is in {student['house']}")

#-----------------------------------------------------------------------------
print("@")
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student={"name" :name, "house" :house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
