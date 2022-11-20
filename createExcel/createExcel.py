import pandas as pd
import env as env


df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['a', 'b', 'c']})
#替换索引 方式 1
df = df.set_index('ID')
path = env.getFilePath('output.xlsx')
print(path)
df.to_excel(path)
print('Done')
