import jieba as jb
import wordcloud as wc
import pandas as pd

#  读取hot_search.csv文件



result_list = jb.lcut(search)

stopwords = ["的", "是", "说", "称", "了", "你"]

