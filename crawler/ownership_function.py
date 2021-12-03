def ownership(stockcodes):
    import requests,pymysql, time, random
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    columns = ["stock_code", "data_date", "total_board",
               "total_holder", "avg_board", "over400_amount",
               "over400_rate", "over400_holder", "between400_600",
               "between600_800", "between800_1000", "over1000_holder",
               "over1000_rate", "closing_price"]

    df = pd.DataFrame([], columns=columns) #輸出結果用的 DataFrame
    for stockcode in stockcodes:
        url = "https://norway.twsthr.info/StockHolders.aspx?stock={}".format(stockcode)

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')
        table = soup.select("div#D1 td")

        #資料
        datas = []
        tmp = [stockcode]
        for data in (table[17:-2]):
            if len(tmp) < 14: #共有 14 columns 的數值
                if data.text != "\xa0": #非 \xa0的空白值才處理
                    if data.text == '': #空值以 None 處理
                        t = None
                        # t += None
                        tmp.append(t)
                    else:
                        # 字串處理:去掉\xa0的空白值並取代 ','
                        tmp.append(data.text.split("\xa0")[0].replace(",", ""))
                    #將每個 row 建立名為 tmp 的 list
            else:
                if float(tmp[4]) > 200.00: #部分原始資料有出現嚴重的錯誤，觀察後可以以"平均張數"欄位的數值判定後排除
                    print(tmp) #呈現有錯誤的原始資料
                    tmp = [stockcode] #將 tmp 回復
                    pass
                else:
                    datas.append(tmp) #將 tmp 插入 datas (成為二維矩陣，用於建立 DataFrame)
                    tmp = [stockcode] #將 tmp 回復

        df_tmp = pd.DataFrame(datas, columns=columns) # 建立 DataFrame
        print(df_tmp)

        df = df.append(df_tmp,ignore_index=True) # 將 DataFrame 加入輸出結果的 DataFrame 中

        print("{},Successfully!".format(stockcode))

        #隨機指定停留秒數，模擬人為使用的情況，避免被阻擋
        sleep_time = random.randint(5,12)
        print('sleep_times = ' + str(sleep_time))
        time.sleep(sleep_time)

    #將輸出結果的 DataFrame 儲存至 SQL 資料表中
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/tfb103d_project')
    df.to_sql('ownership', engine, if_exists="append", index=False)

    return df

# 股權分散圖
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

df = ownership(companys)

print(df)

# if __name__ == "__main__":
#     stockcode = '5483'
#     ownership(stockcode)


