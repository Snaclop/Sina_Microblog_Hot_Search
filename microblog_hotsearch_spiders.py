import requests
import datetime
import pandas as pd
import datetime

url = "https://weibo.com/ajax/side/hotSearch"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    ),
    "Referer": "https://weibo.com/",
}

resp = requests.get(url=url, headers=headers)
resp.close()
resp = resp.json()
hot_list = []

for item in resp['data']['realtime']:
    hot_list.append(item['word'])

data = {'时间': datetime.datetime.today(), '热搜': hot_list}
DataFrame = pd.DataFrame(data=data)
print(DataFrame)

DataFrame.to_csv('Hot_search.csv', index=False, mode='a', header=False)
