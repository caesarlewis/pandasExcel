import pandas as pd
from datetime import date,timedelta

import env


def add_month(d,md):
    yd = md //12
    m = d.month + md % 12
    if m != 12:
        yd += m//12
        m = m%12
    return date(d.year+yd,m,d.day)

# skiprows 跳过多少行
# usecols 选择使用那些列
books = pd.read_excel('books.xlsx',skiprows=3,usecols='C:F',index_col=None,dtype={'ID':str,'InStore':str,'Date':str})
# 查看类型
print(type(books['ID']))
print(books['ID'])
print(books['InStore'])
start = date(2018,1,1)
for i in books.index:
    #获取series之后再改值
    books['ID'].at[i] = i+1
    #获取dateframe之后再改值
    books.at[i,'ID'] = i +1
    books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
    #加天数，timedelta只能增加天 小时 分钟 毫秒
    books['Date'].at[i] = start + timedelta(days=i)
    books['Date'].at[i] = date(start.year+i,start.month,start.day)
    books['Date'].at[i] = add_month(start,i)
print(books)
books.set_index('ID',inplace=True)
books.to_excel(env.getFilePath('output.xlsx'))
print('Done')