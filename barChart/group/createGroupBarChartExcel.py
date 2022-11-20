import random

import pandas as pd
nameValues = []
number1Values = []
number2Values = []
nameStr = 'group_'
for i in range(1,10):
    nameValues.append(nameStr+'00'+str(i))
    number1Values.append(random.randint(0,1000))
    number2Values.append(random.randint(0, 1000))


name = pd.Series(nameValues,name='Group')
number_1 = pd.Series(number1Values,name='2021')
number_2= pd.Series(number2Values,name='2022')

df = pd.DataFrame({name.name:name,number_1.name:number_1,number_2.name:number_2})
df.set_index('Group',inplace=True)
print(df)
df.to_excel('mult_groups.xlsx')
print('Done')