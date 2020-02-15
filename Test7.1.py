#Test7.1.py

f = open("Test7.1.log")
s, c = 0, 0
for i in f:
    i = i.strip("\n")
    if i == "":
        continue
    else:
        s += len(i)
        c += 1
print(s/c)
