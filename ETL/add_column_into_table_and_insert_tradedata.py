#!/usr/bin/env python
# coding: utf-8

# In[84]:


# import pymysql, json, requests
# from bs4 import BeautifulSoup
# # 與mysql進行連線
# conn = pymysql.Connect(host='127.0.0.1',
#                        port=3306,
#                        user='root',
#                        passwd='password',
#                        db='tradedb',
#                        charset='utf8')
# cur = conn.cursor()
# import_export_type = ['export', 'import']
# data_names = ['usd_value', 'ntd_value', 'tne_weight', 'kgm_weight']
# items_code = ['381800', '848610', '848620', '37050000306', '37079090', '37071000', '2804', '2801']
# for typee in import_export_type:
#     for name in data_names:
#         for item in items_code:
#             sql1 = f'''alter table env_factor add column {typee}_{name}_{item} integer ;''' 
# #             print(sql1)
#             cur.execute(sql1)
#             conn.commit()
# conn.close()

import pymysql, json, requests
from bs4 import BeautifulSoup
# 與mysql進行連線
conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='password',
                       db='tradedb',
                       charset='utf8')
cur = conn.cursor()
data_names = ['reproduction_rate', 'positive_rate', 'new_cases_smoothed', 'people_fully_vaccinated_per_hundred']
countries_code = ['USA', 'OWID_EUR', 'GBR', 'FRA', 'JPN', 'CHN', 'TWN', 'OWID_WRL', 'HKG', 'SGP']
for name in data_names:
    for index in countries_code:
        sql1 = f'''alter table env_factor add column {name}_{index} float(10,2) ;''' 
#             print(sql1)
        cur.execute(sql1)
        conn.commit()
conn.close()

# import pandas as pd
# from sqlalchemy import create_engine

# class mysql_engine():
#  user='root'
#  passwd='password'
#  host='localhost'
#  port = '3306'
#  db_name='tradedb'
#  engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,passwd,host,port,db_name))

# def get_data(sql):
#  pg_enine = mysql_engine()
#  try:
#   with pg_enine.engine.connect() as con, con.begin():
#    df = pd.read_sql(sql,con) # 獲取資料
#   con.close()
#  except:
#   df = None
#  return df
# import_export_type = ['export', 'import']
# data_names = ['usd_value', 'ntd_value', 'tne_weight', 'kgm_weight']
# items_code = ['381800', '848610', '848620', '37050000306', '37079090', '37071000', '2804', '2801']
# df_items = pd.DataFrame()
# for typee in import_export_type:
#     for name in data_names:
#         for item in items_code:
#             tmp = get_data(f"SELECT date_season data_date, code_{item} {typee}_{name}_{item} from trade_{typee}_{name} WHERE date_season > '20181' ORDER BY date_season;")
# #             print('@@@@@@@@@@')
# #             print(tmp)
#             try:
#                 df_items.insert(1,f"{typee}_{name}_{item}",tmp[f"{typee}_{name}_{item}"])
# #                 print('-----')
# #                 print(df_items)
#             except:
#                 df_items = tmp
# #                 print('aa')
# # print(df_items)
# enine = mysql_engine()
# df1 =  get_data(f"SELECT data_date,BDI,BCI,BPI,N1NG,avgas_cpc,avgas_fpg,Dubai,WTI_future,WTI_now,WBR_future,WBR_now,avg_import_rate,avg_export_rate FROM env_factor ORDER BY data_date;")
# df2 = pd.merge(df1,df_items,on="data_date",how="outer")
# print(df2)
# df2.to_sql('env_factor' , enine.engine, if_exists="replace", index=False)


# In[ ]:





# In[ ]:




