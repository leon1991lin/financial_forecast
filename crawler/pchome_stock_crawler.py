import time
import requests
import traceback
from bs4 import BeautifulSoup

import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import FinacialStatements

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
#stock_code_list = ['2330']

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent,
    'Host' : 'stock.pchome.com.tw',
    'Origin' : 'https://stock.pchome.com.tw',
    'Referer' : 'https://stock.pchome.com.tw/'
}

stock_report_date_list =[]
for y in range(2016,2021):
    for season in range(1,5):
        stock_report_date_list.append(str(y)+str(season))

stock_report_date_list.append('20211')
stock_report_date_list.append('20212')


#抓財務報表
ss = requests.session()
for stock_code in stock_code_list:
    #抓完網頁就休息一下，盡量不要給人家太多壓力
    time.sleep(5)
    for stock_report_date in stock_report_date_list:
        # 取出對應 stocks 資料表的類別
        newObject = FinacialStatements.FinacialStatements()
        newObject.stock_code=stock_code
        newObject.stock_report_date = stock_report_date
		
        print(stock_code)
        print(stock_report_date)
		
        #0:資產負債表
        #1:損益表
        #2:財務比率
        #3:現金流量
        for i in range(0,4):
            searchUrl = f'https://stock.pchome.com.tw/stock/sto2/ock{i}/{stock_report_date}/sid{stock_code}.html'
            searchRes = ss.get(searchUrl, headers=headers)
            soupSearchResult =BeautifulSoup(searchRes.text, 'html.parser')
            tableDivEleList=soupSearchResult.select('div[id="bttb"]')
            tableEleList=tableDivEleList[0].select('table[style="margin-top:10px"]')
            trList=tableEleList[0].select('tr')
			
            for tr in trList:
                results = tr.findAll("td",{"class":"ct3"})
                tdList=tr.select('td')
                if(len(tdList)) <= 1:
                    continue

                if(len(results) > 0):
                    name = tdList[1].text
                    value = tdList[2].text
                else:
                    name = tdList[0].text
                    value = tdList[1].text

                if value in '-':
                    continue
                value = value.replace(",","")

                #print(name)
                #print(value)
                if "存   貨" in name:
                    newObject.inventories = value
                elif '應收帳款淨額' in name:
                    newObject.receivables = value
                elif '現金及約當現金' in name:
                    newObject.cash_equiv = value
                elif '流動資產' in name:
                    newObject.cur_assets = value
                elif '流動負債' in name:
                    newObject.cur_liabilities = value
                elif '短期借款' in name:
                    newObject.short_debt = value
                elif '應付帳款' in name:
                    newObject.acc_payable = value
                elif '一年' in name:
                    newObject.one_year_liabilities = value
                elif '長期借款' in name:
                    newObject.long_loan = value
                elif '保留盈餘' in name:
                    newObject.retained_earnings = value
                elif '營業收入' in name:
                    newObject.operating_revenue_season = value
                elif '營業成本' in name:
                    newObject.operating_costs = value
                elif '營業毛利(毛損)' in name:
                    newObject.operating_profit = value
                elif '研究發展費用' in name:
                    newObject.research_expense = value
                elif '本期淨利' in name:
                    newObject.tax_interest_income = value
                elif '營業毛利率' in name:
                    newObject.operating_gross_rate = value
                elif '稅後淨利率' in name:
                    newObject.net_profit_rate = value
                elif '營收成長率' in name:
                    newObject.revenue_growth_rate = value
                elif '流動比率' in name:
                    newObject.current_rate = value
                elif '速動比率' in name:
                    newObject.quick_rate = value
                elif '負債比率' in name:
                    newObject.debt_rate = value
                elif '應收帳款週轉率' in name:
                    newObject.receivables_turnover_rate = value
                elif '存貨週轉率' in name:
                    newObject.inventory_turnover_rate = value
                elif '現金再投資比率' in name:
                    newObject.cash_reinvest_rate = value
                elif '本期淨利' in name:
                    newObject.tax_interest_income = value
                elif '營業活動現金流量' in name:
                    newObject.cashflows_operating = value
                elif '投資活動現金流量' in name:
                    newObject.invest_operating = value

            time.sleep(1)

        session.add(newObject)
        session.commit()


