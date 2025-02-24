import requests
import datetime
import pandas as pd
import datetime
from datetime import timedelta

time = datetime.datetime.today()

url = 'https://weibo.com/ajax/side/hotSearch'

resp = requests.get(url=url)
resp.close()
resp = resp.json()
hot_list = []

for i in range(len(resp['data']['realtime'])):
    item = resp['data']['realtime'][i]['word']
    hot_list.append(item)

data = {'时间': time, '热搜': hot_list}
DataFrame = pd.DataFrame(data=data)
print(DataFrame)

DataFrame.to_csv('Hot_search.csv', index=False, mode='a', header=False)