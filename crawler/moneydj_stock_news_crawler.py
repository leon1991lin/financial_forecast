import time
import requests
import traceback
from bs4 import BeautifulSoup

import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymongo
import re


#連接本地端mongodb
conn = pymongo.MongoClient(host='localhost',port=27017)
#選擇或創建資料庫
moneydj = conn['moneydj']
#選擇或創建數據集合
moneydjNewsData = moneydj['moneydjNews']

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent,
    'Host' : 'stock.pchome.com.tw',
    'Origin' : 'https://www.moneydj.com',
    'Referer' : 'https://www.moneydj.com'
}

ss = requests.session()
for index in range(1,2513):
    print("page="+str(index))
    newsDataList=[]
    searchUrl = f'https://www.moneydj.com/kmdj/news/newsreallist.aspx?index1={index}&a=mb010000'
    searchRes = ss.get(searchUrl, headers=headers)
    soupSearchResult = BeautifulSoup(searchRes.text, 'html.parser')
    tableEleList = soupSearchResult.select('table[id="MainContent_Contents_sl_gvList"]')
    trEleList=tableEleList[0].select('tr')
    for trIndex in range(1,21):
        time.sleep(1)
        ahref=trEleList[trIndex].select('a')[0].attrs
        title=trEleList[trIndex].select('a')[0].text
        url ='https://www.moneydj.com'+ahref['href']
        contentRes = ss.get(url, headers=headers)
        contentResult = BeautifulSoup(contentRes.text, 'html.parser')
        timeEleList = contentResult.findAll('span',{'id':'MainContent_Contents_lbDate'})
        date = timeEleList[0].text

        pContentList=contentResult.select('div[class="wikilink"]')[0].select('p')

        content =''
        for pContent in pContentList:
            content += pContent.text
        moneydj_data = {'title': title, 'content': content, 'url': url,'date':date}
        newsDataList.append(moneydj_data)

    moneydjNewsData.insert_many(newsDataList)
