import pandas as pd
import matplotlib.pyplot as plt

#设置可现实的最大列
pd.options.display.max_columns = 777

homes = pd.read_excel('home_data.xlsx')

print(homes.head())
print(homes['price'])
# 调整柱状图分布 bins =100
#homes.sqft_living.plot.hist(bins=100)
#plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation=90)

#homes.price.plot.hist(bins=100)
#plt.xticks(range(0,max(homes.price),100000),fontsize=8,rotation=90)

homes.sqft_living.plot.kde()
plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation=90)

plt.show()