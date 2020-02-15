#Test7.2.py
#法一
f = open("Test7.2.csv","r",encoding='utf-8')
ls = f.readlines()
lt = []
for item in ls:
    item = item[::-1]
    item = item.replace(" ","")
    item = item.strip("\n")
    item = item.replace(",", ";")
    lt.append(item)
lt = lt[::-1]
for item1 in lt:
    print(item1)
f.close()
#法二
f = open("Test7.2.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()
'''
3;8;6;1;7;4;2;5
'k';'j';'i';'c';'z';'x';'b';'y';'a'
'x';'y';'j';'i';'k';'a';'b';'c';'z'
'x';'a';'z';'y';'i';'c';'j';'b';'k'
'k';'j';'i';'z';'y';'x';'c';'b';'a'
2;4;7;5;8;3;1;6
5;6;4;1;7;2;3;8
7;6;5;4;3;2;1
'''
'''
3;8;6;1;7;4;2;5
'k';'j';'i';'c';'z';'x';'b';'y';'a'
'x';'y';'j';'i';'k';'a';'b';'c';'z'
'x';'a';'z';'y';'i';'c';'j';'b';'k'
'k';'j';'i';'z';'y';'x';'c';'b';'a'
2;4;7;5;8;3;1;6
5;6;4;1;7;2;3;8
7;6;5;4;3;2;1
'''
