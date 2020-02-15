#Test6.1.pu
N = input()
ls = []
sum = 0
for i in range(len(N)):
    ls.append(eval(N[i]))
for n in range(10):
    if ls.count(n) > 0:
        sum += n
print(sum)
#使用集合的数据去重功能
'''
n = input()
ss = set(n)
s = 0
for i in ss:
    s += eval(i)
print(s)
'''