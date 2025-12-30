class invalid_numerator(Exception):
    pass

def main():
    fuel = int(get_fuel("What is the fuel level? "))
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def get_fuel(prompt):
    while True:
        try:
            level = input(prompt)
            level = level.split("/")
            x = int(level[0])
            y = int(level[1])
            level = x / y
            if x > y:
                raise invalid_numerator
        except ValueError:
            print("non int")
        except ZeroDivisionError:
            print("zero den")
        except invalid_numerator:
            print("x > y")
        else:
            return round((x/y), 2)*100

main()