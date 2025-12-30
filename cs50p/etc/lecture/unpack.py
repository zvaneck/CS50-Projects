def f(*args, **kwargs):
    for arg in range(len(args)):
        print("positional:", args[arg])


f(100, 50, 25)
