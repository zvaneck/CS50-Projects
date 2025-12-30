import random

while True:
    try:
        n = int(input("Level: "))
        if n < 0:
            pass

        rand = random.randint(1,n)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < rand:
                    print("Too small!")
                    pass
                elif guess > rand:
                    print("Too large!")
                    pass
                else:
                    break
            except ValueError:
                pass

        break

    except ValueError:
        pass

print("Just right!")