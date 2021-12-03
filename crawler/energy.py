def crude_oil():
    import requests
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

    Index_code = {'WBR_now':'131670','WBR_future':'130820','WTI_now':'131680','WTI_future':'130810','Dubai':'131690',
                  'avgas_fpg':'260100','avgas_cpc':'260080'}
    crude_indexes = ['WBR_now','WBR_future','WTI_now','WTI_future','Dubai','avgas_fpg','avgas_cpc']

    #unit: USD,USD,USD,USD,USD, USD/L, USD/GAL

    for i in range(len(crude_indexes)):

        url = "https://fubon-ebrokerdj.fbs.com.tw/Z/ZH/ZHG/CZHG.djbcd?A={}".format(Index_code[crude_indexes[i]])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')
        # print(soup)

        date = str(soup).split(" ")[0].split(",")
        price = str(soup).split(" ")[1].split(",")

        datas = {"crude_index":crude_indexes[i],'data_date':date,'price':price}
        df = pd.DataFrame(datas)

        engine = create_engine('mysql+pymysql://root:ian1991@localhost:3306/tfb103d_project')

        df.to_sql('energy', engine, if_exists="append", index=False)
    return "Successfully!"

def natural_gas(data = '2021/10/01'):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from sqlalchemy import create_engine
    import datetime
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

    url = "https://hk.investing.com/instruments/HistoricalDataAjax"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'origin': 'https://hk.investing.com',
        'referer': 'https://hk.investing.com/commodities/natural-gas-historical-data',
        'x-requested-with': 'XMLHttpRequest'}

    form_data = {'curr_id': '8862','smlID': '300092','header': '天然氣期貨歷史數據','st_date': '2008/02/16','end_date':'{}'.format(data),
                'interval_sec':'Weekly', 'sort_col':'date','sort_ord': 'DESC','action':'historical_data'}

    ss = requests.session()
    url1 = 'https://hk.investing.com/commodities/natural-gas-historical-data'
    ss.get(url1, headers=headers)
    res = ss.post(url, headers=headers,data = form_data)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    data = soup.select("table#curr_table tr")
    energy = []
    for i in data[1:]:
        tmp = ["N1NG"]
        tmp.extend(i.text.replace("K","\n").replace("年","-").replace("月","-").replace("日","").split("\n")[1:3])
        tmp[1] = datetime.datetime.strptime(tmp[1],"%Y-%m-%d") + datetime.timedelta(days=-1)
        tmp[1] = tmp[1].strftime('%Y-%m-%d')
        energy.append(tmp)
    columns = ["crude_index", 'data_date', 'price']
    df = pd.DataFrame(energy, columns=columns)

    engine = create_engine('mysql+pymysql://root:{#your_code}@localhost:3306/tfb103d_project')

    df.to_sql('energy', engine, if_exists="append", index=False)
    return "Successfully!"

#原油與燃油指數
crude_oil()

#天然氣期貨指數
natural_gas()
