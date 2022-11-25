import pandas as pd
import numpy as np

pd.options.display.max_columns = None
orders = pd.read_excel('Orders.xlsx')
print(orders)
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
# pivot_table 透视图方法
# index 透视图的行
# columns 透视图的列
# values 需要统计的列
# aggfunc 具体的计算函数
pt1 =orders.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)
print(pt1)
groups = orders.groupby(['Category','Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum':s,'Count':c})
print(pt2)
