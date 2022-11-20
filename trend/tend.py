import pandas as pd
import matplotlib.pyplot as plt


company = pd.read_excel('company_trend.xlsx',index_col='Week')
print(company)
print(company.columns)

# 普通趋势图
company.plot(y=['Accessories', 'Bikes', 'Clothing'])
# 叠加趋势图
company.plot.area(y=['Accessories', 'Bikes', 'Clothing'])
plt.title('sales weekly trend',fontsize=16,fontweight='bold')
plt.ylabel('Total',fontsize=16,fontweight='bold')
# xticks 重铺横轴
plt.xticks(company.index,fontsize=8)
plt.show()