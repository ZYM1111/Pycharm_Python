#CalHamletV1.py
def getText():
    txt = open("CalHamletV1.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&*()+,-./:;<>=?@[\\]^‘{|}~':
        txt = txt.replace(ch, " ")
    return txt
hamletText = getText()
words = hamletText.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
    #counts[word] = words.count(word) #效率较低
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word , count = items[i]
    print("{:<10}{:>5}".format(word,count))
