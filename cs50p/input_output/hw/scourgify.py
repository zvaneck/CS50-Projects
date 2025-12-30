import sys
import csv
import os

def main():

    list = []

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        with open(sys.argv[1]) as file_reader:
            reader = csv.DictReader(file_reader)
            for row in reader:
                row['last'], row['first'] = row['name'].split(",")
                list.append({"first":row['first'].strip(), "last":row['last'], "house":row['house']})
                #print(row['first'],row['last'],row['house'])


    with open(sys.argv[2], "w") as file_writer:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file_writer, fieldnames=fieldnames)
        writer.writeheader()
        for line in list:
            writer.writerow({"first":line['first'], "last":line['last'], "house":line['house']})



main()