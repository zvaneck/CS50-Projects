import re

url = input("URL: ").strip()

#username = url.removeprefix("https://twitter.com/", "")

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

matches = re.search(r"^https?://?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(1))