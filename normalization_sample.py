string = "       Python 3.0, released in 2008, was a major revision of the language that is not completely backward compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows)."
lower_string = string.lower()
print("String Lowered: ", lower_string)

#numbers removed
import re
no_number_string = re.sub(r'\d+','',lower_string)
print("Numbers removed from string: ", no_number_string)

#removing puncatuation

no_pun_string = re.sub(r'[^\w\s]','',no_number_string)
print("Puncations removed String: ", no_pun_string)

#Removing white spaces
no_wspace_string = no_pun_string.strip()
print(no_wspace_string)

#remove stop words
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)
list_string = no_wspace_string.split()
print(list_string)
no_stopword_string = ""
for i in list_string:
    if i not in stop_words:
        no_stopword_string += i + " "

print(no_stopword_string)