import pandas as pd


def age_18_to_30(a):
    return 18<=a<=30


def level_a(s):
    return 85<=s<=100


students = pd.read_excel('student.xlsx',index_col='ID')
students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
# 特殊语法，可以使用类似属性的方式访问数据
students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]
# lambda表达式写法
students = students.loc[students.Age.apply(lambda a:18<=a<=30)].loc[students.Score.apply(lambda s:85<=s<=100)]
print(students)