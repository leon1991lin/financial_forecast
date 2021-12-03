import pandas as pd
from sqlalchemy import create_engine
import json

class mysql_engine():
 user='root'
 passwd='ian1991'
 host='localhost'
 port = '3306'
 db_name='tfb103d_project'
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

# 能源指數
energy_data = ['WBR_now','WBR_future','WTI_now','WTI_future','Dubai','avgas_fpg','avgas_cpc','N1NG']
for index in energy_data:
    tmp = get_data(f"SELECT data_date, avg_price {index} from energy_afetl WHERE crude_index = '{index}' ORDER BY data_date;")
    try:
        df_energy.insert(1,f"{index}",tmp[f"{index}"])
    except:
        df_energy = tmp
df_energy["avgas_fpg"] = df_energy["avgas_fpg"].apply(lambda x : (x/3.785))
# print(df_energy["avgas_fpg"])

#航運指數
shipping_data = ['BPI','BCI','BDI']
for index in shipping_data:
    tmp = get_data(f"SELECT data_date, avg_index_price {index} from shipping_afetl WHERE Baltic_Index = '{index}' ORDER BY data_date;")
    try:
        df_shipping.insert(1,f"{index}",tmp[f"{index}"])
    except:
        df_shipping = tmp

#美金匯率
df_usdex = get_data(f"SELECT * FROM usd_exrate_afetl ORDER BY data_date;")

df1 = pd.merge(df_shipping,df_energy,on="data_date",how="outer")
# print(df1)
df2 = pd.merge(df1,df_usdex,on="data_date",how="outer")
# print(df2)

# 存入 MySQL
enine = mysql_engine()
df2.to_sql('env_factor', enine.engine, if_exists="append", index=False)

# 存為 Json 格式
result = df2.to_json(orient="columns")
js_path = "env_factor.json"
with open(js_path,"w") as f:
    json.dump(result,f)