import datetime
import calendar
import os
import re
import inflect

p = inflect.engine()

def main():

    today = datetime.date.today().strftime("%m/%d/%Y")
    date = (get_current_date(today))
    number = (get_entry_number())

    while True:
        bed_time = get_sleep_times(input("What time did you go to bed last night? "))
        wake_time = get_sleep_times(input("What time did you wake up this morning? "))
        if bed_time == False or wake_time == False:
            pass
        else:
            break
    gratitude = (get_gratitude())

    min_words = 10
    content = input(f"Please write your journal entry (no less than {min_words} words): ")
    entry = (get_journal_content(content, min_words))

    save_journal_entry(date, number, bed_time, wake_time, gratitude, entry)


def get_current_date(today):
    month, day, year = today.split("/")
    return f"{calendar.month_name[int(month)]} {day}, {year}"

def get_entry_number():
    return len(os.listdir("journal_entries")) + 1

def get_sleep_times(time):

        pattern = r'^(1[0-2]|0?[1-9]):([0-5]\d)\s(AM|PM)$'
        if re.match(pattern, time):
            return time
        else:
            print("Please write times in X:XX AM/PM format")
            return False

def get_gratitude():
    print("Please write down 3 things you are grateful for.")
    gratitude = []
    for i in range(3):
        gratitude.append(input(f"{p.ordinal(i+1)} thing you are grateful for: "))
    return gratitude

def get_journal_content(content, min_words):

    num_words = len(content.strip().split(" "))
    while True:
        if num_words < min_words:
            new_input = input(f"Please add atleast {min_words - num_words} more words: ")
            content += " " + new_input
            num_words += len(new_input.split(" "))
            pass
        else:
            return content

def save_journal_entry(date, num, bed, wake, gr, entry):

    journal_entry = f"Date: {date}\nEntry #: {num}\nBed: {bed}\nWake: {wake}\n\nI am grateful for:\n\t1. {gr[0]}\n\t2. {gr[1]}\n\t3. {gr[2]}\n\n{entry}"

    try:
        with open(f"journal_entries/Journal Entry {num}.txt", "w") as f:
             f.write(journal_entry)
             print("Congratulations! You've journaled", num, p.plural("time", num))
    except FileNotFoundError:
         print("journal_entries directory does not exist")


if __name__ == "__main__":
    main()