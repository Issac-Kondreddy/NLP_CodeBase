import re
string = "Hello my Number is 123456789 and my friend's number is 987654321"
reg = "\d+"
match = re.findall(reg, string)
print(match)

p = re.compile('\d+')
print(p.findall("Hello my Number is 123456789 and my friend's number is 987654321"))


p1 = re.compile('\w')
print(p1.findall("He said * in some_lang."))

p2 = re.compile('\w+')
print(p2.findall("I went to him at 11 A.M., he \
said *** in some_language."))

p3 = re.compile('\W')
print(p3.findall("he said *** in some_language."))


print(re.split("\W+", "Hello my Number is 123456789 and my friend's number is 987654321"))


print(re.sub(r"\bIssac\b", "Pranay", "This is Issac"))

import re
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")
if match != None:
    print ("Match at index %s, %s" % (match.start(), match.end()))
    print ("Full match: %s" % (match.group(0)))
    print ("Month: %s" % (match.group(1)))
    print ("Day: %s" % (match.group(2)))

else:
    print ("The regex pattern does not match.")
