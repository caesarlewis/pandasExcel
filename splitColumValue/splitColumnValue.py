import pandas as pd

employees= pd.read_excel('Employees.xlsx')
# expand = True 默认使用空格或者Tab来进行拆分
# n 为保留切分之后的多少个子字符串，默认为都保留
#
df = employees['Full Name'].str.split(n=1,expand=True)
print(df)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)
