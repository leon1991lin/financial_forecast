import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

Index_code = {'WBR_now':'131670','WBR_future':'130820','WTI_now':'131680','WTI_future':'130810','Dubai':'131690',
              'avgas_fpg':'260100','avgas_cpc':'260080'}
crude_indexes = ['WBR_now','WBR_future','WTI_now','WTI_future','Dubai','avgas_fpg','avgas_cpc']

#unit: USD,USD,USD,USD,USD, USD/L, USD/GAL

for i in range(len(crude_indexes)):

    url = "https://fubon-ebrokerdj.fbs.com.tw/Z/ZH/ZHG/CZHG.djbcd?A={}".format(Index_code[crude_indexes[i]])
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)

    date = str(soup).split(" ")[0].split(",")
    price = str(soup).split(" ")[1].split(",")

    datas = {"crude_index":crude_indexes[i],'data_date':date,'price':price}
    df = pd.DataFrame(datas)
    print(df)
    print('=============================================')

    engine = create_engine('mysql+pymysql://root:ian1991@localhost:3306/tfb103d_project')

    df.to_sql('air_transport', engine, if_exists="append", index=False)

print("Successfully!")