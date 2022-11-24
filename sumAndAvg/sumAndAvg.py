import pandas as pd

students = pd.read_excel('Students.xlsx')
# 获取表中的多个列
temp = students[['Test_1','Test_2','Test_3']]
# sum() 默认纵向求和，axis =1为求横向求和
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1','Test_2','Test_3','Total','Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean,ignore_index=True)
print(students)