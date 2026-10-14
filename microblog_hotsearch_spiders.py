import requests
import datetime
import pandas as pd
import datetime

url = "https://60s.viki.moe/v2/weibo"

resp = requests.get(url=url)
resp.close()
resp = resp.json()
hot_list = []

for i in range(len(resp['data'])):
    item = resp['data'][i]['title']
    hot_list.append(item)

data = {'时间': datetime.datetime.today(), '热搜': hot_list}
DataFrame = pd.DataFrame(data=data)
print(DataFrame)

DataFrame.to_csv('Hot_search.csv', index=False, mode='a', header=False)