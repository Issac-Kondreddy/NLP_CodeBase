import re
s = "Hey, This is Issac Kondreddy studying Masters and searching for a job"
match = re.search(r"Masters", s)
print("start Index: ",match.start())
print("end Index: ", match.end())