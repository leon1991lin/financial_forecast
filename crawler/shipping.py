import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import configparser

# config = configparser.ConfigParser()
# config.read('./../../../config/crawler.ini')
#
# username = config['pchome_stock_crawler-mysql']['username']     # 資料庫帳號
# password = config['pchome_stock_crawler-mysql']['password']     # 資料庫密碼
# host = config['pchome_stock_crawler-mysql']['host']    # 資料庫位址
# port = config['pchome_stock_crawler-mysql']['port']         # 資料庫埠號
# database = config['pchome_stock_crawler-mysql']['database']  # 資料庫名稱
# # 建立連線引擎
# engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

Index_code = {'BPI':'260020','BCI':'260030','BDI':'260050'}
Baltic_Indexes = ['BPI','BCI','BDI']

for i in range(len(Baltic_Indexes)):

    url = "https://fubon-ebrokerdj.fbs.com.tw/Z/ZH/ZHG/CZHG.djbcd?A={}".format(Index_code[Baltic_Indexes[i]])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)

    date = str(soup).split(" ")[0].split(",")
    index = str(soup).split(" ")[1].split(",")

    datas = {"Baltic_Index":Baltic_Indexes[i],'data_date':date,'index_price':index}
    df = pd.DataFrame(datas)
    print(df)
    print('=============================================')

    engine = create_engine('mysql+pymysql://root:{#your_code}@localhost:3306/tfb103d_project')

    df.to_sql('shipping', engine, if_exists="append", index=False)

print("Successfully!")
