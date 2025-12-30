import re

name = input("Name: ").strip()

'''
if "i" in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
'''
'''
matches = re.search(r"^(.+),\ *(.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
'''

if matches := re.search(r"^(.+),\ *(.+)$", name):
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")

