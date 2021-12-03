import pymysql, csv
conn = pymysql.Connect(host='127.0.0.1',
                        port=3306,
                        user='root',
                        passwd='password',
                        db='tradedb',
                        charset='utf8')
cur = conn.cursor()
countriesNames= ['1','2']
for name in countriesNames:
    with open(f'C:/Users/Tibame/Downloads/trade{name}.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            try:
                # usd_value = ''
                # ntd_value = ''
                # tne_weight = ''
                # kgm_weight =''
                # for rr in row[5].split(','):
                #     usd_value += rr
                # for rr in row[6].split(','):
                #     ntd_value += rr
                # for rr in row[7].split(','):
                #     tne_weight += rr
                # for rr in row[8].split(','):
                #     kgm_weight += rr
                # print(row)
                # print(row[0], row[1], row[2], row[3], row[4], int(usd_value), int(ntd_value), int(tne_weight), int(tne_weight))
                sql1 = '''INSERT INTO tradestatistics VALUES ('%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d'); ''' \
                       %(row[0], row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), int(row[7]), int(row[8]))
                       # % (row[0], row[1], row[2], row[3], row[4], int(usd_value), int(ntd_value), int(tne_weight), int(kgm_weight))
                cur.execute(sql1)
                conn.commit()
            except:
                # print('loser')
                print(1, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
conn.close()