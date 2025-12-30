def main():
    dict = {}
    while True:
        try:
            new_item = input()
            if new_item not in dict:
                dict[new_item] = 1
            elif new_item in dict:
                dict[new_item] += 1
            else:
                pass
        except EOFError:
            break

    for key in sorted(dict.keys()):
        print(dict[key], key.upper())

main()