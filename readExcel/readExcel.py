import pandas as pd

temp = pd.read_excel('C:/Temp/output.xlsx')
# 展示数据行列关系，第一个为行，第二个为列
print(temp.shape)
print(temp.columns)
# 展示数据头部多少个数据
print(temp.head(3))
# 展示数据尾部多少个数据
print(temp.tail(3))

# 脏header处理
temp = pd.read_excel('C:/Temp/output.xlsx', header=1)
print(temp.columns)

#没有 header处理
temp = pd.read_excel('C:/Temp/output.xlsx', header=None)
temp.columns = ['ID','Name']
#替换索引 方式 2
temp.set_index('ID',inplace=True)
print(temp.columns)
temp.to_excel('C:/Temp/output_resetColumns.xlsx')

# 指定index columns 防止读取之后会自动生成默认的index
temp = pd.read_excel('C:/Temp/output.xlsx', index_col='ID')
temp.to_excel('C:/Temp/output_resetindex.xlsx')
