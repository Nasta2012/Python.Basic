import csv

students = []

with open("students4.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")   

# csv.DictReader , if the csv file is 
# home,name or name,home
# it will run correctly cause now it returns a dictionary      

#------------------------------------------
print()
import csv

students = []

with open("students4.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")   
