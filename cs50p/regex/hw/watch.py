import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):

    if html := re.search(r"^<iframe\ ?(?:width=\"[0-9]{3}\" height=\"[0-9]{3}\")?\ ?src=\"https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9]+)\".*>.*<\/iframe>$", s):
        return (f"https://youtu.be/{html.group(1)}")
    else:
        return None

if __name__ == "__main__":
    main()