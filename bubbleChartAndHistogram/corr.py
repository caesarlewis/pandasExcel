import pandas as pd
import matplotlib.pyplot as plt

#设置可现实的最大列
pd.options.display.max_columns = 777

homes = pd.read_excel('home_data.xlsx')
#相似性分析 corr()
print(homes.corr())