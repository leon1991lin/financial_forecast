import time
import os
import requests
import json
from bs4 import BeautifulSoup
import pymongo


useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
headers = {'User-Agent' : useragent}

#連接本地端mongodb
conn = pymongo.MongoClient(host='localhost',port=27017)
#選擇或創建資料庫
ptt = conn['pttStock']
#選擇或創建數據集合
pttStockData = ptt['stockNews']


ptt_stock_data = []
#PTTSTOCK版總頁數
indexNum = 4998

countArticle = 0
while indexNum > 4995:
    url = f"https://www.ptt.cc/bbs/Stock/index{indexNum}.html"

    ss = requests.session()

    res = ss.get(url, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    article_title_html = soup.select('div[class="title"]')
    # print(article_title_html)

    for each_article in article_title_html:


        # print("https://www.ptt.cc"+each_article.a['href'])
        try:
            #各篇文章標題
            article_text = each_article.a.text
            # 各篇文章URL
            article_url = "https://www.ptt.cc"+each_article.a['href']
            print(article_text)

            article_res = ss.get(article_url, headers = headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')

            article_content = article_soup.select('div#main-content')[0].text.split("--")[0].strip()

            # print(article_content)
            #將爬取的標題、內容、URL存成JSON格式
            ptt_data = {'title': article_text, 'content': article_content, 'url': article_url}

            ptt_stock_data.append(ptt_data)
            countArticle += 1
            # ptt_data累積50筆存入mongoDB一次
            while countArticle == 50:
                print(ptt_stock_data)
                pttStockData.insert_many(ptt_stock_data)
                countArticle = 0
                ptt_stock_data = []
        except:
            pass


    indexNum -= 1
#最後將未累積滿50筆資料直接存入mongoDB
pttStockData.insert_many(ptt_stock_data)



