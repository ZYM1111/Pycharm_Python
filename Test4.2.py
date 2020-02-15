#Test4.2.py
'''
s = 5
b = 1
for i in range(5,100):
    for a in range(2,int(pow(i, 0.5))+1):
        if i%a == 0:
            b = 0
            break
        else:
            b = 1
    if b == 1:
        s += i
print(s)
'''
def is_Prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

s = 0 #range(2,2)为空，什么也不发生，所以is_Prime(2)返回True
for i in range(2,100):
    if is_Prime(i):
        s += i
print(s)
