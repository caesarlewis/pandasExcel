import random

import pandas as pd
idValues = []
nameValues = []
octValues = []
novValues = []
decValues = []
nameStr = 'user_'
for i in range(1,20):
    idValues.append(i)
    if (i > 9):
        nameValues.append(nameStr + '0' + str(i))
    else:
        nameValues.append(nameStr + '00' + str(i))
    octValues.append(random.randint(0, 50))
    novValues.append(random.randint(0, 50))
    decValues.append(random.randint(0,50))

id = pd.Series(idValues,name='ID')
name = pd.Series(nameValues,name='Name')
oct = pd.Series(octValues,name='Oct')
nov= pd.Series(novValues,name='Nov')
dec = pd.Series(decValues,name='Dec')

df = pd.DataFrame({id.name:id,name.name:name,oct.name:oct,nov.name:nov,dec.name:dec})
df.set_index('ID',inplace=True)
print(df)
df.to_excel('user_login.xlsx')
print('Done')