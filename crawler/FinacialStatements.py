from sqlalchemy import Column, String, DECIMAL, and_, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FinacialStatements(Base):
    __tablename__ = 'finacial_statements'

    stock_code = Column('stock_code', String(4),primary_key=True)
    stock_report_date = Column('stock_report_date', String(20), primary_key=True)
    stock_name = Column('stock_name', String(10))
    inventories = Column('inventories', DECIMAL(18,2))
    receivables = Column('receivables', DECIMAL(18, 2))
    cash_equiv = Column('cash_equiv', DECIMAL(18, 2))
    cur_assets = Column('cur_assets', DECIMAL(18, 2))
    cur_liabilities = Column('cur_liabilities', DECIMAL(18, 2))
    short_debt = Column('short_debt', DECIMAL(18, 2))
    acc_payable = Column('acc_payable', DECIMAL(18, 2))
    one_year_liabilities = Column('one_year_liabilities', DECIMAL(18, 2))
    long_loan = Column('long_loan', DECIMAL(18, 2))
    retained_earnings = Column('retained_earnings', DECIMAL(6, 2))
    operating_gross_rate = Column('operating_gross_rate', DECIMAL(6, 2))
    net_profit_rate = Column('net_profit_rate', DECIMAL(6, 2))
    revenue_growth_rate = Column('revenue_growth_rate', DECIMAL(6, 2))
    current_rate = Column('current_rate', DECIMAL(6, 2))
    quick_rate = Column('quick_rate', DECIMAL(6, 2))
    debt_rate = Column('debt_rate', DECIMAL(6, 2))
    receivables_turnover_rate = Column('receivables_turnover_rate', DECIMAL(6, 2))
    inventory_turnover_rate = Column('inventory_turnover_rate', DECIMAL(6, 2))
    cash_reinvest_rate = Column('cash_reinvest_rate', DECIMAL(6, 2))
    operating_revenue_season = Column('operating_revenue_season', DECIMAL(18, 2))
    operating_costs = Column('operating_costs', DECIMAL(18, 2))
    operating_profit = Column('operating_profit', DECIMAL(18, 2))
    research_expense = Column('research_expense', DECIMAL(18, 2))
    tax_interest_income = Column('tax_interest_income', DECIMAL(18, 2))
    cashflows_operating = Column('cashflows_operating', DECIMAL(18, 2))
    invest_operating = Column('invest_operating', DECIMAL(18, 2))