import os
import sys
import csv
from tabulate import tabulate

def main():

    menu = []

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
                #print(row)

    #print(menu)
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))




main()