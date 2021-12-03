import pymysql, json, requests
from bs4 import BeautifulSoup
# 與mysql進行連線
conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='{#your_code}',
                       db='covidtest',
                       charset='utf8')
cur = conn.cursor()
data_season = {'20201':['2020-01-01', '2020-03-31'],
               '20202':['2020-04-01', '2020-06-30'],
               '20203':['2020-07-01', '2020-09-30'],
               '20204':['2020-10-01', '2020-12-31'],
               '20211':['2021-01-01', '2021-03-31'],
               '20212':['2021-04-01', '2021-06-30'],
               '20213':['2021-07-01', '2021-09-30'],
               '20214':['2021-10-01', '2021-12-31']}
for key, value in data_season.items():
    sql1 = '''select aa.iso_code, aa.location, avg(aa.new_cases_smoothed), avg(aa.reproduction_rate), avg(aa.positive_rate), avg(aa.people_fully_vaccinated_per_hundred) from covid19details aa
        where date_t between '%s' AND '%s'
        group by 1; ''' \
        % (value[0], value[1])
    cur.execute(sql1)
    dataa = cur.fetchall()
    for data in dataa:
        sql2 = '''INSERT INTO covidseason VALUES ('%s', '%s', '%s', '%f', '%f', '%f', '%f'); ''' \
               % (data[0], data[1], key, data[2], data[3], data[4], data[5])
        print(data[0], data[1], key, data[2], data[3], data[4], data[5])
        cur.execute(sql2)
        conn.commit()
conn.close()
