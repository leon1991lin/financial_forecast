import pandas as pd
from sqlalchemy import create_engine

class mysql_engine():
 user='root'
 passwd='password'
 host='localhost'
 port = '3306'
 db_name='covidtest'
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

data_names = ['reproduction_rate', 'positive_rate', 'new_cases_smoothed', 'people_fully_vaccinated_per_hundred']
countries_code = ['USA', 'OWID_EUR', 'GBR', 'FRA', 'JPN', 'CHN', 'TWN', 'OWID_WRL', 'HKG', 'SGP']
for name in data_names:
    for index in countries_code:
        tmp = get_data(f"SELECT date_season, {name} {index} from covidseason WHERE iso_code = '{index}' ORDER BY date_season;")
        try:
            df_countries.insert(1,f"{index}",tmp[f"{index}"])
        except:
            df_countries = tmp
    print('==========', name)
    print(df_countries)
    enine = mysql_engine()
    df_countries.to_sql('covidseason_'+ name , enine.engine, if_exists="append", index=False)