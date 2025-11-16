#reading from a csv file and split it and prining them
#first way
with open ("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

print()
#second way
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


#third way
print()
students=[]
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
       
for student in sorted(students):
     print(student)        


