calc = input("Math problem: ")

array = calc.split(" ")

x = int(array[0])
y = array[1]
z = int(array[2])

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
