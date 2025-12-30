name = input("name: ")

with open("names.csv", "a") as file:
    file.write(f"{name}\n")
