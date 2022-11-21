import random

import pandas as pd
idValues = []
priceValues = []
bedroomsValues = []
bathroomsValues = []
sqft_livingValues =[]
sqft_basementValues = []
sqft_lotValues = []
floorsValues = []
yr_builtValues = []
for i in range(1,20000):
    idValues.append(i)
    priceValues.append(random.randint(100000,1000000))
    bedroomsValues.append(random.randint(1,5))
    bathroomsValues.append(random.randint(1,3))
    sqft_livingValues.append(random.randint(500, 5000))
    sqft_basementValues.append(random.randint(0, 1000))
    sqft_lotValues.append(random.randint(2000, 100000))
    floorsValues.append(random.randint(1, 4))
    yr_builtValues.append(random.randint(1955, 2000))

id = pd.Series(idValues,name='id')
price = pd.Series(priceValues,name='price')
bedrooms = pd.Series(bedroomsValues,name='bedrooms')
bathrooms = pd.Series(bathroomsValues,name='bathrooms')
sqft_living =pd.Series(sqft_livingValues,name='sqft_living')
sqft_basement = pd.Series(sqft_basementValues,name='sqft_basement')
sqft_lot = pd.Series(sqft_lotValues,name='sqft_lot')
floors = pd.Series(floorsValues,name='floors')
yr_built = pd.Series(yr_builtValues,name='yr_built')

df = pd.DataFrame({id.name:id,price.name:price,bedrooms.name:bedrooms,bathrooms.name:bathrooms,
                   sqft_living.name:sqft_living,sqft_basement.name:sqft_basement,
                   sqft_lot.name:sqft_lot,floors.name:floors,yr_built.name:yr_built})
df.set_index('id',inplace=True)
print(df)
print()
df.to_excel('home_data.xlsx')
print('Done')