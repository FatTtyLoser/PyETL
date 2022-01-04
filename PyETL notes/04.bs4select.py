import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Lifeismoney/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

res = requests.get(url=url, headers=headers)
html = res.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# slect() 使用 id 定位與 findAll() 寫法無異
# slect('tag') 調用所有符合 tag 的物件，selece_one() 則與 find() 相同只有第一個符合之物件。
logo = soup.select('a', {'id': 'logo'})
logo = soup.select('a', id='logo')
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])

content = soup.select('div', class_='bbs-content')
# print(content[0])

board = content[0].select_one('a', class_="board")
print(board)

# select() 直接定位標籤 return list
board_text = soup.select('.board')
print(board_text)
# select() 直接定位標籤 return str
board_text = soup.select_one('.board')
print(board_text)
print('https://www.ptt.cc' + board_text['href'])

# 直接定位標籤中的標籤。
title = soup.select('head title')
print(title)