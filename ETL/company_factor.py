import pandas as pd
from sqlalchemy import create_engine

class mysql_engine():
 def __init__(self,db):
  self.user='root'
  self.passwd='{#your_code}'
  self.host='localhost'
  self.port = '3306'
  self.db_name= db
  self.engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(self.user,self.passwd,self.host,self.port,self.db_name))

def get_data(sql,db):
 pg_enine = mysql_engine(db)
 try:
  with pg_enine.engine.connect() as con, con.begin():
   df = pd.read_sql(sql,con) # 獲取資料
  con.close()
 except:
  df = None
 return df

#股權分散圖
ownership = get_data('''select * from ownership_afetl;''','tfb103d_project')
print(ownership)
#董監事持股比例
dsownership = get_data('''select * from dsownership_afetl;''','tfb103d_project')
print(dsownership)
df = pd.merge(ownership, dsownership, on=["data_date",'stock_code'], how="outer")

#財務報表
finacial_statements = get_data('''select * from finacial_statements;''','stock')
finacial_statements = finacial_statements.rename(columns={'stock_report_date':'data_date'})
finacial_statements = finacial_statements.drop("stock_name",axis=1)
print(finacial_statements)

df1 = pd.merge(df, finacial_statements, on=["data_date",'stock_code'], how="inner")
print(df1.head(20))

enine = mysql_engine('tfb103d_project')

df1.to_sql('company_factor', enine.engine, if_exists="append", index=False)

print("Finish!!")
