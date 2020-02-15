#CalThreeKingdomsV2.py
import jieba
txt = open("CalThreeKingdomsV2.txt","r",encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "军士", "不能",\
            "如此", "商议", "如何", "主公", "左右", "军马", "次日",\
            "大喜", "引兵", "天下", "东吴", "于是", "不敢", "今日",\
            "魏兵", "陛下", "人马", "不知", "一人", "都督", "汉中",\
            "众将", "只见", "后主", "蜀兵", "大叫", "上马", "此人",\
            "先主", "太守", "天子", "后人", "背后", "城中", "一面",\
            "何不", "忽报", "大军", "先生", "何故", "然后", "先锋",\
            "夫人", "不如", "赶来", "原来", "令人", "江东", "徐州"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "丞相" or word == "孟德":
        rword = "曹操"
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))