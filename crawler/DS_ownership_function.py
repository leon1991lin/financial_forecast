def DSownership(stockcodes):
    import requests, random, time
    from bs4 import BeautifulSoup
    import pandas as pd
    from sqlalchemy import create_engine
    import configparser

    # config = configparser.ConfigParser()
    # config.read('./../../../config/crawler.ini')
    #
    # username = config['pchome_stock_crawler-mysql']['username']     # 資料庫帳號
    # password = config['pchome_stock_crawler-mysql']['password']     # 資料庫密碼
    # host = config['pchome_stock_crawler-mysql']['host']    # 資料庫位址
    # port = config['pchome_stock_crawler-mysql']['port']         # 資料庫埠號
    # database = config['pchome_stock_crawler-mysql']['database']  # 資料庫名稱
    # # 建立連線引擎
    # engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

    columns = ['stock_code', 'data_date', 'month_price', 'amount_of_change', 'rate_of_change',
               'total_board', 'director_amount', 'director_rate', 'director_dalta', 'director_pledge_amount',
               'director_pledge_rate', 'indirector_amount', 'indirector_rate', 'indirector_dalta',
               'indirector_pledge_amount', 'indirector_pledge_rate', 'toldirector_amount', 'toldirector_rate',
               'toldirector_dalta', 'toldirector_pledge_amount', 'toldirector_pledge_rate', 'foreign_rate']

    df = pd.DataFrame([], columns=columns)  # 輸出結果用的 DataFrame
    for stockcode in stockcodes:
        url = "https://goodinfo.tw/StockInfo/StockDirectorSharehold.asp?STOCK_ID={}".format(stockcode)
        headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
            }

        res = requests.get(url, headers=headers)
        print('status_code = ' + str(res.status_code))
        # print(res.encoding)  => 編碼為ISO-8859-1
        res.encoding = res.apparent_encoding  #解碼，中文才不會出現亂碼
        soup = BeautifulSoup(res.text,'html.parser')
        table = soup.select("table.b1.p4_0.r0_10.row_bg_2n.row_mouse_over tr")

        datas = []
        for i in table:
            text = i.text.replace(",", "").replace('-', '-0').split(" ")[1:]
            tmp = [stockcode]
            tmp.extend(text)
            # print(tmp)
            if len(tmp) == 22:
                tmp[1] += "/01"
                datas.append(tmp)

        df_tmp = pd.DataFrame(datas, columns=columns) # 建立 DataFrame
        # print(df_tmp)
        if df_tmp.values.shape[0] == 0:
            print(str(stockcode)+"Error!!!")
            time.sleep(1800)

        # 將輸出結果的 DataFrame 儲存至 SQL 資料表中
        engine = create_engine('mysql+pymysql://root:{#your_code}@localhost:3306/tfb103d_project')
        df_tmp.to_sql('dsownership', engine, if_exists="append", index=False)

        # 將 DataFrame 加入輸出結果的 DataFrame 中
        df = df.append(df_tmp, ignore_index=True)

        print("{},Successfully!".format(stockcode))

        #隨機指定停留秒數，模擬人為使用的情況，避免被阻擋
        sleep_time = random.randint(20,30)
        print('sleep_times = ' + str(sleep_time))
        time.sleep(sleep_time)

    return df

# companys = ["2330","2303","2379","6488","5347","4966","2454","3529","3105","5483","3034"]

# companys = ["2330","2303","2379","6488","5347","4966","2454","3529","3105","5483","3034",
#             '3686','3711','4919','4952','4961','4967','8110','8131','8150','8261','8271'
#             ,'4968','5222','5269','5285','5471','6202','6239','6243','6257','6271','6415'
#             ,'6451','6515','6525','6531','6533','6552','6573','6756','8016','8028','8081'
#             ]
companys =['2330','2303','2329','2330','2337','2338','2342','2344','2351','2363',
            '2369','2379','2388','2401','2408','2434','2436','2441','2449','2451',
            '2454','2458','2481','3006','3014','3016','3034','3035','3041','3054',
            '3094','3189','3257','3413','3443','3450','3530','3532','3536','3545',
            '3583','3588','3661','3686','3711','4919','4952','4961','4967','4968',
            '5222','5269','5285','5471','6202','6239','6243','6257','6271','6415',
            '6451','6515','6525','6531','6533','6552','6573','6756','8016','8028',
            '8081','8110','8131','8150','8261','8271','3073','3105','3122','3141',
            '3169','3227','3228','3259','3260','3264','3265','3268','3317','3372',
            '3374','3438','3527','3529','3555','3556','3567','3581','3675','3680',
            '3707','4945','4966','4971','4973','4991','5236','5272','5274','5299',
            '5302','5314','5344','5347','5351','5425','5468','5483','5487','6104',
            '6129','6138','6147','6182','6198','6223','6229','6233','6237','6261',
            '6287','6291','6411','6435','6457','6462','6485','6488','6494','6510',
            '6532','6548','6568','6594','6640','6643','6651','6679','6683','6684',
            '6716','6732','6788','7556','8024','8040','8054','8086','8088','8277',
             '8299']

print(len(companys))

df = DSownership(companys)

print(df)

# if __name__ == "__main__":
#     stockcode = '2330'
#     DSownership(stockcode)
