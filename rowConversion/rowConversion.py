import pandas as pd

pd.options.display.max_columns=None
#设置index可以保证转换后的列名为行名
videos = pd.read_excel('Videos.xlsx',index_col='Month')
# 行转列 transpose
table = videos.transpose()

print(table)