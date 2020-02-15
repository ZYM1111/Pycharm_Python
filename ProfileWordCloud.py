#ProfileWordCloud.py
import jieba
import wordcloud

t1 = ""
t2 = ""
t3 = ""
t4 = ""

f1 = open("Doctor.txt","r",encoding="utf-8")
t = f1.read(100)
while t != "":
    t1 = t1 + t
    t = f1.read(100)
f1.close()

f2 = open("惊艳的句子.txt", "r", encoding="utf-8")
t = f2.read(100)
while t != "":
    t2 = t2 + t
    t = f2.read(100)
f2.close()

f3 = open("白发苏州.txt", "r", encoding="utf-8")
t = f3.read(100)
while t != "":
    t3 = t3 + t
    t = f3.read(100)
f3.close()

f4 = open("ProfileWordCloud.txt", "r", encoding="utf-8")
t = f4.read(100)
while t != "":
    t4 = t4 + t
    t = f4.read(100)
f4.close()

txt_1 = t1 + t2 + t3 + t4
ls = jieba.lcut(txt_1)
txt = " ".join(ls)

w = wordcloud.WordCloud(font_path="font1.ttf",\
                        width = 1000, height = 700,\
                        background_color="white")
w.generate(txt)
w.to_file("ProfileWordCloud.jpg")