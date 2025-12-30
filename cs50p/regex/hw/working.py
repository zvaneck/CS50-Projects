import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    if time := re.search(r"^(1?[0-9]):?([0-5][0-9])? ([A|P]M)? to (1?[0-9]):?([0-5][0-9])? ([A|P]M)?$", s):
        hour1 = int(time.group(1))
        hour2 = int(time.group(4))
        min1 = (time.group(2))
        min2 = (time.group(5))
        start = time.group(3)
        end = time.group(6)
        if start == "AM" and hour1 == 12:
            hour1 = 0
        elif start == "AM":
            hour1 = hour1
        elif start == "PM" and hour1 == 12:
            hour1 = 12
        else:
            hour1 = hour1 + 12

        if end == "AM" and hour2 == 12:
            hour2 = 0
        elif end == "AM":
            hour2 = hour2
        elif end == "PM" and hour2 == 12:
            hour2 = 12
        else:
            hour2 = hour2 + 12

        if min1 is not None:
            return (f"{hour1:02}:{min1} to {hour2:02}:{min2}")
        else:
            return (f"{hour1:02}:00 to {hour2:02}:00")
    else:
        raise ValueError

if __name__ == "__main__":
    main()