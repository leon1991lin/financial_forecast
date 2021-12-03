use covidtest;
create table covidseason(
	iso_code varchar(24) comment '國碼',
    location varchar(24) comment '國家',
    date_season varchar(24) comment '年季',
    new_cases_smoothed float(10,2) default 0.0 comment '七天移動平均新增確診數',
    reproduction_rate float(10,2) default 0.0 comment '傳染率',
    positive_rate float(10,2) default 0.0 comment '陽性率',
    people_fully_vaccinated_per_hundred float(10,2) default 0.0 comment '每百人接種疫苗人數'
);
drop table covidseason;
create table covidseason_reproduction_rate(
	date_season varchar(24) comment '年季',
    USA float(10,2) default 0.0 comment '美國',
    OWID_EUR float(10,2) default 0.0 comment '歐洲',
    GBR float(10,2) default 0.0 comment '英國',
    FRA float(10,2) default 0.0 comment '法國',
    JPN float(10,2) default 0.0 comment '日本',
    CHN float(10,2) default 0.0 comment '中國大陸',
    TWN float(10,2) default 0.0 comment '台灣',
    OWID_WRL float(10,2) default 0.0 comment '全球',
    HKG float(10,2) default 0.0 comment '香港',
    SGP float(10,2) default 0.0 comment '新加玻'
);

create table covidseason_positive_rate(
	date_season varchar(24) comment '年季',
    USA float(10,2) default 0.0 comment '美國',
    OWID_EUR float(10,2) default 0.0 comment '歐洲',
    GBR float(10,2) default 0.0 comment '英國',
    FRA float(10,2) default 0.0 comment '法國',
    JPN float(10,2) default 0.0 comment '日本',
    CHN float(10,2) default 0.0 comment '中國大陸',
    TWN float(10,2) default 0.0 comment '台灣',
    OWID_WRL float(10,2) default 0.0 comment '全球',
    HKG float(10,2) default 0.0 comment '香港',
    SGP float(10,2) default 0.0 comment '新加玻'
);

create table covidseason_new_cases_smoothed(
	date_season varchar(24) comment '年季',
    USA float(10,2) default 0.0 comment '美國',
    OWID_EUR float(10,2) default 0.0 comment '歐洲',
    GBR float(10,2) default 0.0 comment '英國',
    FRA float(10,2) default 0.0 comment '法國',
    JPN float(10,2) default 0.0 comment '日本',
    CHN float(10,2) default 0.0 comment '中國大陸',
    TWN float(10,2) default 0.0 comment '台灣',
    OWID_WRL float(10,2) default 0.0 comment '全球',
    HKG float(10,2) default 0.0 comment '香港',
    SGP float(10,2) default 0.0 comment '新加玻'
);

drop table covidseason_new_cases_smoothed;

create table covidseason_people_fully_vaccinated_per_hundred(
	date_season varchar(24) comment '年季',
    USA float(10,2) default 0.0 comment '美國',
    OWID_EUR float(10,2) default 0.0 comment '歐洲',
    GBR float(10,2) default 0.0 comment '英國',
    FRA float(10,2) default 0.0 comment '法國',
    JPN float(10,2) default 0.0 comment '日本',
    CHN float(10,2) default 0.0 comment '中國大陸',
    TWN float(10,2) default 0.0 comment '台灣',
    OWID_WRL float(10,2) default 0.0 comment '全球',
    HKG float(10,2) default 0.0 comment '香港',
    SGP float(10,2) default 0.0 comment '新加玻'
);