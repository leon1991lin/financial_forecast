use TFB103d_project;

create table shipping(
Baltic_Index varchar(24), ##航運指數
data_date date, ##日期
index_price float(8,2) default 0.00); ##指數

drop table shipping;

create table air_transport(
crude_index varchar(24), ##原油指數
data_date date, ##日期
price float(6,2) default 0.00); ##指數

drop table air_transport;