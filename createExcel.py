import pandas as pd


df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['a', 'b', 'c']})
#替换索引 方式 1
df = df.set_index('ID')
df.to_excel('C:/Temp/output.xlsx')
print('Done')
