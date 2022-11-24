import pandas as pd

students = pd.read_excel('Students_Duplicates.xlsx')
# drop_duplicates去重方法
# subset去重列名['Name','ID']
# keep 默认为first 可以选择first  last 保留第一次出现还是最后一次出现的重复值
#students.drop_duplicates(subset='Name',inplace=True,keep='last')

# duplicated 判断是否是重复数据函数
dupe = students.duplicated(subset='Name')
# dupe.any()判断是否存在重复数据
print(dupe.any())
# Series[过滤条件] 可以过滤数据
dupe = dupe[dupe==True]
print(dupe.index)
# iloc 根据索引过滤出需要的数据类似于id查询
print(students.iloc[dupe.index])
