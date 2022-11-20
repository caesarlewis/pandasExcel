import random

import pandas as pd
idValues = []
nameValues = []
ageValues = []
scoreValues = []
nameStr = 'student_'
for i in range(1,20):
    idValues.append(i)
    if(i>9):
        nameValues.append(nameStr+'0'+str(i))
    else:
        nameValues.append(nameStr+'00'+str(i))
    ageValues.append(random.randint(10,20))
    scoreValues.append(random.randint(0,100))

id = pd.Series(idValues,name='ID')
name = pd.Series(nameValues,name='Name')
age = pd.Series(ageValues,name='Age')
score = pd.Series(scoreValues,name='Score')

df = pd.DataFrame({id.name:id,name.name:name,age.name:age,score.name:score})
df.set_index('ID',inplace=True)
print(df)
df.to_excel('student.xlsx')
print('Done')