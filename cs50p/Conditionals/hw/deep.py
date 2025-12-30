ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

match ans.casefold().replace(" ",""):
    case "42"|"fortytwo"|"forty-two":
        print("Yes")
    case _:
        print("No")