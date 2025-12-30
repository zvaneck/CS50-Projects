import random

class Hat:
    houses = ["A", "B", "C", "D"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)

Hat.sort("Harry")