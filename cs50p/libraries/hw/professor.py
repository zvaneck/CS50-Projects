import random


def main():
    level = get_level()

    score = 0

    for i in range(10):
        fail = 0
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        while fail < 3:
            attempt = int(input(f"{x} + {y} = "))
            if attempt == z:
                score += 1
                break
            else:
                fail += 1
                print("EEE")
        print(f"{x} + {y} = {z}")

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
