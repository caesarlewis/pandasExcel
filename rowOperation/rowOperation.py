import pandas as pd

page_001 = pd.read_excel('Students.xlsx',sheet_name='Page_001')
page_002 = pd.read_excel('Students.xlsx',sheet_name='Page_002')

# reset_index() 重置index
# drop= True丢弃之前的index
students = pd.concat([page_001,page_002]).reset_index(drop=True)
print(students)
stu = pd.Series({'ID':41,'Name':'Abel','Score':99})
# 添加一行
# ignore_index 取消index校验
students=students.append(stu,ignore_index=True)
# 单个单元格替换值
students.at[39,'Name'] = 'Bailey'
students.at[39,'Score'] = 100
# 整行替换
stu = pd.Series({'ID':40,'Name':'Bailey','Score':100})
students.iloc[39] = stu

# 在数据行之间插入一行
stu = pd.Series({'ID':101,'Name':'Danni','Score':101})
part1 = students[:20]
part2 = students[20:]

students = part1.append(stu,ignore_index=True).append(part2)

# 删除数据行
#students.drop(index=[0,1,2],inplace=True)

#students.drop(index=range(0,10),inplace=True)

#students.drop(index=students[0:10],inplace=True)
# 有条件的删除

for i in range(5,15):
    students['Name'].at[i] = ''

missing = students.loc[students['Name'] == '']
students.drop(index=missing.index,inplace=True)

print(students)
#print(page_002)