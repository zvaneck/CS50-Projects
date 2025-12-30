import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):

    count = re.findall(r"\b\W*um\b\W*", s, re.IGNORECASE)
    print(count)
    return len(count)


if __name__ == "__main__":
    main()