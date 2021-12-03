import pandas as pd
from sqlalchemy import create_engine

class mysql_engine():
 user='root'
 passwd='password'
 host='localhost'
 port = '3306'
 db_name='tradedb'
 engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,passwd,host,port,db_name))

def get_data(sql):
 pg_enine = mysql_engine()
 try:
  with pg_enine.engine.connect() as con, con.begin():
   df = pd.read_sql(sql,con) # 獲取資料
  con.close()
 except:
  df = None
 return df
import_export_type = {'export': '出口總值(含復出口)', 'import': '進口總值(含復進口)'}
data_names = ['usd_value', 'ntd_value', 'tne_weight', 'kgm_weight']
items_code = ['381800', '848610', '848620', '37050000306', '37079090', '37071000', '2804', '2801']
for key, value in import_export_type.items():
    for name in data_names:
        for index in items_code:
            tmp = get_data(f"SELECT date_season, {name} 'code_{index}' from tradeseason WHERE commodity_code ='{index}' and imports_exports = '{value}' and date_season > '20174' ORDER BY date_season;")
            # print(f"SELECT date_season, {name} '{index}' from tradeseason WHERE commodity_code ='{index}' and imports_exports = '{value}' ORDER BY date_season;")
            try:
                df_items.insert(1,f"code_{index}",tmp[f"code_{index}"])
            except:
                df_items = tmp
        print('==========', key + name)
        print(df_items)
        enine = mysql_engine()
        df_items.to_sql('trade_'+ key+'_'+ name , enine.engine, if_exists="append", index=False)
        #         # print('trade_'+ key+'_'+ name)