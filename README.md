# Sina Microblog Hot Search Spiders 微博热搜爬虫

利用新浪微博的开放接口`https://weibo.com/ajax/side/hotSearch`获取数据

所有数据均保存在同目录下的Hot_search.csv文件里，并带有数据获取时间

一天的热搜数据并不完全相同，会随着时间变化而变化，所以每天运行两次，每次获取50条热搜数据，计划运行一年

当数据量足够庞大时，可据此生成微博热搜词云图
