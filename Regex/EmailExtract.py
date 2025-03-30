import re

string = "Hello issackondreddy@gmail.com, the second account on your name is work.issackondreddy@gmail.com"

patterns = r"([a-zA-Z0-9.]+\@[a-zA-Z]+\.[a-zA-Z]+)"

match = re.findall(patterns, string)
print(match)
