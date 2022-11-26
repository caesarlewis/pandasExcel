import pandas as pd
import numpy as np

page_001 = pd.read_excel('Students.xlsx',sheet_name='Page_001')
page_002 = pd.read_excel('Students.xlsx',sheet_name='Page_002')
#通过axis=1来进行列添加
#students = pd.concat([page_001,page_002],axis=1)

students = pd.concat([page_001,page_002]).reset_index(drop=True)
#追加列
students['Age'] = np.arange(0,len(students))
#删除列
students.drop(columns=['Age','Score'],inplace=True)
#插入列
students.insert(1,column='Foo',value=np.repeat('foo',len(students)))
#修改列名
students.rename(columns={'Foo':'FOO','Name':'NAME'},inplace=True)
#去掉空值操作
# 转换类型
students['ID'] = students['ID'].astype(float)
for i in range(5,15):
    students['ID'].at[i] = np.nan

students.dropna(inplace=True)

print(students)
#print(page_002)