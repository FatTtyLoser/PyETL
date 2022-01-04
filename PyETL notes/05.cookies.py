import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent' : useragent
}
cookies = {
    'over18' : '1'
}
session_requests = requests.session()
session_requests.cookies['over18'] = '1'

# 沒帶入 cookie 時無法入版訪問，透過瀏覽器觀察cookie內容，適用於年齡或真值訪問的簡單入口網站。
# 將cookie作為參數帶入get訪問或是將 cookies 先帶入seession於get前先訪問再請求資料亦可。
# res1 = requests.get(url=url, headers=headers)
res2 = requests.get(url=url, headers=headers, cookies=cookies)
res3 = session_requests.get(url=url, headers=headers)
# print(res1.text)
print(res2.text)
print(res3.text)