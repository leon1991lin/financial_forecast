#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pymysql, json, requests
from bs4 import BeautifulSoup
# 與mysql進行連線
conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='{#your_code}',
                       db='tradedb',
                       charset='utf8')
conn1 = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='{#your_code}',
                       db='covidtest',
                       charset='utf8')
cur = conn.cursor()
cur1 = conn1.cursor()
data_names = ['reproduction_rate', 'positive_rate', 'new_cases_smoothed', 'people_fully_vaccinated_per_hundred']
dates = ['20201', '20202', '20203', '20204', '20211', '20212', '20213']
countries_code = ['USA', 'OWID_EUR', 'GBR', 'FRA', 'JPN', 'CHN', 'TWN', 'OWID_WRL', 'HKG', 'SGP']
for name in data_names:
    for date in dates:
        for index in countries_code:
            sql1 = f'''select {index} from covidseason_{name} where date_season = '{date}';''' 
            cur1.execute(sql1)
            value = cur1.fetchall()
            print(name+" "+date+" "+index+" ", value[0][0])
            sql2 = f''' SET SQL_SAFE_UPDATES=0;
                        update env_factor set {name}_{index} = {value[0][0]} where data_date = '{date}';
                        SET SQL_SAFE_UPDATES=1;'''
            print(f'''update env_factor set {name}_{index} = {value[0][0]} where data_date = '{date}';''')
#             cur.execute(sql2)
#             conn.commit()
#             conn1.commit()
conn.close()
conn1.close()


# In[ ]:




