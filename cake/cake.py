import pandas as pd
import matplotlib.pyplot as plt


cakeDatas = pd.read_excel('cake_datas.xlsx',index_col='Group')
print(cakeDatas)
# 使用index来作为标签显示
# 默认从大到小，逆时针排序 ，如果想要改变，需要改变排序.sort_values(ascending=True)
# startangle 改变排序开始的位置
# counterclock = True 逆时针排序 = False 顺时针排序
cakeDatas['2021'].plot.pie(fontsize=8,counterclock=False,startangle=-270)
plt.title('group number count',fontsize = 16,fontweight='bold')
plt.ylabel('2021',fontsize=16,fontweight='bold')
plt.show()