use TFB103d_project;

create table ownership_afetl(
data_date varchar(36),
stock_code varchar(36),
avg_board_bys  float(4,2) default 0,
over1000_rate_bys float(5,3) default 0,
under400_rate_bys float(5,3) default 0);

create table dsownership_afetl(
data_date varchar(36),
stock_code varchar(36),
avg_director_rate  float(4,2) default 0,
avg_director_pledge_rate float(4,2) default 0,
foreign_rate_bys float(4,2) default 0,
change_rate_bys float(4,2) default 0);

create table dsownership_afetl(
data_date varchar(36),
stock_code varchar(36),
avg_director_rate  float(4,2) default 0,
foreign_rate_bys float(4,2) default 0,
change_rate_bys float(4,2) default 0);

create table energy_afetl(
data_date varchar(36),
crude_index varchar(36),
avg_price  float(4,2) default 0);

create table shipping_afetl(
data_date varchar(36),
Baltic_Index varchar(36),
avg_index_price  float(6,2) default 0);

create table shipping_afetl(
data_date varchar(36),
avg_import_rate  float(5,3) default 0,
avg_export_rate  float(5,3) default 0);
