import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        ip_split = ip.split(".")
        for num in ip_split:
            if int(num) <= 255:
                pass
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()