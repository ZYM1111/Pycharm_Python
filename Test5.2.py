#Test5.2.py

'''
不用.join()
def is_Prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True
k = 0
n = eval(input())
if n % 1 != 0:
    n = int(n) + 1
while k<5:
    if is_Prime(n):
        print(n,end='')
        if k < 4:
            print(",",end="")
        k += 1
    n += 1
'''
#使用.join()
def is_Prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True
k = 0
ls = []
n = eval(input())
if n % 1 != 0:
    n = int(n) + 1
while k<5:
    if is_Prime(n):
        ls.append(str(n))
        k += 1
    n += 1
print(",".join(ls))


