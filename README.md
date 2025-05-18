# Sina Microblog Hot Search Spiders 微博热搜爬虫

利用新浪微博的开放接口`https://weibo.com/ajax/side/hotSearch`获取数据

所有数据均保存在同目录下的`Hot_search.csv`文件里，并带有数据获取时间  
注：从2025年3月22日开始，将采用GitHub Actions实现爬虫的自动化获取数据，设定时间是北京时间20:00（UTC时间12:00）由于GitHub获得的时间是UTC时间，因此在`Hot_search.csv`文件里显示的时间是UTC时间而不是北京时间

当数据量足够庞大时，可据此生成微博热搜词云图，相关代码正在开发中……由于数据量过于庞大，无法从`Hot_search.csv`中读取全部数据，因此最新计划是按月生成词云图

现在已更新4月份的热搜词云图

2月热搜
![feb_png](./assets/feb.png)

4月热搜
![apr_png](./assets/apr.png)
