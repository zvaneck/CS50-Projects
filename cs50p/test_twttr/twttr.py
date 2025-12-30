def main():

    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in range(len(vowels)):
        word = word.replace(vowels[i], "")
    return word

if __name__ == "__main__":
    main()
