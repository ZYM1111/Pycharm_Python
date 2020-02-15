#ReverseChar.py
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:]) + s[0]
s = input()
print(rvs(s))
