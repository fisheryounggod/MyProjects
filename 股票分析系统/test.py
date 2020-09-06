#%%
from StockClass import stock
print(stock.__doc__)
#%%
# 实例调用法：
class StockCode:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    def get_stock(self):
        return (self.name,self.code)
s=StockCode('中国平安','601318.SH')
s.get_stock()
#%%
# 静态方法调用

class Codes(object):
    @staticmethod
    def get_code(s):
        if len(s)==6:
            return (s+'SH') if s.startswith('6') else (s+'SZ')
        else:
            print('股票代码必须为6位数字！')
# Codes.get_code('00001')
print(Codes.get_code('000001'))

#%%
a=111
def get_a(a):
    return a
print(get_a(a))
#%%
class StockCode:
    def __init__(self,stock,code):
        self.stock=stock
        self.code=code
    @classmethod
    # 装饰器，立马执行下面的函数
    def split(cls,sc):
        # cls是默认的这个类的init函数，sc是传入参数
        stock,code=map(str,sc.split('-'))
        # 这里转换成了格式化的结构
        dd = cls(stock,code)
        # 然后执行这个类第一个方法
        return dd
s=StockCode.split(('中国平安-601318.SH'))
#查看属性
print(s.stock,s.code)
#%%
class stock(object):
    def __init__(self,code,price):
        self.code=code
        self.price=price
    #定义打印属性的函数
    def print_attr(self):
        print(f'股票代码为：{self.code}')
        print(f'股票价格为：{self.price}')
#使用“实例.方法”，即“实例名称.函数名()”的方式来调用
s1=stock('000001.SZ',15.8)
s1.print_attr()

#%%
class stock(object):
    def __init__(self,code,price):
        self.__code=code
        self.__price=price
    def get_attr(self):
        return(self.__code,self.__price)
s1=stock('000001.SZ',15.8)
a=s1.get_attr()
print(a)