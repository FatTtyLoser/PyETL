from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.google.com/'

# 透過程式訪問網頁伺服器會辨識來源的身分，將headers帶入與瀏覽器相同的headers做偽裝。
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

# request的縮寫，參數(url, headers)
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

html = res.read().decode('utf-8')
# print(html)