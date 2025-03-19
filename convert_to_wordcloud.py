import jieba as jb
import wordcloud as wc


#  读取hot_search.csv文件

with open("Hot_search.csv", mode="r", encoding="utf-8") as file:
    pass


result_list = jb.lcut(search, cut_all=False)
print(result_list)

stopwords = ["的", "是", "说", "称", "了", "你", " "]

