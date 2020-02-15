#Test4.1.py
for i in range(1000,10000):
    qian = i // 1000
    bai = (i%1000)//100
    shi = (i%100)//10
    ge = i%10
    if i == qian**4 + bai**4 + shi**4 + ge**4:
        print(i)
#可以直接将数字变成字符串，取位数后再eval变成数字
