import jieba as jb
from wordcloud import WordCloud 
import csv

#  读取hot_search.csv文件

data = []
with open("Archieved_feb.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row[1])

#  使用jieba进行分词

words_list = []
stopwords = [' ', '男子', '女子', '被', '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这', '个', '秒', '最', '或', '多', '过', '太', '请', '做', '想', '当', '只', '再', '因', '等', '次', '中', '要求', '不要', '六', '吗', '前', '回应', '称', '曾', '遭', '一天', '发现', '为', '时', '与', '超', '比', '原来', '为什么', '将']
for item in data:
    ret = jb.lcut(item)
    for word in ret:
        if word not in stopwords:
            words_list.append(word)

#  生成词云图

words = ' '.join(words_list)

font_path = 'C:/Windows/Fonts/simhei.ttf'
w = WordCloud(font_path=font_path, height=800, width=1000)
w.generate(str(words))
w.to_file(rf'./assets/feb.png')
