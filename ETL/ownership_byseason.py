import pandas as pd
from sqlalchemy import create_engine

class mysql_engine():
 user='root'
 passwd='{#your_code}'
 host='localhost'
 port = '3306'
 db_name='tfb103d_project'
 engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,passwd,host,port,db_name))

def get_data(sql):
 pg_enine=mysql_engine()
 try:
  with pg_enine.engine.connect() as con, con.begin():
   df=pd.read_sql(sql,con)# 獲取資料
  con.close()
 except:
  df=None
 return df

seasons ={"20182": 'data_date < "2018-07-01"',
           "20183": 'data_date >= "2018-07-01" and data_date < "2018-10-01"',
           "20184": 'data_date >= "2018-10-01" and data_date < "2019-01-01"',
           "20191": 'data_date >= "2019-01-01" and data_date < "2019-04-01"',
           "20192": 'data_date >= "2019-04-01" and data_date < "2019-07-01"',
           "20193": 'data_date >= "2019-07-01" and data_date < "2019-10-01"',
           "20194": 'data_date >= "2019-10-01" and data_date < "2020-01-01"',
           "20201": 'data_date >= "2020-01-01" and data_date < "2020-04-01"',
           "20202": 'data_date >= "2020-04-01" and data_date < "2020-07-01"',
           "20203": 'data_date >= "2020-07-01" and data_date < "2020-10-01"',
           "20204": 'data_date >= "2020-10-01" and data_date < "2021-01-01"',
           "20211": 'data_date >= "2021-01-01" and data_date < "2021-04-01"',
           "20212": 'data_date >= "2021-04-01" and data_date < "2021-07-01"',
           "20213": 'data_date >= "2021-07-01" and data_date < "2021-10-01"'}

for key, value in seasons.items():
    ownership = get_data(f'''select stock_code, round(avg(avg_board),2) avg_board_bys, round(avg(over1000_rate),2) over1000_rate_bys, round(avg(100 - over400_rate),2) under400_rate_bys 
    from ownership
    where {value}
    group by stock_code;''')
    ownership.insert(0,"data_date",key)
    own_engine = mysql_engine()
    ownership.to_sql('ownership_afetl', own_engine.engine, if_exists="append", index=False)
    print(str(key) + " was finish!")

