import pandas as pd

def low_score_red(s):
    color = 'red' if s<60 else 'black'
    return f'color:{color}'

def high_score_greed(col):
    return ['background-color:lime' if s==col.max() else 'background-color:white' for s in col]


students = pd.read_excel('D:\workSpace\PyCharmWorkSpace\PandasExcel\color\Students.xlsx')

result = students.style.applymap(low_score_red,subset=['Test_1','Test_2','Test_3']).apply(high_score_greed,subset=['Test_1','Test_2','Test_3'])

result.to_excel('color_students.xlsx')

# 根据数据大小显示颜色深浅

import seaborn as sns

color_map = sns.light_palette('green',as_cmap=True)

students1 = pd.read_excel('D:\workSpace\PyCharmWorkSpace\PandasExcel\color\Students.xlsx')

students1 = students1.style.background_gradient(color_map,subset=['Test_1','Test_2','Test_3'])
students1.to_excel('color_students1.xlsx')
# 根据数据大小显示柱状图大小
students2 = pd.read_excel('D:\workSpace\PyCharmWorkSpace\PandasExcel\color\Students.xlsx')
students2 = students2.style.bar(color='orange',subset=['Test_1','Test_2','Test_3'])
students2.to_excel('color_students2.xlsx')
