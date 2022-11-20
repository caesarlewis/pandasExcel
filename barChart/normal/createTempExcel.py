import random

import pandas as pd
nameValues = []
numberValues = []
nameStr = 'group_'
for i in range(1,10):
    nameValues.append(nameStr+'00'+str(i))
    numberValues.append(random.randint(0,10000))


name = pd.Series(nameValues,name='Group')
number = pd.Series(numberValues,name='Number')

df = pd.DataFrame({name.name:name,number.name:number})
df.set_index('Group',inplace=True)
print(df)
df.to_excel('groups.xlsx')
print('Done')