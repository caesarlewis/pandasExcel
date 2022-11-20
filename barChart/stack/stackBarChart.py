import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('user_login.xlsx',index_col='ID')
users['Total'] = users.Oct+users.Nov+users.Dec
users.sort_values(by='Total',inplace=True,ascending=False)
print(users)
# 堆叠参数 stacked = True
# 纵向堆叠图
users.plot.bar(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Login Count stack')

# 水平堆叠图
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Login Count barh small2big')

# 水平堆叠图 从上到下 按从大到小排序 排序从小到大排序就可以
users.sort_values(by='Total',inplace=True)
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Login Count barh big2small')

plt.tight_layout()
plt.show()