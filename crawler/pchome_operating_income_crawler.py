import time
import requests
import traceback
from bs4 import BeautifulSoup

import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import OperatingRevenueMonth

Base = declarative_base()

config = configparser.ConfigParser()
config.read('./../../../config/crawler.ini')

username = config['pchome_stock_crawler-mysql']['username']     # 資料庫帳號
password = config['pchome_stock_crawler-mysql']['password']     # 資料庫密碼
host = config['pchome_stock_crawler-mysql']['host']    # 資料庫位址
port = config['pchome_stock_crawler-mysql']['port']         # 資料庫埠號
database = config['pchome_stock_crawler-mysql']['database']  # 資料庫名稱
# 建立連線引擎
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

Session = sessionmaker(bind=engine)
session = Session()

stock_code_list = ['2330','2303','2379','6488','5347','4966','2454','3529','3105','5483','3034']
#stock_code_list = ['1710']

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent,
    'Host' : 'stock.pchome.com.tw',
    'Origin' : 'https://stock.pchome.com.tw',
    'Referer' : 'https://stock.pchome.com.tw/'
}

stock_report_date_list =[]
for y in range(2016,2022):
    stock_report_date_list.append(str(y))


#抓每月營收
ss = requests.session()
for stock_code in stock_code_list:
    print(stock_code)
    #抓完網頁就休息一下，盡量不要給人家太多壓力
    #time.sleep(5)
    for stock_report_date in stock_report_date_list:
        print(stock_report_date)
        searchUrl = f'https://stock.pchome.com.tw/stock/sto3/ock2/{stock_report_date}/sid{stock_code}.html'
        searchRes = ss.get(searchUrl, headers=headers)
        soupSearchResult =BeautifulSoup(searchRes.text, 'html.parser')
        tableDivEleList=soupSearchResult.select('div[id="bttb"]')
        tableEleList=tableDivEleList[0].select('table[style="margin-top:10px"]')
        trList=tableEleList[0].select('tr')

        for j in range(3,15):
            # 取出對應 OperatingRevenueMonth 資料表的類別
            newObject = OperatingRevenueMonth.OperatingRevenueMonth()
            newObject.stock_code = stock_code
            tdList=trList[j].select('td')
            if(len(tdList)) <= 1:
                continue

            name = tdList[0].text
            value = tdList[1].text
            value = value.replace(",", "")

            if value == '':
                continue

            newObject.stock_report_date = stock_report_date+name
            newObject.operating_revenue_month = value
            session.add(newObject)
            session.commit()
            time.sleep(1)






