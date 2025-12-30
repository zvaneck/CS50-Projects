class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        #self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

'''
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("no name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["a", "b", "c", "d"]:
            raise ValueError("invalid house")
        self._house = house
'''
'''
    def charm(self):
        match self.patronus:
            case "Stag":
                return "S"
            case "Otter":
                return "O"
            case _:
                return "None"
'''

def main():
    student = Student.get()

    #print(f"{student['name']} from {student['house']}")
    #print(f"{student.name} in {student.house}")
    #print("Expecto Patronum!")
    #print(student.charm())
    print(student)

'''
def get_student():

    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

    name = input("Name: ")
    house = input("House: ")
    #patronus = input("Patronus: ")
    return Student(name, house)
'''


if __name__ == "__main__":
    main()
