# import urllib.request
# from urllib import request
import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

# 與 urllib 寫法差異。
# req = request.Request(url=url, headers=headers)
# res = request.urlopen(req)
res = requests.get(url, headers=headers)
print(type(res))

# 預設編碼與物件相容相對友好，省去轉換的過程。
# html = res.read().decode('utf-8')
html = res.text
print(html)