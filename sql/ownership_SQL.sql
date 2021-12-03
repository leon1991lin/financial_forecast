drop database TFB103d_project;

create database TFB103d_project charset='utf8';

use TFB103d_project;

create table ownership(
stock_code varchar(36),
data_date date,
total_board int default 0,
total_holder int default 0,
avg_board float(5,2) default 0.0,
over400_amount int default 0,
over400_rate float(4,2) default 0.0,
over400_holder smallint default 0,
between400_600 smallint default 0,
between600_800 smallint default 0,
between800_1000 smallint default 0,
over1000_holder smallint default 0,
over1000_rate float(4,2) default 0.0,
closing_price float(6,2) default 0.0
);

create table DSownership(
stock_code varchar(36),
data_date date,
month_price float(6,2) default 0.0,
amount_of_change float(5,2) default 0.0,
rate_of_change float(5,2) default 0.0,
total_board int default 0,
director_amount int default 0,
director_rate float(5,2) default 0,
director_dalta  int default 0,
director_pledge_amount  int default 0,
director_pledge_rate  float(5,2) default 0,
indirector_amount int default 0,
indirector_rate float(5,2) default 0,
indirector_dalta  int default 0,
indirector_pledge_amount  int default 0,
indirector_pledge_rate  float(5,2) default 0,
toldirector_amount int default 0,
toldirector_rate float(5,2) default 0,
toldirector_dalta  int default 0,
toldirector_pledge_amount  int default 0,
toldirector_pledge_rate  float(5,2) default 0,
foreign_rate float(5,2) default 0
);

drop table ownership;

drop table DSownership;