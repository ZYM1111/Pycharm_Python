#Test1.1.py
#输出 helloworld
i = eval(input())
str = "Hello World"
if i < 0:
    for j in range(11):
        print(str[j])
elif i > 0:
    for j in range(0,11,2):
        if j < 10:
            print(str[j]+str[j+1])
        else:
            print(str[j])
else:
    print(str)
