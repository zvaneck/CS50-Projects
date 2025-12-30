def main():
    percent = convert(input("What is the fuel level? ").strip())
    level = gauge(percent)
    print(level)



def convert(fraction):
        try:
            (x, y) = fraction.split("/")

            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            return round((x/y), 2)*100
        except ValueError:
            raise
        except ZeroDivisionError:
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()