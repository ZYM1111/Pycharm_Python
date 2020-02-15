#Test8.2.py
'''
str = input()
val = eval(str)
k = 1
for i in str:
    if 48<= ord(i)<= 57:
        k = 1
    else:
        k = 0
        break
if type(val) == complex or\
    type(val) == float:
    print(val**2,end="")
elif type(val) == int and\
    k == 1:
    print(val**2)
else:
    print("输入有误")
'''
#这是一个重要方法，若s = 一个算式(string),则complex(s)会报错:complex() arg is a malformed string
s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")

