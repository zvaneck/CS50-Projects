def main():
    greeting = input("Greeting: ")
    check = check_greeting(greeting)
    if check == 0:
        print("$100")
    elif check == 1:
        print("$20")
    else:
        print("$0")

def check_greeting(x):
    if "Hello" in x:
        return 2
    elif x[0].casefold() == "h":
        return 1
    else:
        return 0

main()