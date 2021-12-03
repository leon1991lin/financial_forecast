import pymysql, json, requests
from bs4 import BeautifulSoup
# 與mysql進行連線
conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='{#your_code}',
                       db='tradedb',
                       charset='utf8')
cur = conn.cursor()
years =['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110']
months = {'1':['年1月','年2月','年3月'],'2':['年4月','年5月','年6月'], '3':['年7月','年8月','年9月'],'4':['年10月','年11月','年12月']}
for year in years:
        for key, value in months.items():
            sql1 = '''select imports_exports, commodity_code, chinese_description_good, engish_description_good, avg(usd_value), avg(ntd_value), avg(tne_weight), avg(kgm_weight) from tradestatistics
                    where date_t in ('%s', '%s', '%s')
                    group by imports_exports, commodity_code
                    order by 1,2; ''' \
                % (year+value[0], year+value[1], year+value[2])
            cur.execute(sql1)
            dataa = cur.fetchall()
            for data in dataa:
                sql2 = '''INSERT INTO tradeseason VALUES ('%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d'); ''' \
                       % (data[0], str(int(year)+1911)+key, data[1], data[2], data[3], data[4], data[5], data[6], data[7])
                cur.execute(sql2)
                conn.commit()
                # print(data[0], str(int(year)+1911)+key, data[1], data[2], data[3], data[4], data[5], data[6], data[7])
conn.close()
