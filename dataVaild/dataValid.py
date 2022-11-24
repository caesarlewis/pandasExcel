import pandas as pd

def validScore(row):
    try:
        assert 0<=row.Score<=100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}')


def scoreValid(row):
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}')


students= pd.read_excel('Students.xlsx')
# axis 轴 分为2个 axis=1 从左向右  axis=0从上向下
students.apply(validScore,axis=1)
students.apply(scoreValid,axis=1)
print(students)