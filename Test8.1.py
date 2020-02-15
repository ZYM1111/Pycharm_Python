#Test8.1.py
str = input()
for i in str:
    if 65<= ord(i) <=90 or 97<= ord(i) <= 122:
        print(i,end="")
'''
alpha = []
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
构造一个字母表列表
'''