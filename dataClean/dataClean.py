import pandas as pd

#
students = pd.read_excel('student_clean.xlsx', sheet_name='students')
scores = pd.read_excel('student_clean.xlsx', sheet_name='scores')
# merge， 将两个sheet页的数据关联，类似于数据表的关联
# on 为关联条件 默认使用ID,如果设置了index_col='ID'那么，就需要显示的设置 on='ID'
# 当左右关联名字不一样 使用left_on='student_name'  right_on='name'
# how 为关联方式 默认为join关联
# fillna 处理NAN
table = students.merge(scores, how='left',on='ID').fillna(0)
# astype转换数据类型
table.Score = table.Score.astype(int)
print(table)
students = pd.read_excel('student_clean.xlsx', sheet_name='students',index_col='ID')
scores = pd.read_excel('student_clean.xlsx', sheet_name='scores',index_col='ID')
# merge， 将两个sheet页的数据关联，类似于数据表的关联
# on 为关联条件 默认使用ID,如果设置了index_col='ID'那么，就需要显示的设置 on='ID'
# 当左右关联名字不一样 使用left_on='student_name'  right_on='name'
# how 为关联方式 默认为join关联
# fillna 处理NAN
table = students.merge(scores, how='left', left_on=students.index , right_on= scores.index).fillna(0)
# astype转换数据类型
table.Score = table.Score.astype(int)

print(table)

students = pd.read_excel('student_clean.xlsx', sheet_name='students',index_col='ID')
scores = pd.read_excel('student_clean.xlsx', sheet_name='scores',index_col='ID')
# join， 将两个sheet页的数据关联，类似于数据表的关联
# on 为关联条件 默认使用ID,如果设置了index_col='ID'那么，就需要显示的设置 on='ID'
# 当左右关联名字不一样 使用left_on='student_name'  right_on='name'
# how 为显示关联方式 默认为显示join关联
# fillna 处理NAN
table = students.join(scores, how='left').fillna(0)
# astype转换数据类型
table.Score = table.Score.astype(int)
print(table)