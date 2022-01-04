#!/usr/bin/python
# -*- coding: utf-8 -*-
# 程式檔的標頭，宣告你所使用的語言、編碼為何，由於python3預設，可以省略。

# urllib.request是python內建用於url取得資源的模組。
from urllib import request

# 爬蟲時有些網站需要帶入ssl，此處設置unverified略過ssl驗證錯誤，直接讓程式訪問網頁。
# 最好的方法是更新certifi，並下載證書帶入程式裡。本套件只有urllib可用，requests為第三方套件，不能用此方式。
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.google.com'

# respond縮寫，接收我們請求的資料。
res = request.urlopen(url=url)

# 此時的res成為HTTPResponse物件，所以需要解析才可讀，標註utf-8編碼解析助於識別華文(無論繁簡)。
html = res.read().decode('utf-8')
# print(html)