use TFB103d_project;

create table usd_exrate(
data_date date,
CashRate_Buying float(5,3) default 0.0,
CashRate_Selling float(5,3) default 0.0,
SpotRate_Buying float(5,3) default 0.0,
SpotRate_Selling float(5,3) default 0.0
);

drop table usd_exrate;