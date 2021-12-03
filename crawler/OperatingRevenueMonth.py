from sqlalchemy import Column, String, DECIMAL, and_, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OperatingRevenueMonth(Base):
    __tablename__ = 'operating_revenue_month'

    stock_code = Column('stock_code', String(4),primary_key=True)
    stock_report_date = Column('stock_report_date', String(20), primary_key=True)
    stock_name = Column('stock_name', String(10))
    operating_revenue_month = Column('operating_revenue_month', DECIMAL(18,2))