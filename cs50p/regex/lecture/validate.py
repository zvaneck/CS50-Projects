import re

'''
email = input("Email: ")

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
'''

email = input("Email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")