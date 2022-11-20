import pandas as pd
import env as env

def add_2(x):
    return x+2

books = pd.read_excel('booksPrice.xlsx',index_col='ID')
# 通过列相乘方式计算每个单元格的打折之后的价格
#books['Price'] = books['ListPrice'] * books['Discount']
# 通过获取行索引方式来计算每一行的单元格的价格
#for i in books.index:
#    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

for i in range(5,15):
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
# 每本书增加2块钱
# 使用列相加方式
books['ListPrice'] = books['ListPrice'] +2
# 使用函数方式
books['ListPrice'] = books['ListPrice'].apply(add_2)
# lambda表达式
books['ListPrice'] = books['ListPrice'].apply(lambda x: x+2)
print(books)