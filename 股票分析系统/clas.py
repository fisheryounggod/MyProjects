#导入需要用到的模块
import numpy as np
import pandas as pd
from dateutil.parser import parse
from datetime import datetime,timedelta
#操作数据库的第三方包，使用前先安装pip install sqlalchemy
from sqlalchemy import create_engine
#tushare包设置
import tushare as ts
token='693c84c2aca4dc7b941439006bd946413706e7a9560bf3cce0369bb3'
pro=ts.pro_api(token)

#使用python3自带的sqlite数据库
#数据库名称
db_name='stock_data.db'
engine = create_engine(db_name)
class Data(object):
    def __init__(self,
                 start='20050101',
                 end='20191115',
                 table_name='daily_data'):
        self.start=start
        self.end=end
        self.table_name=table_name
        self.codes=self.get_code()
        self.cals=self.get_cals()
    #获取股票代码列表
    def get_code(self):
        codes = pro.stock_basic(list_status='L').ts_code.values
        return codes
    #获取股票交易日历
    def get_cals(self):
        #获取交易日历
        cals=pro.trade_cal(exchange='')
        cals=cals[cals.is_open==1].cal_date.values
        return cals
    #每日行情数据
    def daily_data(self,code):
        try:
            df0=pro.daily(ts_code=code,start_date=self.start,
                end_date=self.end)
            df1=pro.adj_factor(ts_code=code,trade_date='')
            #复权因子
            df=pd.merge(df0,df1)  #合并数据
        except Exception as e:
            print(code)
            print(e)
        return df
    #保存数据到数据库
    def save_sql(self):
        for code in self.codes:
            data=self.daily_data(code)
            data.to_sql(self.table_name,engine,
                 index=False,if_exists='append')
    #获取最新交易日期
    def get_trade_date(self):
        #获取当天日期时间
        pass
    #更新数据库数据
    def update_sql(self):
        pass #代码省略
    #查询数据库信息
    def info_sql(self):
        pass #代码省略