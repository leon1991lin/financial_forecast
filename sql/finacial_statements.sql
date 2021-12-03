use stock;

drop table if exists finacial_statements;
drop table if exists operating_revenue_month;


create table finacial_statements(
	stock_code  varchar(4),
    stock_name varchar(20),
    stock_report_date varchar(5),
	inventories DECIMAL(18, 2) COMMENT '存貨',
    receivables DECIMAL(18, 2) COMMENT '應收帳款淨額',
    cash_equiv DECIMAL(18, 2) COMMENT '現金及約當現金',
    cur_assets DECIMAL(18, 2) COMMENT '流動資產',
    cur_liabilities DECIMAL(18, 2) COMMENT '流動負債',
    short_debt DECIMAL(18, 2) COMMENT '短期借款',
    acc_payable DECIMAL(18, 2) COMMENT '應付帳款',
    one_year_liabilities DECIMAL(18, 2) COMMENT '一年或一營業週期內到期長期負債',
    long_loan DECIMAL(18, 2) COMMENT '長期借款',
    retained_earnings DECIMAL(18, 2) COMMENT '保留盈餘',
    operating_gross_rate DECIMAL(6, 2) COMMENT '營業毛利率',
    net_profit_rate DECIMAL(6, 2) COMMENT '稅後淨利率',
    revenue_growth_rate DECIMAL(6, 2) COMMENT '營收成長率',
    current_rate DECIMAL(6, 2) COMMENT '流動比率',
    quick_rate DECIMAL(6, 2) COMMENT '速動比率',
    debt_rate DECIMAL(6, 2) COMMENT '負債比率',
    receivables_turnover_rate DECIMAL(6, 2) COMMENT '應收帳款週轉率',
    inventory_turnover_rate DECIMAL(6, 2) COMMENT '存貨週轉率',
    cash_reinvest_rate DECIMAL(6, 2) COMMENT '現金再投資比率',
    operating_revenue_season DECIMAL(18, 2) COMMENT '營業收入(季)',
    operating_costs DECIMAL(18, 2) COMMENT '營業成本',
    operating_profit DECIMAL(18, 2) COMMENT '營業毛利',
    research_expense DECIMAL(18, 2) COMMENT '研究發展費用',
    tax_interest_income DECIMAL(18, 2) COMMENT '本期淨利',
    cashflows_operating DECIMAL(18, 2) COMMENT '營業活動現金流量',
	invest_operating DECIMAL(18, 2) COMMENT '投資活動現金流量',
    CONSTRAINT pk_stock_code_Id PRIMARY KEY (stock_code, stock_report_date)
);

create table operating_revenue_month(
	stock_code  varchar(4),
    stock_name varchar(10),
    stock_report_date varchar(6),
    operating_revenue_month DECIMAL(18, 2) COMMENT '營業收入(月)',
	CONSTRAINT pk_stock_code_Id PRIMARY KEY (stock_code, stock_report_date)
);

