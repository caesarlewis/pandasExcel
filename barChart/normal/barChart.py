import pandas as pd
import matplotlib.pyplot as plt

groups = pd.read_excel('groups.xlsx')
groups.sort_values(by='Number',inplace=True,ascending=False)
print(groups)
# 利用pands绘图
#groups.plot.bar(x='Group',y='Number',color='Green',title='Group human number')
plt.bar(groups.Group,groups.Number,color='Green')
# 设置x轴样式，rotation 为设置横坐标倾斜多少度
plt.xticks(groups.Group,rotation=90)
plt.xlabel('Group')
plt.ylabel('Number')
plt.title('Group Human Number',fontsize=16)
#紧凑型布局
plt.tight_layout()
plt.show()