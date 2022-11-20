import random

import pandas as pd
weekValues = []
accessoriesValues = []
bikesValues = []
clothingValues = []
totalValues = []
for i in range(1,55):
    weekValues.append(i)
    ac = random.randint(100, 5000)
    accessoriesValues.append(ac)
    bi = random.randint(100, 5000)
    bikesValues.append(bi)
    cl = random.randint(100, 5000)
    clothingValues.append(cl)
    totalValues.append(ac+bi+cl)

week = pd.Series(weekValues,name='Week')
acc = pd.Series(accessoriesValues,name='Accessories')
bike = pd.Series(bikesValues,name='Bikes')
cloth= pd.Series(clothingValues,name='Clothing')
total = pd.Series(totalValues,name='Total')

df = pd.DataFrame({week.name:week,acc.name:acc,bike.name:bike,cloth.name:cloth,total.name:total})
df.set_index('Week',inplace=True)
print(df)
df.to_excel('company_trend.xlsx')
print('Done')