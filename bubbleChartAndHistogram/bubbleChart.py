import pandas as pd
import matplotlib.pyplot as plt

#设置可现实的最大列
pd.options.display.max_columns = 777

homes = pd.read_excel('home_data.xlsx',index_col='id')

print(homes.head())
print(homes['price'])

homes.plot.scatter(x='sqft_living',y='price')
homes.plot.scatter(y='sqft_living',x='price')
plt.show()
