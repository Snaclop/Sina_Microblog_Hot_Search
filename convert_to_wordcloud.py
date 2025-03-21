import jieba as jb
import wordcloud as wc
import csv

#  读取hot_search.csv文件

data = []
with open("Hot_search.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row[1])
    print(data)


stopwords = ["的", "是", "说", "称", "了", "你", " "]

