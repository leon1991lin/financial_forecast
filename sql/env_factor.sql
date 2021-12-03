use TFB103d_project;

create table env_factor(
data_date varchar(36),
avg_import_rate float(5,3) default 0,
avg_export_rate float(5,3) default 0,
BDI float(6,2) default 0,
BCI float(6,2) default 0,
BPI float(6,2) default 0,
WBR_now float(4,2) default 0,
WBR_future float(4,2) default 0,
WTI_now float(4,2) default 0,
WTI_future float(4,2) default 0,
Dubai float(4,2) default 0,
N1NG float(4,2) default 0,
avgas_fpg float(4,2) default 0,
avgas_cpc float(4,2) default 0
);