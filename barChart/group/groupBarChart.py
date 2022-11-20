import pandas as pd
import matplotlib.pyplot as plt

mlGroups = pd.read_excel('mult_groups.xlsx')
mlGroups.sort_values(by='2021',inplace=True,ascending=False)
print(mlGroups)
mlGroups.plot.bar(x='Group',y=['2021','2022'],color=['Red','Orange'],title='group number change 2021 vs 2022')
plt.title('group number change 2021 vs 2022',fontsize=16,fontweight='bold')
plt.xlabel('Group',fontweight='bold')
plt.ylabel('Number',fontweight='bold')
# 获取图形的轴
ax = plt.gca()
# 调整图形x轴样式 rotation为旋转多少度 ha为水平对其方向，默认为中心
ax.set_xticklabels(mlGroups['Group'],rotation=45,ha = 'right')
# 获取图形
f = plt.gcf()
# 调整图形上下左右的宽度，使用他不可以使用plt.tight_layout，以免冲突
f.subplots_adjust(left=0.2,bottom=0.2)
#plt.tight_layout()
plt.show()