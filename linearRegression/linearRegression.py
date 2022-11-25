import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#dtype 设置读取某列数据的格式
sales = pd.read_excel('Sales.xlsx',dtype={'Month':str})
print(sales)

#计算线性回归方程
# slope 坡度 斜率
#intercept y轴上的截距
#std_err标准差
slope,intercept,r,p,std_err = linregress(sales.index,sales.Revenue)

# exp期望值
exp = sales.index * slope +intercept

# 预测未来的某一个值
# 35为预测的某一个点的值，这里代表第35行的值，也就是2019年12月
print(slope*35+intercept)

plt.scatter(sales.index,sales.Revenue)
plt.plot(sales.index,exp,color='orange')
plt.title(f'Sales y={slope}*x+{intercept}')
plt.xticks(sales.index,sales.Month,rotation=90)
plt.tight_layout()
plt.show()
