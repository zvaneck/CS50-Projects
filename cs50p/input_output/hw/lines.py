import sys
import os.path

def main():

    num_lines = 0

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        #print(sys.argv[1][-3:])
        sys.exit("Not a Python file")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    pass
                elif line.lstrip():
                    num_lines += 1
                else:
                    pass
        print(num_lines)

main()