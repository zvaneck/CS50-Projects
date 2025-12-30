import sys
from PIL import Image, ImageOps
import os

def main():

    check_file()

    shirt = open_image("shirt.png")
    photo = open_image(sys.argv[1])

    photo = fit_image(photo, shirt)
    paste_image(photo, shirt)

    photo.save(sys.argv[2])


def check_file():

    #print(os.path.splitext(sys.argv[1])[1])
    file_types = [".jpg", ".jpeg", ".png"]

    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    elif os.path.splitext(sys.argv[1])[1] not in file_types:
            sys.exit("Unsupported file type")
    elif os.path.splitext(sys.argv[2])[1] not in file_types:
            sys.exit("Unsupported file type")
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("No shared filetype")
    else:
        return True

def open_image(img):
    return Image.open(img)

def fit_image(photo, shirt):
    size = shirt.size
    return ImageOps.fit(photo, size)

def paste_image(photo, shirt):
    photo.paste(shirt, shirt)

if __name__ == "__main__":
    main()