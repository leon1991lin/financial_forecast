-- create database tradedb;
-- use tradedb;
-- create table tradestatistics(
-- 	imports_exports varchar(24) comment '進出口別',
--     date_t varchar(24) comment '日期',
--     commodity_code varchar(24) comment '貨品號列',
--     chinese_description_good varchar(200) comment '中文貨名',
--     engish_description_good varchar(300) comment '英文貨名',
--     usd_value integer comment '美元(千元)',
--     ntd_value integer comment '新台幣(千元)',
--     tne_weight integer comment '重量(公噸)',
--     kgm_weight integer comment '重量(公斤)'
-- );
-- drop table tradestatistics;

-- create table tradeseason(
-- 	imports_exports varchar(24) comment '進出口別',
--     date_season varchar(24) comment '年季',
--     commodity_code varchar(24) comment '貨品號列',
--     chinese_description_good varchar(200) comment '中文貨名',
--     engish_description_good varchar(300) comment '英文貨名',
--     usd_value integer comment '美元(千元)',
--     ntd_value integer comment '新台幣(千元)',   
--     tne_weight integer comment '重量(公噸)',
--     kgm_weight integer comment '重量(公斤)'
-- );

create table trade_import_usd_value(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
	);

create table trade_import_ntd_value(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);

create table trade_import_tne_weight(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);

create table trade_import_kgm_weight(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);

create table trade_export_usd_value(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
	);

create table trade_export_ntd_value(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);

create table trade_export_tne_weight(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);

create table trade_export_kgm_weight(
		date_season varchar(24) comment '年季',
        code_381800 integer comment '電子工業用已摻雜之化學元素，呈圓片、晶圓或類似形狀者；電子工業用已摻雜之化學化合物',
		code_848610 integer comment '製造晶柱或晶圓之機器及器具',
		code_848620 integer comment '製造半導體裝置或積體電路之機器及器具',
		code_37050000306 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37059090102 integer comment '單晶粒積體電路、混合積體電路、多晶粒積體電路、薄膜型積體電路、光積體電路之光罩或網線',
		code_37079090 integer comment '其他供照相用化學製品（凡立水、膠、接著劑及類似品除外）；供照相用之未經混合產品，已作成劑量或零售包裝立即可用者',
		code_37071000 integer comment '37050000306',
		code_2804 integer comment '氫，稀有氣體及其他非金屬元素',
		code_2801 integer comment '氟、氯、溴、碘'
);