import pandas as pd

def low_score_red(s):
    color = 'red' if s<60 else 'black'
    return f'color:{color}'

def high_score_greed(col):
    return ['background-color:lime' if s==col.max() else 'background-color:white' for s in col]


students = pd.read_excel('D:\workSpace\PyCharmWorkSpace\PandasExcel\color\Students.xlsx')

result = students.style.applymap(low_score_red,subset=['Test_1','Test_2','Test_3']).apply(high_score_greed,subset=['Test_1','Test_2','Test_3'])

result.to_excel('color_students.xlsx')