from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    birth_date = get_birth_date()

    check_birth_date(birth_date)

    #print(type(birth_date))

    birth_date = convert(birth_date)

    #print(type(birth_date))

    today_date = get_today()

    #print(today_date)

    num_days = time_since_birth(birth_date, today_date)

    #print(num_days)

    num_minutes = int(num_days.total_seconds()/60)

    #print(num_minutes)

    print(f"{to_words(num_minutes)} minutes")


def get_birth_date():
    return input("Date of Birth: ")

def check_birth_date(s):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s):
        return True
    else:
        sys.exit(1)

def convert(d):
    return date.fromisoformat(d)

def get_today():
    return date.today()

def time_since_birth(b, t):
    return (t - b)

def to_words(n):
    return p.number_to_words(n, andword="").capitalize()

if __name__ == "__main__":
    main()