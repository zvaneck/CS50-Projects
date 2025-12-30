def main():

    n = int(input("What's n: "))

    for i in sheep(n):
        print(i)


def sheep(n):
    for i in range(n):
        yield "s" * i

if __name__ == "__main__":
    main()