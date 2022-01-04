from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'
UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent' : UserAgent
}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

# 透過bs4讓html從http物件轉為bs4物件
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# bs4有兩種提取網頁資訊的索引方式 find() & css選擇器 select()
# 可以有不同的寫法，find() = findALL('tag' , limit=1)
logo = soup.findAll('a', {'id': 'logo'})
logo = soup.find_all('a', id='logo')
print(logo)
print(logo[0].text)

# logo list裡面仍可進一步提取目標屬性 href 為css中超連結的縮寫。
# print('https://www.ptt.cc' + logo[0]['href'])

# soup 已經是bs4物件，所以可以直接使用 .tag 找到目標物件並重複引用，用來調用下一層。
head = soup.head
title = soup.head.title
# 但此寫法只能調用到第一個符合 tags 的物件。
link_1 = soup.head.link
print(link_1)

# 使用find()物件為 .Tag 物件，而findAll()則是回傳list( .Set 物件)
content = soup.findAll('div', class_='bbs-content')
print(type(content))
# 利用上一層的物件繼續透過find()method定位搜尋。
board = content[0].find_all('a', class_="board")
print(board)