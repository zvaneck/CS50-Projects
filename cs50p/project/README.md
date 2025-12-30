# Personal Journal Application
    #### Video Demo:  <https://youtu.be/Sr8DpN1rW2M>
    ## Description:
    This Python program is a simple journal writing and recording application. It will automatically record the current date, and then prompt the user for the times they went to bed and woke up, three things they are grateful for and finally the main journal entry which can be modified to have a miniumum word count.

    ## Features:
    - Automatically records the current date and converts to "Month Day, Year" format.
    - Automatically calculates which number journal entry is being written based on the number of existing journal entries.
    - Prompts the user for the time they went to bed the previous night and the time they woke that morning.
    - Checks that the times entered by the user adhere to the format "X:XX AM/PM or XX:XX AM/PM"
    - Prompts the user to list three things they are greatful for and records them in a numbered list
    - Prompts the user for a journal entry with a minimum word count.

    ## Use:
    To run the program, navigate to the directory that the project.py file is located, ensure that a directory named "journal_entries" exists in the same path, and run "python project.py" in your command line.

    ## Dependencies:
    The required libraries to run this program are as follows:
        - datetime
        - calendar
        - os
        - re
        - inflect

    ## Project Structure:
    #### 'main()'
    The main function organizes the creation of the current journal entry.
    #### 'get_current_date(today)'
    Takes a datetime object converted to a string as an input and returns a properly formatted string of the current date as output.
    #### 'get_entry_number()'
    Determines the entry number of the current journal entry by finding the number of previous journal entries in the 'journal_entries' directory.
    #### 'get_sleep_times(time)'
    Takes the user input of their bed or wake time and compares it to a regular expression to ensure it adheres to the desired format of 'X:XX AM/PM' or 'XX:XX AM/PM'.
    #### 'get_gratitude()'
    Prompts the user for 3 things they are grateful for, storing them in a list with the matching item number preceding each one.
    #### 'get_journal_content(content, min_words)'
    Takes as input the content provided by the user (i.e. the main journal entry) as well as the minimum number of words required for the entry. It then evaluates whether the provided entry satisfies the minimum words requirement, if not it re-prompts the user for additional input and specifies the number of words remaining to meet the minimum requirement.
    #### 'save_journal_entry(date, num, bed, wake, gr, entry)'
    Takes as input all of the previous values (i.e. date, entry number, bed and wake times, gratitude items and main entry) and combines them into a single string of a desired format. It then saves this string as a new text file in the 'journal_entries' directory and congratulates the user for successfully submitting a journal entry.