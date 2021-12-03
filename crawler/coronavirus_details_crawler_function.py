
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
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent': userAgent
}
countriesNames = ['USA', 'OWID_EUR', 'GBR', 'FRA', 'JPN', 'CHN', 'TWN', 'OWID_WRL', 'HKG', 'SGP']
# countriesNames= ['USA','OWID_EUR','GBR']
for name in countriesNames:
    url = f'https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=3001&limited={name}'
    res = requests.get(url, headers=headers)
    soups = res.json()
    for soup in soups:
        # print(soup)
        # sql1 = '''SELECT location, date_t FROM covid19details where location = '%s' and date_t = '%s' ''' \
        #        % (soup['a03'], soup['a04'])
        # cur.execute(sql1)
        # data = cur.fetchall()
        # if data == ():
        #     sql2 = '''INSERT INTO coviddetails VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'); ''' \
        #            % (soup['a01'], soup['a02'], soup['a03'], soup['a04'], soup['a05'], soup['a06'], soup['a07'],
        #               soup['a08'], soup['a09'], soup['a10'], soup['a11'], soup['a12'], soup['a13'], soup['a14'],
        #               soup['a15'], soup['a16'], soup['a17'], soup['a18'], soup['a19'], soup['a20'], soup['a21'],
        #               soup['a22'], soup['a23'], soup['a24'], soup['a25'], soup['a26'], soup['a27'], soup['a28'],
        #               soup['a29'], soup['a30'], soup['a31'], soup['a32'])
        #     cur.execute(sql2)
        #     # cur.execute(sql1, (soup['a01'], soup['a02'], soup['a03'], soup['a04'], soup['a05'], soup['a06'], soup['a07'], soup['a08'], soup['a09'], soup['a10'], soup['a11'], soup['a12'], soup['a13'], soup['a14'], soup['a15'], soup['a16'], soup['a17'], soup['a18'], soup['a19'], soup['a20'], soup['a21'], soup['a22'], soup['a23'], soup['a24'], soup['a25'], soup['a26'], soup['a27'], soup['a28'], soup['a29'], soup['a30'], soup['a31'], soup['a32']))
        #     conn.commit()
        # 整數區
        total_cases = ''
        new_cases = ''
        total_deaths = ''
        new_deaths = ''
        total_tests= ''
        new_tests = ''
        total_vaccinations = ''
        people_fully_vaccinated =''
        new_vaccinations = ''
        population = ''
        Recovered = ''
        for rr in soup['a05'].split(','):
            total_cases += rr
        for rr in soup['a06'].split(','):
            new_cases += rr
        for rr in soup['a08'].split(','):
            total_deaths += rr
        for rr in soup['a09'].split(','):
            new_deaths += rr
        for rr in soup['a14'].split(','):
            total_tests += rr
        for rr in soup['a15'].split(','):
            new_tests += rr
        for rr in soup['a20'].split(','):
            total_vaccinations += rr
        for rr in soup['a21'].split(','):
            people_fully_vaccinated += rr
        for rr in soup['a22'].split(','):
            new_vaccinations += rr
        for rr in soup['a27'].split(','):
            population += rr
        for rr in soup['a31'].split(','):
            Recovered += rr
        # 浮點數區
        f07 = ''
        f10 = ''
        f11 = ''
        f12 = ''
        f13 = ''
        f16 = ''
        f17 = ''
        f18 = ''
        f19 = ''
        f23 = ''
        f24 = ''
        f25 = ''
        f26 = ''
        f28 = ''
        f29 = ''
        f30 = ''
        f32 = ''
        for rr in soup['a07'].split('.')[0].split(','):
            f07 += rr
        for rr in soup['a10'].split('.')[0].split(','):
            f10 += rr
        for rr in soup['a11'].split('.')[0].split(','):
            f11 += rr
        for rr in soup['a12'].split('.')[0].split(','):
            f12 += rr
        for rr in soup['a13'].split('.')[0].split(','):
            f13 += rr
        for rr in soup['a16'].split('.')[0].split(','):
            f16 += rr
        for rr in soup['a17'].split('.')[0].split(','):
            f17 += rr
        for rr in soup['a18'].split('.')[0].split(','):
            f18 += rr
        for rr in soup['a19'].split('.')[0].split(','):
            f19 += rr
        for rr in soup['a23'].split('.')[0].split(','):
            f23 += rr
        for rr in soup['a24'].split('.')[0].split(','):
            f24 += rr
        for rr in soup['a25'].split('.')[0].split(','):
            f25 += rr
        for rr in soup['a26'].split('.')[0].split(','):
            f26 += rr
        for rr in soup['a28'].split('.')[0].split(','):
            f28 += rr
        for rr in soup['a29'].split('.')[0].split(','):
            f29 += rr
        for rr in soup['a30'].split('.')[0].split(','):
            f30 += rr
        for rr in soup['a32'].split('.')[0].split(','):
            f32 += rr
        new_cases_smoothed = int(soup['a07'].split('.')[1]) / 100 + int(f07)
        new_deaths_smoothed = int(soup['a10'].split('.')[1]) / 100 + int(f10)
        total_cases_per_million = int(soup['a11'].split('.')[1]) / 100 + int(f11)
        total_deaths_per_million = int(soup['a12'].split('.')[1]) / 100 + int(f12)
        reproduction_rate = int(soup['a13'].split('.')[1]) / 100 + int(f13)
        total_tests_per_thousand = int(soup['a16'].split('.')[1]) / 100 + int(f16)
        new_tests_smoothed = int(soup['a17'].split('.')[1]) / 100 + int(f17)
        positive_rate = int(soup['a18'].split('.')[1]) / 100 + int(f18)
        tests_per_case = int(soup['a19'].split('.')[1]) / 100 + int(f19)
        new_vaccinations_smoothed = int(soup['a23'].split('.')[1]) / 100 + int(f23)
        total_vaccinations_per_hundred = int(soup['a24'].split('.')[1]) / 100 + int(f24)
        people_fully_vaccinated_per_hundred = int(soup['a25'].split('.')[1]) / 100 + int(f25)
        stringency_index = int(soup['a26'].split('.')[1]) / 100 + int(f26)
        median_age = int(soup['a28'].split('.')[1]) / 100 + int(f28)
        aged_70_older = int(soup['a29'].split('.')[1]) / 100 + int(f29)
        life_expectancy = int(soup['a30'].split('.')[1]) / 100 + int(f30)
        Unblock = int(soup['a32'].split('.')[1]) / 100 + int(f32)
        # print(soup['a01'], soup['a02'], soup['a03'], soup['a04'], total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed, total_cases_per_million, total_deaths_per_million, reproduction_rate, total_tests, new_tests, total_tests_per_thousand, new_tests_smoothed, positive_rate, tests_per_case, total_vaccinations, people_fully_vaccinated, new_vaccinations, new_vaccinations_smoothed, total_vaccinations_per_hundred, people_fully_vaccinated_per_hundred, stringency_index, population, median_age, aged_70_older, life_expectancy, Recovered, Unblock)
        sql1 = '''SELECT location, date_t FROM covid19details where location = '%s' and date_t = '%s' ''' \
                   % (soup['a03'], soup['a04'])
        cur.execute(sql1)
        data = cur.fetchall()
        if data == ():
            sql2 = '''INSERT INTO covid19details VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'); ''' \
                   % (soup['a01'], soup['a02'], soup['a03'], soup['a04'], int(total_cases), int(new_cases), new_cases_smoothed, int(total_deaths), int(new_deaths), new_deaths_smoothed, total_cases_per_million, total_deaths_per_million, reproduction_rate, int(total_tests), int(new_tests), total_tests_per_thousand, new_tests_smoothed, positive_rate, tests_per_case, int(total_vaccinations), int(people_fully_vaccinated), int(new_vaccinations), new_vaccinations_smoothed, total_vaccinations_per_hundred, people_fully_vaccinated_per_hundred, stringency_index, int(population), median_age, aged_70_older, life_expectancy, int(Recovered), Unblock)
            cur.execute(sql2)
            # cur.execute(sql1, (soup['a01'], soup['a02'], soup['a03'], soup['a04'], soup['a05'], soup['a06'], soup['a07'], soup['a08'], soup['a09'], soup['a10'], soup['a11'], soup['a12'], soup['a13'], soup['a14'], soup['a15'], soup['a16'], soup['a17'], soup['a18'], soup['a19'], soup['a20'], soup['a21'], soup['a22'], soup['a23'], soup['a24'], soup['a25'], soup['a26'], soup['a27'], soup['a28'], soup['a29'], soup['a30'], soup['a31'], soup['a32']))
            conn.commit()
conn.close()
