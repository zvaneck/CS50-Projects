import csv

'''
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
'''

name = input("what's your name: ")
home = input("where do you live: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
