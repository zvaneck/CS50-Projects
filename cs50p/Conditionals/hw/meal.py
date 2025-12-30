def main():
    time = input("what time is it? ")
    check = convert(time)

    if 7 <= check <= 8:
        print("breakfast time")
    elif 12 <= check <= 13:
        print("lunch time")
    elif 18 <= check < 19:
        print("dinner time")
    else:
        exit


def convert(x):
    hour = float(x.split(":")[0])
    minute = float(x.split(":")[1])

    check = hour + (minute/60)

    return check

if __name__ == "__main__":
    main()