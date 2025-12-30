#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "home": home}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
